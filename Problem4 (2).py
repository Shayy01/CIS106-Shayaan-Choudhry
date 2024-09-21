#Input
qty = float(input("How many tickets?"))
#Process
if qty >= 25:
    ppt = 50
elif qty >= 10:
    ppt = 60
elif qty >= 5:
    ppt = 70
else:
    qty < 5
    ppt = 75
total = qty * ppt
#Output  
print(qty, ppt, total)