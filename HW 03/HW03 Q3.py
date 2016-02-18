# Jennifer Walker
# CS 1122
# Created 2/16/2016
# Converts numbers from hex to ASCII 


def wBrackets():
    #user enters series of numbers in hexidecimal
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


def woBrackets():
    #user enters series of numbers in hexidecimal
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

def main():
    #asks which type of list with be inputeds 
    bracketsYN = input("Are you going to enter a list with brackets? Type 'Y' or 'N'. ")
    print("Make sure the list has no returns or spaces prior to it.") 
    if bracketsYN == "Y":
        wBrackets()
    elif bracketsYN == "N":
        woBrackets()
    else:
        print("Input invalid") 
    
        
    

main()
