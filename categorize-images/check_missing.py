import os
import json
from collections import defaultdict

output_folder = 'all_images/output/'
image_types = ["Side1", "Side2", "Main", "Stats"]

def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def get_output_path_prefix(character_name, weapon_name, output_folder):
    corrected_weapon_name = weapon_name.replace(" ", "_")
    un_typed_image_path_prefix = os.path.join(output_folder, f"{character_name}_{corrected_weapon_name}")
    return un_typed_image_path_prefix

def check_missing_images(weapons_data, output_folder):
    missing_images = []
    for weapon in weapons_data:
        character_name = weapon['characterName']
        weapon_name = weapon['weaponName']
        un_typed_image_path_prefix = get_output_path_prefix(character_name, weapon_name, output_folder)
        for image_type in image_types:
            expected_image_path = f"{un_typed_image_path_prefix}_{image_type}.jpg"
            if not os.path.exists(expected_image_path):
                missing_images.append(expected_image_path)
    return missing_images

def print_tree(char_map, indent=""):
    for character, missing_images in char_map.items():
        print(indent + character)
        for image in missing_images:
            print(indent + "├── " + image)

if __name__ == '__main__':
    # Load weapon data
    json_file_path = 'data/all_weapons.json'
    weapons_data = load_json(json_file_path)

    # Check for missing images
    missing = check_missing_images(weapons_data, output_folder)

    # Use defaultdict to store lists of missing images for each character
    char_map = defaultdict(list)
    for path in missing:
        character = path.split("/")[2].split("_")[0]
        missing_image = "_".join(path.split("/")[2].split("_")[1:])
        char_map[character].append(missing_image)

    # Convert defaultdict to a regular dictionary for printing
    char_map = dict(char_map)

    # Print the char_map in a tree-like format
    print_tree(char_map)