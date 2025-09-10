import os

from PIL import ImageChops, Image


def imagepath(dirpath, imgname ):
    return os.path.join(dirpath, imgname)

def compareimages(actual_image_path, expected_image_path):
    aimg = Image.open(actual_image_path)
    eimg = Image.open(expected_image_path)

    if aimg.size != eimg.size:
        print("Image size mismatch")

    return ImageChops.difference(aimg, eimg)