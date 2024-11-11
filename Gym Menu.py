import Gym_Setup as GS

def main_menu():
    print("1. Add Member")

memberList = []

while 1:
    main_menu()
    choice = int(input(""))
    if choice == 1:
        mm = GS.Member()
        mm.add_member()
