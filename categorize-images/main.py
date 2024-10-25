import os
import shutil

input_folder = 'all_images/input/'
output_folder = 'all_images/output/'
allImageDirectories = os.listdir(input_folder)
from categorize.read_image_text import read_text_from_image
from categorize.image_text_decider import determine_picture_type


unmatched_images = []

if __name__ == '__main__':
    if not os.path.exists(output_folder):
        print("Creating output folder: " + output_folder)
        os.makedirs(output_folder)
    # development so we only do 1 folder at a time.
    allImageDirectories = allImageDirectories[0:1]
    for imageDirectory in allImageDirectories:
        side_index = 1
        print("Processing folder: " + imageDirectory)
        for image in os.listdir(input_folder + imageDirectory):
            print("Processing image: " + image)
            # 0. Correct the output character and weapon name
            original_character_name = imageDirectory.split("_")[0]
            original_weapon_name = imageDirectory.split("_")[1].split(".")[0]
            corrected_character_name = correct_character_name(original_character_name)
            corrected_weapon_name = correct_weapon_name(original_weapon_name)

            # 1. read the text of an image
            input_path = input_folder + imageDirectory + "/" + image
            picture_text = read_text_from_image(input_path)
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("Read text: " + picture_text)
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            # 2. determine the type of image
            image_type = determine_picture_type(picture_text)
            if image_type is None:
                print("\033[91mCould not determine the image type for " + input_path + "\033[0m")
                unmatched_images.append(input_path)
                continue
            if image_type == "Side":
                image_type = "Side" + str(side_index)
                side_index += 1

            # 3. concatenate the parent folder name with the type of image as the destination name
            output_path = output_folder + imageDirectory + "_" + image_type + ".jpg"
            # 4. copy paste the image from input into the output directory

            shutil.copy(input_path, output_path)

            print("Created image: " + output_path)

def correct_character_name(character_name):
    return character_name
    
def correct_weapon_name(weapon_name):
    return weapon_name