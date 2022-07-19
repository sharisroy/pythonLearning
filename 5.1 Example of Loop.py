number = [1,2,3,4,5,6,7,8,9,10]

#                   sum
sum = 0;
for x in number:
    sum = sum + x
print(sum)

sum = 0;
for x in range(10):
    sum = sum + x
print(sum)

sum = 0;
i = 1
while i <= 10:
    sum = sum + i
    i = i + 1
print(sum)

square = [value ** 2 for value in range(1,11)]
print(square)



