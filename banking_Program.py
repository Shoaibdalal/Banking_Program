"""def show_balance(balance):
    print("********************")
    print(f"Your balance is ${balance:.2f}")
    print("********************")

def deposit():
    print("********************")
    amount = float(input("Enter an amount to be deposited: "))
    print("********************")
    if amount < 0:
        print("********************")
        print("That's not a valid amount")
        print("********************")
        return 0
    else:
        return amount
def withdraw(balance):
    print("********************")
    amount = float(input("Enter amount to be withdrawn: "))
    print("********************")

    if amount > balance:
        print("********************")
        print("Insufficient Funds")
        print("********************")
        return 0
    elif amount < 0:
        print("Amount must be greater than 0")
        return 0
    else:
        return amount
    
def main():
    balance = 0
    is_running = True

    while is_running:
        print("*********************")
        print("Banking Program")
        print("*********************")
        print("1.Show Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")
        print("*********************")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
            print("*********************")
            print("That is not a valid choice")
            print("*********************")
    print("********************")
    print("Thank you! Have a nice day!")

if __name__ == '__main__':
    main()"""
def show_balance(balance):
    print("********************")
    print(f"Your balance is ${balance:.2f}")
    print("********************")

def deposit():
    print("********************")
    amount = float(input("Enter an amount to be deposited: "))
    print("********************")
    if amount < 0:
        print("********************")
        print("That's not a valid amount")
        print("********************")
        return 0
    else:
        return amount

def withdraw(balance):
    print("********************")
    amount = float(input("Enter amount to be withdrawn: "))
    print("********************")

    if amount > balance:
        print("********************")
        print("Insufficient Funds")
        print("********************")
        return 0
    elif amount < 0:
        print("Amount must be greater than 0")
        return 0
    else:
        return amount

def create_pin():
    while True:
        pin = input("Create a 4-digit PIN: ")
        if pin.isdigit() and len(pin) == 4:
            print("PIN created successfully!")
            return pin
        else:
            print("Invalid PIN. Please enter a 4-digit number.")

def verify_pin(pin):
    entered = input("Enter your PIN: ")
    if entered == pin:
        return True
    else:
        print("Incorrect PIN!")
        return False

def change_pin(current_pin):
    old = input("Enter your current PIN: ")
    if old != current_pin:
        print("Incorrect current PIN!")
        return current_pin
    while True:
        new_pin = input("Enter new 4-digit PIN: ")
        if new_pin.isdigit() and len(new_pin) == 4:
            print("PIN changed successfully!")
            return new_pin
        else:
            print("Invalid PIN. Please enter a 4-digit number.")

def main():
    balance = 0
    is_running = True

    # First-time PIN setup
    pin = create_pin()

    while is_running:
        print("*********************")
        print("Banking Program")
        print("*********************")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Change PIN")
        print("5. Exit")
        print("*********************")

        choice = input("Enter your choice (1-5): ")

        if choice in ['1', '2', '3']:  # Require PIN for money actions
            if not verify_pin(pin):
                continue

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            pin = change_pin(pin)
        elif choice == '5':
            is_running = False
        else:
            print("*********************")
            print("That is not a valid choice")
            print("*********************")

    print("********************")
    print("Thank you! Have a nice day!")

if __name__ == '__main__':
    main()
