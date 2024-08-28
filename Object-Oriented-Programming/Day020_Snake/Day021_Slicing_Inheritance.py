# Snake project cont....

#Class Inheritance

class Animal:
    def __init__(self):
        self.num_of_eyes = 2
        
    def breathe(self):
        print('Inhale, exhale')
        
leo = Animal()
leo.breathe()

#You can create main class with the main functionallity and later create sub-class that will have own 
#but can take some atributes from the main class. You can also modify it in the subclass.."""
            
class Fish(Animal):
    def __init__(self):
        super().__init__()
        
    def breathe(self):
        super().breathe()
        print('Under water')
        
    def swim(self):
        print('Swim swim')
        
nemo = Fish()
nemo.swim()
nemo.breathe()