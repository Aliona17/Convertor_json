# JSON Data Converter

This script converts data stored in a JSON file into separate text files for each attribute.

## Function Explanation

The function `convertor_data_to_json(file)` reads data from a JSON file and extracts specific attributes such as first names, last names, emails, and genders. It then sorts each attribute alphabetically and saves them in separate text files.

### Parameters

- `file`: The name or path of the JSON file to be processed.

### Usage

1. Make sure you have a valid JSON file containing the required data.

2. Import the `json` module.

3. Define empty lists `first_name`, `last_name`, `email`, and `gender` to store the extracted attributes.

4. Call the `convertor_data_to_json` function, passing the JSON file name as the argument.

5. The function will read the JSON file, load the data into `main_data_in_json`, and extract the specified attributes.

6. The extracted attributes will be sorted and stored in separate text files (`first_name.txt`, `last_name.txt`, `email.txt`, and `gender.txt`).

### Example

```python
import json

# Define empty lists
first_name = []
last_name = []
email = []
gender = []

def convertor_data_to_json(file):
    d = open(file, 'r')
    main_data_in_json = json.load(d)
    global first_name, last_name, email, gender
    first_name = sorted([i.get('first_name') for i in main_data_in_json])
    last_name = sorted([i.get('last_name') for i in main_data_in_json])
    email = sorted([i.get('email') for i in main_data_in_json])
    gender = sorted([i.get('gender') for i in main_data_in_json])
    with open('first_name.txt',  'w') as f:
        for i in first_name:
            f.write(i + ',')
    with open('last_name.txt',  'w') as l:
        for i in last_name:
            l.write(i + ',')
    with open('email.txt',  'w') as e:
        for i in email:
            e.write(i + ',')
    with open('gender.txt',  'w') as g:
        for i in gender:
            g.write(i + ',')

# Call the function with the JSON file name
convertor_data_to_json('data.txt')
