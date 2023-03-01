/*
A pangram is a sentence that contains every single letter of the alphabet at least once.
For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because
it uses the letters A-Z at least once (case is irrelevant). Given a string, detect whether or
not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.

CodeWars Kata link:
https://www.codewars.com/kata/545cedaa9943f7fe7b000048/train/javascript

 */

function isPangram(string) {

    const myStringSet = new Set(string.
                            replace(/\s/g, "").
                            replace(/[.,\/\d+#!$%\^&\*;:{}=\-_`~()]/g,"").
                            toLowerCase().
                            split("").
                            sort());

    const myAlphas = "abcdefghijklmnopqrstuvwxyz";

    if ([...myStringSet].length !== myAlphas.length) return false;

    for (var i = 0; i < [...myStringSet].length; ++i) {
        if ([...myStringSet][i] !== myAlphas[i]) return false;
    }
    return true;
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
