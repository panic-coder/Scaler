/*
Problem Description

You are given an integer N you need to print all the Armstrong Numbers between 1 to N.
If sum of cubes of each digit of the number is equal to the number itself, then the number is called an Armstrong number.
For example, 153 = ( 1 * 1 * 1 ) + ( 5 * 5 * 5 ) + ( 3 * 3 * 3 ).


Problem Constraints
1 <= N <= 500


Input Format
First and only line of input contains an integer N.


Output Format
Output all the Armstrong numbers in range [1,N] each in a new line.


Example Input

Input 1:
5

Input 2:
200


Example Output

Output 1:
1

Output 2:
1
153


Example Explanation

Explanation 1:
1 is an armstrong number.

Explanation 2:
1 and 153 are armstrong number under 200.
*/

var N;
var readline = require('readline');
var rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
  terminal: false
});

rl.on('line', function(N){
    for(var i=1;i<=N;i++) {
    // console.log(line);                               
        var oldValue = i;
        var evaluationValue = i;
        // process.stdout.write(i + '\n');
        var sum = 0;
        while(evaluationValue != 0){
            var r = evaluationValue%10;
            sum = sum + (r*r*r);
            evaluationValue = Math.floor(evaluationValue/10);
            // process.stdout.write('evaluationValue: ',evaluationValue + '\n');
        }
        // process.stdout.write('Sum: '+ sum + '\n');
        if(oldValue == sum) {
            // outputArray.push(oldValue)
            process.stdout.write(oldValue + '\n');
        }
    }
    // process.stdout.write('outputArray: '+ outputArray + '\n');
    // return outputArray;
})