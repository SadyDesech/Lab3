import re
text = input()
number = re.findall(r"[0123456789]",text)
print(number)
