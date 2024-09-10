class Bank:


    def create_account(self,account_num,account_type):

        self.account_num=account_num

        self.bank_name="SBT"

        self.__balance=2000

        self.account_type=account_type
    

    def deposit(self,amount):

        self.__balance+=amount

        print(f"your {self.bank_name} account with {self.account_num} has been credited an amount of RS{amount} and the available balanace is {self.__balance}")


    def withdraw(self,amount):

        if amount>self.__balance:
            print("insufficient balance")

        else:
            self.__balance-=amount

            print(f"your {self.bank_name} account with {self.account_num} has been debited RS-{amount} and the available balance is {self.__balance}")

    def get_balance(self):
        print(f"your available current balance is {self.__balance}")


user_account=Bank()

user_account.create_account(1672815116718,"savings")

user_account.deposit(4000)

user_account.withdraw(5000)

user_account.get_balance()

print(user_account.balance) #__ make balance private so it cannot be accesed ouside the calss

