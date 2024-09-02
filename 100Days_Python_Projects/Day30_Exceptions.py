# try: Something that might cause an expection

# expect: Do this if there was an exception. Often to broad, make it more accuarte for example: ('FileNotFoundError")

# else: Do this if there were no exceptions

# finally: Do this no matter what happens

#try:
#    file = open('data.txt')
#    a = {'key':'value'}
#    print(a['dsad'])
#except FileNotFoundError:
#    file = open('data.txt', "w")
#    file.write('something')
#except KeyError as error_message:
#    print(f'The key {error_message} does not exisit')
#    
#    
#

height = float(input('What is your height: '))
weight = int(input('What is your wieght: '))

if height > 3:
    raise ValueError ("Are you really over 3 meters?")

bmi = weight / height ** 2


