#!/bin/sh

marp --pdf front/src/pattern1.md
marp mdFiles/pattern1.md -o front/src/pattern1.pdf
marp --pptx front/src/pattern1.md
marp mdFiles/pattern1.md -o front/src/pattern1.pptx
marp mdFiles/pattern1.md -o front/src/pattern1.md --image-scale 1

marp --pdf  front/src/pattern2.md
marp mdFiles/pattern2.md -o front/src/pattern2.pdf
marp --pptx front/src/pattern2.md
marp mdFiles/pattern2.md -o front/src/pattern2.pptx
marp mdFiles/pattern2.md -o front/src/pattern2.png --image-scale 1

marp --pdf front/src/mdFiles/pattern3.md
marp mdFiles/pattern3.md -o front/src/pattern3.pdf
marp --pptx front/src/pattern3.md
marp mdFiles/pattern3.md -o front/src/pattern3.pptx
marp mdFiles/pattern3.md -o front/src/pattern3.png --image-scale 1

echo "Done!"
