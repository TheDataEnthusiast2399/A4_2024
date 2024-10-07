from typing import List


class Banking:
    def __init__(
        self, acc_no: int, acc_name: str, acc_type: str, acc_branch: str
    ) -> None:
        self.acc_no = acc_no
        self.acc_name = acc_name
        self.acc_type = acc_type
        self.acc_branch = acc_branch
        self.acc_balance = 0.0

    def check_balance(self) -> float:
        return self.acc_balance

    def deposit_amt(self, amt: float) -> float:
        if amt < 0:
            print("Invalid amount entered, Please enter a positive value.")
        else:
            self.acc_balance += amt
            print("Amount deposited successfully.")
            print(f"Current available balance for {self.acc_no} : {self.acc_balance}")
        return self.acc_balance

    def withdraw_amt(self, amt: float) -> float:
        if amt <= 0:
            print("Invalid amount entered, Please enter a positive value.")
        if self.acc_balance - amt < 0:
            print(f"Insufficient balance , Current balance : {self.acc_balance}")
        else:
            self.acc_balance -= amt
            print("Amount withdrawn successfully.")
            print(f"Current available balance for {self.acc_no}: {self.acc_balance}")
        return self.acc_balance

    def transfer_money(self, payee_acc: "Banking", amt: float) -> None:
        if amt <= 0:
            print("Invalid amount entered, Please enter a positive value.")
            return

        if self.acc_balance - amt < 0:
            print(f"Insufficient balance, Current balance: {self.acc_balance}")
            return

        # Withdraw amount from payer's account
        self.withdraw_amt(amt)

        # Deposit into payee's account
        payee_acc.deposit_amt(amt)
        print(
            f"Transfer of Rs.{amt} from {self.acc_name} to {payee_acc.acc_name} successful."
        )

    def display_acc(self):
        print("<---------------------------------------------->")
        print(f"Account Number : {self.acc_no}")
        print(f"Account Holder name : {self.acc_name}")
        print(f"Account type : {self.acc_type}")
        print(f"Account branch : {self.acc_branch}")
        print(f"Current available balance : {self.acc_balance}")
        print("<---------------------------------------------->")


bank_details: List[Banking] = []  # List of objects
bank_acc_no = set()  # Track of bank account numbers

while True:
    print("<------------------------------>")
    print("Welcome to CDB Banking Menu.")
    print("1. Add an account.")
    print("2. Display account details.")
    print("3. Check account balance.")
    print("4. Deposit amount.")
    print("5. Withdraw amount.")
    print("6. Transfer amount.")
    print("7. Exit")
    print("<------------------------------>")
    choice = int(input("Please enter your choice : "))

    # Add account
    if choice == 1:
        acc_no = int(input("Please enter the account number to be added : "))
        if acc_no not in bank_acc_no:
            acc_name = input("Enter the name of account holder : ")
            acc_type = input("Enter the account type (SAV/CURR) : ").upper()
            acc_branch = input("Enter the branch name : ")

            x = Banking(acc_no, acc_name, acc_type, acc_branch)  # Initialize object
            bank_details.append(x)  # Add object to list
            bank_acc_no.add(acc_no)  # Add acc_no to set
            print(f"Account number {acc_no} added successfully.")

        else:
            print("Account number already in the system. Please re-check.")

    # Display account details
    elif choice == 2:
        acc_no = int(
            input("Please enter the account number you want information for : ")
        )
        for acc in bank_details:
            if acc_no == acc.acc_no:
                acc.display_acc()
            else:
                print("Account number not found in the system.")

    # Check account balance
    elif choice == 3:
        acc_no = int(
            input("Please enter the account number you want balance information for : ")
        )
        for acc in bank_details:
            if acc_no == acc.acc_no:
                print(f"Current available balance : {acc.check_balance()}")
                break
            else:
                print("Account number not found in the system")
                break

    # Deposit amount
    elif choice == 4:
        acc_no = int(
            input("Please enter the account number you want to deposit amount for : ")
        )
        for acc in bank_details:
            if acc_no == acc.acc_no:
                amount = int(input("Enter the amount you want to deposit : "))
                acc.deposit_amt(amount)
                break
            else:
                print("Account not found in the system.")
                break

    # Withdraw Amount
    elif choice == 5:
        acc_no = int(
            input("Please enter the account number you want to withdraw amount from : ")
        )
        for acc in bank_details:
            if acc_no == acc.acc_no:
                amount = int(input("Enter the amount you want to withdraw : "))
                acc.withdraw_amt(amount)
                break
            else:
                print("Account not found in the system.")
                break

    # Transfer Amount
    elif choice == 6:
        payer_acc_no = int(input("Enter the sender account number: "))
        payee_acc_no = int(input("Enter the recepient account number: "))

        payer_acc = None
        payee_acc = None

        for acc in bank_details:
            if acc.acc_no == payer_acc_no:
                payer_acc = acc
            if acc.acc_no == payee_acc_no:
                payee_acc = acc

        if payer_acc is None:
            print("Payer account not found in the system.")
        elif payee_acc is None:
            print("Payee account not found in the system.")
        else:
            amount = float(input("Enter the amount you want to transfer: "))
            payer_acc.transfer_money(payee_acc, amount)

    # Exit
    elif choice == 7:
        print("Thanks! Please visit again")
        break

    else:
        print("Invalid choice.")
