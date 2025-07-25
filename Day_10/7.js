/**7.Write a function called removeArrayValues. Given an object, removeArrayValues removes any properties whose values are arrays. */
function removeArrayValues(obj){
    for (let key in obj){
        if(Array.isArray(obj[key])){
            delete obj[key];
        }
    }
}
const sample = {
    name: "Vish",
    age: 21,
    hobbies: ["reading", "cycling"],
    scores: [90, 80],
    active: true
};

removeArrayValues(sample);
console.log(sample);
