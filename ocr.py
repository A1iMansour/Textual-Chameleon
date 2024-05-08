"""
-make sure paths are correct ( they should be but double check)
-exp_number.txt initialy should have 1 in it assuming runs/detect have 
    no exp yet except exp ( no exp2,exp3...etc)
"""

import os
import easyocr
import numpy as np
from yolofolder.yolo import predictlabellocation, getcropedimage
from number import load_exp_number
result=[]
def gettext(image_path):
 
    # Create a reader for English
    reader = easyocr.Reader(['en'])
    print("entering predictlabellocation")
    predictlabellocation(image_path)
    exp_num=  load_exp_number() # at this point detect.py should have created the txt file/update number
    print("entering getcropedimage")
    getcropedimage(image_path,exp_num)
    print("Yolo done! Goodbye")
    for file in os.listdir("ocrimage/"+str(exp_num)):
        result.append(reader.readtext(f'ocrimage/{exp_num}/{file}'))

    for r in result:
        for location, text, acc in r:
            print(f"Location: {location}, Text: {text}")

gettext('images/624f3adced5fe-product.jpg')