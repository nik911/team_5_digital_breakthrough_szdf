#!/bin/sh

marp --pdf slide-deck.md
marp pattern1.md -o pattern1.pdf
marp --pptx slide-deck.md
marp pattern1.md -o pattern1.pptx

marp --pdf slide-deck.md
marp pattern2.md -o pattern2.pdf
marp --pptx slide-deck.md
marp pattern2.md -o pattern2.pptx


marp --pdf slide-deck.md
marp pattern3.md -o pattern3.pdf
marp --pptx slide-deck.md
marp pattern3.md -o pattern3.pptx

echo -n "Done!"
