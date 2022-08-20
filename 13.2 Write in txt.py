# "a" - Append - will append to the end of the file
# "w" - Write - will overwrite any existing content
# "x" - Create - will create a file, returns an error if the file exist

# f = open("File/myWrite.txt", "a")
# f.write("Now the file has more content!")
# f.close()
#
# #open and read the file after the appending:
# f = open("File/myWrite.txt", "r", encoding="utf8")
# print(f.read())


f = open("File/myWrite.txt", "w", encoding="utf8")
print(f.writable())
print(f.encoding)
f.write("\nকলকাতার একটি রেস্তরাঁর বিরিয়ানি খেতে চাইলেন সৌরভ\nसोने के तारों ")
f.close()

#open and read the file after the appending:
f = open("File/myWrite.txt", "r", encoding="utf8")
print(f.read())