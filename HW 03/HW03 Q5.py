
# Jennifer Walker
# CS 1122
# Created 2/17/2016 
# Converts numbers from dec to hex and bin 

def main():
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
    

main()
