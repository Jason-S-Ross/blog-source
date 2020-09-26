#!/bin/bash

source_dir=../resources_raw
target_dir=../images
max_width=512
max_height=256

mkdir -p $target_dir
for filepath in $source_dir/*
do
    filename="$(basename -- $filepath)"
    stem=$(echo "$filename" | cut -f 1 -d '.')
    convert $filepath -resize "${max_width}x${max_height}" "$target_dir/$stem.jpg"
done