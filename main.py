
import os

import cv2
from yolofolder.yolo import predictlabellocation, getcropedimage
from number import load_exp_number
from ocr import gettext


def translate_image():
    image_dir = 'imageinput'

    for filename in os.listdir(image_dir):
        if filename.endswith('.jpg'): 
            image_path=os.path.join(image_dir, filename)
            img = cv2.imread(image_path)
            if img is not None:
                print("Yolo starting")
                predictlabellocation(image_path)
                exp_num=  load_exp_number() # at this point detect.py should have created the txt file/update number
                getcropedimage(image_path,exp_num)
                print("Yolo done! Goodbye")
