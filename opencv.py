import cv2

img = cv2.imread('original_masked/165_jpg.rf.4caf175097e65b1287ba67ff2e7bad29.jpg', 1)

mask=cv2.imread('original_masked/165_jpg.rf.4caf175097e65b1287ba67ff2e7bad29_mask001.jpg',0)

img=cv2.inpaint(img,mask,20,cv2.INPAINT_TELEA)

cv2.imwrite('output.jpg', img)