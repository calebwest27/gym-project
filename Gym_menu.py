import Gym_setup as Gs
import pickle
import random


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
    print("Accessible Equipment: Locker Rooms, Showers, Cardio, Pool and Swim Lanes")
    print(" ")


def plat():
    print("3. Platinum")
    print("Starting Fee: $28")
    print("Payment Plan: $65/month")
    print("Accessible Equipment: Locker Rooms, Showers, Cardio, Pool and Swim Lanes, Resistance and Weight Machines")
    print(" ")


def main_menu():
    print(" ")
    print("1. Become a Member")
    print("2. Display Members")
    print("3. Remove Member")
    print("0. Exit Program")


def remove_menu():
    print("Are You Sure?")
    print("1. Yes")
    print("2. No")


memberSilverList = []
memberGoldList = []
memberPlatList = []
memberInfo = []
memberBilling = []

print(" ")
print("Project Created by Joel Leone and Caleb West")
print(" ")
print("Welcome to Lit Fitness! Below is a Menu with options to select.")
print("Thank You For Choosing Lit Fitness.")
print(" ")
while 99:
    main_menu()
    choice = int(input(""))
    if choice == 1:
        silver()
        gold()
        plat()
        print("0. Exit to Main Menu")
        option1 = int(input("Enter the Desired Membership Level: "))
        print(" ")

        if option1 == 1:
            gymId = random.sample(range(100000, 999999), 1)
            sm = Gs.Member(input("Name: "), input("Age: "), input("Gender: "), gymId, "Silver")
            # for x in range(0, len(memberSilverList)):  # This Makes sure there are no matching id numbers=========
            #     if x == gymId:
            #         new_value = random.sample(range(100000, 999999), 1)
            #         memberSilverList(x) == new_value
            #         print("Your new gym ID is: ", new_value)
            memberSilverList.append(sm)
            print("New member information added. Your gym ID is: ", gymId)
            print("The following info will be kept private, and only accessible by you.")
            info = Gs.Sensitive_Info(input("Email: "), input("Password: "), input("Phone Number: "),
                                     input("Name On Card: "), input("Billing Address: "),
                                     input("Expiration Date: "), input("Credit Card Number: "), input("CVV: "))
            memberInfo.append(info)
            pay = info.silver_billing()
            print("Billing Receipt: ")
            memberBilling.append(pay)
            sd = open('Silver_Gym_mem.dat', 'ab')
            pickle.dump(sm, sd)
            sd.close()

        if option1 == 2:
            gymId = random.sample(range(100000, 999999), 1)
            gm = Gs.Member(input("Name: "), input("Age: "), input("Gender: "), gymId, "Gold")
            # for x in range(0, len(memberGoldList)):  # This Makes sure there are no matching id numbers=========
            #     if x == gymId:
            #         new_value = random.sample(range(100000, 999999), 1)
            #         memberGoldList(x) == new_value
            #         print("Your new gym ID is: ", new_value)
            memberGoldList.append(gm)
            print("New member information added. Your gym ID is: ", gymId)
            print("The following info will be kept private, and only accessible by you.")
            info = Gs.Sensitive_Info(input("Email: "), input("Password: "), input("Phone Number: "),
                                     input("Name On Card: "), input("Billing Address: "),
                                     input("Expiration Date: "), input("Credit Card Number: "), input("CVV: "))
            memberInfo.append(info)
            pay = info.gold_billing()
            memberBilling.append(pay)
            gd = open('Gold_Gym_mem.dat', 'ab')
            pickle.dump(gm, gd)
            gd.close()

        if option1 == 3:
            gymId = random.sample(range(100000, 999999), 1)
            pm = Gs.Member(input("Name: "), input("Age: "), input("Gender: "), gymId, "Platinum")
            # for x in range(0, len(memberPlatList)):  # This Makes sure there are no matching id numbers=========
            #     if x == gymId:
            #         new_value = random.sample(range(100000, 999999), 1)
            #         memberPlatList(x) == new_value
            #         print("Your new gym ID is: ", new_value)
            memberPlatList.append(pm)
            print("New member information added. Your gym ID is: ", gymId)
            print("The following info will be kept private, and only accessible by you.")
            info = Gs.Sensitive_Info(input("Email: "), input("Password: "), input("Phone Number: "),
                                     input("Name On Card: "), input("Billing Address: "),
                                     input("Expiration Date: "), input("Credit Card Number: "), input("CVV: "))
            memberInfo.append(info)
            pay = info.plat_billing()
            memberBilling.append(pay)
            pd = open('Plat_Gym_mem.dat', 'ab')
            pickle.dump(pm, pd)
            pd.close()

        if option1 == 0:
            print("Exiting to Main Menu")

        if option1 > 3:
            print("Please Enter A Valid Input")
            print(" ")
        if option1 < 0:
            print("Please Enter A Valid Input")
            print(" ")

    if choice == 2:
        while 2:
            print(" ")
            print("1. Display Silver Members")
            print("2. Display Gold Members")
            print("3. Display Platinum Members")
            print("0. Exit to Main Menu")
            option2 = int(input())
            if option2 == 1:
                sd = open('Silver_Gym_mem.dat', 'rb')
                print("Silver Members: ")
                while 10:
                    try:
                        silver_data = pickle.load(sd)
                        print(silver_data.name)
                        print(silver_data.age)
                        print(silver_data.gender)
                        print(silver_data.gymID)
                        print(silver_data.memLevel)
                    except EOFError:
                        break
                sd.close()
            if option2 == 2:
                gd = open('Gold_Gym_mem.dat', 'rb')
                print("Gold Members: ")
                while 11:
                    try:
                        gold_data = pickle.load(gd)
                        print(gold_data.name)
                        print(gold_data.age)
                        print(gold_data.gender)
                        print(gold_data.gymID)
                        print(gold_data.memLevel)
                    except EOFError:
                        break
                gd.close()
            if option2 == 3:
                pd = open('Plat_Gym_mem.dat', 'rb')
                print("Platinum Members: ")
                while 12:
                    try:
                        plat_data = pickle.load(pd)
                        print(plat_data.name)
                        print(plat_data.age)
                        print(plat_data.gender)
                        print(plat_data.gymID)
                        print(plat_data.memLevel)
                    except EOFError:
                        break
                pd.close()
            if option2 == 0:
                print("Exiting to Main Menu")
                break

    if choice == 3:
        while 2:
            print("Which membership Level are you? (Silver / Gold / Platinum)")
            print("1. Silver")
            print("2. Gold")
            print("3. Platinum")
            print("0. Return to Menu")
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
            if option3 == 0:
                print("Returning to Main Menu")
                print(" ")
                break

    if choice == 0:
        print("Program Terminated. We thank you for your time with Lit Fitness.")
        break

    else:
        print("Please Enter A Valid Input")
        print(" ")

    # if choice == 4:
