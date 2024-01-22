#i made this 
#setup block
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))
import random
from tensorflow import keras
from tensorflow.keras import layers
#creating training data
num_rows = 1000
#create two numbers randomly assigned 0 or 1 and put them in dataframe
column1 = [random.randint(0, 1) for _ in range(num_rows)] 
column2 = [random.randint(0, 1) for _ in range(num_rows)]
data = {
    'Input1': column1,
    'Input2': column2,
}
df = pd.DataFrame(data)
#calculate the correct output data
df['Anded'] = df['Input1'] & df['Input2']
df.head(10)
#this cell sets up the training and validation data
df_train = df.sample(frac=0.7, random_state=0)
df_valid = df.drop(df_train.index)


df_valid.dropna(axis=1, inplace=True)


X_valid = df_valid.drop('Anded', axis=1)
y_valid = df_valid['Anded']
#create the neural network model
model = keras.Sequential([
    layers.Dense(4, input_shape = [2], activation = 'relu'),
    layers.Dense(4, activation = 'relu'),
    layers.Dense(4, activation = 'relu'),
    layers.Dense(units = 1, activation = 'sigmoid')
])
model.compile(
    optimizer = 'adam',
    loss = 'binary_crossentropy',
    metrics = ['binary_accuracy'],
)
#train the model
history = model.fit(
    X_valid, y_valid,
    validation_data=(X_valid, y_valid),
    batch_size=32,
    epochs=2 ** 7,
    verbose=0,     
)
import numpy as np
#the model likes to make an estimate between 0 and 1, so this corrects that
def reformat(prediction):
    if prediction >= 0.5:
        return 1
    else:
        return 0
#testing the model
input_data1 = np.array([0, 1])  
input_data2 = np.array([0,0])
input_data3 = np.array([1,0])
input_data4 = np.array([1,1])
input_data1 = input_data1.reshape(1, -1) 
input_data2 = input_data2.reshape(1, -1)
input_data3 = input_data3.reshape(1, -1)
input_data4 = input_data4.reshape(1, -1)
# Make the prediction
i = 0
while i < 20:
    for data in [input_data1, input_data2, input_data3, input_data4]:
        prediction = reformat(model.predict(data))
        print(prediction)
        i +=1