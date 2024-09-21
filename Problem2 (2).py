#Input Phase
pnum = input("What is the part number?")
qty = float(input("How many are you buying?"))
#Process
if pnum == "10" or pnum == "55":
    up = 1.00
elif pnum == "99":
    up = 2.00
elif pnum == "80" or pnum == "70":
    up = 3.00
else:
    up = 5.00
total = up * qty
#Output Phase
print(pnum, up, total)