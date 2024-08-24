# Print Hello World Without Using String

# Using List
l = ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']
ans = ''.join([chr(ord(i)) for i in l])
print(ans)
print(type(ans))

# Using Character
ans2 = chr(72) + chr(101) + chr(108) + chr(108) + chr(111) + chr(32) + chr(87) + chr(111) + chr(114) + chr(108) + chr(100)
print(ans2)
print(type(ans2))