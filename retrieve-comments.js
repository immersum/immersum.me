#!/usr/bin/env node

import { glob, open } from "node:fs/promises";
import { join } from "node:path";
import { EOL } from "node:os";
import { URL } from "node:url";
import { parse } from "smol-toml";
import { createRestAPIClient } from "masto";
import { Command } from "commander";

const program = new Command();

program
  .name("retrieve-comments")
  .version("1.0.0")
  .description(
    "Retrieves comments from Mastodon and creates corresponding markdown files",
  )
  .option("--create-empty", "create the missing empty comment files and exit")
  .requiredOption(
    "-i, --input <pattern>",
    "the input pattern for blog entry files",
  )
  .requiredOption(
    "-o, --output <directory>",
    "the output directory for comment files",
  )
  .action(async (options) => {
    const inputFiles = getBlogEntryFiles(options.input);
    for await (const { name, toml } of inputFiles) {
      const comments = toml.extra?.comments;
      if (comments) {
        const path = join(options.output, name);
        if (options.createEmpty) {
          await createCommentFile(path);
        } else {
          await createCommentFile(path, comments.host, comments.id);
        }
      }
    }
  });

await program.parseAsync(process.argv);

/**
 * Retrieves the names of the blog entry files that match the specified pattern. The blog entry
 * files must also have header data in a TOML frontmatter.
 *
 * @param {(string|string[])} pattern The glob pattern.
 * @returns {AsyncIterator} An AsyncIterator that yields names of files along with header data.
 */
async function* getBlogEntryFiles(pattern) {
  const options = { withFileTypes: true };
  const paths = glob(pattern, options);
  for await (const { name, parentPath } of paths) {
    const path = join(parentPath, name);
    let file;
    try {
      file = await open(path);
      let header;
      for await (let line of file.readLines()) {
        line = line.trim();
        if (line === "") {
          // Skip empty line before or inside header.
          continue;
        }
        if (line === "+++") {
          if (header === undefined) {
            // Initialize and begin reading header.
            header = "";
          } else {
            // Return a blog entry file header.
            const toml = parse(header);
            yield { name, toml };
          }
        } else {
          if (header === undefined) {
            // Skip file not having a header.
            break;
          } else {
            // Append line and continue reading header.
            header += line + EOL;
          }
        }
      }
    } finally {
      await file?.close();
    }
  }
}

/**
 * Creates or replaces the file at the specified path with a section for blog entry comments.
 *
 * @param {string} path The file path to write.
 * @param {string} host The Mastodon server instance.
 * @param {(string|number)} The ID of the status announcing the blog entry to Mastodon users.
 */
async function createCommentFile(path, host, id) {
  let file;
  try {
    file = await open(path, "w");
    await file.write(`+++${EOL}render = false${EOL}+++${EOL}`);
    if (host && id > 0) {
      const url = new URL("https://" + host);
      const masto = createRestAPIClient({ url });
      const context = await masto.v1.statuses.$select(id).context.fetch();
      for (const status of context.descendants) {
        let shortcodes = status.account.emojis.map((emoji) => emoji.shortcode);
        let pattern = `:(${shortcodes.join("|")}):`;
        const params = [
          `user_url="${status.account.url}"`,
          `comment_url="${status.url}"`,
          `fullname="${status.account.displayName.replace(pattern, "")}"`,
          `datetime="${status.createdAt}"`,
          `avatar="${status.account.avatarStatic}"`,
          `favorites=${status.favouritesCount}`,
          `level=${status.inReplyToId == id ? 1 : 2}`,
        ];
        shortcodes = status.emojis.map((emoji) => emoji.shortcode);
        pattern = `:(${shortcodes.join("|")}):`;
        await file.write(`
{% comment(${params.join(", ")}) %}
${status.content.replace(pattern, "")}
{% end %}
`);
      }
    }
  } finally {
    await file?.close();
  }
}
