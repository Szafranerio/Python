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

names = ['Alex', 'Beth', 'Mark', 'Thomas', 'Patrick']

grades = {}

