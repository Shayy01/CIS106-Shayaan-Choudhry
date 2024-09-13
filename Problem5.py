# Input phase
CirRad = float(input("Enter radius of circle"))
# Process phase
Radius2 = float(CirRad*CirRad)
AreaPi = float(Radius2*3.174)
L = float(3.174*CirRad)
Perimeter = float(2*L)
# Output phase
print(AreaPi, Perimeter)