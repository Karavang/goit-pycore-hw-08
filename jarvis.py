from modules.parse_input import parse_input
from pickleRick import save_data, load_data
from modules.bookcontacts import Record, AddressBook


def main():
    contacts = load_data()
    while True:
        command = input("Enter a command: ")
        parsed = parse_input(command)
        match parsed[0]:
            case "hello":
                print("How can I help you?")
            case "add":
                name, phone = parsed[1], parsed[2]
                record = contacts.find(name)
                if not record:
                    record = Record(name)
                    contacts.add_record(record)
                record.add_phone(phone)
                print(f"Added {phone} to {name}")
            case "change":
                name, old_phone, new_phone = parsed[1], parsed[2], parsed[3]
                record = contacts.find(name)
                if record:
                    print(record.edit_phone(old_phone, new_phone))
                else:
                    print(f"Contact {name} not found")
            case "phone":
                name = parsed[1]
                record = contacts.find(name)
                if record:
                    print(record)
                else:
                    print(f"Contact {name} not found")
            case "all":
                for name, record in contacts.data.items():
                    print(record)
            case "add-birthday":
                name, birthday = parsed[1], parsed[2]
                record = contacts.find(name)
                if record:
                    print(record.add_birthday(birthday))
                else:
                    print(f"Contact {name} not found")
            case "show-birthday":
                name = parsed[1]
                record = contacts.find(name)
                if record and record.birthday:
                    print(
                        f"{name}'s birthday: {record.birthday.value.strftime('%d.%m.%Y')}"
                    )
                else:
                    print(f"Birthday for {name} not found")
            case "birthdays":
                upcoming = contacts.get_upcoming_birthdays()
                if upcoming:
                    for entry in upcoming:
                        print(f"{entry['name']}: {entry['congratulation_date']}")
                else:
                    print("No upcoming birthdays in the next week")

            case "close" | "exit":
                try:
                    print("Good bye!")
                    save_data(contacts)
                    break
                except:
                    print("Failed to close the window")
            case _:
                print("Unknown command")


if __name__ == "__main__":
    main()
