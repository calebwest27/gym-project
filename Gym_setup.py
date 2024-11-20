class Person:
    def __init__(self, nn, aa, gg):
        self.name = nn
        self.age = aa
        self.gender = gg

    def display(self):
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
        return ""
    
class Sensitive_Info(Member):
    def __sensitiveInfo__(self, nn, aa, gg, id, mem, ee, ph):
        Member.__init__(self, nn, aa, gg, id, mem)
        self.email = ee
        self.phoneNumber = ph

    def __billing__(self, noc, ba, cc, cv, ed):
        self.name_on_card = noc
        self.billing_address = ba
        self.credit_card = cc
        self.cvv = cv
        self.expire_date = ed

    def __display_sensitive__(self):
        print(Member.display_member(self))
        print("Email:", self.email)
        print("Billing Address:", self.billing_address)
        print("Phone Number:", self.phoneNumber)
        return ""