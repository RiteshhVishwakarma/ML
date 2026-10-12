- L1
# Data collection 
# Data cleaning pre processing
# Data analysis 
# Data visualization
# libraries - Numpy, pandas, matplotlib, seaborn


# json
- load data


import json
# load json data
def load_data(filename):
    with open(filename, "r") as f:
        data = json.load(f)

    return data

<!-- load_data("store_data.json") -->
data = load_data("store_data.json")
print(type(data))


<!-- Assignment 1 -->
cleaning and structuring our data
1. data is inconsistence -> mixed values/type
2. missing data 
3. duplicated data

# clean and structure the data
def clean_data(data):
    for user in data:
        print(user)

clean_data(data)


# clean and structure the data
def clean_data(data):
    text_to_num = {"one":1, "two":2, "three":3, "four":4, "five":5}
    for user in data:
        # clean ratings
        raw_rating = user["rating"].strip().lower()
        if(raw_rating in text_to_num):
            raw_rating = text_to_num[raw_rating]
        user["rating"] = raw_rating

