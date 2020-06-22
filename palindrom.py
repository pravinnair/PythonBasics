def ispalindrom(input):
    min = 0
    max = len(input)-1
    while(True):
        if(input[min]!=input[max]):
            print("String is not palindrome")
            return False
        else:
            if(min >= max):
                print("String is palindrome")
                return True
        min += 1
        max -= 1

#1991
#19893
ispalindrom("198991")


def isPali(str):
    max = len(str) - 1
    min = 0
    while(True):
        if(str[min] != str[max]):
            print('Not Palindrom')
            return False
        elif(min>=max):
            print('Palindrom')
            return True
        min += 1
        max -= 1

isPali('1991')

