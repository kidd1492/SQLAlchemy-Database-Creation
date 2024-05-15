import json
import pandas as pd

# open json file for read, assign it a var, load the data into a j_object
json_file = open('json_files/nps_parks.json', 'r')
jdata = json_file.read()
j_object = json.loads(jdata)

# object has 4 fields i want the data asign to var objs
objs = j_object['data']
# print(len(objs))

# make list of data dics to itterate over
data = []
for obj in objs:
    data.append(obj)

# make columns of unique values to use as park_id to start dataframe
park_id = []
count = 1001
for c in range(0, len(data)):
    park_id.append(count)
    count += 1

# make an empty list for each column of data
park_code = []
name = []
description = []
url = []
phone = []

# create a loop to iterate over the data and append data to list
for d in range(0, len(data)):
    name.append(data[d]["fullName"])
    park_code.append(data[d]["parkCode"])
    url.append(data[d]["url"])
    phone.append(data[d]["contacts"])
    description.append(data[d]["description"])

# Create an empty DataFrame
df = pd.DataFrame()

# Append data to the DataFrame
df['park_id'] = park_id
df['park_code'] = park_code
df['name'] = name
df['description'] = description
df['url'] = url

parks = df[['park_id', 'park_code', 'name', 'description', 'url']].copy()
parks.to_csv("NPSparks.csv", index=False)
