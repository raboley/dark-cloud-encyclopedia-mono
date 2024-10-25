## read the text in the picture pictures/Ruby_Goddess_Ring-Main.jpg

import easyocr
from PIL import Image

def read_text_from_image(image_path):
    """
    Reads text from an image using EasyOCR.

    :param image_path: Path to the image file.
    :return: Extracted text from the image.
    """
    try:
        # Initialize the EasyOCR reader
        reader = easyocr.Reader(['en'])  # Specify the languages you want to use

        # Read the text from the image
        result = reader.readtext(image_path)

        # Extract the text from the result
        extracted_text = " ".join([text[1] for text in result])
        
        return extracted_text
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    images = ['pictures/Ruby_Goddes_Ring-Main.jpg', 'pictures/Ruby_Crystal_Ring_Side1.jpg', "pictures/Toan_Choora_Stats.jpg", "pictures/Ruby_Crystal_Ring_Stats.jpg"]
    for image_path in images:
        print("-------------------------------------")
        print("Reading text from image:", image_path)

        extracted_text = read_text_from_image(image_path)
        print("Extracted Text:")
        print(extracted_text)
        print("-------------------------------------")