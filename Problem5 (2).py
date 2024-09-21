#Input
Lname = input("What is your last name?")
$ = float(input("What is your salary?"))
JL = float(input("How many years have you worked here?"))
#Process
if JL >= 10:
    rate = 0.25
elif JL >= 5:
    rate = 0.20
else:
    rate = 0.10
bonus = $ * rate
#Output
print(lname, bonus)
