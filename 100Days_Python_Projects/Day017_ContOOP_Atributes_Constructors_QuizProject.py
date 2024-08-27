#Constructor __init__(self)
class User():
    def __init__(self, user_id, username, user_age, user_sex):
        self.id = user_id
        self.name = username
        self.age = user_age
        self.sex = user_sex
        self.followers = 0
        self.following = 0
    
    def follow(self, user):
        user.followers += 1
        self.following += 1
    
user_1 = User('001', 'Szafranerio', 24, 'Male')

print(f'You are {user_1.name}, your id is {user_1.id} You are allowed to drink, because you are {user_1.age}. You are {user_1.sex}, and you are following {user_1.following} users')


