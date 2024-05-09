
import os

import cv2
from yolofolder.yolo import predictlabellocation, getcropedimage
from number import load_exp_number
from ocr import gettext
from gen_mask_dataset import generate_masks
from opencv import inpaint

def main(image_dir):
    
    for filename in os.listdir(image_dir):
        ocr_result={}
        if filename.endswith('.jpg'): 
            image_path=os.path.join(image_dir, filename)
            img = cv2.imread(image_path)
            if img is not None:

                print("\n********** Yolo starting **********\n")
                predictlabellocation(image_path)# exp_number.txt file number updates
                exp_num=  load_exp_number() # at this point detect.py should have created the txt file/update number
                getcropedimage(image_path,exp_num)
                print("\n********** Yolo done! Goodbye **********\n")

                print("\n********** Generating masks **********\n")
                generate_masks(image_path,image_dir, exp_num)#image_path to ensure we work with one image at a time (exp_number exists)
                print("\n********** Masks generated **********\n")

                print("\n********** Inpaint starting **********\n")
                inpaint(image_path,f'{image_path[:-4]}_mask001.jpg',exp_num)
                print("\n********** Inpaint done! Goodbye **********\n")

                print("\n********** OCR starting **********\n")
                ocr_result=gettext(exp_num)
                print("\n********** OCR done! Goodbye **********\n")

                




if __name__ == "__main__":
    main('imageinput')
