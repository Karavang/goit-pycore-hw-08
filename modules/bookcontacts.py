from collections import UserDict
from datetime import datetime, timedelta


class Field:

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):

    def __init__(self, value):
        super().__init__(value)
        self.name = value

    def getName(self):
        return self.name

    pass


class Phone(Field):
    def __init__(self, value):
        if len(value) == 10 and value.isdigit():
            super().__init__(value)
        else:
            raise ValueError("Invalid phone")

    pass


class Birthday(Field):
    def __init__(self, value):
        try:
            self.value = datetime.strptime(value, "%d.%m.%Y")
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)
                return f"Phone {phone} removed"
        return f"Phone {phone} not found"

    def edit_phone(self, old_phone, new_phone):
        for p in self.phones:
            if p.value == old_phone:
                p.value = new_phone
                return f"Phone {old_phone} changed to {new_phone}"
        return f"Phone {old_phone} not found"

    def find_phone(self, phone):
        return next((p for p in self.phones if p.value == phone), None)

    def add_birthday(self, date):
        self.birthday = Birthday(date)
        return f"Birthday {date} added"

    def __str__(self):
        phones = "; ".join(p.value for p in self.phones)
        return f"Contact name: {self.name.value}, phones: {phones}, birthday: {self.birthday.value.strftime('%d.%m.%Y') if self.birthday else 'No birthday'}"


class AddressBook(UserDict):
    def add_record(self, record):

        self.data[record.name.value] = record

    def find(self, name):

        return self.data.get(name, None)

    def delete(self, name):

        if name in self.data:
            del self.data[name]
            return f"Contact {name} deleted"
        return "Contact not found"

    def get_upcoming_birthdays(self):

        today = datetime.today().date()
        upcoming_birthdays = []

        for record in self.data.values():
            if record.birthday:
                birthday = record.birthday.value.date()
                birthday_this_year = birthday.replace(year=today.year)

                if birthday_this_year < today:
                    birthday_this_year = birthday.replace(year=today.year + 1)

                if 0 <= (birthday_this_year - today).days <= 7:
                    congrats_date = birthday_this_year

                    if congrats_date.weekday() in (5, 6):
                        congrats_date += timedelta(days=(7 - congrats_date.weekday()))

                    upcoming_birthdays.append(
                        {
                            "name": record.name.value,
                            "congratulation_date": congrats_date.strftime("%Y.%m.%d"),
                        }
                    )

        return upcoming_birthdays

    pass
