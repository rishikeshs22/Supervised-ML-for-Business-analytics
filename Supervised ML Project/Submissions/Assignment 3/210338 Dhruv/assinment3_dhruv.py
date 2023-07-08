import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Load the dataset
data = pd.read_csv('CarPrice_Assignment.csv')

# Selecting only the required features
features = ['carlength', 'carwidth', 'carheight', 'enginesize', 'stroke', 'horsepower', 'price']
data = data[features]

# Splitting the dataset into training and testing sets
train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)

# Training the linear regression model
X_train = train_data.drop('price', axis=1)
y_train = train_data['price']
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluating the model on the testing set
X_test = test_data.drop('price', axis=1)
y_test = test_data['price']
y_pred = model.predict(X_test)
accuracy = r2_score(y_test, y_pred)

print("Accuracy of the model:", accuracy)

# Predicting the price for Person A's car
person_a_car = np.array([[190.9, 70.3, 54.9, 183, 3.64, 123]])
price_prediction = model.predict(person_a_car)
print("Predicted price for Person A's car:", price_prediction[0])
