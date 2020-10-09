def yogurtshack():
    
    print("Welcome to yogurt shack! Please type your order below.")

    flavor = input("what would u like ur falvor to be")
    topping1 = input("topping 1?")
    topping2 = input("topping 2?")

    lst = [flavor, topping1, topping2]

    print("Your order is" + str(lst))


    x = 0
    while x<5:
        print("hi")
        x += 1

    if flavor == "chocolate":
        print("ew")
    else:
        print("good choice")

    for i in range(2):
        print("hi")
    
yogurtshack()
yogurtshack()

