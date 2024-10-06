f = open("problem4.txt", "r")

c = 0.0
totalextp = 0.0

item = str(f.readline().rstrip('\n'))

while item !="":
  qty = float(f.readline())
  price = float(f.readline())

  extprice = qty * price

  totalextp = totalextp + extprice

print("Item is: ", item)
print("Quantity is: ", qty)
print("Price is: $", price)
print("Extended price is: $", extprice)

c = c + 1

item = str(f.readline().rstrip('\n'))

f.close()

print("Total extended price is: $", totalextp)