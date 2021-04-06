import datetime
import os

total_members = 0
member_names = []


def retrieve_details(pf):
    print("******************************************")
    f = open(pf, "r")
    for line in f:
        print(line, end="")
    print("\n******************************************")


def add_details(section_type, pf):
    time = "[" + str(get_time()) + "]"
    if section_type == 'd':
        print("Add diet:\n")
        tmp = "\t" + input().capitalize() + "\n"
    elif section_type == 'e':
        print("Add exercise\n")
        tmp = "\t" + input().capitalize() + "\n"
    else:
        return
    with open(pf, "a") as f:
        f.write(time)
        f.write(tmp)


def add_member():
    global total_members
    total_members += 1
    print("Enter name only")
    name = input().capitalize()
    member_names.append(name)
    time = "[" + str(get_time()) + "]\t"
    diet_file = "DIET\\" + name.lower() + "_diet.txt"
    exercise_file = "EXERCISE\\" + name.lower() + "_exercise.txt"
    with open(diet_file, "x") as f:
        f.write("DIET\n")
    with open(exercise_file, "x") as f:
        f.write("EXERCISE\n")
    name += "\n"
    with open("Community.txt", "a") as f:
        f.write(time)
        f.write(name)


def get_time():
    return datetime.datetime.now()


def print_community():
    with open("Community.txt", "r") as f:
        if os.stat("Community.txt").st_size < 2:
            print("No members yet!\nPlease add a member")
        else:
            print("*************COMMUNITY MEMBERS*************")
            for line in f:
                print(line, end="")
            print("******************************************")


def section(n):
    print("Which section?\nDiet\t\tD\nExercise\tE")
    command = input().lower()
    if command == 'd':
        return 'd', "DIET\\" + n + "_diet.txt"
    elif command == 'e':
        return 'e', "EXERCISE\\" + n + "_exercise.txt"
    else:
        print("Invalid selection")
        return "", ""


def get_member_info(name):
    print("*************MEMBER DETAILS SECTION*************")
    print("*************", name.upper(), "*************")
    cont = True
    while cont:
        print("\nAdd Details\t\t\tA\nRetrieve Details\tR\nExit Member Details\tE")
        command = input().lower()
        if command == 'e':
            return
        tmp1, tmp2 = section(name)
        if command == 'a':
            add_details(tmp1, tmp2)
        elif command == 'r':
            retrieve_details(tmp2)
        else:
            print("Invalid option")


def get_members():
    print_community()
    print("Enter member name: ")
    member_name = input().lower().capitalize()
    # if member_name not in member_names:
    #     print("Invalid Member Name")
    # else:
    get_member_info(member_name)


def print_welcome_block():
    print("Press the corresponding keys:\nAdd Member\t\tA\nGet Community\tC\nMember Details\tM\nExit\t\t\tE")
    command = input().lower()
    if command == 'a':
        add_member()
    elif command == 'c':
        print_community()
    elif command == 'm':
        get_members()
    elif command == 'e':
        return True
    else:
        print("Invalid command")


if __name__ == '__main__':
    exit_system = False
    if not os.path.exists("Community.txt"):
        f = open("Community.txt", "x")
        f.close()
    print("******WELCOME TO THE HEALTH MANAGEMENT SYSTEM******")
    while not exit_system:
        if print_welcome_block():
            break
    os.remove("Community.txt")
    print("THANK YOU FOR VISITING!")
