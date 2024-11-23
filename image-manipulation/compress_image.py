from PIL import Image
import os

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

input_directory = 'images'
output_directory = 'optimized-images'
optimize_images_in_directory(input_directory, output_directory)
