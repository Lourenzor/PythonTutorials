var = 24 % 4
var2 = 2**3.1
print(var)

if var % 2 > 0:
    print("This is an odd number")
else:
    print("This is  even number")
if (var + var2) > 6:
    print("the sum of all variable are  \tgreater than 6")
    print(type(var2))
    print(len("this is sweet"))
    mystring = "Hello World"
    print(mystring[-11])

    mystring = "abcdefghijk"
    print(mystring[3:-2])

    mystring = "abcdefghijk"
    print(mystring[:6])

    print(mystring[::2])
    print(mystring[::-1])
    print(mystring[1:7:2])

    name = "sam"
    print(name[1:])
    Last_letters = name[1:]
    name = "p"+Last_letters
    print(name.upper())

    X = "Hey There Please Split My Sausage"
print(X.split("e"))
