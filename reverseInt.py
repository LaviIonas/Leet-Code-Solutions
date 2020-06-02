
def reverse(x):
    # check if number is above 32 long -> return 0
    # check if there is a negative -> remove it -> set boolean true
    # reverse number
    # check if first value is 0 -> remove it
    # return new number

    reversedInt = ""
    finalNum = 0
    count = 0
    negative = False
    num = None

    if x < 0:
        num = str(Math.abs(x))
        negative = True
    else:
        num = str(x)

    for i in range(len(str(num))):
        if i > 32:
            return "Overflow, number too large"

        reversedInt = num[i] + reversedInt

    for i in range(len(reversedInt)):
        if reversedInt[i] == "0":
            count += 1
        else:
            break

    finalNum = reversedInt.replace('0', '', count)
    if negative:
        finalNum = "-" + finalNum

    return finalNum



def main():
    integer = -12300
    print(reverse(integer))

main ()
