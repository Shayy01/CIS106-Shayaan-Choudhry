#Input Phase
NBooks = float(input("Number of books?"))
CostB = float(input("Cost of each book?"))
#Process Phase
if CostB < 50.0:
    shipping = 25.0
else:
    shipping = 0
#Output Phase
Total = CostB * NBooks
print(Total, shipping)