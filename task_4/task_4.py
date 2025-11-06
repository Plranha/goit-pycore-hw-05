def input_error(func):
    def inner (*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact wasn`t found"
        except IndexError:
            return "Enter the argument for the command"
        except ValueError:
            return "Give me name and phone please."       
    return inner


def parse_input(user_input):
    parts = user_input.split()
    if not parts:
        return "", []
    cmd = parts[0].lower()
    args = parts[1:]
    return cmd, args


@input_error
def add_contact(args, contacts):
    name, phone = args  # Якщо args має менше 2 елементів - виникне ValueError
    contacts[name] = phone
    return "Contact added"

@input_error
def change_contact(args, contacts):
    name, new_phone = args
    _ = contacts[name]  # ← Спроба отримати контакт (викине KeyError якщо не існує)
    contacts[name] = new_phone  # ← Зміна існуючого контакту
    return "Contact updated"


@input_error
def show_phone(args, contacts):
    name = args[0]  # Якщо args порожній - виникне IndexError
    return contacts[name]  # Якщо name немає в contacts - виникне KeyError

@input_error
def show_all(contacts):
    if not contacts:
        raise ValueError("No contact found")
    result = []
    for name, phone in contacts.items():
        result.append(f"{name}: {phone}")
    return "\n".join(result)



def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input('Enter a command: ').strip()
        command, args = parse_input(user_input)
        
        if command in ["close",'exit']:
            print('Good bye!')
            break
        elif command == 'hello' or command == 'hi':
            print('How can I help you?')
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print('Invalid command')
    
    
if __name__ == '__main__':
    main()