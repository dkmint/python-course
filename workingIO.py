arr = np.array([[1.2, 2.2, 3], [4.14, 5.65, 6.42]])
arr
np.savetxt('my_arr.d', arr, fmt = '%.2f', header = 'Col1 Col2 Col3')

data = np.random.random((100, 5)) # 100 rows and 5 columns  
data 
np.savetxt('test.csv', data, fmt = '%.2f', delimiter = ',', header = 'c1, c2, c3, c4, c5')

import pickle
dict_a = {'A': 0, 'B': 1, 'C': 2}
pickle.dump(dict_a, open('test.pkl', 'wb'))


my_dict = pickle.load(open('test.pkl', 'rb'))
my_dict


import json
school = {
"school": "UC Berkeley",
"address": {
"city": "Berkeley",
"state": "California",
"postal": "94720"
},
"list":[
"student 1",
"student 2",
"student 3"
],
"array":[1, 2, 3]
}
# school
json.dump(school, open("school.json", "w"))
my_school = json.load(open("school.json", "r"))
my_school
