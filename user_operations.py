import json as j

def getUsersData():
    with open("Nutzerdaten.json", "r") as f:
        data = j.load(f)
        userNames = data["userNames"]
        passwords = data["passwords"]
    
    return userNames, passwords

def login():
    condition = True

    while condition:
        currentUserName = input("Geben Sie den Benutzername ein: ")
        password = input("Geben Sie das Passwort ein: ")

        if currentUserName in getUsersData()[0] and password in getUsersData()[1] and getUsersData()[0].index(currentUserName) == getUsersData()[1].index(password):
            print("Login erfolgreich!", end = "\n\n")
            condition = False
        else:
            print("Login fehlgeschlagen. Bitte überprüfen Sie Ihren Benutzernamen und Ihr Passwort.", end = "\n\n")
    
    return currentUserName

def createUser(currentUserName):
    if currentUserName == "Admin":
        with open("Nutzerdaten.json", "r") as f:
            data = j.load(f)
            userNames = data["userNames"]
            passwords = data["passwords"]

        userNames.append(input("Geben Sie den Benutzernamen für den neuen Nutzer ein: "))
        passwords.append(input("Geben Sie das Passwort für den neuen Nutzer ein: "))

        with open("Nutzerdaten.json", "w") as f:
            j.dump({"userNames": userNames, "passwords": passwords}, f)

        print("Nutzer erfolgreich erstellt!", end = "\n\n")
    else:
        print("Sie haben keine Berechtigung, Nutzer zu erstellen.", end = "\n\n")

def deleteUser(currentUserName):
    if currentUserName == "Admin":
        print("Liste der Benutzer:")

        userNames, passwords = getUsersData()

        for userName in userNames:
            print(userName)

        condition = True

        while condition:
            userNameToDelete = input("Geben Sie den Benutzernamen ein, den Sie löschen möchten: ")
            if userNameToDelete == "exit":
                condition = False
            elif userNameToDelete in userNames and userNameToDelete != "Admin":
                index = userNames.index(userNameToDelete)
                userNames.pop(index)
                passwords.pop(index)

                with open("Nutzerdaten.json", "w") as f:
                    j.dump({"userNames": userNames, "passwords": passwords}, f)

                condition = False
                print(f"Nutzer {userNameToDelete} erfolgreich gelöscht!", end = "\n\n")
            elif userNameToDelete == "Admin":
                print("Der Admin-Benutzer kann nicht gelöscht werden.", end = "\n\n")
            else:
                print("Benutzername nicht gefunden.", end = "\n\n")
    else:
        print("Sie haben keine Berechtigung, Nutzer zu löschen.", end = "\n\n")