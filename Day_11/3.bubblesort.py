a=[5,4,3,2,6,7,4,8]

def bubblesort(num):
    for i in range (len(num)):
        for j in range(0,len(num)-i-1):
            if num[j]>num[j+1]:
                num[j],num[j+1]= num[j+1],num[j]
            
    return num

d=bubblesort(a)
print (f"{d}")