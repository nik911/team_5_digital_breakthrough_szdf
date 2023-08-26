#!/bin/sh

marp --pdf slide-deck.md
marp pattern1.md -o pattern1.pdf
marp --pptx slide-deck.md
marp pattern1.md -o pattern1.pptx
marp pattern1.md -o pattern1.png --image-scale 1



marp --pdf slide-deck.md
marp pattern2.md -o pattern2.pdf
marp --pptx slide-deck.md
marp pattern2.md -o pattern2.pptx
marp pattern2.md -o pattern2.png --image-scale 1

marp --pdf slide-deck.md
marp pattern3.md -o pattern3.pdf
marp --pptx slide-deck.md
marp pattern3.md -o pattern3.pptx
marp pattern3.md -o pattern3.png --image-scale 1

echo -n "Done!"
