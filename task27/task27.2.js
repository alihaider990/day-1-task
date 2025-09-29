let arr1 = [1,2,2,1];
 let arr2 = [2,2,4,5];

let repeating_num = arr1.filter((num => {
   return arr2.includes(num);
}))

console.log(repeating_num)