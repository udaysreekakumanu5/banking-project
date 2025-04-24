import datetime
class Hdfc:
    bank_name="Hdfc"
    manager="monty sir"
    ifsc_code="HDFC239084"
    loc="dilsukhnagar"
    no_account_holders=0
    data={}
    transaction_details={}
    def __init__(self,name,mobile,age,gender,aadhar,address,pin,balance):
        self.name=name
        self.mobile=self.validate_phone(mobile)
        self.age=self.validate_age(age)
        self.gender=gender
        self.aadhar=self.validate_aadhar(aadhar)
        self.pin=self.validate_pin(pin)
        self.balance=balance
        self.address=address
        self.increment_accounts()
        account_num=1000+self.no_account_holders
        self.add_data(account_num,self)
    @classmethod
    def increment_accounts(cls):
        cls.no_account_holders +=1
    @classmethod
    def add_data(cls,account_num,object_address):
        cls.data[account_num]=object_address
    @staticmethod
    def validate_phone(mobile):
        if len(str(mobile))==10 and str(mobile).isdigit():
            return mobile
        else:
            print("enter valid mobile number")

    @staticmethod
    def validate_age(age):
        if age>=18:
            return age
        else:
            print("your are not eligible to open account")

    @staticmethod
    def validate_aadhar(aadhar):
        if len(str(aadhar))==12 and str(aadhar).isdigit():
            return aadhar
        else:
            print("enter valid aadhar number")


    @staticmethod
    def validate_pin(pin):
        if len(str(pin))==4 and str(pin).isdigit():
            return pin
        else:
            print("enter correct pin")

    @classmethod
    def check_balance(cls):
        print("-------BALANCE PAGE--------")

        user_account_num=int(input("enter account number:"))
        user_pin=int(input("Enter a pin:"))

        if user_account_num in cls.data and user_pin==cls.data[user_account_num].pin:
           print(f"your current balance is {cls.data[user_account_num].balance}")
        elif user_account_num in cls.data and user_pin!=cls.data[user_account_num].pin:
            print("enter valid pin")
        else:
            print("invalid user")

    @classmethod
    def deposit(cls):
        print("-------DEPOSIT PAGE--------")

        user_account_num=int(input("enter account number:"))
        user_pin=int(input("Enter a pin:"))

        if user_account_num in cls.data and user_pin==cls.data[user_account_num].pin:
           amount=int(input("enter amount:"))
           if amount>0:
               cls.data[user_account_num].balance+=amount
               print(f"rs{amount} was credited to your account ,your current balance is {cls.data[user_account_num].balance}")


               if cls.data[user_account_num] not in cls.transaction_details:
                   cls.transaction_details[user_account_num]=[{"DATE":datetime.datetime.now().date(),
                                                               "TYPE":"CREDIT",
                                                               "AMOUNT":amount,
                                                               "BALANCE":cls.data[user_account_num].balance}]
               else:
                   cls.transaction_details[user_account_num]+= [{"DATE": datetime.datetime.now().date(),
                                                                 "TYPE": "CREDIT",
                                                                 "AMOUNT": amount,
                                                                 "BALANCE": cls.data[user_account_num].balance}]
           else:
               print("enter valid amount")
        elif user_account_num in cls.data and user_pin!=cls.data[user_account_num].pin:
            print("enter valid pin")
        else:
            print("invalid user")

    @classmethod
    def withdraw(cls):
        print("-------WITHDRAW PAGE--------")

        user_account_num = int(input("enter account number:"))
        user_pin = int(input("Enter a pin:"))

        if user_account_num in cls.data and user_pin == cls.data[user_account_num].pin:
            amount = int(input("enter amount:"))
            if amount > 0:
                cls.data[user_account_num].balance -= amount
                print(f"rs{amount} was debited from your account ,your current balance is {cls.data[user_account_num].balance}")
                if cls.data[user_account_num] not in cls.transaction_details:
                    cls.transaction_details[user_account_num] = [{"DATE": datetime.datetime.now().date(),
                                                                  "TYPE": "DEBIT",
                                                                  "AMOUNT": amount,
                                                                  "BALANCE": cls.data[user_account_num].balance}]
                else:
                    cls.transaction_details[user_account_num] += [{"DATE": datetime.datetime.now().date(),
                                                                   "TYPE": "DEBIT",
                                                                   "AMOUNT": amount,
                                                                   "BALANCE": cls.data[user_account_num].balance}]

            else:
                print("enter valid amount")
        elif user_account_num in cls.data and user_pin != cls.data[user_account_num].pin:
            print("enter valid pin")
        else:
            print("invalid user")


    @classmethod
    def change_pin(cls):
        print("-------CHANGEPIN PAGE--------")

        user_account_num = int(input("enter account number:"))
        user_pin = int(input("Enter a pin:"))

        if user_account_num in cls.data and user_pin == cls.data[user_account_num].pin:
            new_pin=int(input("enter new pin:"))
            confirm_pin=int(input("confirm pin:"))
            if new_pin==confirm_pin:
                cls.data[user_account_num].pin=cls.validate_pin(new_pin)
                if new_pin==cls.data[user_account_num].pin:
                    print("pin has updated successfully!")
            else:
                print("new_pin and confirm_pin are not matching")
        elif user_account_num in cls.data and user_pin != cls.data[user_account_num].pin:
            print("enter valid pin")
        else:
            print("invalid user")
            
    @classmethod
    def create_account(cls):
        name = input("enter your name:")
        aadhar = input ("enter your aadhar number" )
        cls.validate_aadhar(aadhar)
        mobile = int(input("enter your mobile number"))
        age = int(input("enter your age"))
        cls.validate_age(age)
        gender = input ("enter your gender")
        address = input("enter your address")
        pin = int(input("enter your 4 digit valid pin"))
        cls.validate_pin(pin)
        balance = int(input("enter the deposit money"))
        new_customer = cls(name,aadhar,mobile,age,gender,address,pin,balance)
        print("account created succesfully")
       # print(f"your account number is {new_customer.account_number}")                     
    


    @classmethod
    def modify_user_details(cls):
        print("----------MODIFICATION OF USER DETAILS---------")
        user_account_num = int(input("enter account number:"))
        user_pin = int(input("Enter a pin:"))

        if user_account_num in cls.data and user_pin == cls.data[user_account_num].pin:
            while True:
                print("select 1 to modify name\nselect 2 to modify mobile number\nselect 3 to modify address\n")
                select=int(input("enter a number:"))
                match select:
                    case 1:
                        print("-----MODIFICATION OF NAME------")
                        new_name=input("enter new name:")
                        confirm_name=input("confirm name:")
                        if new_name==confirm_name:
                            cls.data[user_account_num].name=new_name
                            print("name has changed successfully")
                        else:
                            print("new name and confirm name are not matched")

                    case 2:
                        print("-------MODIFICATION OF MOBILE NUMBER----------")
                        new_mobile_num=int(input("enter new mobile number:"))
                        confirm_mobile_num=int(input("confirm number:"))
                        if new_mobile_num==confirm_mobile_num:
                            cls.data[user_account_num].mobile=cls.validate_phone(new_mobile_num)
                            print("mobile number has changed successfully")
                        else:
                            print("new mobile number and confirm mobile number  are not matched")
                    case 3:
                        print("-----------MODIFICATION OF ADDRESS-----------")
                        new_address=input("enter new address:")
                        confirm_address=input("confirm address:")
                        if new_address==confirm_address:
                            print("address has changed successfully")

                        else:
                            print("new address and confirm address are not matched")
                    case 4:
                        print("THANKS FOR MODIFYING YOUR DATA")
                        break
                    case _:
                        print("select fom (1,2,3,4)")
        elif user_account_num in cls.data and user_pin != cls.data[user_account_num].pin:
            print("enter valid pin")
        else:
            print("invalid user")

    @classmethod
    def transfer_money(cls):
        print("----------TRANSFER MONEY------------")
        sender_account_num=int(input("enter sender account number:"))
        sender_pin=int(input("enter sender pin:"))

        if sender_account_num in cls.data and sender_pin==cls.data[sender_account_num].pin:

            receiver_account_num=int(input("enter receivers account number:"))
            receivers_ifsc_code=input("enter receiver ifsc code:")

            if receiver_account_num in cls.data and receivers_ifsc_code==cls.ifsc_code:
                amount=int(input("enter amount to transfer:"))
                if amount<=cls.data[sender_account_num].balance:
                    cls.data[sender_account_num].balance-=amount
                    cls.data[receiver_account_num].balance+=amount
                    print("amount tranferred successfully")
                else:
                    print("INSUFFICIENT BALANCE")

        elif sender_account_num in cls.data and sender_pin != cls.data[sender_account_num].pin:
            print("inavlid pin")
        else:
            print("invalid user")

    @classmethod
    def mini_statement(cls):
        print("-----------MINI STATEMENT--------------")
        user_account_num = int(input("enter account number:"))
        user_pin = int(input("Enter a pin:"))
        if user_account_num in cls.data and user_pin == cls.data[user_account_num].pin:
            print("DATE".center(14),"TYPE".center(14),"AMOUNT".center(16),"BALANCE".center(30))
            transaction_history=cls.transaction_details[user_account_num]
            for d in transaction_history:
                print(str(d["DATE"]).center(14),d["TYPE"].center(10),str(d["AMOUNT"]).center(20),str(d["BALANCE"]).ljust(10))


cust1=Hdfc("udaysree",8903627397,21,"female",123783477983,"hyderabad",1234,50000)
cust2=Hdfc("anusha",7836494792,20,"female",467283924678,"AP",5678,45000)
#print(cust1.data)
#cust1.check_balance()
# cust1.deposit()
 #cust1.withdraw()
# cust1.change_pin()
# print(cust1.pin)
# cust1.modify_user_details()
# print(cust1.name)
# cust1.transfer_money()
# print(cust1.balance)
#cust1.mini_statement()
#print(Hdfc.data.keys())
#Hdfc.create_account()
Hdfc.check_balance()