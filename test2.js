
// // for(var i = 0;i<5;i++) {
//     setTimeout(() => {
//         // for(var i = 0;i<5;i++) {
//         console.log(`Kumar`)
//     }, 2000);
// // }

// function evenOdd(size) {
//     var oddArray = [];
//     var evenArray = [];
//     var primeArray = [];
//     for(var i=1;i<=size;i++) {
//         if(i%2 == 0) {
//             evenArray.push(i);
//         } else {
//             oddArray.push(i);
//         }
//         var count = 0;
//         for(j=2;j<i;j++) {
//             if(i%j == 0) {
//                 count++;
//             }
//         }
//         if(count == 0) {
//             primeArray.push(i);
//         }

//     }
//     // console.log("evenArray", evenArray);
//     // console.log("oddArray", oddArray);
//     console.log("primeArray", primeArray);
// }

// evenOdd(100);

// const fs = require('fs');
 
// function readFileFunction(callback) {
//   // Assume this takes 95ms to complete
//   fs.readFile('/path/to/file', callback);
// }
 
// const timeoutScheduled = Date.now();
 
// setTimeout(() => {
//   const delay = Date.now() - timeoutScheduled;
 
//   console.log(`${delay}ms have passed since I was scheduled`);
// }, 100);
 
// // do readFileFunction which takes 95 ms to complete
// readFileFunction(() => {
//   const startCallback = Date.now();
 
//   // do something that will take 10ms...
//   while (Date.now() - startCallback < 10) {
//     // do nothing
//   }
// });

// (function () {
//   var a = b = 3;
// })();
 
// console.log("a defined? " + (typeof a !== 'undefined'));
// console.log("b defined? " + (typeof b !== 'undefined'));

// function foo1() {
//   return {
//     bar: "hello"
//   };
// }
 
// function foo2() {
//   return
//   {
//     bar: "hello"
//   };
// }
 
// console.log(foo1());
// console.log(foo2());

// (function () {
//   console.log(1);
//   setTimeout(function () { console.log(2) }, 1000);
//   setTimeout(function () { console.log(3) }, 0);
//   console.log(4);
// })();

// async function sendMessage() {
//   return "hello world";
// }
 
// console.log(sendMessage());

// console.log('Hello')
// let string = "John doe";
// let object = {};
// let repeatedValue = string[0];
// for (let i = 0; i < string.length; i++) {
//     // console.log(string[i]);
//     if (object[string[i]]) {
//         object[string[i]] = object[string[i]] + 1;
//         repeatedValue = string[i];
//     } else {
//         object[string[i]] = 1;
//     }
// }
// console.log(repeatedValue);
// var array = [10, 1, 4, 2, 6, 8, 5, 13];
// function insert(params) {
//     array.push(params);
// }

// let output = [];
// function rank(params) {
//     let start = 0;
//     let end = array.length - 1;
//     while (start <= end) {
//         // console.log(start);
//         if (array[start] <= params) {
//             output.push(array[start])
//         }
//         if (array[end] <= params) {
//             output.push(array[end])
//         }
//         start++;
//         end--;
//     }
//     console.log(output);
// }

// rank(4)

// console.log('Hello');
// var unitFormula = {
//     kmToM: 1000,
//     kmToCm: 100000,
//     mToKm: 0.001,
//     mToCm: 100,
//     cmToKm: 0.00001,
//     cmToM: 0.01
// }

// function convert(value, unit) {
//     console.log(value*unitFormula[unit]);
// }

// convert(5, 'kmToM');

// var a = [
//     {
//         name: "Darshan",
//         id: 1,
//         dept: "react",
//         age:26
//     },
//     {
//         name: "Kshama",
//         id: 2,
//         dept: "java",
//         age:47
//     },
//     {
//         name: "Shweta",
//         id: 3,
//         dept: "Finance",
//         age:23
//     } ,{
//         name: "Amol",
//         id: 4,
//         dept: "java",
//         age:57
//     },
// ]
// var output = {};
// a.forEach(element => {
//     if (output.length == 0 || output[element.dept] == undefined) {
//         output[element.dept] = []
//         output[element.dept].push(element)
//     } else {
//         output[element.dept].push(element)
//     }
// });
// console.log(output)
// find()
// let arr = [1, 4, 2, 5, 2, 1, 4, 5, 1, 0]
// // console.log(arr);
// output = {};
// for (let i = 0; i < arr.length; i++) {
//     if (output[arr[i]] == undefined) {
//         output[arr[i]] = 1;
//     } else {
//         output[arr[i]] = output[arr[i]] + 1;
//     }
// }

// console.log(output);
let string = 'PAYPALISHIRING';
// 'P A H  N'
// 'APLSIING'
// 'Y I R'
let output1 = ''
for (let i = 0; i < string.length; i = i + 4) {
    // console.log(string[i]);
    output1 = output1 + string[i];
}
let output2 = ''
for (let i = 0; i < string.length; i = i + 2) {
    // console.log(string[i]);
    output2 = output2 + string[i];
}
let output3 = ''
for (let i = 2; i < string.length; i = i + 4) {
    // console.log(string[i]);
    output3 = output3 + string[i];
}
console.log(output1);
console.log(output2);
console.log(output3);