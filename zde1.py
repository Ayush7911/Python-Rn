while True:
    a=float(input('first number: '))
    b=float(input('second number: '))

    try:
        result = a/b
        print("result = {}".format(result))
    except ZeroDivisionError:
        print("Error : DIvision By Zero")

    try_again=input('\nTry Again (Y/N)? ')

    #if the user doesnt want to try again exit the loop
    if try_again.upper() !="Y":
        break

    print()

print('Good Bye!')


