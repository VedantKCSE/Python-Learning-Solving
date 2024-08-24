# Convert a string to int without using built-in int()

str_input = input()

l = []
ans = 0

# Convert each character to an integer (digit) and store in list `l`
for i in str_input:
    l.append(ord(i) - ord('0'))  # Convert char to int by subtracting ASCII value of '0'

length = len(l)
mask = [10**i for i in reversed(range(length))]

# Loop through the list and calculate the integer value
for i in range(length):
    ans += l[i] * mask[i]  # Multiply each digit by its corresponding mask and sum

print(ans)
print(type(ans))
