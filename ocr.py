"""
-image should be jpg
"""

import os
import easyocr
from yolofolder.yolo import predictlabellocation, getcropedimage
from number import load_exp_number
result={}
returend_result={}
def gettext(exp_num):#each image in each sample has a key
 
    # Create a reader for English
    reader = easyocr.Reader(['en'])
    for file in os.listdir("ocrimage/"+str(exp_num)):
        result[int(file.split('roi')[1].split('.')[0])]=reader.readtext(f'ocrimage/{exp_num}/{file}')

    print(result)
    for key in result.keys():
        print(result[key][0])
        for r in result[key]:
            print(r)
            location, text, acc = r
            returend_result[key]={'location':location , 'text':text}
    return returend_result
