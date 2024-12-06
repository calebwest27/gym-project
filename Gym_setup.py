class Person:
    def __init__(self, nn, aa, gg):
        self.name = nn
        self.age = aa
        self.gender = gg

    def display(self):
        print(" ")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)
        return ""


class Member(Person):
    def __init__(self, nn, aa, gg, id, mem):
        Person.__init__(self, nn, aa, gg)
        self.gymID = id
        self.memLevel = mem

    def display_member(self):
        print(Person.display(self))
        print("Gym ID:", self.gymID)
        print("Membership Level:", self.memLevel)
        print(" ")


class Sensitive_Info():
    def __init__(self, ee, ph, noc, ba, cc, cv, ed):
        self.email = ee
        self.phoneNumber = ph
        self.name_on_card = noc
        self.billing_address = ba
        self.credit_card = cc
        self.cvv = cv
        self.expire_date = ed

    def display_sensitive(self):
        print(Sensitive_Info.display_sensitive(self))
        print("Email:", self.email)
        print("Billing Address:", self.billing_address)
        print("Phone Number:", self.phoneNumber)
        print(" ")

    def silver_billing(self):
        start_fee = 15
        monthly_amm = 35
        num_months = int(input("How many months do you plan to wish to be a member? Please state a number of months. "))
        amount = monthly_amm * num_months
        subtotal = amount + start_fee
        # Tax = 10%
        tax = subtotal * 0.1
        print("Subtotal:", subtotal)
        print("Tax:", tax)
        print("Total:", subtotal + tax)

    def gold_billing(self):
        start_fee = 21
        monthly_amm = 50
        num_months = int(input("How many months do you plan to wish to be a member? Please state a number of months. "))
        amount = monthly_amm * num_months
        subtotal = amount + start_fee
        # Tax = 10%
        tax = subtotal * 0.1
        print("Subtotal:", subtotal)
        print("Tax:", tax)
        print("Total:", subtotal + tax)

    def plat_billing(self):
        start_fee = 28
        monthly_amm = 65
        num_months = int(input("How many months do you plan to wish to be a member? Please state a number of months. "))
        amount = monthly_amm * num_months
        subtotal = amount + start_fee
        # Tax = 10%
        tax = subtotal * 0.1
        print("Subtotal:", subtotal)
        print("Tax:", tax)
        print("Total:", subtotal + tax)