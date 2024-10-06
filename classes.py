import datetime as dt

class Cat:
    birth = dt.datetime.now().date()
    name = None
    age = 0

    def __init__(self, name):
        self.name = name

    def info(self):
        return 'Cat ' + str(self.name + ' ') + str(self.birth)

class Dog:
    birth = dt.datetime.now().date()
    name = None
    age = 0

    def __init__(self, name):
        self.name = name

    def info(self):
        self.bark()
        return 'Dog ' + str(self.name + ' ') + str(self.birth)
    
    def bark(self):
        print(self.name, 'GAV!')

myDog = Dog('Harry')
myCat = Cat('Barsik')

print(myDog.info())
print(myCat.info())
    
