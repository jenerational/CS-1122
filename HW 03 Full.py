# Jennifer Walker
# CS 1122
# Created 2/16-17/2016 
# HW 03 - Data Representation and Logic 

#Question 2: 
def Q2():
    #user enters number in Base 10
    userNum = int(input("Enter a number in deicmal. "))
    #converts to binary
    numB = bin(userNum)
    #cuts off the 0b that marks the number as binary
    numB = str(numB[2:])
    #prints number with full 8 characters including first 0s
    while len(numB) < 8:
        numB = "0" + numB
    #prints bin num 
    print("Your number in binary is: " + numB)

#Question 2:
#user enters series of numbers in hexidecimal
def wBrackets():
    userString = input("Enter the list (including brackets) of ASCII in hex form. ")
    userString = userString[1:len(userString)]
    hexString = []
    while len(userString) > 1:
        #separates numbers by adding to list w separation of commas
        comInd = userString.find(",")
        #if program cannot find any comma (aka only last term is left)
        if comInd == -1:
            hexString.append(userString[:len(userString)-1])
            #empties user string
            userString = ""
        else:
            #adds next term to new list
            hexString.append(userString[:comInd])
            #deletes term from user list
            userString = userString[comInd+2:]
    hexToDec(hexString)

#user enters series of numbers in hexidecimal 
def woBrackets():
    userString = input("Enter the list (without brackets) of ASCII in hex form. ")
    hexString = []
    while len(userString) > 1:
        #separates numbers by adding to list w separation of spaces
        comInd = userString.find(" ")
        #if program cannot find any space (aka only last term is left)
        if comInd == -1:
            hexString.append(userString[:len(userString)])
            #empties user string
            userString = ""
        else:
            #adds next term to new list
            hexString.append(userString[:comInd])
            #deletes term from user list
            userString = userString[comInd+1:]
    hexToDec(hexString)

    
def hexToDec(hStr):
    #creates empty list
    decString = []
    #appends decimal conversion of each item to new list
    for x in hStr:
        decString.append(int(x, 16))
    #calls decToASCII
    decToASCII(decString)


def decToASCII(dStr):
    #creates empty string
    ASCIIStr = ""
    #adds ASCII char of each item to new list
    for num in dStr:
        ASCIIStr += chr(num)
    #prints final string
    print(ASCIIStr)

 
def Q3():
    #asks which type of list with be inputed
    bracketsYN = input("Are you going to enter a list with brackets? Type 'Y' or 'N'. ")
    print("Make sure the list has no returns or spaces prior to it.") 
    if bracketsYN == "Y":
        wBrackets()
    elif bracketsYN == "N":
        woBrackets()
    else:
        print("Input invalid") 
    
#Question 4:
def Q4():
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
    #prints hexidecimal number
    print(hexNum)

#Question 5
def Q5():
    #prompts user to enter an octal number 
    userNum = int(input("Please enter an octal number. "))
    #creates a number with no value
    decNum = 0
    #while there is still unconverted value in the octal number,
    #the while loop adds the highest tens value to the new number 
    while userNum != 0:
        numLen = len(str(userNum))
        decNumAdd = (userNum // 10**(numLen-1))
        decNum += decNumAdd * 8**(numLen-1)
        userNum -= decNumAdd * 10**(numLen-1)
    print(decNum)    


def main():
    print("Question 2: \n") 
    Q2()
    print("\nQuestion 3: \n") 
    Q3()
    print("\nQuestion 4: \n") 
    Q4()
    print("\nQuestion 5: \n")
    Q5() 

main()
