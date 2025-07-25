##Write a function merge_list that merges two lists and 
##returns a single new list merging all the values of both lists.

##Declare an empty list.

##Loop the two lists.

##Append the results into an empty list.

##Print the new variable with the merged lists.

##💡 Hints:
##You will have to loop through each list and insert their items into a new list.

##There are more ways to merge lists in Python. This would be a good time for you to search on the Internet "how to merge lists in python".

##Expected result:
##['Lebron', 'Aaliyah', 'Diamond', 'Dominique', 'Aliyah', 'Jazmin', 'Darnell', 'Lucas', 
 ##'Jake', 'Scott', 'Amy', 'Molly', 'Hannah', 'Lucas']
a=['Lebron', 'Aaliyah', 'Diamond', 'Dominique', 'Aliyah', 'Jazmin', 'Darnell', 'Lucas']
b=['Jake', 'Scott', 'Amy', 'Molly', 'Hannah', 'Lucas']
c=[]

for i in range (len(a)-1):
    c.append(a[i])

for j in range(len(b)):
    c.append(b[j])

print(c)