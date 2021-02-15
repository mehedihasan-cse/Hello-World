import time

numbers = {}


class phonBook:
    # make a phoneBook constuctor
    def __init__(self, name, PhoneNumber, gmail):
        self.name = name
        self.PhoneNumber = PhoneNumber
        self.gmail = gmail

    def AddNewNumberAndGmail(self):
        if self.PhoneNumber and self.name:
            numbers[self.name] = self.PhoneNumber, self.gmail
        else:
            print("Phone number is empty1")

    def RemoveNumberAndGmail(self):
        self.name = input("Enter name which you wan to delete: ").title()
        if self.name in numbers:
            del numbers[self.name]
        else:
            print("File not found")

    def ShowDetai(self):
        for key in numbers.keys():
            print("Number:", key, "\tPhone:", numbers[key][0], "\tGmail:", numbers[key][1])

    def LookUp(self):
        print("Look up :")
        self.name = input("Input Your LookUp NAme:").title()
        if self.name in numbers:
            print("Number:", numbers[self.name][0], '\tGmail', numbers[self.name][1])
        else:
            print("Contact not found")


def print_menu():
    print("1. Add contact:")
    print("2. Show contact:")
    print("3. Search contact")
    print("4. Delete contact")
    print("5. Quit")
if __name__ == "__main__":


    menu_choice = 0
    while menu_choice != 5:
        print_menu()
        print("P", end="")
        time.sleep(0.1)
        print("l", end="")
        time.sleep(0.1)
        print("e", end="")
        time.sleep(0.1)
        print("a", end="")
        time.sleep(0.1)
        print("s", end="")
        time.sleep(0.1)
        print("e ", end="")
        time.sleep(0.1)
        print("E", end="")
        time.sleep(0.1)
        print("n", end="")
        time.sleep(0.1)
        print("t", end="")
        time.sleep(0.1)
        print("e", end="")
        time.sleep(0.1)
        print("r ", end="")
        time.sleep(0.1)
        print("Y", end="")
        time.sleep(0.1)
        print("o", end="")
        time.sleep(0.1)
        print("u", end="")
        time.sleep(0.1)
        print("r ", end="")
        time.sleep(0.1)
        print("C", end="")
        time.sleep(0.1)
        print("h", end="")
        time.sleep(0.1)
        print("o", end="")
        time.sleep(0.1)
        print("i", end="")
        time.sleep(0.1)
        print("c", end="")
        time.sleep(0.1)
        print("e ", end="")
        time.sleep(0.1)
        print("(1-5) :")
        time.sleep(0.1)

        try:
            menu_choice = int(input())
        except ValueError as e:
            print('Please Try again..')

        if menu_choice == 1:
            phonDetail = phonBook(input("Name: ").title(), input("Phone Number: ").capitalize(),
                                  input("Gmail account: ").capitalize())
            phonDetail.AddNewNumberAndGmail()

        elif menu_choice == 2:
            try:
                phonDetail.ShowDetai()
            except NameError as e:
                print('Your phone book is totally emty')

        elif menu_choice == 3:
            try:
                phonDetail.LookUp()
            except NameError as e:
                print("Your phonebook is emty or Invalid name..")

        elif menu_choice == 4:
            try:
                phonDetail.RemoveNumberAndGmail()
            except NameError as e:
                print("Your phonebook is emty or Invalid name..")

        elif menu_choice >= 5:
            break
            print_menu()

