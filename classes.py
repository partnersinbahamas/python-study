import datetime as dt

class Cat:
    birth = dt.datetime.now().date()
    name = None
    age = 0

    # constructor
    def __init__(self, name):
        self.name = name

    def set_date(self, name=None, age=None, birth=None):
        if name: self.name = name
        if age: self.age = age
        if birth: self.birth = birth

    def info(self):
        return 'Cat ' + str(self.name + ' ') + str(self.birth)

class Dog:
    birth = dt.datetime.now().date()
    name = None
    age = 0

    # constructor
    def __init__(self, name):
        self.name = name

    def set_date(self, name=None, age=None, birth=None):
        if name: self.name = name
        if age: self.age = age
        if birth: self.birth = birth

    def info(self):
        self.bark()
        return 'Dog ' + str(self.name + ' ') + str(self.birth)
    
    def bark(self):
        print(self.name, 'GAV!')

myDog = Dog('Harry')
myCat = Cat('Barsik')

print(myDog.birth)
myDog.set_date(None, None, '2004')
print(myDog.info())

print(myCat.info())
    
