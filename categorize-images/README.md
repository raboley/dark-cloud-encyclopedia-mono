# Overview

This will read images and and categorize images based on the text on the picture.

# Local setup

```
make init
```

# Function Flow

1. Read in the image from the input folder using [read_text_from_image.py](categorize/read_text_from_image.py)
This should output named images in the output folder

# Output

The output of this needs to be a named file in directory for each type of image

The naming pattern should be '<character>_<weapon name>_<type>.jpg'

for example `Toan_Chronicle 2_Main.jpg`

There are 4 types of images that can be output:

```
stats: 'Stats.jpg',
main: 'Main.jpg',
side1: 'Side1.jpg',
side2: 'Side2.jpg'
```

TODO: use local ocr to determine the different image types

# See the image status

To see all images we have and don't have run

```shell
python3 generate_tree.py
```

you will see something like

```shell
Toan
  ├── Dagger ❌
  ├── Baselard ❌
  ├── Crysknife ✔️
  ├── Gladius ✔️
  ├── Kitchen Knife ❌
```

To see what images are missing you can run

```shell
python3 generate_tree.py --only-missing
```

```shell
├── Babel's Spear ❌
└── Hercule's Wrath ❌
Osmond
├── Machine Gun ❌
├── Snail ❌ 
```
