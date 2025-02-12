str = "RahulShettyAcademy.com"
str1 = "Consulting firm"
str3 = "RahulShetty"

print(str[0])

print(str[0:5])             #range 0 : 5 - 1

print(str + " " + str1)

print(str3 in str)      #check if str3 value consist in str value with result true or false

var = str.split(".")
print(var)
print(var[0])

str4 = "  great  "
print(str4.strip())     #cut all leading and trailing whitespaces
print(str4.lstrip())    #cut all leading whitespaces
print(str4.rstrip())    #cut all trailing whitespaces