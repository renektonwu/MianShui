import re

pattern = "<a (.*?)</a>"
file_path="D:\Daniel\work\code\code_for_work\SpiderProject\CDFSanya\sanya.html"

with open(file_path, "r") as f:
    a = re.findall(pattern,str(f.readlines()))
    # print(a)

for i in a:
    print(i)

