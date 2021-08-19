# image resize app


import os, sys
import PIL.Image
from PIL import Image
import math



def resizeImage(numPixels, imagePath):
    with Image.open(imagePath) as img:
        currentImageHeight = img.height
        currentImageWidth = img.width
        aspectRatio = currentImageWidth / float(currentImageHeight)
        newWidth = math.floor(math.sqrt(numPixels / aspectRatio))
        newHeight = math.floor(aspectRatio * newWidth)
        newImage = img.resize((newHeight, newWidth), resample=PIL.Image.ANTIALIAS)
        newImage.save("parrotBOX.jpg")


desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), "Desktop")
fullFileName = os.path.join(desktop, "parrot.jpg")
resizeImage(2814, fullFileName)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
