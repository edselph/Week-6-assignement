price = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
    
quantity = {
    "banana": 3,
    "apple": 3,
    "orange": 3,
    "pear" :3 ,
}

for x in price:
    print(x)
    print("Price: " ,int(price[x]))
    print("Quantity: " , int(quantity[x]))

Totall = 0
for x in price:
    print(price[x]*quantity[x])
    Totall = Totall + price[x] * quantity[x]
print("Total: ", float(Totall))