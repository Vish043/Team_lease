print("Select any operator number \n " \
"1. Addition \n 2. Substraction \n 3. Multiplication \n 4. Division")
c=int(input("Enter operator number: "))
a=float(input("Enter first number: "))
b=float(input("Enter second number: "))
d=0
if c==1:
    d=a+b
elif c==2:
    d=a-b
elif c==3:
    d=a*b
elif c==4:
    d=a/b
else:
    print("Invalid Choice")

print(f"Your result is {d}")
