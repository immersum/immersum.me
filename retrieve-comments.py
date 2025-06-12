#!/usr/bin/env python3

import argparse
import json
import os.path as path
import re
import tomllib
from glob import glob
from urllib.request import urlopen

from babel.dates import format_date, format_time
from dateutil import parser as datetime_parser

HEADER = "+++\nrender = false\n+++\n"
BLOG_PATH = "content/blog"
BLOG_COMMENTS_PATH = "content/blog-comments"
DEFAULT_LANGUAGE = "en"
ADDITIONAL_LANGUAGES = ["hu"]


def get_blog_entry_files(exclude_translations):
    """
    Returns a list of all markdown blog entry filenames from the given directory.

    The index files are always excluded from this list and it can optionally be
    requested with the exclude_translations parameter, to only return the files
    of the default language, but exclude all translation files.
    """

    translation_pattern = re.compile(".*\\.[a-z]{2}\\.md$")

    files = []

    for file in glob(f"{BLOG_PATH}/*.md"):
        file = file.replace(f"{BLOG_PATH}/", "")

        if not file.startswith("_index") and (
            not exclude_translations or not translation_pattern.match(file)
        ):
            files.append(file)

    return files


def get_blog_entry_comments_config(exclude_translations):
    """
    Returns a dictionary with the Mastodon comments configuration from each
    blog entry file from the given path.

    It can optionally be requested with the exclude_translations parameter, to
    only return the configuration from the files of the default language.
    """
    files_config = {}

    for file in get_blog_entry_files(exclude_translations):
        with open(f"{BLOG_PATH}/{file}") as f:
            config_part = f.read().split("+++\n")[1]
            data = tomllib.loads(config_part)

            if "extra" in data and "comments" in data["extra"]:
                files_config[file] = data

    return files_config


def create_empty_comment_files(files_comments_config):
    """
    Creates the markdown files for the comments of each blog entry.

    There are no comments in the files, only the header is written. Existing
    files are not overwritten.
    """
    for file in files_comments_config:
        comments_file = f"{BLOG_COMMENTS_PATH}/{file}"
        if not path.isfile(comments_file):
            with open(comments_file, "x") as f:
                f.write(HEADER)


def get_display_name_without_emojis(comment):
    """
    Returns the display name from the given comment dict, but with all emojis
    removed from the name.
    """
    name = comment["account"]["display_name"]
    for emoji in comment["account"]["emojis"]:
        name = name.replace(f":{emoji['shortcode']}:", "")
    return name


def create_markdown_entry(comment, locale):
    """
    Returns the string for the macro instance of the comment.

    The macro is defined in templates/shortcodes/comment.html. For now, only
    the date and time are translated according to the given locale.
    """
    connecting_word = {"en": "at", "hu": "–"}

    level = 1 if comment["in_reply_to_id"] == str(config["id"]) else 2
    datetime = datetime_parser.parse(comment["created_at"])
    date = format_date(datetime, format="long", locale=locale)
    time = format_time(datetime, "H:mm", locale=locale)
    return (
        f'\n{{% comment(user_url="{comment['account']['url']}", comment_url="{comment['url']}", fullname="{get_display_name_without_emojis(comment)}", datetime="{date} {connecting_word[locale]} {time}", avatar="{comment['account']['avatar_static']}", favorites={int(comment['favourites_count'])}, level={level}) %}}'
        f"\n{comment['content']}"
        f"\n{{% end %}}\n"
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="Retrieve Comments",
        description="Retrieves comments from Mastodon and creates corresponding markdown files",
    )
    parser.add_argument(
        "--create-empty",
        action="store_true",
        help="Only create the missing empty comment files",
    )
    args = parser.parse_args()

    if args.create_empty:
        files_comments_config = get_blog_entry_comments_config(
            exclude_translations=False
        )
        create_empty_comment_files(files_comments_config)

    else:
        files_comments_config = get_blog_entry_comments_config(
            exclude_translations=True
        )

        for file, data in files_comments_config.items():
            config = data["extra"]["comments"]

            url = f"https://{config['host']}/api/v1/statuses/{config['id']}/context"
            response = json.loads(urlopen(url).read())

            with open(f"{BLOG_COMMENTS_PATH}/{file}", "w") as f:
                f.write(HEADER)
                for comment in response["descendants"]:
                    f.write(create_markdown_entry(comment, locale=DEFAULT_LANGUAGE))

            for language in ADDITIONAL_LANGUAGES:
                file_with_language = file.replace(".md", f".{language}.md")
                with open(f"{BLOG_COMMENTS_PATH}/{file_with_language}", "w") as f:
                    f.write(HEADER)
                    for comment in response["descendants"]:
                        f.write(create_markdown_entry(comment, locale=language))
