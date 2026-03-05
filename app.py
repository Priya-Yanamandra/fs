from sklearn.linear_model import LinearRegression
import numpy as np

X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 6, 8, 10])

def train_model():
    model = LinearRegression()
    model.fit(X, y)
    return model

def predict_value(value):
    model = train_model()
    prediction = model.predict(np.array([[value]]))
    return prediction[0]

if __name__ == "__main__":
    result = predict_value(6)
    print("Prediction:", result)