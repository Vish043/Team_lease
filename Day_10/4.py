##4. Our customer needs a program that counts the letter repetitions in a given string, for example:

##The string "Hello World" contains the following repetitions h=1 e=1 l=3 o=2 w=1 r=1 d=1.

##Count the letters of the string in the variable par and print the number of times a letter is repeated throughout the string.

##Capitalization should not affect the count (i.e. if there is a string that contains a capital A as well as a lowercase a the count for "a" should be 2).

##Spaces should be ignored!

##Expected result:
##print(count("Hello World"))
# This will print: {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}

def count(a):
    a=a.lower()
    a=a.replace(" ","")
    letter_count = {}

    for char in a:
        if char in letter_count:
            letter_count[char]+=1
        else:
            letter_count[char] = 1
    return letter_count

print(count("Hello hi"))
