#02200201056
#AsumanBucak

from matplotlib import pyplot as plt
import cv2
import numpy as np

#görseli okutma
foto = cv2.imread("./images/anime.png",0)
cv2.imshow("image",foto)

#Histogram hesaplama
def cal_hist(gray_img):
    hist = np.zeros(shape=(256))
    (h,w) = gray_img.shape
    for i in range(w):
        for j in range(h):
            hist[gray_img[j,i]] += 1
    return hist

plt.plot(cal_hist(foto))
plt.show()

#calcHist fonksiyonu ile sağlama
# histr = cv2.calcHist([foto], [0], None, [256], [0, 256])
# plt.plot(histr)
# plt.show()