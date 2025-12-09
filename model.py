import numpy as np
from sklearn.linear_model import LinearRegression
import joblib

#create random data with np
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([3, 5, 7, 9, 11])
print("data created")

# model initialisation 
model = LinearRegression()
model.fit(X, y)
print("model fitted")

# save the model
joblib.dump(model, "model.pkl")
print("model trained and saved")