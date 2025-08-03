def multiplication_table(n):
    for i in range (1,11):
        print(f"{n*i}={i}x{n}")
num=int(input("enter a number:"))
multiplication_table(num)