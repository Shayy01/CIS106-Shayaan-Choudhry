# Input Phase
STS = input("Enter Stock Ticker Symbol")
amount = float(input("Enter amount of shares"))
price = float(input("Enter cost per share"))
# Process Phase
total = amount + price

# Output Phase
print("Stock: ", STS)
print("Amount invested ",total)