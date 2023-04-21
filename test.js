// const words = ['react', 'script', 'interview', 'style', 'javascript']
// var array = [];
// words.forEach(element => {
//     if(element.length > 6) {
//         array.push(element);
//     }
// });

// console.log(array);

// let obj = { id: "1", name: "Test User", age: "25", profession: "Developer" };
// var array = [];
// console.log(Object.entries(obj))




// JOgeNDra => joGEndRA
// var value = 'JOgeNDra'
// value.forEach(element => {
//     console.log(element);
// });

// let user = {
//     name: "GFG",
//     gfg1:() => {
//         console.log("hello " + this.name);
//     },
//     gfg2(){     
//         console.log("Welcome to " + this.name);
//     }
//  };
// user.gfg1();
// user.gfg2();
// user.gfg1();

// function sum(x, y, z) {
//     return x + y + z;
//   }
  
// let numbers = [1, 2, 3, 4, 5];
// console.log(sum(...numbers))

// let x = new String("Matellio");            
// let y = new String("Matellio");
//     console.log(x == y)

    // console.log('Start'); 
    // setTimeout(()=>{
    //     console.log('setTimeOut---1');    
    // },2);
    // setTimeout(()=>{
    //     console.log('setTimeOut---2');    
    // },1);
    // Promise.resolve().then(r=> console.log('Promise 1')).then(s=>console.log('Promise 2'));
    // console.log('End');

// var router = require('Ro')
// var controller = req

// router.get('/get-details', auth,  middleware, controller) 

// dealers.find({ "$and": [ { "length": { "$gt": 2000 } }, { "cars.weight": { "$gte": 800 } } ] });

// dealers.find({ "length": { "$gt": 2000 }, "cars.weight": { "$gte": 800 } });


// function myFun() {
//     var myName  = "my name";
//     console.log(myName);
// }

// myFun(); //output => "my name"
// console.log(myName)

// let myName = "your name";

// function myFun() {
//     console.log(myName); 
// }

// myFun(); //output => "your name"

// if(true) {
//     console.log(myName); //output => "your name"
// }

// console.log(myName);

// console.log(myName); //output => undefined 
// var myName = "my name";

// var myName = "my name";
// var myName = "not my name";

// console.log(myName)

// let myAge = 20;
// if(myAge > 18) {
//     var myName = "my name";
//     console.log(myName) //output => "my name"
// }
// console.log(myName);

// console.log(myName); //output => ReferenceError
// let myName = "my name";

// const myName = "my name";
// myName = "not my name";


// //Array Destructuring
// let fruits = ["Apple", "Banana"];
// let [a, b] = fruits; // Array destructuring assignment
// console.log(a, b);


//Object Destructuring
// let person = {name: "Peter", age: 28};
// let {name, age} = person; // Object destructuring assignment
// console.log(name, age);

// var array = [
//     1,  2,  3,  5,  7, 11, 13, 17,
//    19, 23, 29, 31, 37, 41, 43, 47,
//    53, 59, 61, 67, 71, 73, 79, 83,
//    89, 97
//  ]

// console.log(array.includes(5));
// console.log(array.indexOf(100));

// console.log('Hello');

// let str = '{}[()]'
// Balanced brackets - {[]}
// un Balanced brackets - {[}]
//{[()]}
// let stack = [];
// stack.push(str[0]);
// n=1;
// m=0;
// while(stack.length>0 && n < str.length) {
//     console.log("str[n] ", str[n]);
//     console.log("stack[m] ", stack[m]);
//    if(str[n] == stack[m]) {
//        stack.pop();
//    } else {
//        stack.push(str[n]);
//        n++;
//        m++;
//    }
// }
// let str = '{}[()]'
// for(var i=0)

var array = [4, 1, 6, 5, 9];
largest = -9999;
secondLargest = largest;
for(var i=0;i<array.length;i++) {
    if(array[i] > largest) {
        secondLargest = largest;
        largest = array[i]
    }
}
console.log("largest", largest);
console.log("secondLargest", secondLargest);