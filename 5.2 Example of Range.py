# 1 to n print
n = int(input("Enter a number: "))
for x in range(1, n+1, 1):
    print(x, end=' ')
print("\nEnd 1 to n print")

# 1*1 + 2*2 + 3*3 + ..... n*n
result = 0
for x in range(1, n+1, 1):
    result = result + x * x
    print(x*x, end=' ')
print("\n", result)
print("End 1*1 + 2*2 + 3*3 + ..... n*n")