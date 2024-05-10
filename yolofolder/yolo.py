import os
import subprocess
import glob
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

#use this function to make predictions
def predictlabellocation(image_path):
    command = f"python yolofolder/yolov5/detect.py --weights  yolofolder/last.pt --img 640 --conf 0.4 --source {image_path} --save-txt"
    subprocess.run(command, shell=True, check=True)
    print("YOLO finished predicting labellocation")
    print("YOLO finished predicting labellocation")


#use this function to get the cropped image
def getcropedimage(image_path, num):# chose path and exp number to get the cropped image
    image= Image.open(image_path)
    bbox = getyolocoordinate(num)
    for key in bbox:
        left = bbox[key][0] - bbox[key][2] / 2
        upper = bbox[key][1] - bbox[key][3] / 2
        right = bbox[key][0] + bbox[key][2] / 2
        lower = bbox[key][1] + bbox[key][3] / 2
        
        # Convert to pixel coordinates
        width, height = image.size
        left, upper, right, lower = map(int, [left * width, upper * height, right * width, lower * height])
        
        # Extract the region of interest (ROI)
        roi = image.crop((left, upper, right, lower))
        
        
        plt.imshow(roi)
        roi2 =roi.convert('RGB')
        try:
            save_image(roi2, num,key)#key is line number in run/exp/label
            print("image saved")
            
        except:
            print("error saving image")


    #return bbox # function returns bbox dictionary (key:label, value: location)
        
def save_image(roi2, num,key):
    # Define the directory where you want to save the images
    directory = f'ocrimage/{num}'
    directory2=f'inpaintout/{num}'#to save inpainted output
    # Create the directory if it does not exist
    if not os.path.exists(directory):
        os.makedirs(directory)
    # Save the image in the directory
    roi2.save(f'{directory}/roi{key}.jpg')
    if not os.path.exists(directory2):
        os.makedirs(directory2)
    if not os.path.exists(directory2):
        os.makedirs(directory2)






"""this gets coordinate for single image"""
def getyolocoordinate(expnum):
# Get a list of all output .txt files
    txt_files = glob.glob(f'yolofolder/yolov5/runs/detect/exp{expnum}/labels/*.txt')
    bbox = {}
    # For each .txt file
    label=0
    for txt_file in txt_files:
        # Open the file
        with open(txt_file, 'r') as f:
            # For each line in the file
            for line in f:
                # Split the line into components
                components = line.strip().split()
                # The remaining components are the bounding box coordinates
                bbox[label] = [float(x) for x in components[1:]]
                label+=1
    return bbox


