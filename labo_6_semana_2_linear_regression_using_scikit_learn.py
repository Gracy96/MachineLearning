# -*- coding: utf-8 -*-
"""Labo 6 - Semana 2: Linear Regression using Scikit-Learn

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1pOmfLevCtc5sI3U_6_6827YGR1OU2tC8
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from lab_utils_multi import load_house_data
plt.style.use('./deeplearning.mplstyle')
np.set_printoptions(precision=2)

X_train = np.array([1.0, 2.0])   #features
y_train = np.array([300, 500])   #target value

linear_model = LinearRegression()
#X must be a 2-D Matrix
linear_model.fit(X_train.reshape(-1, 1), y_train)

b = linear_model.intercept_
w = linear_model.coef_
print(f"w = {w:}, b = {b:0.2f}")
print(f"'manual' prediction: f_wb = wx+b : {1200*w + b}")

y_pred = linear_model.predict(X_train.reshape(-1, 1))

print("Prediction on training set:", y_pred)

X_test = np.array([[1200]])
print(f"Prediction for 1200 sqft house: ${linear_model.predict(X_test)[0]:0.2f}")
