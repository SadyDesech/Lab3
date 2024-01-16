import re
text = input()
num = re.findall(r"[0123456789]",text)
print(num)