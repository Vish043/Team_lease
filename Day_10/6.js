/**6.Write a function called addFullNameProperty. Given an object that has a firstName 
property and a lastName property, addFullNameProperty adds a fullName property to the object, 
its value is a string with the first name and last name separated by a space.**/
function addFullNameProperty(obj){
    obj.fullName = obj.firstName + " " + obj.lastName;
}

let person ={
    firstName : "Vishal",
    lastName:"Gaonkar"
}

addFullNameProperty(person)
console.log(person.fullName)