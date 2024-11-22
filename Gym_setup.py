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
        return " "


class Member(Person):
    def __init__(self, nn, aa, gg, ii, mem):
        Person.__init__(self, nn, aa, gg)
        self.gymID = ii
        self.memLevel = mem

    def display_member(self):
        print(Person.display(self))
        print("Gym ID:", self.gymID)
        print("Membership Level:", self.memLevel)
        print(" ")
        return " "


class Info(Member):
    def __init__(self, nn, aa, gg, ii, mem, ee, ph, noc, ba, cc, cv, ed):
        Member.__init__(self, nn, aa, gg, ii, mem)
        self.email = ee
        self.phoneNumber = ph
        self.name_on_card = noc
        self.billing_address = ba
        self.credit_card = cc
        self.cvv = cv
        self.expire_date = ed
        print("Member information successfully stored========================================")

    def billing(self):  # Different Ways of paying, so many months in advance
        start_fee = int(input("Enter the Starting Fee: "))
        monthly_amm = int(input("Enter the Monthly Amount: "))
        num_months = int(input("Enter the Number of Months Payment: "))
        amount = monthly_amm * num_months
        subtotal = amount + start_fee
        # Tax = 10%
        tax = subtotal * 0.1
        print("Subtotal:", subtotal)
        print("Tax:", tax)
        print("Total:", )

    def display_sensitive(self):
        print(Member.display_member(self))
        print("Email:", self.email)
        print("Billing Address:", self.billing_address)
        print("Phone Number:", self.phoneNumber)
        return ""