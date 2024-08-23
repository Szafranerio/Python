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
    
#Nested lists

travel_log = {
    'France': ['Paris', 'Lyon', 'Montepllier']
}

#print Lyon
print(travel_log['France'][1])

nested_list = ['A', 'B', ['C', 'D']]
print(nested_list[2][1])


#Dictionary in dictionary

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


#Bid program

print('Welcome to the bid program')

bid_dic = {}

continue_bid = True

while continue_bid:
    key = input('What is your name: ')
    value = int(input('What is your bid in $: '))
    bid_dic[key] = value
    
    restart = input("Is there any new bid? 'y' for yes, 'n' for no: ")
    if restart == "n":
        continue_bid = False
        highest_bid = max(zip(bid_dic.values(), bid_dic.keys()))[1]
        print(f'Total bids {bid_dic}')
        print(f'The {highest_bid} has won, with the value of {(max(bid_dic.values()))}')