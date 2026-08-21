#!/bin/bash
fails=0
cd dist
echo "Extracting links..."
# Find all html files
files=$(find . -name "*.html")
for f in $files; do
  # Extract internal links (starting with /)
  links=$(grep -oP 'href="\K/[^"]+' "$f" | sort | uniq)
  for l in $links; do
    # Convert /en/about/ to ./en/about/index.html
    # Remove leading slash
    path=${l#/}
    
    # If path ends with /, append index.html
    if [[ $path == */ ]]; then
      target="./${path}index.html"
    elif [[ -z $path ]]; then
      target="./index.html"
    else
      # It might just point to a file, or a directory without trailing slash
      if [ -d "./$path" ]; then
        target="./${path}/index.html"
      else
        target="./$path"
      fi
    fi
    
    if [ ! -f "$target" ]; then
      echo "BROKEN LINK: $l in file $f (Target $target not found)"
      fails=$((fails + 1))
    fi
  done
done

if [ $fails -eq 0 ]; then
  echo "All internal links are valid."
  exit 0
else
  echo "Found $fails broken links."
  exit 1
fi
