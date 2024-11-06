import os
import shutil
from categorize.read_image_text import read_text_from_image
from categorize.image_text_decider import determine_picture_type
from generate_tree import load_json, correct_character_name, correct_weapon_name

input_folder = 'all_images/input/'
output_folder = 'all_images/output/'
allImageDirectories = os.listdir(input_folder)
image_types = ["Side1", "Side2", "Main", "Stats"]

unmatched_images = []

def remove_already_processed_folders(characters, weapons, allImageDirectories, output_folder):
    input_output_mapping = {input_folder: get_output_path_prefix(characters, weapons, input_folder, output_folder) for input_folder in allImageDirectories}

    directories_to_process = {}
    # cross apply the input_output_mapping to the image_types array to see if all 4 images exist
    for input_folder, output_folder in input_output_mapping.items():
        for image_type in image_types:
            if not os.path.exists(output_folder + "_" + image_type + ".jpg"):
                directories_to_process[input_folder] = output_folder
                break

    return directories_to_process.keys()


def get_output_path_prefix(characters, weapons, imageDirectory, output_folder):
    original_character_name = imageDirectory.split("_")[0]
    original_weapon_name = imageDirectory.split("_")[1].split(".")[0]
    corrected_character_name = correct_character_name(original_character_name, characters)
    corrected_weapon_name = correct_weapon_name(original_weapon_name, weapons)
    corrected_weapon_name = corrected_weapon_name.replace(" ", "_")
    un_typed_image_path_prefix = output_folder + corrected_character_name + "_" + corrected_weapon_name
    return un_typed_image_path_prefix

if __name__ == '__main__':
    if not os.path.exists(output_folder):
        print("Creating output folder: " + output_folder)
        os.makedirs(output_folder)

    # Load weapon data
    json_file_path = 'data/all_weapons.json'
    weapons_data = load_json(json_file_path)
    characters = {weapon['characterName'] for weapon in weapons_data}
    weapons = {weapon['weaponName'] for weapon in weapons_data}


    # remove any nondirectory files
    allImageDirectories = [d for d in allImageDirectories if os.path.isdir(input_folder + d)]
    ### Development so we only do 1 folder at a time.
    # allImageDirectories = ["Toan_Mardan Eins"]

    ### Create a mapping of the directory name in the all images folder, to the correct character name and weapon name, plus resulting folder name.
    ### Then check if the resulting folder exists, and if it has all 4 images (ends in side1, side2, main, and stats)
    ### If it does, then we can skip that folder, otherwise we need to process it.

    allImageDirectories = remove_already_processed_folders(characters, weapons, allImageDirectories, output_folder)

    for imageDirectory in allImageDirectories:
        side_index = 1
        print("Processing folder: " + imageDirectory)
        for image in os.listdir(input_folder + imageDirectory):
            if image.endswith(".jpg") is not True:
                continue

            print("Processing image: " + image)
            # 0. Correct the output character and weapon name
            un_typed_image_path_prefix = get_output_path_prefix(characters, weapons, imageDirectory, output_folder)

            # 1. Read the text of an image
            input_path = input_folder + imageDirectory + "/" + image
            picture_text = read_text_from_image(input_path)


            # 2. Determine the type of image
            image_type = determine_picture_type(picture_text)
            if image_type is None:
                unmatched_images.append({
                    'path': input_path,
                    'text': picture_text
                })
                continue

            if image_type == "Side":
                image_type = "Side" + str(side_index)
                side_index += 1

            # 3. Concatenate the parent folder name with the type of image as the destination name
            output_path = un_typed_image_path_prefix + "_" + image_type + ".jpg"
            # 4. Copy paste the image from input into the output directory
            shutil.copy(input_path, output_path)

            print("Created image: " + output_path)
            print("------------------------------------")
            print(picture_text)
            print("------------------------------------")

    # Output error messages and paths at the end
    if unmatched_images:
        print("\033[91mCould not determine the image type for the following images:\033[0m")
        for error in unmatched_images:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("Image path: " + error['path'])
            print("Read text was: " + error['text'])
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
