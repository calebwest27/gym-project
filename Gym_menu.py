import Gym_setup as GS
from Gym_setup import *

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


memberSilverList = []
memberGoldList = []
memberPlatList = []
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
            print ("0. Exit to Main Menu")
            option1 = int(input("Enter the Desired Membership Level: "))
            print(" ")

            if option1 == 1:
                gymId = random.sample(range(10000, 99999), 1)
                sm = GS.Member(input("Name: "), input("Age: "), input("Gender: "), gymId, "Silver")
                memberSilverList.append(sm)
                info = GS.Sensitive_Info(input("Email: "), input("Phone Number: "),
                    input("Name On Card: "), input("Billing Address: "), input("Expiration Date: "), input("Credit Card Number: "), input("CVV: "))
                memberInfo.append(info)
                pay = info.billing()
                memberBilling.append(pay)
                for x in range(0, len(memberSilverList)):
                    if x == gymId:
                        new_value = random.sample(range(10000, 99999), 1)
                        memberSilverList(x) == new_value

            if option1 == 2:
                gymId = random.sample(range(10000, 99999), 1)
                gm = GS.Member(input("Name: "), input("Age: "), input("Gender: "), gymId, "Gold")
                memberGoldList.append(gm)
                info = GS.Sensitive_Info(input("Email: "), input("Phone Number: "),
                    input("Name On Card: "), input("Billing Address: "), input("Expiration Date: "), input("Credit Card Number: "), input("CVV: "))
                memberInfo.append(info)
                pay = info.billing()
                memberBilling.append(pay)
                for x in range(0, len(memberGoldList)):
                    if x == gymId:
                        new_value = random.sample(range(10000, 99999), 1)
                        memberGoldList(x) == new_value

            if option1 == 3:
                gymId = random.sample(range(10000, 99999), 1)
                pm = GS.Member(input("Name: "), input("Age: "), input("Gender: "), gymId, "Platinum")
                memberPlatList.append(pm)
                info = GS.Sensitive_Info(input("Email: "), input("Phone Number: "),
                    input("Name On Card: "), input("Billing Address: "), input("Expiration Date: "), input("Credit Card Number: "), input("CVV: "))
                memberInfo.append(info)
                pay = info.billing()
                memberBilling.append(pay)
                for x in range(0, len(memberPlatList)):
                    if x == gymId:
                        new_value = random.sample(range(10000, 99999), 1)
                        memberPlatList(x) == new_value

            if option1 == 0:
                print("Exiting to Main Menu")
                break

            else:
                print("Please Enter A Valid Input")
                print(" ")
            
    if choice == 2:
        while 2:
            print("1. Display Silver Members")
            print("2. Display Gold Members")
            print("3. Display Platinum Members")
            print("0. Exit to Main Menu")
            option3 = int(input())
            if option3 == 1:
                for x in range(0, len(memberSilverList)):
                    sm.display_member()
            if option3 == 2:
                for x in range(0, len(memberGoldList)):
                    gm.display_member()
            if option3 == 3:
                for x in range(0, len(memberPlatList)):
                    pm.display_member()
            if option3 == 0:
                print("Exiting to Main Menu")
                break
    
    if choice == 3:
        while 2:
            remove_menu()
            option2 = int(input())
            print(" ")
            if option2 == 1:
                user = input("Enter Name: ")
                for x in memberSilverList:
                    if x == user:
                        memberSilverList.remove(x)
                        break
                    else:
                        for x in memberGoldList:
                            if x == user:
                                memberGoldList.remove(x)
                                break
                            else:
                                for x in memberPlatList:
                                    if x == user:
                                        memberPlatList.remove(x)
                                        break
                                    else:
                                        print("Member not found")
                                        break
                
            if option2 == 2:
                print("Returning to Main Menu")
                break

    if choice == 4:
        print("Program Terminated.")
        break
