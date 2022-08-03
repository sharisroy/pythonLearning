import re

# match function check only start value
pattern = r"Bangladesh"
if re.match(pattern, "Bangladesh is a beautiful country"):
    print("Match")
else:
    print("Not Match")

# search function check in full string
pattern = r"Bangladesh"
if re.search(pattern, "I love Bangladesh"):
    print("Match")
else:
    print("Not Match")

# find All return a list of item
pattern = r"Bangladesh"
print(re.findall(pattern, "Bangladesh is a beautiful country. I love Bangladesh"))

# More Expressions

pattern = r"Bangladesh"
text = r"Bangladesh is a beautiful country. I love Bangladesh"

match = re.search(pattern, text)
if match:
    # print start index where match
    print(match.start())
    # print last index where match
    print(match.end())
    # print both index where match
    print(match.span())
