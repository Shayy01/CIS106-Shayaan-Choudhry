#Input Phase
Item = input("What Item?")
Qty = float(input("How many?"))
#Process Phase
if Item == "A":
    Unitprice = 10.00
else: 
    Unitprice = 20.00
Ext = Qty * Unitprice
#Output Phase
print(Item, Unitprice, Ext)