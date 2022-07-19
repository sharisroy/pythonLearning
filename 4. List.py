name = ['1', '2', '3', "4"]
print(name)
print(name[3].title())
print(len(name))
name.insert(4, "5") # insert
print(len(name))
print(name)
print(name[4])

#remove item
name.remove("1")
print(len(name))
print(name)

del name[0]
print(len(name))
print(name)

#Append and pop
print("\t\t.........POP...............")
print(name)
print("POP: ", name.pop(0))
print("Lenth: ", len(name))
print(name)

print("\t\t.........Append...............")
print(name)
print("POP: ", name.append("6"))
print("Lenth: ", len(name))
print(name)

print("\t\t.........Remove...............")
name.remove("4")
print("Lenth: ", len(name))
print(name)

number = [5,2,3,10,8,6,7,1,9,4]
print(min(number))
print(max(number))
print(sum(number))
print(number.reverse())
print(number)
number.sort()
print(number)


#                           tuples

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

dimensions = (400, 10)
print(dimensions[0])
print(dimensions[1])

