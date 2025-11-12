import pandas as pd 
import datetime
#from sklearn.model_selection import train_test_split
#from sklearn.linear_model import LinearRegression
#import matplotlib.pyplot as plt

ds = pd.read_csv('btcusd_1-min_data.csv')

print(ds.head())
print(ds.tail())

#x = ds['Timestamp'].apply(lambda h: datetime.datetime.fromtimestamp(h))
#y = ds['High']

#x_training, x_test, y_training, y_test = train_test_split(x, y, test_size=1/3, random_state=0)

#regressor = LinearRegression()

#regressor.fit(x_training, y_training)
#y_pred = regressor.predict(x_test)

#plt.figure(figsize=(15,8))
#plt.plot(x_test, 'Dr')
#plt.plot(x_training, regressor.predict(x_training), color='blue')
#plt.title("Linear Regression of Bitcoin's Maximum Value per Minute")
#plt.xlabel('TIMING')
#plt.ylabel('MAXIMUN VALUE')
#plt.show()