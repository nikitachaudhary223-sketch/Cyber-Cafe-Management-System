# ==========================================
#       CYBER CAFE MANAGEMENT SYSTEM
# ==========================================

customers = []
daily_earnings = 0


# ------------------------------------------
# 1. Add Customer
# ------------------------------------------
def add_customer():
    print("\n========== ADD CUSTOMER ==========")

    name = input("Enter customer name: ")
    computer = input("Enter computer number: ")

    try:
        hours = float(input("Enter hours used: "))
        pages = int(input("Enter number of printed pages: "))
    except ValueError:
        print("Invalid input! Please enter numbers correctly.")
        return

    # Check whether computer is already occupied
    for customer in customers:
        if customer["computer"] == computer:
            print("This computer is already occupied!")
            return

    customer = {
        "name": name,
        "computer": computer,
        "hours": hours,
        "pages": pages
    }

    customers.append(customer)

    print("\nCustomer added successfully!")
    print(f"Customer: {name}")
    print(f"Computer: {computer}")


# ------------------------------------------
# 2. Show Customers
# ------------------------------------------
def show_customers():
    print("\n========== ACTIVE CUSTOMERS ==========")

    if len(customers) == 0:
        print("No active customers.")
        return

    for number, customer in enumerate(customers, start=1):
        print(f"\nCustomer {number}")
        print(f"Name     : {customer['name']}")
        print(f"Computer : {customer['computer']}")
        print(f"Hours    : {customer['hours']}")
        print(f"Pages    : {customer['pages']}")


# ------------------------------------------
# 3. Search Customer
# ------------------------------------------
def search_customer():
    print("\n========== SEARCH CUSTOMER ==========")

    search_name = input("Enter customer name: ").lower()

    found = False

    for customer in customers:
        if customer["name"].lower() == search_name:
            print("\nCustomer found!")
            print(f"Name     : {customer['name']}")
            print(f"Computer : {customer['computer']}")
            print(f"Hours    : {customer['hours']}")
            print(f"Pages    : {customer['pages']}")

            found = True

    if not found:
        print("Customer not found.")


# ------------------------------------------
# 4. Checkout Customer
# ------------------------------------------
def checkout_customer():
    global daily_earnings

    print("\n========== CUSTOMER CHECKOUT ==========")

    computer = input("Enter computer number: ")

    found = False

    for customer in customers:

        if customer["computer"] == computer:

            # Pricing
            computer_rate = 50
            printing_rate = 2

            computer_charge = customer["hours"] * computer_rate
            printing_charge = customer["pages"] * printing_rate

            total = computer_charge + printing_charge

            print("\n========== BILL ==========")
            print(f"Customer          : {customer['name']}")
            print(f"Computer          : {customer['computer']}")
            print(f"Computer Charge   : Rs. {computer_charge:.2f}")
            print(f"Printing Charge   : Rs. {printing_charge:.2f}")
            print("---------------------------")
            print(f"Total Bill        : Rs. {total:.2f}")
            print("===========================")

            daily_earnings += total

            customers.remove(customer)

            print("\nCustomer checked out successfully!")
            print("Thank you for using our Cyber Cafe!")

            found = True
            break

    if not found:
        print("No customer found on this computer.")


# ------------------------------------------
# 5. Show Daily Earnings
# ------------------------------------------
def show_earnings():
    print("\n========== DAILY EARNINGS ==========")
    print(f"Total earnings: Rs. {daily_earnings:.2f}")


# ------------------------------------------
# 6. Main Menu
# ------------------------------------------
def main():

    while True:

        print("\n")
        print("========================================")
        print("        CYBER CAFE MANAGEMENT")
        print("========================================")
        print("1. Add Customer")
        print("2. Show Active Customers")
        print("3. Search Customer")
        print("4. Checkout Customer")
        print("5. Show Daily Earnings")
        print("6. Exit")
        print("========================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_customer()

        elif choice == "2":
            show_customers()

        elif choice == "3":
            search_customer()

        elif choice == "4":
            checkout_customer()

        elif choice == "5":
            show_earnings()

        elif choice == "6":
            print("\nThank you for using Cyber Cafe Management System!")
            break

        else:
            print("\nInvalid choice! Please select 1-6.")


# ------------------------------------------
# Start Program
# ------------------------------------------
main()