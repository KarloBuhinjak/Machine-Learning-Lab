import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn.linear_model as lm
from sklearn import linear_model

from sklearn.metrics import mean_squared_error,max_error,mean_squared_log_error,r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler,StandardScaler


df = pd.read_csv('cars_processed.csv')
print(df.info())

#odabir ulaznih velicina
df.drop(['name','mileage'],axis=1)
print(df.info())

x=df[['km_driven','year','engine','max_power']]
y=df['selling_price']

#podijela na train i test
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=300)
print(x_train.shape)

#skaliranje ulaznih velicina
Scaler=MinMaxScaler()
x_train_s=Scaler.fit_transform(x_train)
x_test_s=Scaler.transform(x_test)

#izrada modela
linear_model = LinearRegression()
linear_model.fit(x_train_s,y_train)