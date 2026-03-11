# Scotland population data
a = 5.08  # Scotland population in 2004 (millions)
b = 5.33  # Scotland population in 2014 (millions)
c = 5.55  # Scotland population in 2024 (millions)

d = b - a  # Population change 2004-2014
e = c - b  # Population change 2014-2024

if d > e:
    t = "decelerating"
elif d < e:
    t = "accelerating"
else:
    t = "stable"

# Output results
print("Change from 2004-2014 was", d)
print("Change from 2014-2024 was", e)
print("Population growth trend was", t)

# 4.2 Booleans
# Define boolean variables X=True, Y=False
X = True
Y = False
W = X or Y  # Define W = X or Y
print("W = X or Y:", W)

# Truth table for W = X or Y:
# X | Y | W
# T | T | T
# T | F | T
# F | T | T
# F | F | F