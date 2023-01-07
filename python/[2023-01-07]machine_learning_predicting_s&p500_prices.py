#!/usr/bin/env python
# Predicts stock prices with LSTM (Long Short Term Memory)
# Import libraries
import math
import yfinance as yf
import pandas_datareader as dtr
import numpy as np
import pandas as pd
from keras.layers import Dense, LSTM
from keras.models import Sequential
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('fivethirtyeight')

information = yf.Ticker('^GSPC').history(start='2018-01-01', end='2023-01-01')
print(information.shape)

# Use only the Close prices
data = information['Close']
data

# Convert dataframe to numpy array
dataset = data.values

# Get number of rows to train model on (assuming 80% of data is used for training) and round up with math.ceil
training_data_len = math.ceil(len(dataset)*0.8)
print(training_data_len)

# Reshape and scale the data -> this is important for model accuracy
# Transforms data based on min and max values
dataset = dataset.reshape(-1, 1)
scaler = MinMaxScaler(feature_range=(0,1))
scaled_data = scaler.fit_transform(dataset)
scaled_data

# Create training data set and scaled training dataset
train_data = scaled_data[0:training_data_len,:]
# Split data, assigned to x_train and y_train
x_train = []
y_train = []

days = 100
for i in range(days, len(train_data)):
    x_train.append(train_data[i-days:i,0])
    y_train.append(train_data[i, 0])
    if i <= days:
        print(x_train)
        print(y_train)

# Convert x_train and y_train to numpy arrays for training
x_train, y_train = np.array(x_train), np.array(y_train)

# Reshape x_train to 3D from 2D since LSTM requires 3D arrays
x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
x_train.shape

# Build LSTM model and assign 50 neurons to layers 1 and 2
model = Sequential()
# Layer 1
model.add(LSTM(50, return_sequences=True, input_shape=(x_train.shape[1], 1)))
# Layer 2
model.add(LSTM(50, return_sequences=False))
# Dense layer with 25 neurons
model.add(Dense(25))
# Another dense layer with 1 neuron
model.add(Dense(1))

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error')

# Train the model
model.fit(x_train, y_train, batch_size=1, epochs=1)

# Create testing data set
test_data = scaled_data[training_data_len - days:, :]
# Create x_test and y_test
x_test = []
y_test = dataset[training_data_len:,:]
for i in range(days, len(test_data)):
    x_test.append(test_data[i-days:i,0])

# Convert data to numpy array
x_test = np.array(x_test)

# Reshape data from 2D to 3D for LSTM model
x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))

# Get model's predicted prices
predictions = model.predict(x_test)
# "Unscale" values
predictions = scaler.inverse_transform(predictions)

# Get RMSE (Root Mean Squared Error)
rmse = np.sqrt(np.mean(predictions - y_test)**2)
print(rmse)

train = data[:training_data_len].to_frame()
train.columns = ['Close']
validation = data[training_data_len:].to_frame()
validation['Predictions'] = predictions
validation

# Visualize Predictions
plt.figure(figsize=(20,8))
plt.title('S&P 500 Prices Using LSTM')
plt.xlabel('Date', fontsize=18)
plt.ylabel('Close Price in USD', fontsize=18)
plt.plot(train['Close'])
plt.plot(validation[['Close', 'Predictions']])
plt.legend(['Training', 'Actual', 'Predictions'], loc='lower right')
plt.show()

# Saved as s&p500_price_predictions under the images folder on my Github page
