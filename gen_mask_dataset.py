import sys
import cv2
import numpy as np

from pathlib import Path
maskdir = Path(__file__).resolve().parent
ocr_dir = maskdir.parents[0]
sys.path.append(str(ocr_dir))  #parent of yolofolder

from number import save_exp_number,load_exp_number

def yolo_to_pixel(yolo_x1, yolo_y1, yolo_x2, yolo_y2, img_width, img_height):
    """
    Converts Yolo bounding box coordinates to pixel coordinates

    Source: https://stackoverflow.com/a/64097592
    """

    pixel_x1 = int((yolo_x1 - yolo_x2 / 2) * img_width)
    pixel_x2 = int((yolo_x1 + yolo_x2 / 2) * img_width)
    pixel_y1 = int((yolo_y1 - yolo_y2 / 2) * img_height)
    pixel_y2 = int((yolo_y1 + yolo_y2 / 2) * img_height)

    if pixel_x1 < 0:
        pixel_x1 = 0
    if pixel_x2 > img_width - 1:
        pixel_x2 = img_width - 1
    if pixel_y1 < 0:
        pixel_y1 = 0
    if pixel_y2 > img_height - 1:
        pixel_y2 = img_height - 1
    
    # Extend the mask by 4 pixels on each side to account for small errors in detection
    pixel_x1 -= 4
    pixel_y1 -= 4
    pixel_x2 += 4
    pixel_y2 += 4

    return (pixel_x1, pixel_y1), (pixel_x2, pixel_y2)


def generate_masks(input_dir, output_dir):
    """
    Generates a mask for each .png file in the specified input directory
    based on the output from YoloV5
    """

    input_path = Path(input_dir)
    print(input_path)
    for file in input_path.glob('*.jpg'):

        img = cv2.imread(str(file))
        img_height, img_width, _ = img.shape

        mask = np.zeros((img_height, img_width))

        try:
            coordinates_file = open(f'yolofolder/yolov5/runs/detect/exp{load_exp_number()}/labels/' + file.stem + '.txt', 'r')
        except FileNotFoundError:
            print("No coordinates found for", file.stem)
            continue

        coordinates = coordinates_file.readlines()
        coordinates_file.close()
        print(coordinates)
        for line in coordinates:
            _, x1, y1, x2, y2 = map(float, line.split(' '))

            point1, point2 = yolo_to_pixel(x1, y1, x2, y2, img_width, img_height)

            cv2.rectangle(mask, point1, point2, (255, 255, 255), -1)

        cv2.imwrite(output_dir + '/' + file.stem + '_mask001.jpg', mask)


def main(input_dir, output_dir):
    print('\nGenerating Masks\n')

    generate_masks(input_dir, output_dir)

    print('Masks generated\n')


if __name__ == "__main__":
    main("original_masked","original_masked")