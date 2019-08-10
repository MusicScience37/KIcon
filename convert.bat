magick convert -density 1000 KIcon.svg -resize 16x16 -transparent white PNG/KIcon16.png
magick convert -density 1000 KIcon.svg -resize 24x24 -transparent white PNG/KIcon24.png
magick convert -density 1000 KIcon.svg -resize 32x32 -transparent white PNG/KIcon32.png
magick convert -density 1000 KIcon.svg -resize 48x48 -transparent white PNG/KIcon48.png
magick convert -density 1000 KIcon.svg -resize 64x64 -transparent white PNG/KIcon64.png
magick convert -density 1000 KIcon.svg -resize 152x152 -transparent white PNG/KIcon152.png
magick convert -density 1000 KIcon.svg -resize 512x512 -transparent white PNG/KIcon512.png
magick convert PNG/KIcon16.png PNG/KIcon24.png PNG/KIcon32.png PNG/KIcon48.png PNG/KIcon64.png PNG/KIcon152.png PNG/KIcon512.png -colors 256 KIcon.ico

magick convert -density 1000 KIcon.svg -resize 512x512 -transparent white KIcon.jpg