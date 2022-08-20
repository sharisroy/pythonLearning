file = open("File/myread.txt", "r", encoding="utf8")

print(file.readable())
text = file.read()
print(text)
print("Line: ", len(text))
file.close()
