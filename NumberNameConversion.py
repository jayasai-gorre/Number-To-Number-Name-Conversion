"""
                                 GORRE JAYA SAI'S PROJECT
                THIS IS A MINI PROJECT ON NUMBERS TO NUMBER NAME CONVERSION

    What will the below code do?
    ----------------------------
    1) The below code scans input from the user in the form of int.
    2) Based on users input by checking the conditions given in the code it will 
       print the number name of given value.


    Data Types Used in below code:
    ------------------------------
    1) int
    2) dict


    Variables used in the below code:
    ---------------------------------
    1) n: an int value to store the read value by user.
    2) numberNames: a dict used to store 0 to 19 number names.
    3) doubleDigits: a dict used to store base values of 10 from 20 to 90.
    4) tripleDigits: a dict used to store base values of 100 from 100 to 900.
    5) seperator: 'AND' is used for seperating (hundered and).
    6) unitsPlace: to seperate units place value  from given number.
    7) tensPlace: to seperate tens place value from given number.
    8) hundredsPlace: to seperate hundreds place value from given number.
    9) lastTwoDigits: to seperate last two digits for 10 to 19 (edge-case).


    Edge Cases:
    -------------------
    1) For example if I take a number 101... there is zero inside in the second digit so we should print 
       One Hundered And Eleven.
    2) For 202 Two Hundered And Two we should consider like this.
    3) So, we can conclude that if there is any zero in between numbers it will creates problem.
    4) For a 4 digit number, there are 8 cases to check for zeros.
    5) For a 5 digit number, 16 cases.
    6) For a 6 digit number, 32 cases.
    7) For a 7 digit number, 64 cases.
    8) And so on...


    Conclusion:
    ----------
    Final conclusion it becomes hectic write logic for big numbers like 10000000000, 9879752875927, and .........


"""
n = int(input("Enter an Integer number: "))
numberNames = {
    0: "Zero",
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine",
    10: "Ten",
    11: "Eleven",
    12: "Twelve",
    13: "Thirteen",
    14: "Fourteen",
    15: "Fifteen",
    16: "Sixteen",
    17: "Seventeen",
    18: "Eighteen",
    19: "Nineteen",
}
doubleDigits = {
    1: "Ten",
    2: "Twenty",
    3: "Thirty",
    4: "Fourty",
    5: "Fifty",
    6: "Sixty",
    7: "Seventy",
    8: "Eighty",
    9: "Ninety",
}
tripleDigits = {
    1: "One Hundered",
    2: "Two Hundered",
    3: "Three Hundered",
    4: "Four Hundered",
    5: "Five Hundered",
    6: "Six Hundered",
    7: "Seven Hundered",
    8: "Eight Hundered",
    9: "Nine Hundered",
}
seperator = "And"
unitsPlace = n % 10
tensPlace = (n // 10) % 10
hunderedsPlace = (n // 100) % 10

if n < 19:
    print(numberNames[n])
elif n > 9 and n < 100:
    if n % 100 == 0:
        print(doubleDigits[tensPlace])
    else:
        print(doubleDigits[tensPlace], numberNames[unitsPlace])
elif n > 99 and n < 1000:
    if n % 100 == 0:
        print(tripleDigits[hunderedsPlace])
    else:
        if tensPlace == 0:
            print(
                tripleDigits[hunderedsPlace],
                seperator,
                numberNames[unitsPlace],
            )
        else:
            if n > 99 and n < 200:
                lastTwoDigits = n % 100
                if lastTwoDigits > 9 and lastTwoDigits < 20:
                    print(
                        tripleDigits[hunderedsPlace],
                        seperator,
                        numberNames[lastTwoDigits],
                    )
                else:
                    print(
                        tripleDigits[hunderedsPlace],
                        seperator,
                        doubleDigits[tensPlace],
                        numberNames[unitsPlace],
                    )
            else:
                if n % 100 == 0:
                    print(tripleDigits[hunderedsPlace])
                else:
                    if unitsPlace == 0:
                        print(
                            tripleDigits[hunderedsPlace],
                            seperator,
                            doubleDigits[tensPlace],
                        )
                    else:
                        lastTwoDigits = n % 100
                        if lastTwoDigits > 9 and lastTwoDigits < 19:
                            print(
                                tripleDigits[hunderedsPlace],
                                seperator,
                                numberNames[lastTwoDigits],
                            )
                        else:
                            print(
                                tripleDigits[hunderedsPlace],
                                seperator,
                                doubleDigits[tensPlace],
                                numberNames[unitsPlace],
                            )
