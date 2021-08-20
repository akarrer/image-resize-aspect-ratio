# this app resizes an image while maintaining the aspect ratio


import os, sys
import PIL.Image
from PIL import Image, ImageFilter
import math

def resizeImage(numPixels, imagePath):
    with Image.open(imagePath) as img:
        currentImageHeight = img.height
        currentImageWidth = img.width
        aspectRatio = currentImageWidth / float(currentImageHeight)
        newWidth = math.floor(math.sqrt(numPixels / aspectRatio))
        newHeight = math.floor(aspectRatio * newWidth)
        newImage = img.resize((newHeight, newWidth), resample=PIL.Image.LANCZOS)

        newImage.save("parrotLANCZOS.jpg", quality=99)
        imgSharpened = newImage.filter(ImageFilter.SHARPEN)
        imgSharpened.save("parrotsharpened2.jpg")

desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), "Desktop")
fullFileName = os.path.join(desktop, "parrot.jpg")
resizeImage(2814, fullFileName)
