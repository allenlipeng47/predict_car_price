import pandas as pd
import pickle
import configparser

# update the variable here
ODOMETER = 98
YEAR_MAKE = 2017

# read config
config = configparser.ConfigParser()
config.read('./CONFIG')

MODEL_NAME = config['DEFAULT']['MODEL_NAME']
CURRENT_YEAR = int(config['DEFAULT']['CURRENT_YEAR'])

new_data = pd.DataFrame({
    'odometer': [ODOMETER],
    'age': [CURRENT_YEAR - YEAR_MAKE]
})

file_model = "./%s/model.pkl" % MODEL_NAME

with open(file_model, 'rb') as f:
    model = pickle.load(f)

# Make predictions for the new car
new_price = model.predict(new_data[['odometer', 'age']])

# Print the predicted price
print("Predicted Price:{:,}".format(int(new_price[0])))
