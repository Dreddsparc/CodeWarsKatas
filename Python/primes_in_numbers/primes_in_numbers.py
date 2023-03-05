"""
DESCRIPTION:
Given a positive number n > 1 find the prime factor decomposition of n. The result will be a string with the following form :

 "(p1**n1)(p2**n2)...(pk**nk)"
with the p(i) in increasing order and n(i) empty if n(i) is 1.

Example: n = 86240 should return "(2**5)(5)(7**2)(11)"

CodeWars Kata Link:
https://www.codewars.com/kata/54d512e62a5e54c96200019e/train/javascript

"""
def reduceFactors(factors) :
    factorList = list(set(factors))
    factorList.sort()
    finalResult = ""
    for factor in factorList :
        if (factors.count(factor) > 1) :
            finalResult += "("+str(factor)+"**"+str(factors.count(factor))+")"
        else :
            if (int(factor) != 1) :
                finalResult += "("+str(factor)+")"
    return finalResult

def primeFactors(n):
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d = d + 1
    return reduceFactors(factors)

### Local test Code beyond this line
describe("Tests", () => {
  it("test", () => {
Test.assertEquals(primeFactors(7775460),"(2**2)(3**3)(5)(7)(11**2)(17)")
  });
});

