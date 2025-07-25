class Bank:
    def __init__(self,account_number,name,balance=0):
        self.account_number=account_number
        self.name=name
        self.balance=balance
    
    def deposit(self,amount):
        self.balance += amount
        print(f"{amount} deposited")

    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount} withdrawn.")
        else:
            print("Insufficient balance.")
        
    def showAccountDetails(self):
        print("Account No:", self.account_number)
        print("Name:", self.name)
        print("Balance: ₹", self.balance)

class SavingsAccount(Bank):
    def __init__(self,account_number,name,balance=0,interest_rate=4):
        super().__init__(account_number,name,balance)
        self.interest_rate = interest_rate
    
    def showAccountDetails(self):
        super().showAccountDetails()
        print("Interest Rate:",self.interest_rate,"%")

acc = SavingsAccount("12345","Vishal",5000)
acc.deposit(1500)
acc.withdraw(2000)
acc.showAccountDetails()