##Please create a delete_person function that deletes any given person from the list and returns a new list without that person.
##Expected result:
##Result:

##['juan', 'ana', 'michelle', 'stefany', 'lucy', 'barak']
##['ana', 'michelle', 'daniella', 'stefany', 'lucy', 'barak']
##['juan', 'ana', 'michelle', 'daniella', 'stefany', 'lucy', 'barak']

name=['juan', 'ana', 'michelle', 'daniella', 'stefany', 'lucy', 'barak']
def delete_person(a):
    if a in name:
        name.remove(a)
    else:
        print(f"{a} not found in the list.")

delete_person('ana')
print(name)