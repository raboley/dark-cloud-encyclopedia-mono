import os
import json
import argparse

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
        exists = folder_name in directories
        if only_missing and exists:
            continue
        if character not in tree:
            tree[character] = []
        tree[character].append((weapon_name, exists))
    return tree

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

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Generate a tree structure of weapons and their presence in directories.")
    parser.add_argument('--only-missing', action='store_true', help="Show only missing weapons")
    args = parser.parse_args()

    json_file_path = 'categorize/data/all_weapons.json'
    input_dir_path = 'all_images/input'

    weapons_data = load_json(json_file_path)
    directories = list_directories(input_dir_path)
    tree = generate_tree(weapons_data, directories, only_missing=args.only_missing)
    print_tree(tree)
