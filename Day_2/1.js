//Write a program in javascript to check the input number is largest or smallest

let num = [2,3,4.8,6,9,10]
let max = num[0];
let min = num[0];
for (let i=0;i<num.length;i++){
    if (num[i]>=max)
        max=num[i]
    if (num[i]<=min)
        min=num[i]
}
console.log("max number is " + max)
console.log("min number is " + min)