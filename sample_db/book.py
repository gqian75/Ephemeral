# This code generate the corresponding json file of the dict "sample"
import json
sample = {'Books': [{'title': 'Software Engineering', 'id': '1'}, {'title':'Algorithm Design', 'id':'2'},{'title':'Python', 'id':'3'}]}

with open('books.json', 'w') as fp:
    json.dump(sample, fp, indent=4)