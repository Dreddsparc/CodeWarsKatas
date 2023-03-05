"""
DESCRIPTION:
Task:
Your task is to write a function which returns the sum of following series upto nth term(parameter).

Series: 1 + 1/4 + 1/7 + 1/10 + 1/13 + 1/16 +...
Rules:
You need to round the answer to 2 decimal places and return it as String.

If the given value is 0 then it should return 0.00

You will only be given Natural Numbers as arguments.

Examples:(Input --> Output)
1 --> 1 --> "1.00"
2 --> 1 + 1/4 --> "1.25"
5 --> 1 + 1/4 + 1/7 + 1/10 + 1/13 --> "1.57"


CodeWars Kata Link :
https://www.codewars.com/kata/555eded1ad94b00403000071

"""

from math import fsum
# Im probably going to facepalm when I see all of the elegant solutions
# of my peers on here, but I really enjoyed figuring this out and making
# it work as is.

def series_sum(seriesLen):
    if (seriesLen == 0) :       # Check for possible 0 and
        return "0.00"           # get out quick if So
    else:
        seriesList = list()      #  Start up an empty list
        seriesDenom = 4          # Start denominator at 4
        seriesList.append(1.00)  # get the first number into the list

        # build the list with the remaining fractional values
        for i in range(1, int(seriesLen)) :
            seriesList.append(1/seriesDenom)  # Make fractional and add to the list
            seriesDenom += 3                  # increase denominator by 3 for next fraction

    # get the sum of all items in the list, round it to 2 decimal places and format the result
    # to pass back to the caller
    return '{:01.2f}'.format(round(fsum(seriesList),2))


    # Happy Coding ^_^

# Local Testing code below this line