## Models 

### Price Data
  - View the correlation between cryptocurrencies. 

### One Variable LSTM

  - Use the weighed price to predict the values of 2017. 
  - Hyperparametrizing efforts
    - Using a look_back size of one seems to have the greatest results compared to greater lookbacks. This could be attributed to the idea that the price from two days ago will not affect the price for the next day. 
      - This should be tested with minute based data though. 
    - Multi-layer LSTM's do not perform as well as a one layer LSTM. I tried passing in the output sequences from the initial layers (using Keras' return_sequences=True method) to the next layers, but that increased the MSE. 
    - Using a one layer LSTM with 150 nodes provided the lowest MSE for the data. 
      - This should be tested with multi-variable model.  
    - Dropout 
      - Increases MSE but decreases overfitting. It should definitely be included. Tested with 0.3 and 0.1 dropout. 
  - Normalization 
    - MinMaxScaler by SKlearn. 
    - Differentiation between points (negative or positive increase over period of time).

### Stateful RNN
  - Results are equivalent to using a stateless network with LSTM's. 
  - multi-day prediction has a low RMSE for day two and day three (expected). This could be effective for long term intervals with short-term data (within the hour, or maybe even hourly). 