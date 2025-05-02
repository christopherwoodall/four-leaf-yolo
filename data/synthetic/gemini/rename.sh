#!/bin/bash

# This script renames all image files in the current directory to their MD5 hash.
# It identifies images based on common MIME types.

# Define a list of common image MIME types
IMAGE_MIMES=("image/jpeg" "image/png" "image/gif" "image/bmp" "image/tiff" "image/webp")

echo "Starting image renaming process in the current directory: $(pwd)"

# Iterate through all files in the current directory
for filename in *; do
  # Check if it's a regular file and not the script itself
  if [[ -f "$filename" && "$filename" != "$(basename "$0")" ]]; then
    # Get the MIME type of the file
    # Using -b to get only the MIME type, without the filename
    mime_type=$(file --mime-type -b "$filename")

    # Check if the MIME type is in the list of image MIME types
    is_image=false
    for img_mime in "${IMAGE_MIMES[@]}"; do
      if [[ "$mime_type" == "$img_mime" ]]; then
        is_image=true
        break
      fi
    done

    if "$is_image"; then
      # Calculate the MD5 hash of the file
      # Using awk to extract only the hash value
      md5_hash=$(md5sum "$filename" | awk '{print $1}')

      # Get the file extension
      # Using bash parameter expansion to get the part after the last dot
      extension="${filename##*.}"

      # Construct the new filename with the hash and original extension
      if [[ "$filename" == *.* ]]; then
        new_filename="${md5_hash}.${extension}"
      else
        # Handle files without an extension (though less common for images)
        new_filename="${md5_hash}"
      fi

      # Check if the new filename is different from the original filename
      if [[ "$filename" != "$new_filename" ]]; then
        # Check if a file with the new name already exists to prevent overwriting
        if [[ -e "$new_filename" ]]; then
          echo "Error: File with hash '$new_filename' already exists. Skipping '$filename'."
        else
          # Rename the file
          mv "$filename" "$new_filename"
          echo "Renamed '$filename' to '$new_filename'"
        fi
      else
        echo "File '$filename' already has a name based on its hash. Skipping."
      fi
    # else
      # Optional: Uncomment the following line to see which files are skipped and why
      # echo "'$filename' is not identified as a supported image type ($mime_type). Skipping."
    fi
  fi
done

echo "Image renaming process finished."
