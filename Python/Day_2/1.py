#Data Types & Variables

class name:
    def __init__(self):
        self.name = str(input("Enter Your name : "))
        print(f'Hello, {self.name}')

        self.age = int(input("Enter your age : "))
        self.variables_dataTypes()
        self.teenage_adult()
        self.swap()
        self.string()
        self.AreaOfRectangle()
        self.CelsiusToFahrenheit()
        self.count_vowels()
        self.tostring()
        self.fruits()

    def teenage_adult(self):
        if self.age < 19 and self.age >=13:
            print("Your teen.")
        elif self.age >=18 and self.age <= 60:
            print("Your adult.") 
        elif self.age>60 and self.age<=150:
            print("Your old aged.")
        elif self.age>0 and self.age<13:
            print("Your minor")
        else:
            print("Enter valid age")

    def variables_dataTypes(self):
        self.a = 1
        self.b = 1.1
        self.c = "HI"
        self.d = True
        print(type(self.a))
        print(type(self.b))
        print(type(self.c))
        print(type(self.d))

    def swap(self):
        self.a = 1
        self.b = 2
        print(f"A : {self.a}")
        print(f"B : {self.b}")
        self.a,self.b = self.b,self.a
        print(f"A : {self.a}")
        print(f"B : {self.b}")

    def string(self):
        self.s = str(input("Enter the string : "))
        print(f'First 6 characters : {self.s[:6]}')
        print(f'last 4 characters : {self.s[-4:]}')
        print("Every second number is: \n")
        for i in range(len(self.s)):
            if i%2 != 0:
                print(self.s[i])

    def AreaOfRectangle(self):
        self.l = int(input("Enter length of rectangle: "))
        self.b = int(input("Enter breadth of rectangle: "))
        self.area = self.l * self.b
        print(f"Area of Rectangle is {self.area}")

    def CelsiusToFahrenheit(self):
        self.c = int(input("Eneter the celsius: "))
        self.f = (self.c * (9/5)) + 32
        print(f"Fahrenheit : {self.f}")

    def count_vowels(self):
        self.w = str(input("Enter Your word: "))
        self.w = self.w.lower()
        self.count =0
        for i in range (len(self.w)):
            if self.w[i] == "a" or self.w[i] == "e" or self.w[i] == "i" or self.w[i] == "o" or self.w[i] == "u":
                self.count = self.count+1
        print(f"Number of vowels = {self.count}")

    def tostring(self):
        self.a = 10
        self.b = str(self.a)
        print(f'{self.b} {type(self.b)}') 
            
    def fruits(self):
        self.fruits = ["apple","mango","Pineapple","Avacado","Banana"]
        print(f"First fruit is {self.fruits[0]}")
        print(f"First fruit is {self.fruits[-1]}")
name()