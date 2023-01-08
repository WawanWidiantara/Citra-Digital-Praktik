# %%
import cv2
import numpy as np

# %% read image
ori = cv2.imread("D:/Citra Digital Praktik/5210411135/image/fruit.jpg")
row, column = ori.shape[:2]

# %% padding
img = np.zeros(((row + 2, column + 2, 3))).astype(np.uint8)
img[1:-1, 1:-1] = ori
prow, pcolumn = img.shape[:2]
newImg = np.zeros(ori.shape).astype(np.uint8)

# %% kernel
#  kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]]) # sharp
kernel = np.array([[1, 2, 1], [1, 4, 1], [1, 2, 1]]) # blur

t_kernel = kernel.sum()
if t_kernel == 0:
    t_kernel = 1
    
# %% looping
for i in range(1, prow - 1):
    for j in range(1, pcolumn - 1):
        for k in range(3):
            mconv = img[i - 1 : i + 2, j - 1 : j + 2, k]
            konvolusi = np.round((mconv * kernel).sum() / t_kernel)
            
            if konvolusi > 255:
                konvolusi = 255
            if konvolusi < 0:
                konvolusi = 0

            newImg[i-1, j-1, k] = konvolusi
            
# %% show imaage
cv2.imshow("ori", ori)
cv2.imshow("konvolusi", newImg)
cv2.waitKey()
