n = int(input('Напишите сколько раз '))
max1 = -99999999999999999999999999999999999
max2 = -99999999999999999999999999999999999

for i in range(n):
    n2 = int(input())
    if n2 > max1 :
        max2 = max1
        max1 = n2
    elif n2 > max2 and n2 != max1:
        max2 = n2
        
print(max1)
print(max2)
