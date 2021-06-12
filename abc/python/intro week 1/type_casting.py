""" 
typecasting is used to change data types eg. str to int
syn> int() --- wrap inside the syntax
float()
str()
** input is always str ** convert it to int or float for calculations
"""
age = "7789"
print(type(age), "this is a string", age)



age = int(age)
print("this is converted to no",age,  type(age))

print("please write your age")
age1 = input()
print("hey you are ",age1, "years old")
print(type(age1))
