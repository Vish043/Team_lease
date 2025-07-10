class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def greet(self):
        print(f"Hello, Iam {self.name} and I'm {self.age} years old.")

    def have_birthday(self):
        self.age +=1
        print(f"Happy Birthday, {self.name} you are now {self.age}.")

person1 = Person("Vishal", 21)
person1.greet()
person1.have_birthday()