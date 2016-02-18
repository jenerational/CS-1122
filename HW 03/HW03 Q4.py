# Jennifer Walker
# CS 1122
# Created 2/17/2016
# Converts numbers from bin to hex

    

def main():
    #asks user for number w inserted whitespace in binary
    userString = input("Enter a number in binary with whitespace. ")
    #creates empty string
    userNum = ""
    #adds non whitespace char to new string
    for x in userString:
        if x != " ":
            userNum += x
    #converts number into int from base 2 and then into hex
    hexNum = hex(int(userNum,2))
    #prints hexidecimal num
    print(hexNum)


main()
