import Gym_setup as Gs

import random

import tkinter as tk
from tkinter import *

top = Tk()


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

top.geometry("500x500")
answer = Text(width=47, height=2)
answer.place(x=100, y=100)


def show(x):
    try:

        if x == "=":
            final_answer = eval(answer.get(1.0, "end-1c"))
            answer.insert(tk.INSERT, x)
            answer.insert(tk.INSERT, final_answer)
        elif x == "C":
            answer.delete(1.0, END)
        else:
            answer.insert(tk.INSERT, x)
    except:
        answer.delete(1.0, END)

B1 = Button(top, text="1", width=10, height=5, command=lambda: show("1"))
B1.place(x=100, y=150)
B2 = Button(top, text="2", width=10, height=5, command=lambda: show("2"))
B2.place(x=200, y=150)
B3 = Button(top, text="3", width=10, height=5, command=lambda: show("3"))
B3.place(x=300, y=150)
B4 = Button(top, text="4", width=10, height=5, command=lambda: show("4"))
B4.place(x=100, y=250)
B5 = Button(top, text="5", width=10, height=5, command=lambda: show("5"))
B5.place(x=200, y=250)
B6 = Button(top, text="6", width=10, height=5, command=lambda: show("6"))
B6.place(x=300, y=250)
B7 = Button(top, text="7", width=10, height=5, command=lambda: show("7"))
B7.place(x=100, y=350)
B8 = Button(top, text="8", width=10, height=5, command=lambda: show("8"))
B8.place(x=200, y=350)
B9 = Button(top, text="9", width=10, height=5, command=lambda: show("9"))
B9.place(x=300, y=350)
B0 = Button(top, text="0", width=10, height=5, command=lambda: show("0"))
B0.place(x=100, y=450)

top.mainloop()

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
                for y in range(0, len(memberList)):
                    if y == memberList:
                        new_value = random.sample(range(10000, 99999), 1)
                        memberList[y] = new_value

            if option1 == 0:
                print("Exiting to Main Menu")
                break

            else:
                print("Please Enter A Valid Input")
                print(" ")

    if choice == 2:
        for z in range(0, len(memberList)):
            info.display_member()

    if choice == 3:
        while 2:
            remove_menu()
            option2 = int(input())
            print(" ")
            if option2 == 1:
                user = input("Enter Name: ")
                for v in memberList:
                    if v == user:
                        memberList.remove(v)
                break

            if option2 == 2:
                print("Returning to Main Menu")
                break

    if choice == 4:
        print("Program Terminated.")
        break
