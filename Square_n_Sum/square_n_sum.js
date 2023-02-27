/*
*
*Complete the square sum function so that it squares each number passed into it and then sums the results together.

For example, for [1, 2, 2] it should return 9 because
1^2 + 2^2 + 2^2 =

* */
function squareSum(numbers){
    let sumSquares = 0;
    let debug = true;
    if(debug){ console.log(numbers);}
    for (let i = 0; i < numbers.length; i++) {
        if (debug) { console.log(numbers[i]);}
        sumSquares += numbers[i]**2;

    }
    return sumSquares;
}


console.log(squareSum([1, 2, 7, 19, 11, 22, 43]));
