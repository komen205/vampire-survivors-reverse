import re

file = open("main.bundle.js", "r", encoding="UTF-8")
file_content = file.read()
expression = re.sub("_baseExperienceMultiplier..\s=([^,]*)","_baseExperienceMultiplier'] = 0xff",file_content)
print(expression)
file.close()
file = open("main.bundle.js", "w", encoding="UTF-8")
file.write(expression)
file.close()