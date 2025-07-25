##. At this time, the function format_greeting is printing the names only. Please update the mapping function so it creates a list where each item contains the following:
##'Hello, my name is <name> and I am <age> years old'
##💡 Hints:
##You have to get the age of each person based on their birth_date.

##Take your time to understand the already defined calculate_age function.

##Search in Google "How to get the age of a given birth date in python".

##Inside your format_greeting function you have to return a concatenation.

##Expected result:
##The result should be similar to this, but the ages might be different.

##[ 'Hello, my name is Joe and I am 32 years old',
  ##'Hello, my name is Bob and I am 42 years old',
  ##'Hello, my name is Erika and I am 28 years old',
  ##'Hello, my name is Dylan and I am 18 years old',
  ##'Hello, my name is Steve and I am 14 years old' ]
from datetime import datetime

people=[
    {"name":"Joe","birth_date":"1992-03-12"},
    {"name": "Bob", "birth_date": "1982-07-03"},
    {"name": "Erika", "birth_date": "1996-11-23"},
    {"name": "Dylan", "birth_date": "2006-01-30"},
    {"name": "Steve", "birth_date": "2010-06-10"}
]

def calculate_age(birth_date_str):
    birth_date = datetime.strptime(birth_date_str,"%Y-%m-%d")
    today = datetime.today()
    age = today.year - birth_date.year - (
        (today.month,today.day)<(birth_date.month, birth_date.day)
    )
    return age

def format_greeting(people):
    return[
        f"Hello, my name is {person['name']} and I am {calculate_age(person['birth_date'])} years old"
        for person in people
    ]

result = format_greeting(people)
for line in result:
    print (line)