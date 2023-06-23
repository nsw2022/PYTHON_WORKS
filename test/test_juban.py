import re

user_str=input("입력값 : ")

pt = re.compile("\d")
m = re.findall(pt, user_str)
result = "".join(m)

print(result)