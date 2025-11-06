""""
assignment operator (equal sign=)
its is a messenger used to take value on the right and store them on 
the memory location represented by the variables name 
as addresss on the left.

input function allows us to enter the value before running the program
input()function
it extracts values from the keyboard and stores them on memory represented by 
the address which is variable.
it allows us to enter the values while the program is running.
syntax:
Variable = input("prompt statement:")

"""
#Example of assignment operator
total = 100
print(total)
#input() function
#result = input("enter result:")
#print(result)

#type casting
oranges = int(input("enter total oranges:"))
mangoes = int(input("enter total mangoes:"))
total = oranges + mangoes
print("the total mangoes and oranges is", total)
