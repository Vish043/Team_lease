#Control Structures (Loop & Conditionals)

class Exercises():
    def __init__(self):
        self.even_odd()
        self.largest_number()
        self.number_1_20()
        self.even()
        self.multiplication_table()
        self.password_auth()
        self.sum()
        self.factorial()
        self.guessing_game()
        self.prime()

    def even_odd(self):
        self.a = int(input("Enter a number : "))
        if self.a%2 == 0:
            print(f'{self.a} is even number')
        else:
            print(f'{self.a} is odd number')

    def largest_number(self):
        self.n = int(input("Enter total numbers : "))
        self.a=[]
        for i in range (self.n):
            self.a.append(int(input(f'Enter the {i + 1} number : ')))
        self.l = float('-inf')
        for j in range (self.n):
            if self.l <= self.a[j]:
                self.l = self.a[j]
        print(f'The largest number is {self.l}')

    def number_1_20(self):
        for i in range(1,21):
            print(f'{i}')
    
    def even(self):
        for i in range (1,51):
            if i%2 == 0:
                print(f'{i}')

    def multiplication_table(self):
        self.n = int(input("Enter the number : "))
        for i in range (1,11):
            print(f"{self.n} x {i} = {self.n * i}")

    def password_auth (self):
        self.password = "python123"
        self.auth = input("Enter your password : ")
        if self.password == self.auth:
            print ('Acces Granted')
        else:
            print("Acces denied")

    def sum(self):
        self.count = 0
        for i in range (1,101):
            self.count = self.count + i
        print(f'{self.count}')

    def factorial(self):
        self.f = int(input("Enter a number for factorial : "))
        self.value = 1
        for i in range (1,self.f+1):
            self.value = self.value * i
        print(f'{self.value}')

    def guessing_game(self):
        self.sn = 7
        self.a = int(input("Guess the number between 1-10 : "))
        if self.a == self.sn:
            print("Correct!")
        elif self.a < self.sn:
            print("Too low")
            self.guessing_game()
        elif self.a > self.sn:
            print("Too high")
            self.guessing_game()

    def prime(self):
        self.n = int(input("Enter the number : "))
        if self.n<2:
            print(f"{self.n} is not prime")
            return
        for i in range(2,self.n):
            if self.n % i == 0:
                print(f"{self.n} is not prime")
                return
            else:
                print(f"{self.n} is prime")
                return
Exercises()
    




