fruit = "mangoes"
print(fruit)

#how to create a list
#syntax variable = [items]
vegetables = ["kales","spinach","managu","cabbage", "Bak choi","kunde"]

print(vegetables)

#index 0,1,2,3,4,5...
print(vegetables[0])

item = vegetables[0]
print (item)

#method 2
print(vegetables[3])

#method 2
item = vegetables[5]
print(item)

#reversed index
# #-1,-2,-3,-4
print(vegetables[-4])
#slicing variables[start_index:stop_index], stop_index is ignored
#values in index 0, 1 will be retrieved item 
#in index 2 will be ignored

sliced = vegetables[0:2]
print(sliced)
sliced = vegetables[2:4]
print(sliced)

#lists of numbers
numbers =[10,14,16,22,57]
t = numbers[0]+ numbers[4]
print(t)

#mixed lists

mixed=["suluhu", 453,78,88,34,["kenya","uganda","tanzania",["hello","world"]], True, False]
inner_list = mixed[5][3][1]
print(inner_list)

countries = ["kenya", "congo", "uganda"]
countries[1]= "malawi"

print(countries)

#append (add item)

countries.append("kenya")
countries.append("uganda")
print(countries)

#exercise 1
#Practices Exercise 1
#a) Create an empty list called  "fruits_list"
#b) add three fruits, [mangoes, banana, apples]
#c) remove item called banana in its index replace "pineapples"
#d) reverse the list in that the last item is the first.

fruit_list = []

fruit_list.append("mangoes")
fruit_list.append("banana")
fruit_list.append("apples")

print(fruit_list)






