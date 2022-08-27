from os import get_terminal_size
from price_notifier import get_link_data
import time

def main():
    user_Option = print_menu()

def print_menu():
    # Variable holding width of terminal
    terminal_Width = get_terminal_size().columns

    # Print bounding box to fit terminal
    print("┏", end = "", flush = True)
    for columns in (range(terminal_Width - 2)):
        print("━", end = "", flush = False)
    print("┓", end = "", flush = True)
    print("┃", end = "", flush = False)

    # Print title to fit terminal
    columns = 0
    while (columns < terminal_Width - 2):
        if (columns == int(terminal_Width / 2) - 15):
            print("PRICE NOTIFIER APPLICATION", end = "", flush = False)
            columns += 26
        else:
            print(" ", end = "", flush = False)
            columns += 1
    print("┃", end = "", flush = True)

    # Print disconnector to fit terminal
    print("┣", end = "", flush = False)
    for columns in (range(terminal_Width - 2)):
        print("━", end = "", flush = False)
    print("┫", end = "", flush = True)
    
    # Print option 1 to fit terminal
    print("┣ (1) Add A Link", end = "", flush = False)
    for columns in (range(terminal_Width - 17)):
        print(" ", end = "", flush = False)
    print("┃", end = "", flush = True)

    # Print option 2 to fit terminal
    print("┣ (2) Remove A Link", end = "", flush = False)
    for columns in (range(terminal_Width - 20)):
        print(" ", end = "", flush = False)
    print("┃", end = "", flush = True)

    # Print option 3 to fit terminal
    print("┣ (3) View Links", end = "", flush = False)
    for columns in (range(terminal_Width - 17)):
        print(" ", end = "", flush = False)
    print("┃", end = "", flush = True)
    
    # Print option 4 to fit terminal
    print("┣ (4) START SCRIPT", end = "", flush = False)
    for columns in (range(terminal_Width - 19)):
        print(" ", end = "", flush = False)
    print("┃", end = "", flush = True)

    print("┣", end = "", flush = False)
    user_Option = get_user_input()

    return user_Option

def get_user_input():
    user_Option = input(" ")
    # Check if user input is valid
    is_Invalid = True
    while(is_Invalid):
        if(user_Option.isdigit()):
            user_Option = int(user_Option)
            if(user_Option >= 1 and user_Option <= 4):
                is_Invalid = False
            else:
                print("┣ Please A Number Corresponding To The Options Provided!")
                user_Option = input("┣ ")
        else:
            print("┣ Please A Number Corresponding To The Options Provided!")
            user_Option = input("┣ ")
    
    if(user_Option == 1):
        add_Link = input("┣ Enter The New Link You Want To Add: ")
        desired_Price = input("┣ Enter Your Desired Price For Product: ")
        with open("links.txt", "a") as lf:
            lf.write("\n" + add_Link + "^" + desired_Price)

        print("PRODUCT ADDED")
    elif(user_Option == 2):
        products = get_link_data()

        x = 1
        for product in products:
            print("(" + str(x) + ") " + product[0])
            x = x + 1
        remove_Link = input("┣ Enter The Number For The Product You Want To Remove: ")

        x = 1
        with open("links.txt", "r") as f:
            lines = f.readlines()
        with open("links.txt", "w") as f:
            for line in lines:
                if (int(remove_Link) != int(x)) and (line.strip("\n") != "anything"):
                    f.write(line)
                    x = x + 1
                else:
                    x = x + 1
        
        print("PRODUCT REMOVED")
    elif(user_Option == 3):
        products = get_link_data()

        x = 1
        for product in products:
            print("(" + str(x) + ") " + product[0])
            x = x + 1
    else:
        while(True):
            get_link_data()
            time.sleep(5)

    return user_Option

main()