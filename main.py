
import os
import shutil
import easyocr


for filename in os.listdir('yolov5/runs/detect/'):
        if filename.startswith('exp'):
            file_path = os.path.join('yolov5/runs/detect/', filename)
            if os.path.isdir(file_path):
                shutil.rmtree(file_path)

def translate_image():
    