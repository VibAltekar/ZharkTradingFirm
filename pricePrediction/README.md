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
    - Using a Stateful RNN (batch memories are passed to the next batch for long term sequences)
      - TBD
  - Moving forward
    - Should we be using shuffle=False? 
    - Dropout? 
    - Initial embedding layer? 