a=[2,3,4,5,6,7,8]

def binarysearch(num,b):
    low = 0
    high = len(num)-1

    while low<=high:
        
        mid = int((low+high)/2)

        if num[mid]== b:
          print(f"{b} is found at {mid}")
          return
        elif (b>num[mid]):
          low = mid + 1
        elif (b<num[mid]):
          high=mid - 1
        else:
           print(f"{b} not found")

binarysearch(a,9)

