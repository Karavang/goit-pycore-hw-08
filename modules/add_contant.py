from modules.decocatcher import input_error

def add_contact(parsed:list, contacts: dict) -> str:
   
    name: str = parsed[1]
    phone: int = int(parsed[2])
    # if not isinstance(phone, int) or not isinstance(name, str):
    #     raise ValueError
    
    if name in contacts:
        return "This contact already exists"
    else:
        contacts[name] = phone
    return "Contact added"
