student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for student in student_scores:
    score = student_scores[student]

    if score >= 91:
        student_grades[student] = "Outstanding"

    elif score >= 81:
        student_grades[student] = "Exceeds Expectations"

    elif score >= 71:
        student_grades[student] = "Accaptable"

    else:
        student_grades[student] = "Fail"

print(student_grades)


capitals = {
    'France': 'Paris',
    'Germany': 'Berlin',
    'Poland': 'Warsaw',
    'Denmark': 'Copenhagen'
}

print(capitals)

for city in capitals:
    print(city)

# Nested lists

travel_log = {
    'France': ['Paris', 'Lyon', 'Montepllier']
}

# print Lyon
print(travel_log['France'][1])

nested_list = ['A', 'B', ['C', 'D']]
print(nested_list[2][1])


# Dictionary in dictionary

travel_dic = {
    'France': {
        'cities_visited': ['Paris', 'Lyon'],
        'total_visits': 5
    },
    'Germany': {
        'cities_visited': ['Berlin', 'Munich'],
        'total_visits': 4
    }
}

print(travel_dic['Germany']['cities_visited'][1])


# Bid program

#rint('Welcome to the bid program')
#
#id_dic = {}
#
#ontinue_bid = True
#
#hile continue_bid:
#   #key = input('What is your name: ')
#   #value = int(input('What is your bid in $: '))
#   bid_dic[key] = value
#
#   #restart = input("Is there any new bid? 'y' for yes, 'n' for no: ")
#   if restart == "n":
#       continue_bid = False
#       highest_bid = max(zip(bid_dic.values(), bid_dic.keys()))[1]
#       print(f'Total bids {bid_dic}')
#       print(
#           f'The {highest_bid} has won, with the value of {(max(bid_dic.values()))}')


###Extended lists and dictionaries

a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
print('Two middle ', a[3:5]) # Zero index = a, so 0=a, 1=b, etc...
print('Everything besides outsiders: ', a[1:10]) 

print(a[:]) #Print all
print(a[:5]) #Print first 5 elements
print(a[5:]) #Print last 6 elements
print(a[-3:]) #Print last 3 elements rmemeber about (-)
print(a[2:5]) #Print third element till 5th element

#You can make a var to a specific list you want
first_five = a[:5]
print(first_five)
last_five = a[-5:]
print(last_five)

#Save up new var for a new list
b = a[3:]
print(b)
b[1] = 99999 #Index is changing the value in the list
print(b)

colors = ['red', 'orange', 'blue', 'green', 'black', 'pink', 'white']
odds = colors[::2] #Odds last number indicates the jumps in the list
even = colors[1::2]
print(odds)
print(even)

#[::2] = chooses every second elemnt from the list
#[::-2] = same action but from the end of the list

#Sorting
car_ages = [2, 5, 7, 9, 1, 0, 3, 5, 10, 4, 5, 15, 19]
car_ages_descending = sorted(car_ages, reverse=True)
print(car_ages_descending)
    
oldest_car = car_ages_descending[0]
second_oldest = car_ages_descending[1]
rest = car_ages_descending[2:]
print(oldest_car, second_oldest, rest)

#If you have two var from one list, I can make a third var and add *before var and it will take all values that very used.
oldest_car, second_oldest, *others = car_ages_descending
print(oldest_car, second_oldest, others)

ani_names = {
    'dog': 'Azor',
    'cat': 'Rollo',
}
print(ani_names)
print(list(ani_names.keys()))
print(list(ani_names.values()))
print(list(ani_names.items()))
