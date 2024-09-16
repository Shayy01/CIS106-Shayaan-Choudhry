#Input Phase
Lname = input("Lastname?") 
Ndep = float(input("Number of Dependents?"))
GI = float(input("Gross Income?"))
#Process Phase
GDep = Ndep * 12000
AGI = GDep - GI
if AGI > 50000:
    trate = 0.2
else:
    trate = 0.1
IT = AGI * trate
if IT > 0:
    trate = 100
else:
    IT
#Output Phase
print(Lname, GI, Ndep, AGI, IT)