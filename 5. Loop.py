number = [1,2,3,4,5,6,7,8,9,10]
print(number)
# For Loop
for n in number:
    print(n)
print("End For loop")

#                           Range

for x in range(10): # last value
    print(x, end=' ')
print("\nEnd Range loop")

for x in range(2,10): # start and last value
    print(x, end=' ')
print("\nEnd Range loop")

for x in range(2,10, 3): # start, last and Increment value
    print(x, end=' ')
print("\nEnd Range loop")

#                           While

i = 0
while i < 10:
    print(i, end=' ')
    i = i + 1
print("\nEnd While loop")


