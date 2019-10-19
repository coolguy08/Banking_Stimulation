import re

str = "0123456789"

#Check if the string has any + characters:

x = re.findall("[0-9]", str)

print(x)

if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")
