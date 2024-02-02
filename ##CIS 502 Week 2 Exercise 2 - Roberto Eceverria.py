##CIS 502 Week 2 Exercise 2 -  Roberto Echeverria

# This program acts as a bank account creator and transaction tracker.

import datetime # importing datetime to keep track of transaction times and dates

class Transaction:
    def __init__(self, amount, transaction_type):
        self.amount = amount
        self.transaction_type = transaction_type
        self.date = datetime.datetime.now()

    def display_transaction(self):
        print(f"Transaction Details:")
        print(f"Amount: ${self.amount:.2f}")
        print(f"Transaction Type: {self.transaction_type}")
        print(f"Date: {self.date}\n")


class BankAccount: # transactions list will store deposits and withdraws
    def __init__(self, account_number, account_holder, initial_balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.account_balance = initial_balance
        self.transactions = []

    def account_balance_check(self):
        print("+--------------------------------------------------+")
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Number: {self.account_number}")
        print(f"Account Balance: ${self.account_balance:.2f}")
        print("+--------------------------------------------------+")

    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
            transaction = Transaction(amount, "Deposit")
            self.transactions.append(transaction)
            print("+--------------------------------------------------+")
            print(f"Deposited ${amount:.2f}. Updated balance: ${self.account_balance:.2f}")
            print("+--------------------------------------------------+")
        else:
            print("Please enter a valid deposit amount such as: 50.")

    def withdraw(self, amount):
        if 0 < amount <= self.account_balance:
            self.account_balance -= amount
            transaction = Transaction(amount, "Withdrawal")
            self.transactions.append(transaction)
            print("+--------------------------------------------------+")
            print(f"Withdrew ${amount:.2f}. Updated balance: ${self.account_balance:.2f}")
            print("+--------------------------------------------------+")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def display_transactions(self): # range based function to display all stored transactions
        print("\nTransaction History:")
        print("+--------------------------------------------------+")
        for transaction in self.transactions:
            transaction.display_transaction()
        print("+--------------------------------------------------+")    


class Menu: # Initially sets bank account to none so the user cant use functions before creating a valid bank account
    def __init__(self):
        self.bank_account = None

    def create_account(self):
        while True:
            try:
                account_number = input("Enter your new 8-digit account number: ")
                if account_number.isdigit() and len(account_number) == 8:
                    account_holder = input("Enter account holder's name: ")
                    initial_balance = float(input("Enter initial balance: $"))
                    self.bank_account = BankAccount(account_number, account_holder, initial_balance)
                    break  # Exit the loop if account creation is successful
                else:
                    print("Invalid account number. Please enter a valid 8-digit number.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")





    def show_menu(self): # Menu displaying the options
        print("\n          Welcome to Chase Bank!\n")
        print("To create an account................Press 1: ")
        print("To check account balance............Press 2: ")
        print("To deposit money into your account..Press 3: ")
        print("To withdraw money from your account.Press 4: ")
        print("To display transaction history......Press 5: ")
        print("To quit.............................Press 6: \n")

    def getInputs(self): # checks for bank account creation to employ bank functions
        while True:
            self.show_menu()
            try:
                choice = int(input("Choose an option: "))
                if choice == 6:
                    print("Have a nice day!")
                    break
                elif choice == 1:
                    self.create_account()
                elif choice == 2 and self.bank_account:
                    self.bank_account.account_balance_check()
                elif choice == 3 and self.bank_account:
                    amount = float(input("Enter the amount you would like to deposit: $"))
                    self.bank_account.deposit(amount)
                elif choice == 4 and self.bank_account:
                    amount = float(input("Enter the amount you would like to withdraw: $"))
                    self.bank_account.withdraw(amount)
                elif choice == 5 and self.bank_account:
                    self.bank_account.display_transactions()
                else:
                    print("Please create a bank account first or enter a valid option such as 1, 2, 3, 4, 5, or 6 to quit.\n\n")
            except ValueError:
                print("Invalid input. Please enter a number.")


menu = Menu()
menu.getInputs()


'''
SAMPLE OUTPUTS WITH NEGATIVE TESTING

          Welcome to Chase Bank!

To create an account................Press 1: 
To check account balance............Press 2: 
To deposit money into your account..Press 3: 
To withdraw money from your account.Press 4:
To display transaction history......Press 5:
To quit.............................Press 6:

Choose an option: 2
Please create a bank account first or enter a valid option such as 1, 2, 3, 4, 5, or 6 to quit.



          Welcome to Chase Bank!

To create an account................Press 1:
To check account balance............Press 2:
To deposit money into your account..Press 3:
To withdraw money from your account.Press 4:
To display transaction history......Press 5:
To quit.............................Press 6:

Choose an option: 1
Enter your new 8-digit account number: 3
Invalid account number. Please enter a valid 8-digit number.
Enter your new 8-digit account number: 12345678
Enter account holder's name: Rob
Enter initial balance: $1000

          Welcome to Chase Bank!

To create an account................Press 1:
To check account balance............Press 2:
To deposit money into your account..Press 3:
To withdraw money from your account.Press 4:
To display transaction history......Press 5:
To quit.............................Press 6:

Choose an option: 2
+--------------------------------------------------+
Account Holder: Rob
Account Number: 12345678
Account Balance: $1000.00
+--------------------------------------------------+

          Welcome to Chase Bank!

To create an account................Press 1:
To check account balance............Press 2:
To deposit money into your account..Press 3:
To withdraw money from your account.Press 4:
To display transaction history......Press 5:
To quit.............................Press 6:

Choose an option: 3
Enter the amount you would like to deposit: $f
Invalid input. Please enter a number.

          Welcome to Chase Bank!

To create an account................Press 1:
To check account balance............Press 2:
To deposit money into your account..Press 3:
To withdraw money from your account.Press 4:
To display transaction history......Press 5:
To quit.............................Press 6:

Choose an option: 3
Enter the amount you would like to deposit: $4.50
+--------------------------------------------------+
Deposited $4.50. Updated balance: $1004.50
+--------------------------------------------------+

          Welcome to Chase Bank!

To create an account................Press 1:
To check account balance............Press 2:
To deposit money into your account..Press 3:
To withdraw money from your account.Press 4:
To display transaction history......Press 5:
To quit.............................Press 6:

Choose an option: 4
Enter the amount you would like to withdraw: $1.75
+--------------------------------------------------+
Withdrew $1.75. Updated balance: $1002.75
+--------------------------------------------------+

          Welcome to Chase Bank!

To create an account................Press 1:
To check account balance............Press 2:
To deposit money into your account..Press 3:
To withdraw money from your account.Press 4:
To display transaction history......Press 5:
To quit.............................Press 6:

Choose an option: 5

Transaction History:
+--------------------------------------------------+
Transaction Details:
Amount: $4.50
Transaction Type: Deposit
Date: 2024-01-29 22:30:19.058146

Transaction Details:
Amount: $1.75
Transaction Type: Withdrawal
Date: 2024-01-29 22:30:29.990935

+--------------------------------------------------+

          Welcome to Chase Bank!

To create an account................Press 1:
To check account balance............Press 2:
To deposit money into your account..Press 3:
To withdraw money from your account.Press 4:
To display transaction history......Press 5:
To quit.............................Press 6:

Choose an option: 6
Have a nice day!

'''


    

    
