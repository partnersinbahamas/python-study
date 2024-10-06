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

print('Python OOP basic')
print('--- Buildings ----')

class Building:
    # Encapsulation
    __architec = None
    year = None
    city = None

    def get_architec(self):
        return self.__architec

    def __init__(self, year, city, architec = None):
        self.year = year
        self.city = city

        if (architec == None):
            self.__architec = 'Denys Bokov'
        else:
            self.__architec = architec

    def info(self):
       return 'Building ' + str(self.year) + ' ' + self.get_architec()

building = Building(1999, 'Kyiv')
print(building.info())

class House(Building): # class(inherit), Inheritance
    rooms = None
    people = None

    def __init__(self, rooms, people, year, city, architec):
        super(House, self).__init__(year, city, architec)
        self.rooms = rooms
        self.people = people

    # Polymorphism
    def info(self):
        print(super().info())
        return '\tHouse with ' + str(self.rooms) + ' rooms, ' + str(self.people) + ' people.' 
    
house = House(3, 1, 1984, 'Berlin', 'unknown')
print(house.info())

class School(House):
    # Encapsulation
    __principal = None
    school_num = None

    def get_principal(self):
        return self.__principal

    def __init__(self, principal, school_num, rooms, people, year, city, architec = None):
        super().__init__(rooms, people, year, city, architec)
        self.__principal = principal
        self.school_num = school_num
    
    # Polymorphism
    def info(self):
        print(super().info())
        return '\tSchool ' + str(self.school_num) + ' principal: ' + self.get_principal()
    

school = School('H. Potter', 302, 188, 1123, 1666, 'London')
print(school.info())