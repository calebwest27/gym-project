import Gym_setup as GS
import random

# Joel why do we have these definitions in the menu? Not because I think it's wrong I would just think that it's
# supposed to be on the setup page. But I won't change it because it's fine
def silver():
    print(" ")
    print("1. Silver")
    print("Starting Fee: $15")
    print("Payment Plan: $35/month")
    print("Accessible Equipment: Locker Rooms, Showers, Cardio")
    print(" ")


def gold():
    print("2. Gold")
    print("Starting Fee: $21")
    print("Payment Plan: $50/month")
    print("Accessible Equipment: Locker Rooms, Showers, Cardio, Pool + Swim Lanes")
    print(" ")


def plat():
    print("3. Platinum")
    print("Starting Fee: $28")
    print("Payment Plan: $65/month")
    print("Accessible Equipment: Locker Rooms, Showers, Cardio, Pool + Swim Lanes, Resistance / Weight Machines")
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


memberSilverList = []
memberGoldList = []
memberPlatList = []
memberInfo = []
memberBilling = []

# ====================================================== this is where the code actually begins ===================== #
print(" ")
print("Created by: Joel Leone and Caleb West")
print(" ")
print("Welcome to the Lit Fitness database! Below is a menu for options to select.")
print("We thank you for choosing Lit Fitness.")
print(" ")
while 99:
    main_menu()
    choice = int(input(""))
    if choice == 1:
        silver()
        gold()
        plat()
        print("0. Exit to Main Menu")
        print(" ")
        option1 = int(input("Enter the Desired Membership Level: "))
        print(" ")

        if option1 == 1:
            gymId = random.sample(range(10000, 99999), 1)
            sm = GS.Member(input("Name: "), input("Age: "), input("Gender: "), gymId, "Silver")
            print("New member information added. Your gym ID is: ", gymId)
            print("The following info will be kept private, and only accessible by you.")
            memberSilverList.append(sm)
            info = GS.Sensitive_Info(input("Email: "), input("Phone Number: "),
                                     input("Name On Credit Card: "), input("Billing Address: "),
                                     input("Expiration Date: "), input("Credit Card Number: "), input("CVV: "))
            memberInfo.append(info)
            pay = info.silver_billing()
            memberBilling.append(pay)
            for x in range(0, len(memberSilverList)):  # hey joel what do these codes do===============
                if x == gymId:
                    new_value = random.sample(range(10000, 99999), 1)
                    memberSilverList(x) == new_value

        if option1 == 2:
            gymId = random.sample(range(10000, 99999), 1)
            gm = GS.Member(input("Name: "), input("Age: "), input("Gender: "), gymId, "Gold")
            print("New member information added. Your gym ID is: ", gymId)
            print("The following info will be kept private, and only accessible by you.")
            memberGoldList.append(gm)
            info = GS.Sensitive_Info(input("Email: "), input("Phone Number: "),
                                     input("Name On Credit Card: "), input("Billing Address: "),
                                     input("Expiration Date: "), input("Credit Card Number: "), input("CVV: "))
            memberInfo.append(info)
            pay = info.gold_billing()
            memberBilling.append(pay)
            for x in range(0, len(memberGoldList)):  # hey joel what do these codes do===============
                if x == gymId:
                    new_value = random.sample(range(10000, 99999), 1)
                    memberGoldList(x) == new_value

        if option1 == 3:
            gymId = random.sample(range(10000, 99999), 1)
            pm = GS.Member(input("Name: "), input("Age: "), input("Gender: "), gymId, "Platinum")
            print("New member information added. Your gym ID is: ", gymId)
            print("The following info will be kept private, and only accessible by you.")
            memberPlatList.append(pm)
            info = GS.Sensitive_Info(input("Email: "), input("Phone Number: "),
                                     input("Name On Credit Card: "), input("Billing Address: "),
                                     input("Expiration Date: "), input("Credit Card Number: "), input("CVV: "))
            memberInfo.append(info)
            pay = info.plat_billing()
            memberBilling.append(pay)
            for x in range(0, len(memberPlatList)):  # hey joel what do these codes do====================
                if x == gymId:
                    new_value = random.sample(range(10000, 99999), 1)
                    memberPlatList(x) == new_value

        if option1 == 0:
            print("Exiting to Main Menu")

    if choice == 2:
        while 2:
            print("1. Display Silver Members")
            print("2. Display Gold Members")
            print("3. Display Platinum Members")
            print("0. Exit to Main Menu")
            option2 = int(input())
            if option2 == 1:
                for x in range(0, len(memberSilverList)):
                    sm.display_member()
            if option2 == 2:
                for x in range(0, len(memberGoldList)):
                    gm.display_member()
            if option2 == 3:
                for x in range(0, len(memberPlatList)):
                    pm.display_member()
            if option2 == 0:
                print("Exiting to Main Menu")
                break

    if choice == 3:
        while 2:
            print("Which membership (silver / gold / platinum) is your membership?")
            print("1. Silver")
            print("2. Gold")
            print("3. Platinum")
            print("4. Return to Menu")
            option3 = int(input())
            if option3 == 1:  # silver
                user = input("Enter gym ID: ")
                for x in memberSilverList:
                    if x == user:
                        remove_menu()  # are you sure?
                        option4 = int(input())
                        print(" ")
                        if option4 == 1:  # if yes
                            memberSilverList.remove(x)
                            break
                        else:  # if not
                            print("Returning to 'remove' menu")
                    else:
                        print("ID not found in database.")
            if option3 == 2:
                user = input("Enter gym ID: ")
                for x in memberGoldList:
                    if x == user:
                        remove_menu()  # are you sure?
                        option4 = int(input())
                        print(" ")
                        if option4 == 1:  # if yes
                            memberGoldList.remove(x)
                            break
                        else:
                            print("Returning to 'remove' menu")
                    else:
                        print("ID not found in database.")
            if option3 == 3:
                user = input("Enter gym ID: ")
                for x in memberPlatList:
                    if x == user:
                        remove_menu()  # are you sure?
                        option4 = int(input())
                        print(" ")
                        if option4 == 1:  # if yes
                            memberPlatList.remove(x)
                            break
                        else:
                            print("Returning to 'remove' menu.")
                    else:
                        print("ID not found in database.")
            if option3 == 4:
                print("Returning to Main Menu")
                print(" ")
                break

    if choice == 4:
        print(" ")
        print("Program terminated. We thank you for your time with Lit Fitness.")
        break
