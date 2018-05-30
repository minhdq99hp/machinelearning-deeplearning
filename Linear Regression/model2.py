import numpy as np 
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model

# INPUT DATA
# Getting data form data?.csv file
import csv

data_file = open('data.csv')
data_file_reader = csv.reader(data_file)
raw_data = list(data_file_reader)

dataset = []
for data_points in raw_data:
	dataset.append([float(data_points[0]), float(data_points[1])])

# height 
X = np.array([[data_points[0] for data_points in dataset]]).T
# weight
y = np.array([[data_points[1] for data_points in dataset]]).T

# Building Xbar 
one = np.ones((X.shape[0], 1))
Xbar = np.concatenate((one, X), axis = 1)



# fit the model by Linear Regression
regr = linear_model.LinearRegression(fit_intercept=False) # fit_intercept = False for calculating the bias
regr.fit(Xbar, y)

print('Solution found by scikit-learn: ', regr.coef_)



# Preparing the fitting line 
w_0 = regr.coef_[0][0]
w_1 = regr.coef_[0][1]
x0 = np.linspace(min([data_points[0] for data_points in dataset]), max([data_points[0] for data_points in dataset]), 2)
y0 = w_0 + w_1*x0

# Drawing the fitting line 
plt.plot(X.T, y.T, 'ro')     # data 
plt.plot(x0, y0)               # the fitting line

plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')
plt.show()
