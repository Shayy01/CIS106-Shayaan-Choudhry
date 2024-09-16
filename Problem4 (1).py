#Input Phase
Name = input("Appliance?")
Cost = float(input("Cost of appliance?"))
#Process Phase
if Cost > 1000:
    warrentee = 0.1
else:
    warrentee = 0.05
TW = Cost * warrentee
total = TW + Cost
#Output Phase
print(Name, Cost, TW, total)