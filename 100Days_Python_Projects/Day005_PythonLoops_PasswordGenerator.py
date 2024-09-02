import random
student_score = [150, 12, 56, 87, 65, 32, 145,
                 67, 123, 45, 87, 98, 187, 87, 65, 90, 34, 56]

sum = 0
for score in student_score:
    sum += score
print(sum)

max_score = 0
for score in student_score:
    if score > max_score:
        max_score = score
print(max_score)

# Range
for number in range(1, 10, 2):
    print(number)

# Gauss challange
sum = 0
for number in range(1, 101):
    sum += number
print(sum)

# FizzBuzz
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print('FizzBuzz')
    elif number % 3 == 0:
        print('Fizz')
    elif number % 5 == 0:
        print('Buzz')
    else:
        print(number)

# Password generator
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = int(input('How many letters you would like to have?: '))
nr_number = int(input('How many numbers you would like to have?: '))
nr_symbols = int(input('How many symbols you would like to have?: '))

password = ''

for char in range(0, nr_letters):
    password += random.choice(letters)

for char in range(0, nr_number):
    password += random.choice(numbers)

for char in range(0, nr_symbols):
    password += random.choice(symbols)

print(password)

# Hard
password_list = []
for char in range(0, nr_letters):
    password_list.append(random.choice(letters))

for char in range(0, nr_number):
    password_list.append(random.choice(numbers))

for char in range(0, nr_symbols):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)
print(password_list)

password = ''
for char in password_list:
    password += char

print(f'Your password is: {password}')
