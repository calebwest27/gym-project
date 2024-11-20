class Person:
    def __init__(self, nn, aa, gg):
        self.name = nn
        self.age = aa
        self.gender = gg

    def __addPerson__(self):
        self.name = input("Enter Your Name: ")
        self.age = input("Enter Your Age: ")
        self.gender = input("Enter Your Gender: ")

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)
        return ""

class Membership_level:
    def display_silver(self):
        print("Starting Fee: $15")
        print("Payment Plan: $35/month")
        print("Accessible Equipment: ")

    def display_gold(self):
        print("Starting Fee: $21")
        print("Payment Plan: $50/month")
        print("Accessible Equipment: ")

    def display_plat(self):
        print("Starting Fee: $28")
        print("Payment Plan: $65/month")
        print("Accessible Equipment: ")

class Member(Person):
    def __init__(self, nn, aa, gg, ee, id, ad, ph):
        Person.__init__(self, nn, aa, gg)
        self.email = ee
        self.gymID = id
        self.address = ad
        self.phoneNumber = ph

    def add_member(self):
        Person.__addPerson__(self)
        self.email = input("Enter Your Email Address: ")
        self.gymID = input("Work on this")
        self.address = input("Enter Your Address: ")
        self.phoneNumber = input("Enter Your Phone Number: ")

    def display_member(self):
        print(Person.display(self))
        print("Email:", self.email)
        print("Gym ID:", self.gymID)
        print("Address:", self.address)
        print("Phone Number:", self.phoneNumber)
        return ""
    