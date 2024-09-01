#List comprehension

#name = [new_item for item in list if condition]

#Numbers
numbers = [1,2,3]
new_list = [n + 1 for n in numbers]
print(new_list)

#Strings
name = 'Bartlomiej'
new_name = [letter for letter in name]
print(new_name)

#Range
range_list = [num*2 for num in range(1,5)]
print(range_list)

#With condition
names = ['Alex', 'Beth', 'Mark', 'Thomas', 'Patrick']
short_names = [name for name in names if len(name) < 5]
print(short_names)

#Make names longer than 5 with capitalize names
long_names = [name.upper() for name in names if len(name) > 5]
print(long_names)

#Squared numbers
numbers = [1,1,2,3,5,8,13,21,34,55]
squared_numbers = [num**2 for num in numbers]
print(squared_numbers)

#String to int and later only even numbers
list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [int(string) for string in list_of_strings]
result = [num for num in numbers if num%2==0]
print(result)

#Dictionary Comprehension

#new_dict = {new_key:new_value for item in list}
#new_dict = {new_key:new_value for (key,value) in dict.items()}
#new_dict = {new_key:new_value for (key,value) in dict.items() if test}

import random
names = ['Alex', 'Beth', 'Mark', 'Thomas', 'Patrick']

scores = {student:random.randint(1,100) for student in names}
print(scores)

passed = {student:score for (student, score) in scores.items() if score >=50 }
print(passed)

#Dictionary with the length of words
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word:len(word) for word in sentence.split()}
print(result)

weather_c = {'Monday':12, 'Tuesday':14, 'Wednsday':15, 'Thursday':14, 'Friday': 21, 'Saturday':22, 'Sunday':24}
weather_f = {day:(temp_c * 9/5 + 32 ) for (day, temp_c) in weather_c.items()}
print(weather_f)

#Looping through dictionary
student_dict = {"student": ['Angela', 'James', 'Thomas', 'Bartek'], "score": [56, 76, 87, 45]}

for (key,value) in student_dict.items():
    print(value)
    
import pandas 
student_dataframe = pandas.DataFrame(student_dict)
print(student_dataframe)

#Loop over each of rows in DataFrame

for(index, row) in student_dataframe.iterrows():
    print(index)
    print(row.student)
    
#NATO Alphabet Project

data = pandas.read_csv('/Users/bartlomiejszafran/Desktop/GitHub/Python/100Days_Python_Projects/data/Day026_NATO_Alphabet/nato_phonetic_alphabet.csv')

print(data.to_dict())

data = {row.letter:row.code for (index, row) in data.iterrows()}
print(data)


name = input('What is your name: ').upper()
new_name = [letter for letter in name]
nato_alphabet = [data[letter] for letter in name]
print(nato_alphabet)