# Overview

This will read images and and categorize images based on the text on the picture.

# Local setup

```
make init
```

# Function Flow

To run this, ve in the categorize-images directory, and run

```shell
uv run main.py
```

The exection start is in `main.py` where we read the images from the `all_images/input/` directory. In there should be a directory in the pattern <CharacterName>_<WeaponName> with all the weapon images in there.
*note these should be proper casing e.g. Toan_Chronicle 2 spaces are okay*

1.Categorize the image types

The first step is to categorize the images, this takes a helping hand from the folder naming schema, and then corrects any character or weapon name misspelling.

To ensure everything worked right you can copy from the output directory, just the files (no folders) to the `src/api/weapons/images` directory of the [dark-cloud-website](https://gitlab.com/russell_boley/dark-cloud-website.git)
project. After there it should show up in the details page of the website (not thumbnails yet)

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
