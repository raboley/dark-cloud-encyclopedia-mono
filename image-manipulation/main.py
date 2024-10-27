from PIL import Image
import os

# Define input and output folders
input_folder = '../categorize-images/all_images/output'
output_folder = 'output'

# Create output folder if it doesn't exist
if not os.path.exists(output_folder):
    print("Creating output folder: " + output_folder)
    os.makedirs(output_folder)

def crop_out_black_bars(image):
    topY = 0
    topX = 117
    bottomY = 675
    bottomX = 1085
    area = (topX, topY, bottomX, bottomY)
    cropped_img = image.crop(area)
    return cropped_img

def crop_side_image_to_thumbnail(image):
    topY = 584
    topX = 156
    bottomY = topY + 55
    bottomX = topX + 60
    area = (topX, topY, bottomX, bottomY)
    cropped_img = image.crop(area)
    return cropped_img

def get_thumbnail_name(file_name):
    replace_string = 'Side1.jpg'
    thumbnail_string = 'Thumbnail.jpg'
    thumbnail_name = file_name.replace(replace_string, thumbnail_string)
    return thumbnail_name

def process_images(input_folder, output_folder):
    for file_name in os.listdir(input_folder):
        if file_name.endswith('.jpeg') or file_name.endswith('.jpg'):
            input_path = os.path.join(input_folder, file_name)
            output_path = os.path.join(output_folder, file_name)

            # Open the image
            image = Image.open(input_path)

            # Crop out black bars and save the image
            cropped_image = crop_out_black_bars(image)

            cropped_image.save(output_path)
            print(f"Saved cropped image: {output_path}")

            # If the image ends with 'Side1.jpeg', create a thumbnail
            if file_name.endswith('Side1.jpg'):
                thumbnail_image = crop_side_image_to_thumbnail(image)
                thumbnail_name = get_thumbnail_name(file_name)
                thumbnail_path = os.path.join(output_folder, thumbnail_name)
                thumbnail_image.save(thumbnail_path)
                print(f"Saved thumbnail image: {thumbnail_path}")

if __name__ == '__main__':
    process_images(input_folder, output_folder)
