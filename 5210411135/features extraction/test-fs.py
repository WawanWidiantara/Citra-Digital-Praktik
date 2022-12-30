import cv2
import numpy as np
import pandas as pd
from copy import deepcopy
import os
# from copy import deepcopy

datastore = {
    'gambar' : [],
    'red' : [],
    'green' : [],
    'blue' : [],
    'label' : []   
}

def featuresExtract(imgpath):
    img = cv2.imread(imgpath)
    b, r, g = cv2.split(img)
        
    sum_r = round(np.mean(r))
    sum_g = round(np.mean(g))
    sum_b = round(np.mean(b))
    
    return [sum_r, sum_g, sum_b]


def testing(x_train, y_train, testpath):
    dt_test = [featuresExtract(testpath)]
    jarak = np.sum(abs(dt_test - x_train), axis=1)
    val_dekat = min(jarak)
    index = np.where(jarak == val_dekat)[0][0]
    prediksi = y_train[index]
    
    return prediksi
        
        
directory = "D:/Citra Digital Praktik/5210411135/image"
files = os.listdir(directory)
training = deepcopy(datastore)
    
for f in files:
    imgpath = os.path.join(directory, f)
    sum_channel = featuresExtract(imgpath)
    training['gambar'].append(f)
    training['red'].append(sum_channel[0])
    training['green'].append(sum_channel[1])
    training['blue'].append(sum_channel[2])
    training['label'].append(f[0:-4])
    
    training_df = pd.DataFrame(training)
    
    
dirpath = "D:/Citra Digital Praktik/5210411135/imgtest"
fltest = os.listdir(dirpath)
datatest = deepcopy(datastore)

for f in fltest:
    testpath = os.path.join(dirpath, f)
    datates = featuresExtract(testpath)
    
    x_train = np.array(training_df[['red', 'green', 'blue']])
    y_train = np.array(training_df['label'])
    prediksi = testing(x_train, y_train, testpath)
    
    datatest['gambar'].append(f)
    datatest['red'].append(datates[0])
    datatest['green'].append(datates[1])
    datatest['blue'].append(datates[2])
    datatest['label'].append(prediksi)
    
    test_df = pd.DataFrame(datatest)
    test_df.rename(columns = {'label':'prediksi'}, inplace=True)            

print(test_df)
    
    