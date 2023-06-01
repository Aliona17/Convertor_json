import json
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
convertor_data_to_json('data.txt')

