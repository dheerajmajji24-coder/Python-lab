#lab4:task4.5

items = {
    "Pen": 20,
    "Book": 100,
    "Pencil": 10,
    "Bag": 500,
    "Eraser": 5
}
sorted_items = sorted(items.items(), key=lambda item: item[1])
print("Items from cheapest to most expensive:")
for item, price in sorted_items:
    print(item, ":", price)



#output:
#Items from cheapest to most expensive:
#Eraser : 5
#Pencil : 10
#Pen : 20
#Book : 100
#Bag : 500
