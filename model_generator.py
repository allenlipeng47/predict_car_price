import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
import pickle

# Read the Excel data into a pandas DataFrame
data = pd.read_csv('./odyssey_year_odometer_price.csv')

data['age'] = 2023 - data['year']
model = LinearRegression()

X = data[['odometer', 'age']]  # Features
y = data['price']  # Target variable

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model.fit(X_train, y_train)

# Make predictions on the testing set
y_pred = model.predict(X_test)

# Calculate the Mean Absolute Error (MAE)
MAE = mean_absolute_error(y_test, y_pred)
print("MAE:", MAE)

with open('odyssey_year_odometer_price.pkl', 'wb') as f:
    pickle.dump(model, f)
