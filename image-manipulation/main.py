from PIL import Image
import os
# Define input and output folders
input_folder = '../categorize-images/all_images/output'
middle_folder = './crop/output/'
output_folder = '../dark-cloud-website/src/api/weapons/images/'

# Create output folder if it doesn't exist
if not os.path.exists(middle_folder):
    print("Creating middle_folder folder: " + middle_folder)
    os.makedirs(middle_folder)
if not os.path.exists(output_folder):
    print("Creating output_folder folder: " + output_folder)
    os.makedirs(output_folder)

def crop_out_black_bars(image):
    width, height = image.size

    # Define crop values as percentages of the image dimensions
    topY_pct = 0
    topX_pct = 117 / 1200
    bottomY_pct = 675 / 675
    bottomX_pct = 1085 / 1200

    # Calculate actual crop values based on image dimensions
    topX = int(topX_pct * width)
    topY = int(topY_pct * height)
    bottomX = int(bottomX_pct * width)
    bottomY = int(bottomY_pct * height)

    area = (topX, topY, bottomX, bottomY)
    cropped_img = image.crop(area)
    return cropped_img

def crop_side_image_to_thumbnail(image):
    width, height = image.size

    if width > 1200 and height > 675:
        # Use new coordinates for larger images
        topX = 470
        topY = 1870
        bottomX = topX + 200
        bottomY = topY + 180
    else:
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

def process_single_image(input_path, output_folder):
    file_name = os.path.basename(input_path)
    output_path = os.path.join(output_folder, file_name)

    # Open the image
    image = Image.open(input_path)

    # Crop out black bars and save the image
    cropped_image = crop_out_black_bars(image)
    cropped_image.save(output_path)
    print(f"Saved cropped image: {output_path}")

    # If the image ends with 'Side1.jpg', create a thumbnail
    if file_name.endswith('Side1.jpg'):
        thumbnail_image = crop_side_image_to_thumbnail(image)
        thumbnail_name = get_thumbnail_name(file_name)
        thumbnail_path = os.path.join(output_folder, thumbnail_name)
        thumbnail_image.save(thumbnail_path)
        print(f"Saved thumbnail image: {thumbnail_path}")

    return cropped_image, thumbnail_image if file_name.endswith('Side1.jpg') else None

def process_images(input_folder, output_folder):
    for file_name in os.listdir(input_folder):
        if file_name.endswith('.jpeg') or file_name.endswith('.jpg'):
            input_path = os.path.join(input_folder, file_name)
            process_single_image(input_path, output_folder)


def optimize_image(input_path, output_path, quality=75):
    with Image.open(input_path) as img:
        img.save(output_path, optimize=True, quality=quality)

def optimize_images_in_directory(directory, output_directory, quality=75):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for filename in os.listdir(directory):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            input_path = os.path.join(directory, filename)
            output_path = os.path.join(output_directory, filename)
            optimize_image(input_path, output_path, quality)
            print(f'Optimized {filename}')

if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == 'dev':
        test_image_name = "Toan_Mardan_Eins_Side1.jpg"
        test_image_path = os.path.join(input_folder, test_image_name)

        cropped_image, thumbnail_image = process_single_image(test_image_path, middle_folder)

        # Show the resulting images
        cropped_image.show()
        if thumbnail_image:
            thumbnail_image.show()
    else:
        process_images(input_folder, middle_folder)
        optimize_images_in_directory(middle_folder, output_folder)
