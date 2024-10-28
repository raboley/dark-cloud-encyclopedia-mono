import os
import json
import argparse
from fuzzywuzzy import process

json_file_path = 'data/all_weapons.json'
input_dir_path = 'all_images/input'
final_output_dir = '../dark-cloud-website/src/api/weapons/images/'

IMAGE_TYPES = ['Side1', 'Side2', 'Main', 'Stats', 'Thumbnail']

def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def list_directories(path):
    return [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]

def generate_tree(weapons_data, directories, only_missing=False, show_details=False, show_errored=False):
    tree = {}
    for weapon in weapons_data:
        character = correct_character_name_from_directories(weapon['characterName'], directories)
        weapon_name = correct_weapon_name_from_directories(weapon['weaponName'], directories)
        folder_name = f"{character}_{weapon_name}"
        exists = weapon_exists(folder_name, directories)
        if only_missing and exists:
            continue
        if character not in tree:
            tree[character] = []
        if show_details or show_errored:
            final_image_prefix = f"{weapon['characterName']}_{weapon['weaponName'].replace(' ', '_')}"
            images_status = check_images_status(final_image_prefix)
            if show_errored and exists and not all(images_status.values()):
                tree[character].append((weapon_name, exists, images_status))
            elif show_details:
                if only_missing and all(images_status.values()):
                    continue
                tree[character].append((weapon_name, exists, images_status))
        else:
            tree[character].append((weapon_name, exists))
    return tree

def weapon_exists(folder_name, directories):
    if folder_name in directories:
        return True

    if fuzzy_match(folder_name, directories)[1] > 90:
        return True

    return False

def find_unmatched_folders(weapons_data, directories):
    weapon_folders = {f"{correct_character_name_from_directories(weapon['characterName'], directories)}_{correct_weapon_name_from_directories(weapon['weaponName'], directories)}" for weapon in weapons_data}
    unmatched_folders = [folder for folder in directories if not weapon_exists(folder, weapon_folders)]
    return unmatched_folders

def fuzzy_match(folder_name, weapon_folders):
    result = process.extractOne(folder_name, weapon_folders)
    if result is None:
        return None, 0
    match, score = result
    return match, score

def correct_character_name(character_name, characters):
    match, score = process.extractOne(character_name, characters)
    return match if score > 90 else character_name

def correct_weapon_name(weapon_name, weapons):
    match, score = process.extractOne(weapon_name, weapons)
    return match if score > 90 else weapon_name

def correct_character_name_from_directories(character_name, directories):
    characters = {d.split('_')[0] for d in directories}
    print("looking for match for character: ", character_name)
    correct_character_name(character_name, characters)

def correct_weapon_name_from_directories(weapon_name, directories):
    weapons = {d.split('_')[1] for d in directories if '_' in d}
    print("looking for match for weapon: ", weapon_name)
    correct_weapon_name(weapon_name, weapons)

def check_images_status(folder_name):
    images_status = {}
    for image_type in IMAGE_TYPES:
        image_name = f"{folder_name}_{image_type}.jpg"
        image_path = os.path.join(final_output_dir, image_name)
        images_status[image_type] = os.path.exists(image_path)
    return images_status

def print_tree(tree, show_details=False, show_errored=False):
    for character, weapons in tree.items():
        print(character)
        for i, weapon_info in enumerate(weapons):
            weapon_name = weapon_info[0]

            exists = weapon_info[1]
            if i == len(weapons) - 1:
                prefix = "└──"
            else:
                prefix = "├──"
            status = "✔️" if exists else "❌"
            print(f"  {prefix} {weapon_name} {status}")
            if show_details and exists:
                images_status = weapon_info[2]
                for image_type, image_exists in images_status.items():
                    image_status = "✔️" if image_exists else "❌"
                    print(f"    ├── {image_type}: {image_status}")
            elif show_errored and exists:
                images_status = weapon_info[2]
                for image_type, image_exists in images_status.items():
                    if not image_exists:
                        print(f"    ├── {image_type}: ❌")

def print_unmatched_folders(unmatched_folders, weapon_folders):
    print("Unmatched Folders:")
    for i, folder in enumerate(unmatched_folders):
        if i == len(unmatched_folders) - 1:
            prefix = "└──"
        else:
            prefix = "├──"
        match, score = fuzzy_match(folder, weapon_folders)
        if score < 90:
            print(f"  {prefix} {folder} (Best Match: {match} with score {score}) ❌")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Generate a tree structure of weapons and their presence in directories.")
    parser.add_argument('--only-missing', action='store_true', help="Show only missing weapons")
    parser.add_argument('--only-unmatched', action='store_true', help="Show only unmatched folders")
    parser.add_argument('--show-details', action='store_true', help="Show detailed image status")
    parser.add_argument('--show-errored', action='store_true', help="Show only errored weapons with missing images")
    args = parser.parse_args()

    weapons_data = load_json(json_file_path)
    directories = list_directories(input_dir_path)

    weapon_folders = {f"{correct_character_name_from_directories(weapon['characterName'], directories)}_{correct_weapon_name_from_directories(weapon['weaponName'], directories)}" for weapon in weapons_data}
    characters = {weapon['characterName'] for weapon in weapons_data}
    weapons = {weapon['weaponName'] for weapon in weapons_data}

    if args.only_unmatched:
        unmatched_folders = find_unmatched_folders(weapons_data, directories)
        print_unmatched_folders(unmatched_folders, weapon_folders)
    else:
        tree = generate_tree(weapons_data, directories, only_missing=args.only_missing, show_details=args.show_details, show_errored=args.show_errored)
        print_tree(tree, show_details=args.show_details, show_errored=args.show_errored)
