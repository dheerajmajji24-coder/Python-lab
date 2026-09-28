#lab2:task2.5


def order_summary(customer, *items, discount=0, **extra):
    print("Customer:", customer)
    print("Ordered Items:")
    for item in items:
        print("-", item)
    print("Discount:", discount)
    print("Extra Information:")
    for key, value in extra.items():
        print(key.replace("_", " ").title(), ":", value)
order_summary(
    "Asha",
    "Laptop",
    "Mouse",
    "Keyboard",
    discount=500,
    delivery_address="Hyderabad",
    gift_wrap=True
)


#output:
#Customer: Asha
#Ordered Items:
#- Laptop
#- Mouse
#- Keyboard
#Discount: 500
#Extra Information:
#Delivery Address : Hyderabad
#Gift Wrap : True

