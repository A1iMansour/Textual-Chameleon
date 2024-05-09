import cv2



def inpaint(impath,maskpath, exp_num):
    img = cv2.imread(impath, 1)

    mask=cv2.imread(maskpath,0)
    print(impath)
    print(maskpath)
    img=cv2.inpaint(img,mask,20,cv2.INPAINT_TELEA)
    cv2.imwrite(f'inpaintout/{exp_num}/output.jpg', img)