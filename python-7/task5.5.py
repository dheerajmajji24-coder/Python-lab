#lab5:task5.5


balance = 1000

def deposit(amount):
    global balance
    balance += amount
    print("Amount deposited:", amount)
def withdraw(amount):
    global balance
    if amount <= balance:
        balance -= amount
        print("Amount withdrawn:", amount)
    else:
        print("Insufficient funds")
def check_balance():
    print("Current balance:", balance)
while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        amount = float(input("Enter deposit amount: "))
        deposit(amount)
    elif choice == 2:
        amount = float(input("Enter withdrawal amount: "))
        withdraw(amount)
    elif choice == 3:
        check_balance()
    elif choice == 4:
        print("Thank you!")
        break
    else:
        print("Invalid choice")


#output:
#1. Deposit
#2. Withdraw
#3. Check Balance
#4. Exit
#Enter your choice: 2
#Enter withdrawal amount: 100000
#Insufficient funds
#1. Deposit
#2. Withdraw
#3. Check Balance
#4. Exit
#Enter your choice: 3
#Current balance: 1000
