# this app resizes an image while maintaining the aspect ratio

import os, sys
import PIL.Image
from PIL import Image, ImageFilter
import math

def resize_image(num_pixels, image_path):
    with Image.open(imagePath) as img:
        current_image_height = img.height
        current_image_width = img.width
        aspect_ratio = current_image_width / float(current_image_height)
        new_width = math.floor(math.sqrt(num_pixels / aspect_ratio))
        new_height = math.floor(aspect_ratio * new_width)
        new_image = img.resize((new_height, new_width), resample=PIL.Image.LANCZOS)
        new_image.save("parrotLANCZOS.jpg", quality=95)
        img_sharpened = new_image.filter(ImageFilter.SHARPEN)
        img_sharpened.save("parrotsharpened2.jpg")

desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), "Desktop")
full_file_name = os.path.join(desktop, "parrot.jpg")
resize_image(2814, full_file_name)
