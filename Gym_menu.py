import Gym_setup as Gs


import random


def silver():
    print(" ")
    print("1. Silver")
    print("Starting Fee: $15")
    print("Payment Plan: $35/month")
    print("Accessible Equipment: ")
    print(" ")


def gold():
    print("2. Gold")
    print("Starting Fee: $21")
    print("Payment Plan: $50/month")
    print("Accessible Equipment: ")
    print(" ")


def plat():
    print("3. Platinum")
    print("Starting Fee: $28")
    print("Payment Plan: $65/month")
    print("Accessible Equipment: ")
    print(" ")


def main_menu():
    print("1. Become a Member")
    print("2. Display Members")
    print("3. Remove Member")
    print("4. Exit Program")


def remove_menu():
    print("Are You Sure?")
    print("1. Yes")
    print("2. No")


memberList = []
memberInfo = []
memberBilling = []


while 99:
    main_menu()
    choice = int(input(""))
    if choice == 1:
        while 1:
            silver()
            gold()
            plat()
            print("0. Exit to Main Menu")
            option1 = int(input("Enter the Desired Membership Level: "))
            print(" ")

            if option1 == 1:
                gymId = random.sample(range(10000, 99999), 1)
                mm = Gs.Member(input("Name: "), input("Age: "), input("Gender: "), gymId, "Silver")
                memberList.append(mm)
                # info = Gs.Info(input("Email: "), input("Phone Number: "), input("Name On Card: "),
                #                input("Billing Address: "), input("Expiration Date: "),
                #                input("Credit Card Number: "), input("CVV: "))
                # memberInfo.append(info)
                # pay = info.billing()
                # memberBilling.append(pay)
                # for x in range(0, len(memberList)):
                #     if x == memberList:
                #         new_value = random.sample(range(10000, 99999), 1)
                #         memberList[x] = new_value

            if option1 == 2:
                gymId = random.sample(range(10000, 99999), 1)
                mm = Gs.Member(input("Name: "), input("Age: "), input("Gender: "), gymId, "Gold")
                memberList.append(mm)
                # info = Gs.Info(input("Email: "), input("Phone Number: "), input("Name On Card: "),
                #                input("Billing Address: "), input("Expiration Date: "),
                #                input("Credit Card Number: "), input("CVV: "))
                # memberInfo.append(info)
                # pay = info.billing()
                # memberBilling.append(pay)
                # for x in range(0, len(memberList)):
                #     if x == memberList:
                #         new_value = random.sample(range(10000, 99999), 1)
                #         memberList[x] = new_value

            if option1 == 3:
                gymId = random.sample(range(10000, 99999), 1)
                # mm = Gs.Member()
                # memberList.append(mm)
                info = Gs.Info(input("Name: "), input("Age: "), input("Gender: "), gymId, "Platinum",
                               input("Email: "), input("Phone Number: "), input("Name On Card: "),
                               input("Billing Address: "), input("Expiration Date: "),
                               input("Credit Card Number: "), input("CVV: "))
                memberInfo.append(info)
                pay = info.billing()
                memberBilling.append(pay)
                for x in range(0, len(memberList)):
                    if x == memberList:
                        new_value = random.sample(range(10000, 99999), 1)
                        memberList[x] = new_value

            if option1 == 0:
                print("Exiting to Main Menu")
                break

            else:
                print("Please Enter A Valid Input")
                print(" ")

    if choice == 2:
        for x in range(0, len(memberList)):
            mm.display_member()

    if choice == 3:
        while 2:
            remove_menu()
            option2 = int(input())
            print(" ")
            if option2 == 1:
                user = input("Enter Name: ")
                for x in memberList:
                    if x == user:
                        memberList.remove(x)
                break

            if option2 == 2:
                print("Returning to Main Menu")
                break

    if choice == 4:
        print("Program Terminated.")
        break
