/*
A pangram is a sentence that contains every single letter of the alphabet at least once.
For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because
it uses the letters A-Z at least once (case is irrelevant). Given a string, detect whether or
not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.

CodeWars Kata link:
https://www.codewars.com/kata/545cedaa9943f7fe7b000048/train/javascript

 */

/*
    This is the fun part.  After you solve the Kata yourself at least once, you
    are then able to see the solutions that others have come up with.  This is where
    the learning really kicks in, as you can see other more elegant solutions to the
    problem.  Having solved the problem yourself, you can gain much greater insights
    on how to more efficiently solve the problem, as opposed to just copy and pasting
    a solution without really knowing what it took to solve the problem in the first place.

 */
function isPangram(string) {
    string = string.toLowerCase();
    console.log("abcdefghijklmnopqrstuvwxyz".
            split("").
            every(function(x) {
                console.log(x)
            }));
}

// Code for local testing below this line
testString = "the quick brown fox jumps over the lazy dog.";

console.log(isPangram(testString));

// Lines below are test code from CodeWars
// const chai = require("chai");
// const assert = chai.assert;
// chai.config.truncateThreshold=0;
//
// describe("Tests", () => {
//     it("test1", () => {
//         var string = "The quick brown fox jumps over the lazy dog."
//         assert.strictEqual(isPangram(string), true)
//     })
//     it("test2", () => {
//         var string = "This is not a pangram."
//         assert.strictEqual(isPangram(string), false)
//     });
// });
