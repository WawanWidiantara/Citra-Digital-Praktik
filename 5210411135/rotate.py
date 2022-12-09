import cv2
import numpy as np
import math

# membaca gambar
img = cv2.imread("D:/Citra Digital Praktik/5210411135/image/fruit.jpg")
newImg = np.uint8(np.zeros((len(img), len(img[0]), 3)))

def rotate(derajat, wrap=False):
    t = math.radians((derajat))
    cos,sin = (math.cos(t), math.sin(t))
    cx,cy = (len(img)//2, len(img[0])//2)

    r = int(abs(len(img) * cos) + abs(len(img[0]) * sin)) 
    c = int(abs(len(img) * sin) + abs(len(img[0]) * cos)) 
    xs = round((r - len(img))//2)
    ys = round((c - len(img[0]))//2)
    
    affine = np.uint8(np.zeros((r, c, 3)))
    for i in range(len(img)):
        for j in range(len(img[0])):
            x = round(cx + (i-cx) * cos - (j-cy) * sin)
            y = round(cy + (i-cx) * sin + (j-cy) * cos)
            
            if (0 <= x < len(img))and(0 <= y < len(img[0])):
                newImg[x,y] = img[i,j]
            affine[x+xs,y+ys] = img[i,j]
        
    # if wrap == True:
    return affine
    # else:
    # return newImg

         
cv2.imshow("original", img)
cv2.imshow("bagi", rotate(80))

cv2.waitKey()