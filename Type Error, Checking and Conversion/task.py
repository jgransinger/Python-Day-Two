#len() does not work on integers
len("12345")

#print(type) / type checking of data types
print(type("Randy Moss"))
print(type(84))
print(type(19.98))
print(type(True))

#type conversation type casting typecasting - returns 1368 (string converted to int +  int)
print(int("1245") + 123)

# challenge - fix errors in line:  print("Number of letters in your name: " + len(input("Enter your name"))
name = input("Enter your name")
nameLength = str((len(name)))
print("Number of letters in your name: " + nameLength)