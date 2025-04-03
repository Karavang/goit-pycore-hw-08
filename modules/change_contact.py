def change_contact(parsed:list, contacts):
    name: str = parsed[1]
    phone: int = int(parsed[2])
    if name in contacts:
        contacts[name] = phone
    return "Contact changed"
