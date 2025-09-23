import tkinter as tk
from collections import deque

class AtmApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bank ATM Machine")
        self.root.geometry("1000x700")
        self.root.resizable(False, False)
        self.root.configure(bg="black")

        # ATM Data
        self.pin = ""
        self.balance = 0
        self.transactions = deque(maxlen=5)
        self.input_value = ""
        self.state = None

        # Fake Account Info
        self.account_details = {
            "Name": "Shoaib Khan",
            "Account No": "1234 5678 9876",
            "IFSC": "BKID0001234",
            "Branch": "Mumbai Main Branch"
        }

        # ========= ATM Screen =========
        self.display = tk.Label(root, text="💳 Welcome to Bank ATM 💳\n\nSelect an option",
                                font=("Arial", 18, "bold"),
                                bg="black", fg="lime",
                                width=60, height=6, relief="sunken", anchor="center", justify="center")
        self.display.place(x=100, y=30)

        # ========= Left Menu =========
        self.left_frame = tk.Frame(root, bg="black")
        self.left_frame.place(x=50, y=220)

        tk.Button(self.left_frame, text="Create PIN", font=("Arial", 14, "bold"),
                  width=18, bg="#ff7043", fg="white", command=self.create_pin).grid(row=0, column=0, pady=10)
        tk.Button(self.left_frame, text="Change PIN", font=("Arial", 14, "bold"),
                  width=18, bg="#ffcc80", fg="black", command=self.change_pin).grid(row=1, column=0, pady=10)
        tk.Button(self.left_frame, text="Deposit", font=("Arial", 14, "bold"),
                  width=18, bg="#42a5f5", fg="white", command=self.deposit).grid(row=2, column=0, pady=10)
        tk.Button(self.left_frame, text="More Services", font=("Arial", 14, "bold"),
                  width=18, bg="#9c27b0", fg="white", command=self.more_services).grid(row=3, column=0, pady=10)

        # ========= Right Menu =========
        self.right_frame = tk.Frame(root, bg="black")
        self.right_frame.place(x=730, y=220)

        tk.Button(self.right_frame, text="Check Balance", font=("Arial", 14, "bold"),
                  width=18, bg="#66bb6a", fg="white", command=self.check_balance).grid(row=0, column=0, pady=10)
        tk.Button(self.right_frame, text="Withdraw", font=("Arial", 14, "bold"),
                  width=18, bg="#29b6f6", fg="white", command=self.withdraw).grid(row=1, column=0, pady=10)
        tk.Button(self.right_frame, text="Fast Cash", font=("Arial", 14, "bold"),
                  width=18, bg="#ffb300", fg="black", command=self.fast_cash).grid(row=2, column=0, pady=10)
        tk.Button(self.right_frame, text="Bill Payment", font=("Arial", 14, "bold"),
                  width=18, bg="#ef5350", fg="white", command=self.bill_payment).grid(row=3, column=0, pady=10)

        # ========= Number Keypad =========
        self.keypad_frame = tk.Frame(root, bg="black")
        self.keypad_frame.place(x=360, y=350)

        btn_texts = [
            ("1",0,0), ("2",0,1), ("3",0,2),
            ("4",1,0), ("5",1,1), ("6",1,2),
            ("7",2,0), ("8",2,1), ("9",2,2),
            ("Clear",3,0), ("0",3,1), ("Enter",3,2)
        ]

        for (text, row, col) in btn_texts:
            tk.Button(self.keypad_frame, text=text, font=("Arial", 14, "bold"),
                      width=8, height=3, bg="gray20", fg="white",
                      command=lambda t=text: self.keypad_press(t)).grid(row=row, column=col, padx=5, pady=5)

    # =================== Keypad Handling ===================
    def keypad_press(self, key):
        if key == "Clear":
            self.input_value = ""
            self.display.config(text="🔄 Cleared. Enter again...")
        elif key == "Enter":
            self.process_input()
        else:
            if self.state in ["create_pin", "change_old", "change_new", "check", "withdraw_pin", "deposit_pin", "bill_pin"]:
                if len(self.input_value) >= 4:
                    self.display.config(text="❌ PIN can only be 4 digits!")
                    return
            self.input_value += key
            self.display.config(text=f"👉 {self.input_value}")

    # =================== ATM Operations ===================
    def create_pin(self):
        self.state = "create_pin"
        self.input_value = ""
        self.display.config(text="🔑 Create PIN\n\nEnter your new 4-digit PIN:")

    def change_pin(self):
        self.state = "change_old"
        self.input_value = ""
        self.display.config(text="🔑 Change PIN\n\nEnter your old PIN:")

    def check_balance(self):
        self.state = "check"
        self.input_value = ""
        self.display.config(text="💰 Balance Enquiry\n\nEnter your PIN:")

    def withdraw(self):
        self.state = "withdraw_pin"
        self.input_value = ""
        self.display.config(text="🏧 Withdraw Money\n\nEnter your PIN:")

    def fast_cash(self):
        self.state = "fast_cash_pin"
        self.input_value = ""
        self.display.config(text="⚡ Fast Cash\n\nEnter your PIN:")

    def deposit(self):
        self.state = "deposit_pin"
        self.input_value = ""
        self.display.config(text="💰 Deposit Money\n\nEnter your PIN:")

    def account_info(self):
        self.state = "acc_info"
        self.input_value = ""
        self.display.config(text="📋 Account Information\n\nEnter your PIN:")

    def bill_payment(self):
        self.state = "bill_pin"
        self.input_value = ""
        self.display.config(text="🧾 Bill Payment\n\nEnter your PIN:")

    def more_services(self):
        self.state = "more_menu"
        self.input_value = ""
        self.display.config(text="📌 More Services\n\n1. Mini Statement\n2. Card Services\n3. Loan Inquiry\n4. Account Info\n👉 Enter option number:")

    # =================== Input Processing ===================
    def process_input(self):
        if self.state == "create_pin":
            if len(self.input_value) == 4:
                self.pin = self.input_value
                self.state = "create_balance"
                self.input_value = ""
                self.display.config(text="💰 Enter initial balance:")
            else:
                self.display.config(text="❌ PIN must be 4 digits!")

        elif self.state == "create_balance":
            try:
                self.balance = int(self.input_value)
                self.transactions.append(f"Account created ₹{self.balance}")
                self.display.config(text="✅ Account created!\nPIN set & Balance added.")
                self.state = None
            except:
                self.display.config(text="❌ Balance must be a number!")
            self.input_value = ""

        elif self.state == "change_old":
            if self.input_value == self.pin:
                self.state = "change_new"
                self.display.config(text="Enter new 4-digit PIN:")
            else:
                self.display.config(text="❌ Incorrect PIN!")
                self.state = None
            self.input_value = ""

        elif self.state == "change_new":
            if len(self.input_value) == 4:
                self.pin = self.input_value
                self.transactions.append("PIN Changed")
                self.display.config(text="✅ PIN changed successfully!")
            else:
                self.display.config(text="❌ PIN must be 4 digits!")
            self.state = None
            self.input_value = ""

        elif self.state == "check":
            if self.input_value == self.pin:
                self.display.config(text=f"💰 Your balance is ₹{self.balance}")
            else:
                self.display.config(text="❌ Incorrect PIN!")
            self.state = None
            self.input_value = ""

        elif self.state == "withdraw_pin":
            if self.input_value == self.pin:
                self.state = "withdraw_amount"
                self.display.config(text="💰 Enter amount to withdraw:")
            else:
                self.display.config(text="❌ Incorrect PIN!")
                self.state = None
            self.input_value = ""

        elif self.state == "withdraw_amount":
            try:
                amt = int(self.input_value)
                if amt <= self.balance:
                    self.balance -= amt
                    self.transactions.append(f"Withdraw ₹{amt}")
                    self.display.config(text=f"✅ Withdraw Successful!\nRemaining Balance: ₹{self.balance}")
                else:
                    self.display.config(text="❌ Insufficient Balance!")
            except:
                self.display.config(text="❌ Invalid amount!")
            self.state = None
            self.input_value = ""

        elif self.state == "fast_cash_pin":
            if self.input_value == self.pin:
                self.state = "fast_cash_menu"
                self.display.config(text="⚡ Fast Cash Options\n\nLeft: 1) ₹200   2) ₹1000   3) ₹2000\nRight: 4) ₹500   5) ₹1500   6) ₹2500\n👉 Enter option number:")
            else:
                self.display.config(text="❌ Incorrect PIN!")
                self.state = None
            self.input_value = ""

        elif self.state == "fast_cash_menu":
            options = {"1":200, "2":1000, "3":2000, "4":500, "5":1500, "6":2500}
            if self.input_value in options:
                amt = options[self.input_value]
                if amt <= self.balance:
                    self.balance -= amt
                    self.transactions.append(f"Fast Cash ₹{amt}")
                    self.display.config(text=f"✅ Fast Cash ₹{amt} Withdrawn\nRemaining Balance: ₹{self.balance}")
                else:
                    self.display.config(text="❌ Insufficient Balance!")
            else:
                self.display.config(text="❌ Invalid choice!")
            self.state = None
            self.input_value = ""

        elif self.state == "deposit_pin":
            if self.input_value == self.pin:
                self.state = "deposit_amount"
                self.display.config(text="💰 Enter amount to deposit:")
            else:
                self.display.config(text="❌ Incorrect PIN!")
                self.state = None
            self.input_value = ""

        elif self.state == "deposit_amount":
            try:
                amt = int(self.input_value)
                self.balance += amt
                self.transactions.append(f"Deposit ₹{amt}")
                self.display.config(text=f"✅ Deposit Successful!\nNew Balance: ₹{self.balance}")
            except:
                self.display.config(text="❌ Invalid amount!")
            self.state = None
            self.input_value = ""

        elif self.state == "acc_info":
            if self.input_value == self.pin:
                masked_pin = "*" * len(self.pin)
                history = "\n".join(self.transactions) if self.transactions else "No transactions yet"
                info = f"📋 Account Info\n\nName: {self.account_details['Name']}\nAccount: {self.account_details['Account No']}\nIFSC: {self.account_details['IFSC']}\nBranch: {self.account_details['Branch']}\nPIN: {masked_pin}\nBalance: ₹{self.balance}\n\nLast Transactions:\n{history}"
                self.display.config(text=info)
            else:
                self.display.config(text="❌ Incorrect PIN!")
            self.state = None
            self.input_value = ""

        elif self.state == "bill_pin":
            if self.input_value == self.pin:
                self.state = "bill_amount"
                self.display.config(text="💰 Enter bill amount to pay:")
            else:
                self.display.config(text="❌ Incorrect PIN!")
                self.state = None
            self.input_value = ""

        elif self.state == "bill_amount":
            try:
                amt = int(self.input_value)
                if amt <= self.balance:
                    self.balance -= amt
                    self.transactions.append(f"Bill Paid ₹{amt}")
                    self.display.config(text=f"✅ Bill Payment Successful!\nRemaining Balance: ₹{self.balance}")
                else:
                    self.display.config(text="❌ Insufficient Balance!")
            except:
                self.display.config(text="❌ Invalid amount!")
            self.state = None
            self.input_value = ""

        elif self.state == "more_menu":
            choice = self.input_value
            if choice == "1":
                self.display.config(text="📑 Mini Statement\n\nShows last few transactions.\n(Use Account Info for details)")
            elif choice == "2":
                self.display.config(text="💳 Card Services\n\nOptions: Block Card, Request New Card, PIN Reset.")
            elif choice == "3":
                self.display.config(text="🏦 Loan Inquiry\n\nCheck eligibility for Personal Loan, Car Loan, Home Loan.")
            elif choice == "4":
                self.account_info()
                return
            else:
                self.display.config(text="❌ Invalid choice!")
            self.state = None
            self.input_value = ""


# Run the App
if __name__ == "__main__":
    root = tk.Tk()
    app = AtmApp(root)
    root.mainloop()
