# Predict Car Price
This is simple car price prediction model. It uses linear regression. It takes price, odometer as variants, price as the prediction result. Built a crawler to crawl craiglist price.

This is built with python 3.1.0.

**_Just use it to check if the car is a worth to buy!!!_**

## Step 1: Update CONFIG
Update [CONFIG](CONFIG) file. It's just a single line in the file. It defines the model, current year.

## Step2 : crawl.py
The crawler, it crawls craiglist url. Such as https://orangecounty.craigslist.org/cto/d/laguna-beach-2015-nissan-quest-low/7686040359.html

An example batch command is:
```
python crawl.py https://orangecounty.craigslist.org/cto/d/laguna-beach-2015-nissan-quest-low/7686040359.html
python crawl.py https://orangecounty.craigslist.org/cto/d/laguna-woods-2013-nissan-quest/7689145337.html
```

After each command, it appends a line consisting of year, odometer, price, url to `./[MODEL_NAME]/data.csv`.

## Step 3: generate_model.py
It reads data from `./[MODEL_NAME]/data.csv`, builds the model, and stores the generated model to `./[MODEL_NAME]/data.pkl`.

```
python generate_model.py
```

## Step 4: predict.py
In the `predict.py` file, update the `ODOMETER`, `YEAR_MAKE`. Run and get the predicted result:
```commandline
python predict.py
```
