def func1():
    your_age = input("How old are you?")
    friends_age = input('How old is your friend?')
    if your_age >= 18 or friends_age >= 18:
        print('Sorry no cake at least one of you!')
    else:
        print('Hey, you both can have cakes')

    ###
    username = input("Welcome, please enter your username:")
    password = input("Please enter your password:")

    if username != 'tony' and password != 'password123':
        print("Access granted.")
    else:
        print("Access denied")

def func2():
    #Name registering
    registered_names = ['tony', 'frank', 'mary', 'peter']
    username = input("Please enter the user name you would like to use:")

    #check if username is already taken
    if username in registered_names:
        print("Sorry, username is already taken")
    else:
        print("This username is available")

def func3():
    #Admin users
    admin_users = ['thang', 'huy']

    # ask for username
    username = input("Please enter your username:")

    #check if user is an admin user
    if username not in admin_users:
        print("Access denied!")
    else:
        print("Access granted!")

def func4():
    # Get user balance
    balance = input("What is your bank balance?")

    # Check the balance
    if int(balance) <= 50:
        print("You are not qualified for interest.")
    elif int(balance) < 100:
        print("Your interest rate is 1%")
    else:
        print("Your interest rate is 2%.")

def func5():
    # Create a list of booking details
    booking_details = ['thang', 'middle row', 'screen two']

    if 'tony' in booking_details:
        print('Welcome to Udemy cinema')
    if 'middle row' in booking_details:
        print('Your seat number is 010 in the middle row')
    if 'screen two' in booking_details:
        print('Screen two it is!')

def func6():
    # Creating our shopping cart
    shopping_cart = ['pens', 'paper', 'stapler', 'rubber']

    # Adding each item to an order
    for item in shopping_cart:
        if item == 'pens':
            print("Sorry, " + item + " is out of stock")
        else:
            print("Adding " + item + " to your order.")

    print("Your order is complete")

def func7():
    #Working with empty lists
    shopping_cart = []

    if shopping_cart:
        for item in shopping_cart:
            print("Adding " + item + " to your cart")
        print("Your order is complete")
    else:
        print("You must select an item before proceeding.")

def concat(*args, sep = ", "):
    return sep.join(args)

def func8():
    # Working with multiple lists
    in_stock = ['blue pens', 'paper', 'staples']
    shopping_cart = ['blue pens', 'paper', 'staples', 'orange notebook']
    order = []
    for item in shopping_cart:
        if item in in_stock:
            print("Adding " + item + " to your order")
            order.append(item)
        else:
            print("Sorry " + item + " is out of stock")
    print("Your order is completed: ",concat(*order),".") #*order de pha' list





