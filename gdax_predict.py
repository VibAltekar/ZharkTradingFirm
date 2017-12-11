



import quandl


gdax = quandl.get('GDAX/USD', returns='pandas')
gdax["WP"] = (gdax["Open"][0] + gdax["High"][0] + gdax["Low"][0])/3
for i in range(0,1033):
    gdax["WP"][i] = (gdax["Open"][i] + gdax["High"][i] + gdax["Low"][i])/3
gdax.drop(gdax.columns[[0]],axis=1,inplace=True)
gdax["tomHIGH"] = gdax["High"][1]

for i in range(1032):
    gdax["tomHIGH"][i] = gdax["High"][i+1]
gdax.drop(gdax.tail(1).index,inplace=True)
