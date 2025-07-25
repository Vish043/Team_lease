a=[2,3,4,5,6,7,8]

def linearsearch(num,a):
    for i in range (len(num)):
        if (a == num[i]):
            print(f"{a} is found at {i}")
    if a not in num:
        print(f"{a} doesn't exist in array")

linearsearch(a,9)