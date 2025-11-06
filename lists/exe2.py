#create a list to use as your shopping list with 3 items

#"milk","bread", and "apples"
shopping_list = ["milk","bread","apples"]


#check your list length and print
print(len(shopping_list))

#update bread with banana and eggs
shopping_list.insert(1, "banana")
shopping_list.insert(1,"eggs")


#remove the last item from the list and output it into the console
show = shopping_list.pop()
print(show)

#sort the list alphabetically
shopping_list.sort()
print(shopping_list)

#find and output the value of milk
show = shopping_list.index("milk")
print(show)

#after bananas,add carrots and lettuce

shopping_list.insert(1,"carrots")
shopping_list.insert(1,"lettuce")
print(shopping_list)

#create a new list containing juice and pop.
list = []
shop = ["juice","pop"]

#combine both lists, adding the new list twice to the end of the first list
shopping_list.extend(shop)
shopping_list.extend(shop)
print(shopping_list)

#get the last index value of pop and output it to the console.

L = shop.index("pop")
print(L)
#your final list should look like that
print(shopping_list)

shopping_list.remove("bread")
print(shopping_list)

shopping_list.remove("lettuce")
print(shopping_list)

shopping_list.insert(2,"lettuce")
print(shopping_list)

#create a list containing three values: 1,2,3.

new_list =[1,2,3]
print(new_list)
#nest the original list into a new list three times
new_list.extend(new_list)
new_list.extend(new_list)
print(new_list)

#output the value of 2 from one of the lists into console
v = new_list.pop(1)
print(v)

