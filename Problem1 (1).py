#Input Phase
qty = float(input("How many?:"))
#Process Phase
if qty > 1000:
   unit = 3.00
else:
    unit = 5.00
exp = qty * unit
tax = exp * 0.7
total = exp + tax


#Output Phase
print(qty, exp, tax, total)