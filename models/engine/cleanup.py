import json

# Step 1: Open the JSON file in read mode and load the data
with open('file.json', 'r') as f:
    data = json.load(f)

# Step 2: Iterate over the data and remove the "storage": key if it doesn't have a value
for item in data.values():
    if 'storage' in item and not item['storage']:
        del item['storage']

# Step 3: Open the JSON file in write mode and write the cleaned data back to the file
with open('file.json', 'w') as f:
    json.dump(data, f, indent=4)