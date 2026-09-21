year = int(input("In wich year were you born ?"))
age = 2026 - year
print("At the end of 2026 you will be " + str(age) + ".")
if age <= 12:
    print("You are a kid.")
if  17<=age > 12:
    print("You're a teenager.")
if age >= 18:
    print("You are an adult.")
