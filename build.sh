#!/bin/bash

# get the directory in which this script is located (the zola site source dir)
SOURCE_DIR=$(cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd)

# create blog comments files, if needed
"$SOURCE_DIR/retrieve-comments.py" --create-empty

# build the website via zola
npm install && npm run build && zola build
