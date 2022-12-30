import numpy as np
import pandas as pd

# tr = np.array([[123,176,90],
#                [112,70,6],
#                [111,85,10]])
# lb = np.array(['babi', 'sapi', 'babi'])

# ts = np.array([[111,80,12]])

# sm = np.sum(abs(ts-tr), axis=1)
# a = min(sm)
# ind = np.where(sm == a)[0][0]

# print(f'data test\t: {ts}\nprediksi\t: {lb[ind]}')

# print(round(np.mean(tr)))

training = {
    'gambar' : ['adddragronfruit.jpg', 'fruit.jpg', 'kalimerah.jpg', 'minusbucket.jpg'],
    'red' : [4, 144, 151, 172],
    'green' : [10, 186, 255, 197],
    'blue' : [5, 125, 151, 161],
    'label' : []   
}

training_df = pd.DataFrame.from_dict(training, orient='index').T
a = np.array(training_df[['red', 'green', 'blue']])