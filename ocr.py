"""
-make sure paths are correct ( they should be but double check)
-exp_number.txt initialy should have 1 in it assuming runs/detect have 
    no exp yet except exp ( no exp2,exp3...etc)
-image should be jpg
"""

import os
import easyocr
from yolofolder.yolo import predictlabellocation, getcropedimage
from number import load_exp_number
result=[]
def gettext(exp_num):
 
    # Create a reader for English
    reader = easyocr.Reader(['en'])
    for file in os.listdir("ocrimage/"+str(exp_num)):
        result.append(reader.readtext(f'ocrimage/{exp_num}/{file}'))

    for r in result:
        for location, text, acc in r:
            print(f"Location: {location}, Text: {text}")

gettext('original_masked/165_jpg.rf.4caf175097e65b1287ba67ff2e7bad29.jpg')