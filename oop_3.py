# bank acc == owner,acc no , balance, history
import datetime
from datetime import date


class Client:
    def __init__(self,names:str, kra_pin:str, dob, gender):
        self.names = names
        self.kra_pin = kra_pin
        self.dob = dob
        self.gender = gender

    def print_details(self):
        print(self.names)
        print(self.kra_pin)

    def calc_age(self):
        today = date.today()
        birth_date = date.strptime(self.dob, '%Y-%m-%d')
        age = today.year - birth_date.year
        return age


class BankAccount:
    def __init__(self, owner:Client, acc_no:str, balance:int):
        self.owner = owner
        self.acc_no = acc_no
        self.balance = balance

    def deposit(self,amount):
        self.balance += abs(amount)

    def withdraw(self,amount):
        if amount > self.balance:
            print("Not enough money")
        else:
            self.balance -= abs(amount)
    def print_details(self):
        print(self.owner.names)
        # self.owner.print_details()
        print(self.acc_no)
        print(self.balance)
        print("------")


joyce = Client('joyce heta','A001','2004-08-15','F')
kelly = Client('collins kelly','A002','2003-06-20','M')

acc1 = BankAccount(joyce,"1111",100_000)
acc2 = BankAccount(joyce,"2222",200_000)
acc3 = BankAccount(kelly,"3333",300_000_000)

acc1.deposit(10_000)
acc2.deposit(5_000)

acc1.print_details()
acc1.withdraw(7_000)
acc1.print_details()

print("Joyce's Age",joyce.calc_age())
print("kelly's Age",kelly.calc_age())

print(acc1.owner.names, acc1.owner.calc_age())
print(joyce.names, joyce.calc_age())

# dob = '2004-08-15'  # Y.m.d

# today = date.today()
# # print(f"{today.day}--{today.month}--{today.year}")
# # convert string to date
# birth_date = date.strptime(dob,'%Y-%m-%d')
#
# age = today.year - birth_date.year
# print(age)
#
# accurate_age = today - birth_date
# print(accurate_age)