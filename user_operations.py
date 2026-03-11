import json as j

def createUser(userName, password):
    with open("Nutzerdaten.json", "r") as f:
        data = j.load(f)
        userNames = data["userNames"]
        passwords = data["passwords"]

    userNames.append(userName)
    passwords.append(password)

    with open("Nutzerdaten.json", "w") as f:
        j.dump({"userNames": userNames, "passwords": passwords}, f)

    print("Nutzer erfolgreich erstellt!")

def deleteUser(userNames, passwords, currentUserName):
    if currentUserName == "Admin":
        print("Liste der Benutzer:")
        for userName in userNames:
            print(userName)
        userNameToDelete = input("Geben Sie den Benutzernamen ein, den Sie löschen möchten: ")
        if userNameToDelete in userNames and userNameToDelete != "Admin":
            index = userNames.index(userNameToDelete)
            userNames.pop(index)
            passwords.pop(index)

            with open("Nutzerdaten.json", "w") as f:
                j.dump({"userNames": userNames, "passwords": passwords}, f)

            print(f"Nutzer {userNameToDelete} erfolgreich gelöscht!", end = "\n\n\n\n\n")
        elif userNameToDelete == "Admin":
            print("Der Admin-Benutzer kann nicht gelöscht werden.", end = "\n\n\n\n\n")
        else:
            print("Benutzername nicht gefunden.", end = "\n\n\n\n\n")
    else:
        print("Sie haben keine Berechtigung, Nutzer zu löschen.", end = "\n\n\n\n\n")

def getUsersData():
    with open("Nutzerdaten.json", "r") as f:
        data = j.load(f)
        userNames = data["userNames"]
        passwords = data["passwords"]
    
    return userNames, passwords

def login(userNames, passwords):
    condition = True

    while condition:
        currentUserName = input("Geben Sie den Benutzername ein: ")
        password = input("Geben Sie das Passwort ein: ")

        if currentUserName in userNames and password in passwords and userNames.index(currentUserName) == passwords.index(password):
            print("Login erfolgreich!")
            condition = False
        else:
            print("Login fehlgeschlagen. Bitte überprüfen Sie Ihren Benutzernamen und Ihr Passwort.")
    
    return currentUserName