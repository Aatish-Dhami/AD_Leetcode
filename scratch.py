low = 6
high = 10
root = [10,5,15,3,7,13,18,1,0,6]
sum = 0

for i in range(low, high + 1):
    if i in root:
        sum = sum + i

print(sum)