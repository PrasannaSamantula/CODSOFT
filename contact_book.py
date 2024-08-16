# CONTACT BOOK

contacts = {}

def display_contacts():
    print("Name\t\tMobile Number")
    for key in contacts:
        print("{}\t\t{}".format(key,contacts.get(key)))


while True:
    choice = int(input("1.Add Contact \n 2.View Contact \n 3.Search Contact \n 4.Update Contact \n 5.Delete Contact \n 6.Exit \n Enter your choice:"))
    if choice == 1:
        name = input("Enter contact name:").upper()
        phone = input("Enter mobile number:")
        contacts[name] = phone
    elif choice == 2:
        if not contacts:
            print("Contact book is empty")
        else:
            display_contacts()
    elif choice == 3:
        search_contact = input("Enter contact name to search details:").upper()
        if search_contact in contacts:
            print(search_contact,"'s contact number is:",contacts[search_contact])
        else:
            print("Name is not found in contact book")
    elif choice == 4:
        update_contact = input("Enter contact to update:").upper()
        if update_contact in contacts:
            update_contact = input("Enter contact to be updated:").upper()
            contacts[update_contact] = phone
            print("Contact updated")
            display_contacts()
        else:
            print("Name is not found in contact book")
    elif choice == 5:
        del_contact = input("Enter contact to delete:").upper()
        if del_contact in contacts:
            confirm = input("Do you want to delete the contact(yes/no):").lower()
            if confirm == "yes":
                contacts.pop(del_contact)
            display_contacts()
        else:
            print("Name is not found in contact book")
    elif choice == 6:
        break
    else:
        print("Invalid number")