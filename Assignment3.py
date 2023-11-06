# Declare variables and lists to be used in our main functions

items = [["tomato", 1], ["potato", 2], ["chocolate", 3], ["soap", 0.5]]
available_items = []
wanted_item_list = []
wanted_item_list_items = []
bill = 0

# Creating a list to view only the available names of the items,so we can check later whether the input items are
# available

for n in range(0, len(items)):
    available_items.append(items[n][0])


# declaring global variable bill. I want the value of bill to be used in and out of the function.
# The reason being is I want to return the whole list of items including item name, quantities, and price. I don't want
# to return a tuple at this stage of our course.

# So many nested lists, so I can temporarily pick the current information of the user buying. 

def addItem():
    more = "y"
    global bill
    while more != "n":
        print("\nItems available:")
        for n in range(0, len(items)):
            print("\n", f"{n + 1}.", f"{items[n][0]}\t", f"{items[n][1]}$")
        wanted = input("\nWhat items do you like to buy ?\n")
        wanted_items = wanted.split()
        print(wanted_items)
        wanted_and_available_list = []
        for n in range(0, len(wanted_items)):
            for num in range(0, len(items)):
                if wanted_items[n] in items[num]:
                    wanted_and_available_list.append([items[num][0], items[num][1]])
        print(wanted_and_available_list)
        for n in range(0, len(wanted_items)):
            if wanted_items[n] not in available_items:
                print(f"sorry {wanted_items[n]} is not available")
        for n in range(0, len(wanted_item_list)):
            wanted_item_list_items.append(wanted_item_list[n][0])
        for n in range(0, len(wanted_and_available_list)):
            wanted_quantity = int(input(f"How many {wanted_and_available_list[n][0]} do you want\t"))
            product_name = wanted_and_available_list[n][0]
            if wanted_and_available_list[n][0] not in wanted_item_list_items:
                wanted_item_list.append([wanted_and_available_list[n][0], wanted_quantity, wanted_quantity *
                                         wanted_and_available_list[n][1]])
                bill += wanted_quantity * wanted_and_available_list[n][1]
            else:
                product_name_index = wanted_item_list_items.index(product_name)
                wanted_item_list[product_name_index][1] += wanted_quantity
                wanted_item_list[product_name_index][2] += wanted_quantity * wanted_and_available_list[n][1]
                bill += wanted_quantity * wanted_and_available_list[n][1]
            print(bill)
        print(wanted_item_list)
        more = input("Do you want more items ? y/n\t")
    return wanted_item_list


def checkTotal():
    print(f"\nThe total bill is {bill} $\n")


def addCoupon(coupon_sum):
    for i in range(0, coupon_sum):
        coupon = input(f"Enter the value of coupon number {i + 1}\t")
        coupon_sum += int(coupon)
    print(f"\nThe Total Value of Your Coupons is: {coupon_sum}")
    final_bill = bill - coupon_sum
    print(f"The Final Bill Will be: \n Total Bill: {bill}\n - \n Coupon Sum: {float(coupon_sum)} \n = {final_bill} $")
    return final_bill


def check0ut(coupon_sum, final_bill):
    print("You have bought the following items: ")
    for n in range(0, len(wanted_item_list)):
        print(f"{wanted_item_list[n][0]}\t Quantity: {wanted_item_list[n][1]}\t Price: {wanted_item_list[n][2]}")
    print(f"Tal Price is: \t{bill} $")
    print(f"Your Total number of coupons is: {coupon_sum}")
    print(f"Final Price After Discount: {final_bill} $")


def newOrder():
    choice = -99  # dummy value
    while choice != 4:
        print("Enter")
        print("1. to add an item")
        print("2. to check total")
        print("3. to add a coupon")
        print("4. to checkout")
        choice = int(input())

        if choice == 1:
            addItem()
        elif choice == 2:
            checkTotal()
        elif choice == 3:
            coupon_sum = int(input("How many coupons do you have ?\t"))
            final_bill = addCoupon(coupon_sum)
        elif choice == 4:
            check0ut(coupon_sum, final_bill)
        else:
            print("invalid input")


# Menus
def mainMenu():
    choice = -99  # dummy value
    while choice != 2:
        print("Enter")
        print("1. to start a new order")
        print("2. to close the program")

        choice = int(input())

        if choice == 1:
            print("starting a new order...")
            newOrder()
        elif choice == 2:
            print("Have a Good Day!")
        else:
            print("invalid input")


mainMenu()
