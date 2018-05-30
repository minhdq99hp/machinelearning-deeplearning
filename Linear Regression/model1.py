import numpy as np
import matplotlib.pyplot as plt

# INPUT DATA
# Getting data form data?.csv file
import csv

data_file = open('data2.csv')
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

# Calculating weights of the fitting line 
A = np.dot(Xbar.T, Xbar)
b = np.dot(Xbar.T, y)
w = np.dot(np.linalg.pinv(A), b)
print('w = ', w)

# Preparing the fitting line 
w_0 = w[0][0]
w_1 = w[1][0]
x0 = np.linspace(min([data_points[0] for data_points in dataset]), max([data_points[0] for data_points in dataset]), 2)
y0 = w_0 + w_1*x0

# Drawing the fitting line 
plt.plot(X.T, y.T, 'ro')     # data 
plt.plot(x0, y0)               # the fitting line

plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')
plt.show()
