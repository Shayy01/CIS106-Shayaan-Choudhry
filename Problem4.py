# Input phase
Make = input("What is the make")
Model = input("What is the model")
MSRP = float(input("What is the MSRP amount"))
DiscountP = float(input("What is the discount percent"))
# Process phase
Amountoff = MSRP * DiscountP
DiscountA = MSRP - Amountoff 
# Output phase
print(Make, Model, MSRP, DiscountP, Amountoff, DiscountA)