import numpy as np
from sklearn.linear_model import LinearRegression

X = np.array([1,2,3,4,5]).reshape(-1,1)
y = np.array([3,5,7,9,11])

def train_model():
    model = LinearRegression()
    model.fit(X, y)
    return model

def predict_value(value):
    model = train_model()
    prediction = model.predict([[value]])
    return prediction[0]

if __name__ == "__main__":
    result = predict_value(6)
    print("Predicted salary for 6 years experience:", result)