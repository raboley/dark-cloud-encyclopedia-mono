import os
import json
import argparse
from fuzzywuzzy import process

def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def list_directories(path):
    return [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]

def generate_tree(weapons_data, directories, only_missing=False):
    tree = {}
    for weapon in weapons_data:
        character = weapon['characterName']
        weapon_name = weapon['weaponName']
        folder_name = f"{character}_{weapon_name}"
        exists = weapon_exists(folder_name, directories)
        if only_missing and exists:
            continue
        if character not in tree:
            tree[character] = []
        tree[character].append((weapon_name, exists))
    return tree

def weapon_exists(folder_name, directories):
    if folder_name in directories:
        return True

    if fuzzy_match(folder_name, directories)[1] > 90:
        return True

    return False

def find_unmatched_folders(weapons_data, directories):
    weapon_folders = {f"{weapon['characterName']}_{weapon['weaponName']}" for weapon in weapons_data}
    unmatched_folders = [folder for folder in directories if not weapon_exists(folder, weapon_folders)]
    return unmatched_folders

def fuzzy_match(folder_name, weapon_folders):
    match, score = process.extractOne(folder_name, weapon_folders)
    return match, score

def correct_character_name(character_name, characters):
    match, score = process.extractOne(character_name, characters)
    return match if score > 90 else character_name

def correct_weapon_name(weapon_name, weapons):
    match, score = process.extractOne(weapon_name, weapons)
    return match if score > 90 else weapon_name

def print_tree(tree):
    for character, weapons in tree.items():
        print(character)
        for i, (weapon, exists) in enumerate(weapons):
            if i == len(weapons) - 1:
                prefix = "└──"
            else:
                prefix = "├──"
            status = "✔️" if exists else "❌"
            print(f"  {prefix} {weapon} {status}")

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
    args = parser.parse_args()

    json_file_path = 'categorize/data/all_weapons.json'
    input_dir_path = 'all_images/input'

    weapons_data = load_json(json_file_path)
    directories = list_directories(input_dir_path)

    weapon_folders = {f"{weapon['characterName']}_{weapon['weaponName']}" for weapon in weapons_data}
    characters = {weapon['characterName'] for weapon in weapons_data}
    weapons = {weapon['weaponName'] for weapon in weapons_data}

    if args.only_unmatched:
        unmatched_folders = find_unmatched_folders(weapons_data, directories)
        print_unmatched_folders(unmatched_folders, weapon_folders)
    else:
        tree = generate_tree(weapons_data, directories, only_missing=args.only_missing)
        print_tree(tree)