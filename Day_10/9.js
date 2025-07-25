/**9. Given a sorted array, such as this:

10. let arr = [1, 3, 16, 22, 31, 33, 34];
You can use binary search for the value 31, as follows:

Pick the midpoint: 22.

The value is higher than 22, so now consider only the right half of the previous array: [...31, 33, 34]

Pick the midpoint: 33.

The value is lower than 33, so now consider only the left half of the previous array: [...31...]

Pick the midpoint: 31.

You've hit the value.

Return the index of the value.

The function search receives an array of numbers and a number, it should return the position of the number given using binary search.
 Example:
let arr = [1, 3, 16, 22, 31, 33, 34];
console.log(search(arr, 31)); // --> 4 */

let arr = [1, 3, 16, 22, 31, 33, 34];

function position(arr,value){
    let left = 0;
    let right = arr.length - 1;

    while(left<=right){
        let  mid = (left+right)/2;

        if (arr[mid]===value){
            return mid
        }
        else if (arr[mid]<value){
            left = mid+1;
        }
        else {
            right = mid-1;
        }
    }
    return -1;
}

console.log(position(arr,3))
console.log(position(arr,100))