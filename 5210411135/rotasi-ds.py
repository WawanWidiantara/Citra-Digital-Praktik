import cv2
import numpy as np
import matplotlib.pyplot as plt

gambar = cv2.imread('D:/Citra Digital Praktik/5210411135/image/fruit.jpg')

jml_baris = len(gambar)
jml_kolom = len(gambar[0])

rotasi = -45
rotasi_rad = 22 / 7 * rotasi / 180

matriks_baru = np.zeros((jml_baris, jml_kolom, 3))

pivot_brs = round(jml_baris / 2)
pivot_klm = round(jml_baris / 2)

for i in range (jml_baris):
    for j in range (jml_kolom):
        brs = pivot_brs + (i - pivot_brs) * np.cos(rotasi_rad) - (j - pivot_klm) * np.sin(rotasi_rad)
        klm = pivot_klm + (i - pivot_brs) * np.sin(rotasi_rad) + (j - pivot_klm) * np.cos(rotasi_rad)

        brs= round(brs)
        klm= round(klm)

        if brs < jml_baris and brs > 0:
            if klm < jml_kolom and klm > 0:
                matriks_baru[i , j] = gambar[brs,klm]
#konversi citra translasi menjadi uint8
matriks_baru = matriks_baru.astype(np.uint8)

cv2.imshow('gambar', gambar)
cv2.imshow('gambar baru' , matriks_baru)
cv2.waitKey()