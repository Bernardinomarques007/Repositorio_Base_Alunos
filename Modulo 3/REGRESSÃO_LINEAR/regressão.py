import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

dataset = pd.read_csv('Walmart_Vendas.csv')
x = dataset[['Vendas_Semanais']]
y = dataset[['Temperatura']]

x_training, x_test, y_training, y_test = train_test_split(x, y, test_size=1/3, random_state=0)

regressor = LinearRegression()

regressor.fit(x_training, y_training)
y_pred = regressor.predict(x_test)

plt.figure(figsize=(15,8))
plt.plot(x,y, 'Dr')
plt.title('Test of regression linear of week sells x tempeture in fahrenheit')
plt.xlabel('Weeks sells')
plt.ylabel('Tempeture in farenheit')
plt.show()

plt.figure(figsize=(15,8))
plt.plot(x_test, y_test, 'Dr')
plt.plot(x_training, regressor.predict(x_training), color='blue')
plt.title('Regression linear of sell weeks x tempeture in farenheit')
plt.xlabel('Sells weeks')
plt.ylabel('Tempeture in farenheit')
plt.show()