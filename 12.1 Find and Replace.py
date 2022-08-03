import re

# Find and Replace

pattern = r"Bangladesh"
text = "Bangladesh is a beautiful country. I love Bangladesh"

newText = re.sub(pattern, "BD", text)
print(newText)

# Count use for number of replace of number
newText = re.sub(pattern, "BD", text, count=1)
print(newText)