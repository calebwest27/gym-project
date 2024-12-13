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
memberSilverInfo = []
memberGoldInfo = []
memberPlatInfo = []
memberBilling = []

print(" ")
print("Project Created by Joel Leone and Caleb West")
print(" ")
print("Welcome to Lit Fitness! Below is a Menu with options to create a membership.")
print("Thank You For Choosing Lit Fitness.")

while True:
    main_menu()
    choice = int(input())
    if choice == 1:
        silver()
        gold()
        plat()
        print("0. Exit to Main Menu")
        option1 = int(input("Enter the Desired Membership Level: "))
        print(" ")

        if option1 == 1:
            gymID = random.sample(range(100000, 999999), 1)
            sm = Gs.Member(input("Name: "), input("Age: "), input("Gender: "), gymID, "Silver")
            memberSilverList.append(sm)
            print("New member information added. Your gym ID is: ", gymID), ". Do not forget this ID."
            print("The following info will be kept private, and only accessible by you.")
            silver_info = Gs.Sensitive_Info(input("Email: "), input("Password: "), input("Phone Number: "),
                                            input("Name On Card: "), input("Billing Address: "),
                                            input("Expiration Date: "), input("Credit Card Number: "), input("CVV: "))
            memberSilverInfo.append(silver_info)
            pay = silver_info.silver_billing()
            print("Billing Receipt: ")
            memberBilling.append(pay)
            sd = open('Silver_Gym_mem.dat', 'ab')
            pickle.dump(sm, sd)
            sd.close()

        if option1 == 2:
            gymID = random.sample(range(100000, 999999), 1)
            gm = Gs.Member(input("Name: "), input("Age: "), input("Gender: "), gymID, "Gold")
            memberGoldList.append(gm)
            print("New member information added. Your gym ID is: ", gymID), ". Do not forget this ID."
            print("The following info will be kept private, and only accessible by you.")
            gold_info = Gs.Sensitive_Info(input("Email: "), input("Password: "), input("Phone Number: "),
                                          input("Name On Card: "), input("Billing Address: "),
                                          input("Expiration Date: "), input("Credit Card Number: "), input("CVV: "))
            memberGoldInfo.append(gold_info)
            pay = gold_info.gold_billing()
            memberBilling.append(pay)
            gd = open('Gold_Gym_mem.dat', 'ab')
            pickle.dump(gm, gd)
            gd.close()

        if option1 == 3:
            gymID = random.sample(range(100000, 999999), 1)
            pm = Gs.Member(input("Name: "), input("Age: "), input("Gender: "), gymID, "Platinum")
            memberPlatList.append(pm)
            print("New member information added. Your gym ID is: ", gymID), ". Do not forget this ID."
            print("The following info will be kept private, and only accessible by you.")
            plat_info = Gs.Sensitive_Info(input("Email: "), input("Password: "), input("Phone Number: "),
                                          input("Name On Card: "), input("Billing Address: "),
                                          input("Expiration Date: "), input("Credit Card Number: "), input("CVV: "))
            memberPlatInfo.append(plat_info)
            pay = plat_info.plat_billing()
            memberBilling.append(pay)
            pd = open('Plat_Gym_mem.dat', 'ab')
            pickle.dump(pm, pd)
            pd.close()

        if option1 == 0:
            print("Exiting to Main Menu")

        if option1 not in [0, 1, 2, 3]:
            print("Invalid input. Returning to Main Menu")

    if choice == 2:
        while True:
            print(" ")
            print("1. Display Silver Members")
            print("2. Display Gold Members")
            print("3. Display Platinum Members")
            print("4. Search Personal Information")
            print("0. Exit to Main Menu")
            option2 = int(input())
            print(" ")
            if option2 == 1:
                sd = open('Silver_Gym_mem.dat', 'rb')
                print("Silver Members: ")
                while True:
                    try:
                        silver_data = pickle.load(sd)
                        print(silver_data.name)
                        print(silver_data.age)
                        print(silver_data.gender)
                        print(silver_data.gymID)
                        print(silver_data.memLevel)
                        print(" ")
                    except EOFError:
                        break
                sd.close()
            if option2 == 2:
                gd = open('Gold_Gym_mem.dat', 'rb')
                print("Gold Members: ")
                while True:
                    try:
                        gold_data = pickle.load(gd)
                        print(gold_data.name)
                        print(gold_data.age)
                        print(gold_data.gender)
                        print(gold_data.gymID)
                        print(gold_data.memLevel)
                        print(" ")
                    except EOFError:
                        break
                gd.close()
            if option2 == 3:
                pd = open('Plat_Gym_mem.dat', 'rb')
                print("Platinum Members: ")
                while True:
                    try:
                        plat_data = pickle.load(pd)
                        print(plat_data.name)
                        print(plat_data.age)
                        print(plat_data.gender)
                        print(plat_data.gymID)
                        print(plat_data.memLevel)
                        print(" ")
                    except EOFError:
                        break
                pd.close()
            if option2 == 4:
                while True:
                    print(" ")
                    print("1. Silver")
                    print("2. Gold")
                    print("3. Platinum")
                    print("0. Back to Display Menu")
                    option5 = int(input("Enter Your Membership Level: "))
                    if option5 == 1:
                        user_Email = str(input("Enter Your Email: "))
                        user_password = str(input("Enter Your Passphrase: "))
                        for z in memberSilverInfo:
                            if z.email == user_Email:
                                print("Email Found")
                                for z in memberSilverInfo:
                                    if z.password == user_password:
                                        print("Passphrase Found")
                                        print("Displaying Member Information Below.")
                                        print(" ")
                                        print("Email:", z.email)
                                        print("Phone Number:", z.phoneNumber)
                                        print("Name:", z.name_on_card)
                                        print("Billing Address:", z.billing_address)
                                        break
                    if option5 == 2:
                        user_Email = str(input("Enter Your Email: "))
                        user_password = str(input("Enter Your Passphrase: "))
                        for z in memberGoldInfo:
                            if z.email == user_Email:
                                print("Email Found")
                                for z in memberGoldInfo:
                                    if z.password == user_password:
                                        print("Passphrase Found")
                                        print("Displaying Member Information Below.")
                                        print(" ")
                                        print("Email:", z.email)
                                        print("Phone Number:", z.phoneNumber)
                                        print("Name:", z.name_on_card)
                                        print("Billing Address:", z.billing_address)
                                        break
                    if option5 == 3:
                        user_Email = str(input("Enter Your Email: "))
                        user_password = str(input("Enter Your Passphrase: "))
                        for z in memberPlatInfo:
                            if z.email == user_Email:
                                print("Email Found")
                                for z in memberPlatInfo:
                                    if z.password == user_password:
                                        print("Passphrase Found")
                                        print("Displaying Member Information Below.")
                                        print(" ")
                                        print("Email:", z.email)
                                        print("Phone Number:", z.phoneNumber)
                                        print("Name:", z.name_on_card)
                                        print("Billing Address:", z.billing_address)
                                        break
                    if option5 == 0:
                        print("Exiting to Display Menu")
                        break

                    if option5 not in [0, 1, 2, 3]:
                        print("Invalid input.")

            if option2 == 0:
                print("Exiting to Main Menu")
                break

            if option2 not in [0, 1, 2, 3, 4]:
                print("Invalid input. Returning to Main Menu")

    if choice == 3:

        while True:
            print("Which membership Level are you? (Silver / Gold / Platinum)")
            print("1. Silver")
            print("2. Gold")
            print("3. Platinum")
            print("0. Return to Menu")
            option3 = int(input())
            if option3 == 1:  # silver
                with open('Silver_Gym_mem.dat', 'rb') as sd:
                    memberSilverList = []
                    try:
                        while True:
                            member = pickle.load(sd)
                            memberSilverList.append(member)
                    except EOFError:
                        pass
                userID = int(input("Enter gym ID: "))
                id_found = False
                for Member in memberSilverList:
                    if Member.gymID[0] == userID:
                        id_found = True
                        remove_menu()  # are you sure?
                        option4 = int(input())
                        print(" ")
                        if option4 == 1:  # if yes
                            memberSilverList.remove(Member)
                            print("Your ID was found and has successfully been removed.")
                            with open('Silver_Gym_mem.dat', 'wb') as sd:
                                for sm in memberSilverList:
                                    pickle.dump(sm, sd)
                            break
                        else:  # if not
                            print("Returning to 'remove' menu")
                if not id_found:
                    print("ID not found. Returning to 'remove' menu")
            if option3 == 2:
                with open('Gold_Gym_mem.dat', 'rb') as gd:
                    memberGoldList = []
                    try:
                        while True:
                            member = pickle.load(gd)
                            memberGoldList.append(member)
                    except EOFError:
                        pass
                userID = int(input("Enter gym ID: "))
                id_found = False
                for Member in memberGoldList:
                    if Member.gymID[0] == userID:
                        id_found = True
                        remove_menu()  # are you sure?
                        option4 = int(input())
                        print(" ")
                        if option4 == 1:  # if yes
                            memberGoldList.remove(Member)
                            print("Your ID was found and has successfully been removed.")
                            with open('Gold_Gym_mem.dat', 'wb') as gd:
                                for sm in memberGoldList:
                                    pickle.dump(gm, gd)
                                    pickle.load
                            break
                        else:
                            print("Returning to 'remove' menu")
                if not id_found:
                        print("ID not found. Returning to 'remove' menu")
            if option3 == 3:
                with open('Plat_Gym_mem.dat', 'rb') as pd:
                    memberPlatList = []
                    try:
                        while True:
                            member = pickle.load(pd)
                            memberPlatList.append(member)
                    except EOFError:
                        pass
                userID = int(input("Enter gym ID: "))
                id_found = False
                for Member in memberPlatList:
                    if Member.gymID[0] == userID:
                        id_found = True
                        remove_menu()  # are you sure?
                        option4 = int(input())
                        print(" ")
                        if option4 == 1:  # if yes
                            memberPlatList.remove(Member)
                            print("Your ID was found and has successfully been removed.")
                            with open('Plat_Gym_mem.dat', 'wb') as pd:
                                for sm in memberPlatList:
                                    pickle.dump(pm, pd)
                            break
                        else:
                            print("Returning to 'remove' menu.")
                if not id_found:
                    print("ID not found. Returning to 'remove' menu")
            if option3 == 0:
                print("Returning to Main Menu")
                print(" ")
                break
            if option3 not in [0, 1, 2, 3]:
                print("Error. Returning to Main Menu")

    if choice == 0:
        print("Program Terminated. We thank you for your time with Lit Fitness.")
        break

    if choice not in [0, 1, 2, 3,]:
        print("Input unknown. Please try again.")
