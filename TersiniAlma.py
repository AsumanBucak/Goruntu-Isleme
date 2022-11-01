#Goruntuyu ters cevirme

import cv2
import numpy as np

#gorseli okutma
image = cv2.imread("./images/elric.jpg",0)
cv2.imshow("original",image)

#manuel ters çevirme
[h,w] = image.shape
new_image = np.zeros([h,w], dtype=np.uint8)
for i in range(h):
    for j in range(w):
        new_image[i,j] = 255 - image[i,j]
print(image[0,0])
cv2.imshow("Manuel_inverted",new_image)


#ters cevirme islemi saglama
inverted = np.invert(image)
cv2.imshow("inverted",inverted)
negimage = 255 - image
cv2.waitKey()
