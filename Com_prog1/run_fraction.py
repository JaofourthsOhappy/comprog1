import fraction

# 1/2 + 1/3 = 5/6
x = [1, 2]
y = [1, 3]
z = fraction.add(x, y)
print(fraction.fstring(z))

# 1/3 + 1/6 = 1/2
x = [1, 3]
y = [1, 6]
z = fraction.add(x, y)
print(fraction.fstring(z))

# 8/9 + 1/9 = 1/1
x = [8, 9]
y = [1, 9]
z = fraction.add(x, y)
print(fraction.fstring(z))

# 1/200000000 + 1/300000000 = 1/120000000
x = [1, 200000000]
y = [1, 300000000]
z = fraction.add(x, y)
print(fraction.fstring(z))

# 1073741789/20 + 1073741789/30 = 1073741789/12
x = [1073741789, 20]
y = [1073741789, 30]
z = fraction.add(x, y)
print(fraction.fstring(z))

# 4/17 + 17/4 = 305/68
x = [4, 17]
y = [17, 4]
z = fraction.add(x, y)
print(fraction.fstring(z))

# 4/17 + 17/4 = 1/1
x = [4, 17]
y = [17, 4]
z = fraction.multiply(x, y)
print(fraction.fstring(z))

# 3037141/3247033 * 3037547/3246599 = 841/961 
x = [3037141, 3247033]
y = [3037547, 3246599]
z = fraction.multiply(x, y)
print(fraction.fstring(z))

# 1/6 - -4/-8 = -1/3
x = [1, 6]
y = [-4, -8]
z = fraction.subtract(x, y)
print(fraction.fstring(z))


