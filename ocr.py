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
result={}
returend_result={}
def gettext(exp_num):#each image in each sample has a key
 
    # Create a reader for English
    reader = easyocr.Reader(['en'])
    for file in os.listdir("ocrimage/"+str(exp_num)):
        result[int(file.split('roi')[1].split('.')[0])]=reader.readtext(f'ocrimage/{exp_num}/{file}')

    
    for key in result.keys():#key is number after roi ,=> line number in run/exp/label
       
        for r in result[key]:
            
            location, text, acc = r
            returend_result[key]={'text':text}
    return returend_result
