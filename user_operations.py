import json as j

def getUsersData():
    with open("Nutzerdaten.json", "r") as f:
        data = j.load(f)
        userNames = data["userNames"]
        passwords = data["passwords"]
    
    return userNames, passwords

def rewriteUsersData(userNames, passwords):
    with open("Nutzerdaten.json", "w") as f:
        j.dump({"userNames": userNames, "passwords": passwords}, f)

def login():
    condition = True

    while condition:
        currentUserName = input("Geben Sie den Benutzername ein: ")
        password = input("Geben Sie das Passwort ein: ")

        if currentUserName in getUsersData()[0] and password in getUsersData()[1]:
            print("Login erfolgreich!", end = "\n\n")
            condition = False
        else:
            print("Login fehlgeschlagen. Bitte überprüfen Sie Ihren Benutzernamen und Ihr Passwort.", end = "\n\n")
    
    return currentUserName

def giveUserList():
    userNames, passwords = getUsersData()

    print("Liste der Benutzer:")
    for userName in userNames:
        print(userName, end = "\n")
    print("\n")

def createUser(currentUserName):
    if currentUserName == "Admin":
        condition = True
        while condition:
            userNames, passwords = getUsersData()

            newUserName = input("Geben Sie den Benutzernamen für den neuen Nutzer ein: ")
            if newUserName == "exit":
                condition = False
            elif userNames.count(newUserName) == 0:
                userNames.append(newUserName)
                passwords.append(input("Geben Sie das Passwort für den neuen Nutzer ein: "))
            
                rewriteUsersData(userNames, passwords)

                print("Nutzer erfolgreich erstellt!", end = "\n\n")
            else:
                print("Benutzer mit solche Benutzername schon existiert. Überprüffen Sie die Liste der Nutzer und versuchen Sie es erneut.")
    else:
        print("Sie haben keine Berechtigung, Nutzer zu erstellen.", end = "\n\n")

def deleteUser(currentUserName):
    if currentUserName == "Admin":
        giveUserList()

        userNames, passwords = getUsersData()
        condition = True

        while condition:
            userNameToDelete = input("Geben Sie den Benutzernamen ein, den Sie löschen möchten: ")
            if userNameToDelete == "exit":
                condition = False
            elif userNameToDelete in userNames and userNameToDelete != "Admin":
                index = userNames.index(userNameToDelete)
                userNames.pop(index)
                passwords.pop(index)

                rewriteUsersData(userNames, passwords)

                print(f"Nutzer {userNameToDelete} erfolgreich gelöscht!", end = "\n\n")
            elif userNameToDelete == "Admin":
                print("Der Admin-Benutzer kann nicht gelöscht werden.", end = "\n\n")
            else:
                print("Benutzername nicht gefunden.", end = "\n\n")
    else:
        print("Sie haben keine Berechtigung, Nutzer zu löschen.", end = "\n\n")

def changePassword(currentUserName):
    userNames, passwords = getUsersData()
    index = userNames.index(currentUserName)
    oldPassword = input("Geben Sie das alte Passwort ein: ")

    newPassword = input("Geben Sie das neue Passwort ein: ")
    newPassword1 = input("Geben Sie das neue Passwort nochmal ein: ")

    if oldPassword == passwords[index] and newPassword == newPassword1:
        passwords.pop(index)
        passwords.insert(index, newPassword)
        rewriteUsersData(userNames, passwords)

        print("Passwort erfolgreich geändeert!", end = "\n\n")
    else:
        print("Etwas hat nicht geklappt. Überprüffen Sie Ihre Eingaben und versuchen Sie es erneut.", end = "\n\n")