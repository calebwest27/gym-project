import Gym_setup as GS
from Gym_setup import *

import random


def main_menu():
    print("1. Add Member")

memberList = []
memberInfo = []


while 1:
    main_menu()
    choice = int(input(""))
    if choice == 1:
        a = random.sample(range(10000, 99999), 1)
        mm = GS.Member(input("Name: "), input("Phone Number: "), a)
        memberList.append(mm)
    if choice == 2:
        for x in memberList:
            print(Person.display)

    if choice == 0:
        print("Program Terminated.")
        break
