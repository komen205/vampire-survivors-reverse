#Beautifier of main.bundle.js
#C:\Program Files (x86)\Steam\steamapps\common\Vampire Survivors\resources\app\.webpack\renderer\formatter.py
#Change main3.js for main.bundle.js



#CLI js-beautify does not work because of encoding issues
#https://stackoverflow.com/questions/33059280/error-using-jsbeautifier-in-python-with-unicode-text




import jsbeautifier


with open("main.bundle.js", "r", encoding="UTF-8") as myfile:
    input_string = myfile.read()
    res = jsbeautifier.beautify(input_string)


file = open("main3.js", "w", encoding="utf-8")
file.write(res)
file.close()