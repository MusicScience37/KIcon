#!/bin/bash

mkdir PNG

convert -density 1000 KIcon.svg -resize 16x16 -transparent white PNG/KIcon16.png
convert -density 1000 KIcon.svg -resize 24x24 -transparent white PNG/KIcon24.png
convert -density 1000 KIcon.svg -resize 32x32 -transparent white PNG/KIcon32.png
convert -density 1000 KIcon.svg -resize 48x48 -transparent white PNG/KIcon48.png
convert -density 1000 KIcon.svg -resize 64x64 -transparent white PNG/KIcon64.png
convert -density 1000 KIcon.svg -resize 152x152 -transparent white PNG/KIcon152.png
convert -density 1000 KIcon.svg -resize 512x512 -transparent white PNG/KIcon512.png
convert PNG/KIcon16.png PNG/KIcon24.png PNG/KIcon32.png PNG/KIcon48.png PNG/KIcon64.png PNG/KIcon152.png PNG/KIcon512.png -colors 256 KIcon.ico

convert -density 1000 KIcon.svg -resize 512x512 -transparent white KIcon.jpg
