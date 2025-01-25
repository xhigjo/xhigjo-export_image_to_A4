from PIL import Image
import cv2
import os
import numpy as np
import math

CUR_DIR = os.path.realpath(__file__).replace("\\","/")
FILENAME = CUR_DIR.split("/")[-1]
CUR_DIR = CUR_DIR.replace(FILENAME, "")

# define input folder and make sure it exists
IMAGES_DIR = os.path.join(CUR_DIR, 'images')
if not os.path.exists(IMAGES_DIR):
    os.mkdir(IMAGES_DIR)

# define output folder and make sure it exists
IMAGES_DIR_OUT = os.path.join(CUR_DIR, "images_out")
if not os.path.exists(IMAGES_DIR_OUT):
    os.mkdir(IMAGES_DIR_OUT)

# read filenames of images in the IMAGES_DIR path
images = os.listdir(IMAGES_DIR)

# define final output ratio for images
RATIO_OUT = math.sqrt(2)

for image in images:
    print(image)

    # use PIL for reading images since cv2 suffers of the "large tEXt chunks" bug of libpng
    img = Image.open(os.path.join(IMAGES_DIR, image)).convert('RGB')
    img_cv = np.array(img)[:, :, ::-1].copy()    # Convert RGB to BGR
    
    print(img_cv.shape)
    width = float(img_cv.shape[1])
    height = float(img_cv.shape[0])
    ratio = width/height

    if ratio >= RATIO_OUT:  # longer than needed => increase height
        height = int(width / RATIO_OUT)
    else:                    # higher than needed => increase width
        width = int(height * RATIO_OUT)

    width = int(width)
    height = int(height)

    print("\n")
    resized = cv2.resize(img_cv,(width,height),interpolation = cv2.INTER_LANCZOS4)
    cv2.imwrite(os.path.join(IMAGES_DIR_OUT,image), resized)

