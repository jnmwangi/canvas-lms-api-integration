from helpers import user
from menu import menu

# accounts = user.get_user()
session = [menu]

while True:
    current = session[-1]
    
    for i in range(len(current)):
        print(f"{i+1}: {current[i]['name']}")
        
    print("0: Go back or exit")
        
    option = int(input("Select option: "))
    print("")
    if option == 0:
        if len(session) > 0:
            session.pop()
            continue
        else: exit
    
    if 0 < option <= len(current):
        selected = current[option-1]
        if "fields" in selected:
            data = {}
            for field in selected["fields"]:
                if "action" in field: field["action"]()
                data[field["field"]] = input(f"{field['name']}: ")
            selected["action"](data)
            print("")
        elif "actions" in selected:
            session.append(selected["actions"])
        elif "action" in selected:
            selected["action"]()
            print("")
    else:
        print("Invalid Option")
        input("Retry (y): ")
            

