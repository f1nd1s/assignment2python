import math
result = 0
n = int(input('Enter a number: '))
for i in range(1,n+1):
    result += math.factorial(i)
print(result)