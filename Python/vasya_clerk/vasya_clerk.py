"""
Hmm. this one was retired and description of the problem removed 'due to copyright issues'?

will have to dig in and see if i can figure out the original problem by looking at the solution
at some point.



"""

def tickets(people) :
    #print(people)
    moviePrice = 25
    drawer = []
    for paid in people :
        drawer.append(paid)
        change = paid - moviePrice
        #print(drawer)
        # case change == 75
        if (change == 75) :
            if (drawer.count(50) >=1 and drawer.count(25) >=1) :
                drawer.remove(50)
                drawer.remove(25)
            else :
                if (drawer.count(25) >=3) :
                    for i in range(3) :
                        drawer.remove(25)
                else :
                    return "NO"
        # case change == 50
        if (change == 50) :
            if (drawer.count(50) > 1) :
                drawer.remove(50)
            else :
                if (drawer.count(25) >= 2) :
                    for i in range(2) :
                        drawer.remove(25)
                else:
                    return "NO"
        # case change == 25
        if (change == 25) :
            if (drawer.count(25) >= 1) :
                drawer.remove(25)
            else :
                return "NO"

    return "YES"

# Local testing code beyond this line

const chai = require('chai');
const assert = chai.assert;
chai.config.truncateThreshold = 0;

describe("Sample tests", () => {

  let tests = [
    [[25, 25, 50, 50], "YES"],
    [[25, 100],        "NO"]
  ];

  for(let [input, expected] of tests) {
    it(`People in line: [${input}]`, () => {
      let actual = tickets([...input]);
      assert(actual === expected, `Incorrect answer for input: ${input}\nExpected: ${expected}\nActual: ${actual}`);
    });
  }
});
