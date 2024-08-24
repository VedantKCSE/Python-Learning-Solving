# Multiply Two Numbers without using * operator

a = int(input("No. 1: "))
b = int(input("No. 2: "))
c = int(input("No. 3: "))

ans = 0

for i in range(0,b):
    ans = ans + a
    i=i+1
    
ans2 = 0

for i in range(0,c):
    ans2 = ans2 + ans
    i = i+1
print(ans2)