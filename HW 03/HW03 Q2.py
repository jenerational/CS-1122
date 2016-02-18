# Jennifer Walker
# CS 1122
# Created 2/16/2016
# Converts numbers from dec to hex and bin 


def main():
    #user enters number in Base 10
    userNum = int(input("Enter a number in deicmal. "))
    #converts to binary
    numB = bin(userNum)
    #cuts off the 0b that marks the number as binary
    print(numB)
    numB = numB[2:]
    #prints number with full 8 characters including first 0s
    while len(numB) < 8:
        numB = "0" + numB
    #prints bin num 
    print("Your number in binary is: " + numB)

main()
