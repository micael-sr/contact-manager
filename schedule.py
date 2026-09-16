import os
import time
import csv


contacts = []


def add():

    name = input("Enter your name: ").title()

    for person in contacts:
        if name in person:
            print("This contact already exists")
            time.sleep(2)
            return

    person = {}

    while True:
        phone = input("Enter your phone number: ")

        if phone.isdigit():
            break

        print("Numbers only, please try again..\n")
        time.sleep(2)

    person[name] = {
        'phone': phone,
        'email': input("Enter your email: "),
        'address': input("Enter your address: "),
    }
    contacts.append(person)
    print("Contact added successfully: ")
    print()
    time.sleep(2)
    input("Press Enter to continue..")


def show_contacts():

    if len(contacts) == 0:
        print("There are no contacts")
    
    else:
        for contact in contacts:
            for name, info in contact.items():
                print(f"Name: {name}")
                print(f"Phone: {info['phone']}")
                print(f"Email: {info['email']}")
                print(f"Address: {info['address']}")
                print("-" * 30)
                time.sleep(1.5)
    input("Press Enter to continue..")


def search_contacts():
    p = input("Enter the name of the contact you want to find: ").title()
    for contact in contacts:
        if p in contact:
            print("Loading...")
            time.sleep(2)
            print("Contact found!")
            time.sleep(1)
            for name, info in contact.items():
                print(f"Name: {p}")
                print(f"Phone: {info['phone']}")
                print(f"Email: {info['email']}")
                print(f"Address: {info['address']}")
                print("-" * 30)
            break
    else:
        print("Loading...")
        time.sleep(2)
        print("Contact not found...")
        print()
    input("Press Enter to continue..")

def delete_contact():
    p = input("Type the contact you want to delete: ").title()
    for contact in contacts:
        if p in contact:
            contacts.remove(contact)
            time.sleep(1)
            print("Contact deleted successfully!")
            break
        else:
            print("This account doesn't exist")
            print()
    input("Press Enter to continue..")

    
def edit_contact():
    p = input("Type the contact you want to edit: ").title()
    for contact in contacts:
        if p in contact:
            contacts.remove(contact)
            time.sleep(2)
            print("=========Add edited contact=========")
            add()
            break
        else:
            print("Contact not found..")
            print()
        input("Press Enter to continue..")


def export_csv():
    with open("contacts.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=[
                "name",
                "phone",
                "email",
                "address"

            ],
            delimiter=";"
        )

        writer.writeheader()

        for contact in contacts:


            for name, info in contact.items():


                writer.writerow({
                    "name": name,
                    "phone": info["phone"],
                    "email": info["email"],
                    "address": info["address"]
                })


    print("Contact exported successfully!")

    input("Press Enter to continue..")


def import_csv():
    try:

        with open(
            "contacts.csv",
            "r",
            newline="",
            encoding="utf-8"
        ) as file:

            reader = csv.DictReader(
                file,
                delimiter=";"

        )

            contacts.clear()

            for row in reader:


                person = {
                    row["name"]: {
                        "phone": row["phone"],
                        "email": row["email"],
                        "address": row["address"]

                    }

                }

                contacts.append(person)

        print("Contacts imported successfully!") 


    except FileNotFoundError:

        print("Contacts file not found.")

    input("Press Enter to continue..")






while True:
    os.system("cls")
    print("-" * 30)
    print("Menu")
    print("-" * 30)
    print("1. Add Contacts")
    print("2. Show Contacts")
    print("3. Search Contacts")
    print("4. Edit Contacts")
    print("5. Delete Contact")
    print("6. Export Contacts")
    print("7. Import Contacts")
    print("8. Exit ")
    print("-" * 30)

    while True:
        try:
            r = int(input("Choose an option: "))
            break
        except ValueError:
            print("Numbers only, Please try again.")
            continue

    if r == 1:
        add()

    elif r == 2:
        show_contacts()

    elif r == 3:
        search_contacts()

    elif r == 4:
        edit_contact()

    elif r == 5:
        delete_contact()

    elif r == 6:
        export_csv()

    elif r == 7:
        import_csv()

    elif r == 8:
        print("Saving the contacts...")
        time.sleep(4)
        print("Ending the program.")
        time.sleep(2)
        break

    else:
        print("Invalid option")
        input("Press to enter for try again..")