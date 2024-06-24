import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

data = pd.read_csv('road_accidents.csv')

print(data.head())

data = data.dropna()

data = pd.get_dummies(data, drop_first=True)

X = data[['weather', 'road_type', 'speed_limit', 'time_of_day']]
y = data['severity']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Save the model
with open('accident_severity_model.pkl', 'wb') as file:
    pickle.dump(model, file)

# Load the model
with open('accident_severity_model.pkl', 'rb') as file:
    loaded_model = pickle.load(file)

# Hypothetical data
hypothetical_data = np.array([[2, 1, 60, 3]]) 

# Predict
predicted_severity = loaded_model.predict(hypothetical_data)
print(f'Predicted Accident Severity: {predicted_severity[0]}')
