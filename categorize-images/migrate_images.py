
import os
import shutil

def move_images(data_folder, input_folder):
    # Get all high-resolution images from the data folder
    high_res_images = []
    for root, _, files in os.walk(data_folder):
        for file in files:
            if file.endswith('.jpg') or file.endswith('.jpeg'):
                high_res_images.append(os.path.join(root, file))
    
    # Get all low-resolution images from the input folder
    low_res_images = []
    for root, _, files in os.walk(input_folder):
        for file in files:
            if file.endswith('.jpg') or file.endswith('.jpeg'):
                low_res_images.append(os.path.join(root, file))
    
    # Move high-resolution images to the corresponding subfolders in the input folder
    for low_res_image in low_res_images:
        low_res_name = os.path.basename(low_res_image)
        low_res_name_without_ext = os.path.splitext(low_res_name)[0]
        
        for high_res_image in high_res_images:
            high_res_name = os.path.basename(high_res_image)
            
            if low_res_name_without_ext in high_res_name:
                destination_folder = os.path.dirname(low_res_image)
                destination_path = os.path.join(destination_folder, high_res_name)
                
                # Move the high-resolution image
                shutil.move(high_res_image, destination_path)
                print(f'Moved {high_res_image} to {destination_path}')
                break

# Example usage
data_folder = 'all_images/data'
input_folder = 'all_images/input'
move_images(data_folder, input_folder)