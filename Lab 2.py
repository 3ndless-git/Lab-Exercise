#Write a Python program to convert temperatures to and from celsius,
#fahrenheit.
#C = (5/9) * (F - 32)

def temp():
    C = int((5 / 9) * (F - 32))
    print("The temp of weather is "+ " " + str(C) + " "+ "degree celsius.")
F = int(input("Temp in Fahrenheit : "))
temp()