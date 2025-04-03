def show_phone(parsed, contacts):
    name = parsed[1]
    if name in contacts:
        return contacts[name]
    else:
        return "Unknown name"
