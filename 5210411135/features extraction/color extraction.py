import cv2
import numpy as np
import pandas as pd
from copy import deepcopy
import os


def featuresExtract(imgpath):
    img = cv2.imread(imgpath)
    b, r, g = cv2.split(img)
        
    sum_r = np.mean(r)
    sum_g = np.mean(g)
    sum_b = np.mean(b)
    
    return [sum_r, sum_g, sum_b]


def featuresExtractManual(imgpath):
    img = cv2.imread(imgpath)
    b, r, g = cv2.split(img)
    
    sum_r = 0
    sum_g = 0
    sum_b = 0
    for i in range(len(img)):
        for j in range(len(img[0])):
            # blue
            px_b = b[i, j]
            sum_b += px_b / (len(img) * len(img[0]))
            
            # red
            px_r = r[i, j]
            sum_r += px_r / (len(img) * len(img[0]))
            
            # green
            px_g = g[i, j]
            sum_g += px_g / (len(img) * len(img[0]))
            
    return [sum_r, sum_g, sum_b]


def testing(x_train, y_train, testpath):
    dt_test = [featuresExtract(testpath)]
    jarak = abs(dt_test - x_train)
    tot_jarak = np.sum(jarak, axis=1)
    val_dekat = min(tot_jarak)
    index = np.where(tot_jarak == val_dekat)[0][0]
    prediksi = y_train[index]
    
    return prediksi


datastore = {
    'gambar' : [],
    'red' : [],
    'green' : [],
    'blue' : [],
    'label' : []}


directory = "D:/Citra Digital Praktik/5210411135/image/DatasetDaging"
files = os.listdir(directory)
training = deepcopy(datastore)
    
for f in files:
    imgpath = os.path.join(directory, f)
    sum_channel = featuresExtract(imgpath)
    training['gambar'].append(f)
    training['red'].append(sum_channel[0])
    training['green'].append(sum_channel[1])
    training['blue'].append(sum_channel[2])
    training['label'].append(f[0:4])
    
training_df = pd.DataFrame(training)
training_df.set_index('gambar', inplace=True)   


testdir = "D:/Citra Digital Praktik/5210411135/imgtest/DatasetTestDaging"
fltest = os.listdir(testdir)
datatest = deepcopy(datastore)

for f in fltest:
    testpath = os.path.join(testdir, f)
    test_extract = featuresExtract(testpath)
    
    x_train = np.array(training_df[['red', 'green', 'blue']])
    y_train = np.array(training_df['label'])
    prediksi = testing(x_train, y_train, testpath)
    
    datatest['gambar'].append(f)
    datatest['red'].append(test_extract[0])
    datatest['green'].append(test_extract[1])
    datatest['blue'].append(test_extract[2])
    datatest['label'].append(prediksi)
  
    
datatest_df = pd.DataFrame(datatest)
datatest_df.rename(columns = {'label':'prediksi'}, inplace=True)
datatest_df.set_index('gambar', inplace=True)   


with pd.ExcelWriter('feature extraction color.xlsx') as writer:
    training_df.to_excel(writer, sheet_name='Data Training')
    datatest_df.to_excel(writer, sheet_name='Hasil Testing')


