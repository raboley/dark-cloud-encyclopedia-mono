# Overview

This project is aimed at getting images from PS4/PS5 of Dark Cloud, processing them, and then showing them in a nice way on my website.

0. Get images from PS4/PS5 to the folder path [categorize-images/all_images/input](categorize-images/all_images/input),
because I can't get them in groups of 4 from twitter anymore, they must be grouped in a folder with the pattern `<characterName>_<Weapon Name>` for example `Toan_Atlamillia Sword`.the names of the images themselves do not matter.
1. Name the images. using `task categorize-images` to categorize and name the images into the output path [categorize-images/all_images/output](categorize-images/all_images/output)
The images will be named in the format `<characterName>_<Weapon Name>_<type>.jpeg` for example `Toan_Atlamillia_Sword_Side1.jpeg`
2. Next we need to crop the image


## Pre-requisites

- [install taskfile](https://taskfile.dev/installation)
- [install uv](https://github.com/astral-sh/uv?tab=readme-ov-file#installation)

## Getting started

```bash
