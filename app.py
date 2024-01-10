def myFunc(*variableArgs):
    print(variableArgs[0])
myArray =[i for i in range(15)]
print(myArray)
for f in myArray:
    print(f)
    if f%2!=0:
        print("none\n")
myFunc("Hellos")
