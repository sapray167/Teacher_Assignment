import json
with open('S:/Repositories/Teacher_Assignment/data.json','r') as jfile:
    data=json.load(jfile)
    print(data)
for person in data:
    if person.get('isStudent'):
        print(f'{person['name']} is a student.')
    else:
        print(f'{person['name']} is not a student.')