import json as j

def give_user_list():
    userNames = get_users_data()[0]
    print("\nListe der Benutzer:")
    
    for userName in userNames:
        print(f"    {userName}")
    print("")

def get_users_data():
    with open("Nutzerdaten.json", "r") as f:
        data = j.load(f)
        userNames = data["userNames"]
        passwords = data["passwords"]
    return userNames, passwords

def rewrite_users_data(userNames, passwords):
    with open("Nutzerdaten.json", "w") as f:
        j.dump({"userNames": userNames, "passwords": passwords}, f)

def login():
    condition = True

    while condition:
        currentUserName = input("Geben Sie den Benutzername ein: ")
        password = input("Geben Sie das Passwort ein: ")

        if currentUserName in get_users_data()[0] and password in get_users_data()[1]:
            index = get_users_data()[0].index(currentUserName)

            if password == get_users_data()[1][index]:
                print("Login erfolgreich!\n")
                condition = False

            else:
                print("Login fehlgeschlagen. Bitte überprüfen Sie Ihren Benutzernamen und Ihr Passwort.\n")

        else:
            print("Login fehlgeschlagen. Bitte überprüfen Sie Ihren Benutzernamen und Ihr Passwort.\n")
    return currentUserName

def create_user(currentUserName):
    if currentUserName == "Admin":
        userNames, passwords = get_users_data()
        newUserName = input("\nGeben Sie den Benutzernamen für den neuen Nutzer ein: ")

        if userNames.count(newUserName) == 0:
            userNames.append(newUserName)
            passwords.append(input("Geben Sie das Passwort für den neuen Nutzer ein: "))

            rewrite_users_data(userNames, passwords)
            print("Nutzer erfolgreich erstellt!\n")

        else:
            print("Benutzer mit solche Benutzername schon existiert. Überprüffen Sie die Liste der Nutzer und versuchen Sie es erneut.\n")

    else:
        print("\nSie haben keine Berechtigung, Nutzer zu erstellen.\n")

def delete_user(currentUserName):
    if currentUserName == "Admin":
        give_user_list()
        userNames, passwords = get_users_data()
        userNameToDelete = input("Geben Sie den Benutzernamen ein, den Sie löschen möchten: ")

        if userNameToDelete in userNames and userNameToDelete != "Admin":
            index = userNames.index(userNameToDelete)
            userNames.pop(index)
            passwords.pop(index)

            rewrite_users_data(userNames, passwords)
            print(f"Nutzer {userNameToDelete} erfolgreich gelöscht!\n")

        elif userNameToDelete == "Admin":
            print("Der Admin-Benutzer kann nicht gelöscht werden.\n")

        else:
            print("Benutzername nicht gefunden.\n")

    else:
        print("\nSie haben keine Berechtigung, Nutzer zu löschen.\n")

def change_password(currentUserName):
    userNames, passwords = get_users_data()
    index = userNames.index(currentUserName)

    oldPassword = input("\nGeben Sie das alte Passwort ein: ")
    newPassword = input("Geben Sie das neue Passwort ein: ")
    newPassword1 = input("Geben Sie das neue Passwort nochmal ein: ")

    if oldPassword == passwords[index] and newPassword == newPassword1:
        passwords.pop(index)
        passwords.insert(index, newPassword)

        rewrite_users_data(userNames, passwords)
        print("\nPasswort erfolgreich geändert!\n")

    else:
        print("\nEtwas hat nicht geklappt. Überprüffen Sie Ihre Eingaben und versuchen Sie es erneut.\n")

def change_user_name(currentUserName):
    userNames, passwords = get_users_data()

    if currentUserName == "Admin":
        give_user_list()
        userNameToChange = input("Geben Sie den Benutzernamen ein, den Sie ändern möchten: ")

        if userNameToChange in userNames and userNameToChange != "Admin":
            newUserName = input("Geben Sie den neuen Benutzernamen ein: ")

            if newUserName not in userNames:
                index = userNames.index(userNameToChange)
                userNames.pop(index)
                userNames.insert(index, newUserName)

                rewrite_users_data(userNames, passwords)
                print(f"Benutzername {userNameToChange} erfolgreich zu {newUserName} geändert!\n")

            else:
                print("Benutzer mit solche Benutzername schon existiert. Überprüffen Sie die Liste der Nutzer und versuchen Sie es erneut.\n")

        elif userNameToChange == "Admin":
            print("Der Admin-Benutzername kann nicht geändert werden.\n")

        else:
            print("Benutzername nicht gefunden.\n")

    else:
        print("\nSie haben keine Berechtigung, Benutzernamen zu ändern.\n")

def userOperationsMenu(currentUserName):
    print("Willkommen zum Benutzerverwaltungsmenü!\nHier können Sie folgende Operationen durchführen:\n1: Neuer Benutzer hinterlegen\n2: Benutzer löschen\n3: Ihre Passwort ändern\n4: Benutzernamen ändern\n5: Benutzerliste ausgeben\n6: Logout\n")    #Заменить 5 на возвращение в меню на уровешь выше; возможно заменить на 0; возможно оставить 5, но добавить 0 на этом уровне для выхода из программы без возврата в меню на уровешь выше
    condition = True

    while condition:
        choice = input("Geben Sie die Nummer der gewünschten Operation ein: ")

        try:
            if choice == "1":
                create_user(currentUserName)

            elif choice == "2":
                delete_user(currentUserName)

            elif choice == "3":
                change_password(currentUserName)

            elif choice == "4":
                change_user_name(currentUserName)

            elif choice == "5":
                give_user_list()

            elif choice == "6":
                print("Logout erfolgreich!\n")
                condition = False

            else:
                print("Ungültige Eingabe. Bitte geben Sie eine Zahl zwischen 1 und 6 ein.\n")

        except Exception as e:
            print(f"Ein Fehler ist aufgetreten: {e}. Bitte versuchen Sie es erneut oder wenden Sie sich an einen Administrator.\n")
