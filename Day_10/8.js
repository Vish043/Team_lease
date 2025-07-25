/**8. Write a function called select. Given an array and an object, select returns a new object whose properties must be on the given array and 
the given object as well
 */
function select(keys,obj){
    let result = {}
    for (let key of keys){
        if (obj.hasOwnProperty(key)){
            result[key]=obj[key];
        }
    }
    return result;
}

let keys = ['name','age'];
let person = {
    name:'Visha;',
    age:25,
    city:'Bangalore',
    hobby:'swimming'
};

let selected = select(keys,person);
console.log(selected)