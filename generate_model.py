import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
import pickle
import configparser

config = configparser.ConfigParser()
config.read('./CONFIG')

MODEL_NAME = config['DEFAULT']['MODEL_NAME']
CURRENT_YEAR = int(config['DEFAULT']['CURRENT_YEAR'])

file_data = "./%s/data.csv" % MODEL_NAME
file_model = "./%s/model.pkl" % MODEL_NAME

# Read the Excel data into a pandas DataFrame
data = pd.read_csv(file_data)

data['age'] = CURRENT_YEAR - data['year']
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
print("Model created at %s" % file_model)

with open(file_model, 'wb') as f:
    pickle.dump(model, f)
