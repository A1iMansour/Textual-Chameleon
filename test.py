import os


image_dir = 'imageinput'
for filename in os.listdir(image_dir):
        ocr_result={}
        if filename.endswith('.jpg'): 
                image_path=os.path.join(image_dir, filename)
                print(image_path[:-4])