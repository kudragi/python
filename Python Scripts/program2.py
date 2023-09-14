#loop for largest number
lnum=-99999999999

number=int(input("enter a number or enter -1 to stop"))

while number != -1:
    if number > lnum:
        lnum = number
    number=int(input("enter a number or enter -1 to stop"))

print("the largest number is=",lnum)
