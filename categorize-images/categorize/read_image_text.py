## read the text in the picture pictures/Ruby_Goddess_Ring-Main.jpg

import pytesseract
from PIL import Image

def read_text_from_image(image_path):
    """
    Reads text from an image using Tesseract OCR.

    :param image_path: Path to the image file.
    :return: Extracted text from the image.
    """
    try:
        # Open the image file
        img = Image.open(image_path)

        # Use pytesseract to do OCR on the image
        text = pytesseract.image_to_string(img)

        return text
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    images = ['pictures/Ruby_Goddes_Ring-Main.jpg', 'pictures/Ruby_Crystal_Ring_Side1.jpg', "pictures/Toan_Choora_Stats.jpg", "pictures/Ruby_Crystal_Ring_Stats.jpg"]
    # image_path = 'pictures/Ruby_Goddes_Ring-Main.jpg'
    for image_path in images:
        print("-------------------------------------")
        print("Reading text from image:", image_path)

        extracted_text = read_text_from_image(image_path)
        print("Extracted Text:")
        print(extracted_text)
        print("-------------------------------------")
