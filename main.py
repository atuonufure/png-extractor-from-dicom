import os

import numpy as np
import pydicom
from PIL import Image as Img


def get_names(path):
    names = []
    for root, dirnames, filenames in os.walk(path):
        for filename in filenames:
            _, ext = os.path.splitext(filename)
            if ext in [".dcm"]:
                names.append(filename)
    return names


def convert_dcm_jpg(name):
    im = pydicom.dcmread("dicom-files/" + name)
    im = im.pixel_array.astype(float)
    rescaled_image = (np.maximum(im, 0) / im.max()) * 255  # float pixels
    final_image = np.uint8(rescaled_image)  # integers pixels
    final_image = Img.fromarray(final_image)
    return final_image


def create_folder(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)


def main():
    names = get_names("dicom-files")
    create_folder("png-files")
    for name in names:
        image = convert_dcm_jpg(name)
        image.save("png-files/" + name + ".png")


if __name__ == "__main__":
    main()
