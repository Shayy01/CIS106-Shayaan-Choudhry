#Input phase
qty = float(input("how many widgets?"))
#Process
if qty > 10000:
    up = 10
elif qty > 5000:
    up = 20
else:
    up = 30
extp = qty * up
tax = extp * 0.07
total = extp + tax
#Output phase
print(extp, tax, total)