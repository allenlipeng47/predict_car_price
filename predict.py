import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
import pickle

with open('odyssey_year_odometer_price.pkl', 'rb') as f:
    model = pickle.load(f)

new_odometer = 74
new_age = 2023 - 2012

new_data = pd.DataFrame({
    'odometer': [new_odometer],
    'age': [new_age]
})

# Make predictions for the new car
new_price = model.predict(new_data[['odometer', 'age']])

# Print the predicted price
print("Predicted Price:{:,}".format(int(new_price[0])))
