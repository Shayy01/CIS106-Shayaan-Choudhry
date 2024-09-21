#Input
p = float(input("What is the principle?"))
mature = float(input("How many years old is it?"))
#Process
if p > 100000 and mature >= 5:
    rate = 0.06
elif p >= 50000 and mature >= 10:
    rate = 0.05
elif p >= 50000 and mature >= 5:
    rate = 0.04
else 
    rate = 0.02
first_year = p * rate
#Output
print(p, rate, first_year)