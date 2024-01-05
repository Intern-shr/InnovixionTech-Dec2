class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance

    def display_balance(self):
        print(f"Account Balance for {self.account_holder}: ${self.balance:.2f}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Invalid deposit amount. Please enter a positive value.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

def main():
    print("Welcome to the Bank Account Management System!")
    account_holder_name = input("Enter your name: ")
    initial_balance = float(input("Enter initial balance (if any): "))
    
    # Creating a new account
    user_account = BankAccount(account_holder_name, initial_balance)
    
    while True:
        print("\nOptions:")
        print("1. Display Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            user_account.display_balance()
        elif choice == '2':
            deposit_amount = float(input("Enter deposit amount: "))
            user_account.deposit(deposit_amount)
        elif choice == '3':
            withdrawal_amount = float(input("Enter withdrawal amount: "))
            user_account.withdraw(withdrawal_amount)
        elif choice == '4':
            print("Exiting Bank Account Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
