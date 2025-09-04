#Day 1: Practice in Python
from math import pi
class details:
    def __init__(self):
        self.first = str(input("Enter your First name: "))
        self.last = str(input("Enter Your Second name: "))
        self.Full_name = self.first +" "+ self.last
        self.country = str(input("Enter your Country name :"))
        self.city = "Karwar"
        self.age = int(input("Enter your age: "))
        self.year = 2004
        self.is_married = False
        self.is_true = True
        self.is_light_on = False
        self.a,self.b,self.c = 1,2,3
        print(f'{self.Full_name}\n{self.country}\n{self.age}')

        self.DataType()
        self.length ()
        self.maths()
        self.circle()

    def DataType(self):
        print(type(self.first))
        print(type(self.last))
        print(type(self.Full_name))
        print(type(self.country))
        print(type(self.city))
        print(type(self.age))
        print(type(self.year))
        print(type(self.is_married))
        print(type(self.is_true))
        print(type(self.is_light_on))
        print(type(self.a))
        print(type(self.b))
        print(type(self.c))

    def length(self):
        print(f'Length of first name is : {len(self.first)}')
        print(f'Length of Last name is : {len(self.last)}')

    def maths(self):
        self.num_one = 5
        self.num_two = 4
        self.total = self.num_one + self.num_two
        self.diff = self.num_one - self.num_two
        self.product = self.num_one * self.num_two
        self.division = self.num_one / self.num_two
        self.remainder = self.num_one % self.num_two
        self.exp = self.num_one ** self.num_two
        self.floor_division = self.num_one // self.num_two
        print(f'{self.total}\n{self.diff}\n{self.product}\n{self.division}\n{self.remainder}\n{self.exp}\n{self.floor_division}')

    def circle(self):
        self.radius1 = 30
        self.area1 = pi*self.radius1**2
        self.circumference1 = 2*pi*self.radius1
        print(f'Area of circle 1 :{self.area1}')
        self.radius2 = int(input('Enter radius of a circle : '))
        self.area2 = pi*self.radius2**2
        print(f'Area of circle 2 :{self.area2}')


d = details()
help('keywords')