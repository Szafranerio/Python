# Subscripting, prints the chosen letter in the []
print('Hello World'[3])

word = 'Hello this is my world'
print(word[3] + word[6])

name_of_user = input('Enter your name: ')
lenght_of_the_name = len(name_of_user)
print(lenght_of_the_name)

# Tip calculator
print('Welcome to the bill calculator!')
bill = float(input('Input the amount that you have to pay for the service: '))
tip = float(input('How much tip you would like to give?: '))
people = int(input('How many people are you with?: '))

tip_percentage = tip / 100
total_tip_amount = bill * tip_percentage
total_bill = total_tip_amount + bill
# print(type(total_amount))
per_person = total_bill / people
final_amount = round(per_person, ndigits=2)
print(
    f'Total amount is:  {total_bill} . You have to pay {per_person} per person')
