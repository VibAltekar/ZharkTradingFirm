# ZharkTradingFirm

A collection of algorithms used to create a BTC and ETH trading bot. The objective is to create a Q-learning agent that will utilize RNN's to trade BTC on Gdax. 

### Current RNN's 
  - RNN with one layer LSTM for one feature (weighted price)
  - RNN with one lyaer LSTM for multiple features 
  - Stateful RNN with one layer LSTM for one feature 
  - Stateful RNN with one layer LSTM for multi-day predictions

### To Do
  - Test short term data - hourly, or real-time socket data from GDAX
  - Implement the Q-learning strategy 