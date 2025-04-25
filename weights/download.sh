#!/bin/bash

# List of URLs to download
urls=(
    "https://github.com/WongKinYiu/yolov9/releases/download/v0.1/caption_files.zip"
    "https://github.com/WongKinYiu/yolov9/releases/download/v0.1/gelan-c-det.pt"
    "https://github.com/WongKinYiu/yolov9/releases/download/v0.1/gelan-c-pan.pt"
    "https://github.com/WongKinYiu/yolov9/releases/download/v0.1/gelan-c-seg.pt"
    "https://github.com/WongKinYiu/yolov9/releases/download/v0.1/gelan-c.pt"
    "https://github.com/WongKinYiu/yolov9/releases/download/v0.1/gelan-e.pt"
    "https://github.com/WongKinYiu/yolov9/releases/download/v0.1/gelan-m.pt"
    "https://github.com/WongKinYiu/yolov9/releases/download/v0.1/gelan-s.pt"
    "https://github.com/WongKinYiu/yolov9/releases/download/v0.1/gelan-s2.pt"
    "https://github.com/WongKinYiu/yolov9/releases/download/v0.1/lh-yolov9-c-coarse-.pt"
    "https://github.com/WongKinYiu/yolov9/releases/download/v0.1/lh-yolov9-c-coarse.pt"
    "https://github.com/WongKinYiu/yolov9/releases/download/v0.1/lh-yolov9-c-fine-.pt"
    "https://github.com/WongKinYiu/yolov9/releases/download/v0.1/lh-yolov9-c-fine.pt"
    "https://github.com/WongKinYiu/yolov9/releases/download/v0.1/semantic-labels.zip"
    "https://github.com/WongKinYiu/yolov9/releases/download/v0.1/yolov9-c-coarse-.pt"
    "https://github.com/WongKinYiu/yolov9/releases/download/v0.1/yolov9-c-coarse.pt"
    "https://github.com/WongKinYiu/yolov9/releases/download/v0.1/yolov9-c-converted.pt"
    "https://github.com/WongKinYiu/yolov9/releases/download/v0.1/yolov9-c-fine-.pt"
    "https://github.com/WongKinYiu/yolov9/releases/download/v0.1/yolov9-c-fine.pt"
    "https://github.com/WongKinYiu/yolov9/releases/download/v0.1/yolov9-c-seg-converted.pt"
    "https://github.com/WongKinYiu/yolov9/releases/download/v0.1/yolov9-c-seg.pt"
    "https://github.com/WongKinYiu/yolov9/releases/download/v0.1/yolov9-c.pt"
    "https://github.com/WongKinYiu/yolov9/releases/download/v0.1/yolov9-e-converted.pt"
    "https://github.com/WongKinYiu/yolov9/releases/download/v0.1/yolov9-e.pt"
    "https://github.com/WongKinYiu/yolov9/releases/download/v0.1/yolov9-m-converted.pt"
    "https://github.com/WongKinYiu/yolov9/releases/download/v0.1/yolov9-m.pt"
    "https://github.com/WongKinYiu/yolov9/releases/download/v0.1/yolov9-relu-converted.pt"
    "https://github.com/WongKinYiu/yolov9/releases/download/v0.1/yolov9-relu.pt"
    "https://github.com/WongKinYiu/yolov9/releases/download/v0.1/yolov9-s-converted.pt"
    "https://github.com/WongKinYiu/yolov9/releases/download/v0.1/yolov9-s.pt"
    "https://github.com/WongKinYiu/yolov9/releases/download/v0.1/yolov9-t-converted.pt"
    "https://github.com/WongKinYiu/yolov9/archive/refs/tags/v0.1.zip"
    "https://github.com/WongKinYiu/yolov9/archive/refs/tags/v0.1.tar.gz"
)

# Loop through each URL and download the file
for url in "${urls[@]}"; do
    echo "Downloading: $url"
    # Use wget to download the file. -P . ensures it downloads to the current directory.
    wget -P . "$url"
    if [ $? -ne 0 ]; then
        echo "Error downloading $url"
    else
        echo "Successfully downloaded $(basename "$url")"
    fi
    echo "----------------------------------------"
done

echo "Download process finished."
