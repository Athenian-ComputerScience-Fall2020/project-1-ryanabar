def rerun():
    y = 0
    while y<2:
        yogurtshack()
        y += 1

def yogurtshack():
    
    print("Welcome to Yogurt Shack! Please type your order below. ") #Introducing the store and asking for order
    print("\n")
    flavor = input("What would you like your yogurt flavor to be? ") #input ICE CREAM FLAVOR
    topping1 = input("Topping 1? ") #input FIRST TOPPING
    topping2 = input("Topping 2? ") #input SECOND TOPPING
    print("\n")
    lst = [flavor, topping1, topping2]

    print("Your order is" + str(lst))


    x = 0
    while x<1:
        print("Great selection!")
        print("\n")
        x += 1

    try:
        drink = input("What drink would you like with that? You can either say tea, water, coffee, or soda. ")
        if drink == "tea":
            print("Our tea is world-famous!")
        if drink == "Tea":
            print("Our tea is world-famous!")
        elif drink == "water":
            print("Sounds good!")
        elif drink == "Water":
            print("Sounds good!")
        elif drink == "coffee":
            print("I could go for some coffee now.")
        elif drink == "Coffee":
            print("I could go for some coffee now.")
        elif drink == "soda":
            print("Lucky you! This is our last one!")
        elif drink == "Soda":
            print("Lucky you! This is our last one!")
    except:
        print("Sorry, that is not a valid entry.")


    for i in range(1):
        print("\n")
        print("We hope you enjoy your meal. Have a great day and we hope to see you soon!")
        print("\n")
    

if __name__ == '__main__': 
    rerun()