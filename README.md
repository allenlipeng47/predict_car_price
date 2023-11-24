# predict_car_price
This is simple car price prediction model. It uses linear regression. It takes price, odometer as variants, price as the prediction result. Built a crawler to crawl craiglist price.

**_Just use it to check if your car is a worth to buy!!!_**

## crawl.py
The crawler, it crawls craiglist url. Such as https://losangeles.craigslist.org/lac/cto/d/south-pasadena-honda-odyssey/7687944106.html

The command is:
```
python crawl.py https://losangeles.craigslist.org/lac/cto/d/south-pasadena-honda-odyssey/7687944106.html
```

After each command, it appends a line consisting of year, odometer, price, url to `odyssey_year_odometer_price.csv`.

## model_generator.py
It reads data from `odyssey_year_odometer_price.csv`, builds the model, and stores to `odyssey_year_odometer_price.pkl` file.

```
python model_generator.py
```

## predict.py
Just put the odometer, car year. Output predicted price.
