a=[5,6,7,3,8,9,2,1,0]

def insertionsort(num):
    for i in range (1,len(num)):
        key=num[i]
        j=i-1

        while j >= 0 and num[j] > key:
            num[j+1] = num[j]
            j -=1
            num [j+1] = key
    
    return num

print(insertionsort(a))