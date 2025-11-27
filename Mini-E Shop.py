print("--- WELCOME TO MINI E-SHOP ---")

# arraylist
usernames = []  
passwords = []  

# LOGIN / REGISTER function
while True:
    print("\n1. Register")
    print("2. Login")
    choice = input("Enter your choice (1-2): ")

    if choice == "1":  # Register
        new_user = input("Enter new username: ")
        if new_user in usernames:
            print("Username already exists! Try another.")
            continue
        new_pass = input("Enter new password: ")
        usernames.append(new_user)
        passwords.append(new_pass)
        print("Registration successful!")

    elif choice == "2":  # Login
        login_user = input("Enter username: ")
        login_pass = input("Enter password: ")
        if login_user in usernames:
            index = usernames.index(login_user)
            if passwords[index] == login_pass:
                print("Login successful! Welcome,", login_user)
                break
            else:
                print("Wrong username or password!")
        else:
                print("Wrong username or password!")

    else:
                print("Invalid choice! Enter 1 or 2.")

# SHOP ITEMS
items = ["Perfume", "Umbrella", "Tumbler", "Skincare", "Bag"]
prices = [50, 100, 60 , 150, 300]

# CART LISTS
cart_items = []
cart_qty = []
cart_total = []

# MAIN SHOP LOOP
while True:
    print("\n--- MINI E-SHOP MENU ---")
    print("1. Add to Cart")
    print("2. View Cart")
    print("3. Remove Item from Cart")
    print("4. Clear Cart")
    print("5. Checkout")
    print("6. Exit")

    # Input validation
    while True:
        choice = input("Enter your choice (1-6): ")
        if choice in ["1","2","3","4","5","6"]:
            break
        else:
            print("Wrong input! Enter a number between 1 and 6.")

    # Add to cart
    if choice == "1":
        print("\nSelect item to add:")
        for i in range(len(items)):
            print(i + 1, items[i], "- â‚±", prices[i])

        while True:
            item_no = input("Enter item number (1-5): ")
            if item_no in ["1","2","3","4","5"]:
                item_no = int(item_no) - 1
                break
            else:
                print("Wrong input! Enter 1-5 only.")

        while True:
            qty = input("Enter quantity: ")
            if qty.isdigit() and int(qty) > 0:
                qty = int(qty)
                break
            else:
                print("Enter valid quantity (number > 0).")

        cart_items.append(items[item_no])
        cart_qty.append(qty)
        cart_total.append(prices[item_no] * qty)
        print(qty, items[item_no], "added to cart.")

    # View Cart
    elif choice == "2":
        if cart_items == []:
            print("Cart is empty.")
        else:
            print("\nYour Cart:")
            total = 0
            for i in range(len(cart_items)):
                print(i + 1, "-", cart_items[i], "x", cart_qty[i], "= â‚±", cart_total[i])
                total += cart_total[i]
            print("Subtotal: â‚±", total)

    # Remove item from cart
    elif choice == "3":
        if cart_items == []:
            print("Cart is empty. Nothing to remove.")
        else:
            print("\nYour Cart:")
            for i in range(len(cart_items)):
                print(i + 1, "-", cart_items[i], "x", cart_qty[i], "= â‚±", cart_total[i])

            while True:
                remove_no = input("Enter the item number to remove: ")
                if remove_no.isdigit() and 1 <= int(remove_no) <= len(cart_items):
                    remove_no = int(remove_no) - 1
                    removed_item = cart_items.pop(remove_no)
                    cart_qty.pop(remove_no)
                    cart_total.pop(remove_no)
                    print(removed_item, "has been removed from your cart.")
                    break
                else:
                    print("Invalid number! Enter correct item number.")

    # Clear Cart
    elif choice == "4":
        if cart_items == []:
            print("Cart is already empty.")
        else:
            cart_items = []
            cart_qty = []
            cart_total = []
            print("All items have been removed from your cart.")

    # Checkout
    elif choice == "5":
        if cart_items == []:
            print("Cart is empty.")
        else:
            total = 0
            print("\nCheckout:")
            for i in range(len(cart_items)):
                print(cart_items[i], "x", cart_qty[i], "= â‚±", cart_total[i])
                total += cart_total[i]

            if total > 500:
                discount = total * 0.10
                total -= discount
                print("10% discount applied: -â‚±", discount)

            print("Total Amount: â‚±", total)
            print("Thank you for shopping!")

            while True:
                again = input("Do you want to shop again? (yes/no): ").lower()
                if again in ["yes","no"]:
                    break
                else:
                    print("Type 'yes' or 'no' only.")

            if again == "yes":
                cart_items = []
                cart_qty = []
                cart_total = []
                continue
            else:
                print("Exiting Mini E-Shop.")
                break

    # Exit
    elif choice == "6":
        print("Exiting Mini E-Shop.")
        break