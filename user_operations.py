import json as j    #imported JSON-module; used for saving usernames and passwords (this file), as well as students data (id, name, grade) (students_and_grades_operations.py), as one of the easier options (see Nutzerdaten.json and/or Studentendaten.json respectively); json module imported as j for more readable code and shorter code lines

def give_user_list():   #function used for displaying list of usernames in the terminal via for-loop and print commands
    userNames = get_users_data()[0]     #function explaind later, (see 11-16)
    print("\nListe der Benutzer:")

    for userName in userNames:
        print(f"    {userName}")        #tabulation and blank line (see 9) added for more readable output
    print("")

def get_users_data():   #function for internal use only; used for getting user data from the JSON file
    with open("Nutzerdaten.json", "r") as f:    #solution of form "with open(...) as f " recommended by Copilot; arguments are the name of the file (path to it if not in the same directory) and type of interaction (in this case "r" for "read"; other case: "w" for "write", see 18-20)
        data = j.load(f)    #load gets data from the file
        userNames = data["userNames"]   #saves array of usernames
        passwords = data["passwords"]   #saves array of passwords
    return userNames, passwords     #function returns arguments, which are arrays. Function added to reduce redundancies in code (same is true for the next function, see 18-20)

def rewrite_users_data(userNames, passwords):   #for the function is true the information given above; is used for rewriting user data into the JSON file
    with open("Nutzerdaten.json", "w") as f:
        j.dump({"userNames": userNames, "passwords": passwords}, f) #saves arrays, that function gets as arguments, in the JSON file mentioned before

def login():            #function for logging in; returns the username of the user who logged in, which is used for checking permissions in other functions (see 47-166)
    condition = True    #boolean variable used for following while-loop (as here, "condition" variable is used in many other functions for the same purpose throughout few files, so it will not be explained again)

    while condition:    #while-loop, that is true until the user logs in successfully or types "exit" to end the login process; used to give the user multiple tries to log in and to avoid errors in case of wrong input (as here, while-loops are used in many other functions for the same purpose throughout few files, so they will not be explained again)
        currentUserName = input("Geben Sie den Benutzername ein (exit zum Beenden): ")  #saves the username, that the user types in, in a variable to be returned by the function (see 45) and used for permission checks (see comment line 22)

        if str.lower(currentUserName) == str.lower("exit"):    #case-insensitive cancel-sequence, in case is needed to end the login process
            condition = False                       #sets "condition" (explanation see line 23) to false, breaking the loop

        elif currentUserName not in get_users_data()[0]:    #checks if user with give username exists
            print("Benutzer mit diesem Namen existiert nicht.\n")   #error message in case of non-existing username

        else:
            password = input("Geben Sie das Passwort ein: ")    #asks for password and saves it in a variable; used for checking if the password is correct 

            if password == get_users_data()[1][get_users_data()[0].index(currentUserName)]: #checks if password given by the user (see 35) is the same as the password on the same index as the "currentUserName" in lists of passwords and usernames (respectively)
                print("Login erfolgreich!\n")   #message in case of successful login
                condition = False   #see 29

            else:
                print("Login fehlgeschlagen. Bitte überprüfen Sie Ihr Passwort.\n") #error message in case of wrong password
    return currentUserName  #returns the username of the user

def create_user(currentUserName):   #function for creating new users
    if currentUserName == "Admin":  #function is available only for the Admin user to use
        userNames, passwords = get_users_data() #gets the lists of usernames and passwords to use locally in the function
        condition = True    #see 23

        while condition:    #see 25
            newUserName = input("\nGeben Sie den Benutzernamen für den neuen Nutzer ein (exit zum Beenden): ")  #asks for the username of the new user

            if str.lower(newUserName) == str.lower("exit"):    #case-insensitive cancel-sequence
                condition = False

            elif userNames.count(newUserName) == 0: #the condition only allows to add user with the username that is not currently used
                userNames.append(newUserName)
                passwords.append(input("Geben Sie das Passwort für den neuen Nutzer ein: "))    #asks for the password of the new user

                rewrite_users_data(userNames, passwords)    #saves the updated lists of usernames and passwords
                print("Nutzer erfolgreich erstellt!\n")     #success message

                condition = False

            else:
                print("Benutzer mit solche Benutzername schon existiert. Überprüffen Sie die Liste der Nutzer und versuchen Sie es erneut.\n")  #error message in case, which is opposite to cases in line 58

    else:
        print("\nSie haben keine Berechtigung, Nutzer zu erstellen.\n") #error message if user is not Admin

def delete_user(currentUserName):   #function for deleting users
    if currentUserName == "Admin":  #see 48
        give_user_list()            #displays the list of users to make it easier to choose the user to delete

        userNames, passwords = get_users_data() #see 49
        condition = True    #see 23

        while condition:    #see 25
            userNameToDelete = input("Geben Sie den Benutzernamen ein, den Sie löschen möchten (exit zum Beenden): ")   #asks for the username of the user to delete

            if str.lower(userNameToDelete) == str.lower("exit"):   #see 55
                condition = False

            elif userNameToDelete == "Admin":   #prohibits deleting Admin user for security reasons
                print("Der Admin-Benutzer kann nicht gelöscht werden.\n")   #error message

            elif userNameToDelete in userNames: #checks if the user with given username exists
                passwords.pop(userNames.index(userNameToDelete))    #deletes the "user-to-delete" password from the password list. Some redundancy was discarded by swaping the deletion of the username and password, so, whe password will be deleted, the "userNameToDelete" will still be in the "userNames" list, allowing to find the index
                userNames.pop(userNames.index(userNameToDelete))    #deletes the "user-to-delete" username from the username list

                rewrite_users_data(userNames, passwords)    #see 62
                print(f"Nutzer {userNameToDelete} erfolgreich gelöscht!\n") #success message

                condition = False

            else:
                print("Benutzername nicht gefunden.\n") #error message in case of non-existing user

    else:
        print("\nSie haben keine Berechtigung, Nutzer zu löschen.\n")   #see 71

def change_password(currentUserName):   #function for changing the password of the user; available for all users, but only for their own accounts (e.g., Admin can change only his own password, but not passwords of other users)
    userNames, passwords = get_users_data() #see 49
    condition = True    #see 23

    while condition:    #see 25
        oldPassword = input("\nGeben Sie das alte Passwort ein (exit zum Beenden): ")   #asks for the old password

        if str.lower(oldPassword) == str.lower("exit"):    #see 55
            condition = False

        else:
            newPassword = input("Geben Sie das neue Passwort ein: ")    #asks for the new password
            newPassword1 = input("Geben Sie das neue Passwort nochmal ein: ")   #asks for the new password again to avoid mistakes in typing

            if oldPassword == passwords[userNames.index(currentUserName)] and newPassword == newPassword1:  #checks if the old password is correct and if both instances of the new password are the same
                passwords[userNames.index(currentUserName)] = newPassword   #changes the old password to the new one in the list of passwords

                rewrite_users_data(userNames, passwords)    #see 62
                print("\nPasswort erfolgreich geändert!\n") #success message

                condition = False

            else:
                print("\nEtwas hat nicht geklappt. Überprüffen Sie Ihre Eingaben und versuchen Sie es erneut.\n")   #error message in case of wrong old password or different instances of the new password. The error is not specified for security reasons

def change_user_name(currentUserName):  #function for changing the username of any of the users
    userNames, passwords = get_users_data() #see 49

    if currentUserName == "Admin":  #see 48
        give_user_list()    #see 75
        condition = True    #see 23

        while condition:    #see 25
            userNameToChange = input("Geben Sie den Benutzernamen ein, den Sie ändern möchten (exit zum Beenden): ")    #asks for the username of the user, whose username is going to be changed

            if str.lower(userNameToChange) == str.lower("exit"):   #see 55
                condition = False

            elif userNameToChange == "Admin":   #see 86
                print("Der Admin-Benutzername kann nicht geändert werden.\n")   #error message

            elif userNameToChange in userNames: #see 89
                newUserName = input("Geben Sie den neuen Benutzernamen ein: ")  #asks for the new username

                if newUserName not in userNames:    #the condition only allows to change the username to the username that is not currently used
                    userNames[userNames.index(userNameToChange)] = newUserName   #changes the old username to the new one in the list of usernames; some redundancy was discarded by changing the process from deleting the old username and adding the new one to changing the old username to the new one directly. Sometimes I'm just faster then my thoughts, and when they catch up, I already forget that they exist...

                    rewrite_users_data(userNames, passwords)    #see 62
                    print(f"Benutzername {userNameToChange} erfolgreich zu {newUserName} geändert!\n")  #success message

                    condition = False

                else:
                    print("Benutzer mit solche Benutzername schon existiert. Überprüffen Sie die Liste der Nutzer und versuchen Sie es erneut.\n")  #error message in case of already existing user

            else:
                print("Benutzername nicht gefunden.\n") #error message in case of non-existing user

    else:
        print("\nSie haben keine Berechtigung, Benutzernamen zu ändern.\n")  #error message if user is not Admin

def user_operations_menu(currentUserName):  #function for the user operations menu, which is one of the two submenus in the main menu (see menu_operations.py); available for all users, but with different permissions
    condition = True    #see 23

    while condition:    #see 25
        choice = input("\nWillkommen zum Benutzerverwaltungsmenü!\nHier können Sie folgende Operationen durchführen:\n1: Neuer Benutzer erstellen\n2: Benutzer löschen\n3: Ihre Passwort ändern\n4: Benutzernamen ändern\n5: Benutzerliste ausgeben\n0: Zum Hauptmenü\nGeben Sie die Nummer der gewünschten Operation ein: ")     #asks for the user's choice. Such a long line, init?

        try:            #try-except block used to catch any unexpected errors and avoid crashing the program; also gives the user a chance to try again in case of an error
            #next lines are the implementation of the choices in the menu, calling for the function chosen by the user. All functions are explained above
            if choice == "1":
                print("\nBenutzer erstellen:")
                create_user(currentUserName)

            elif choice == "2":
                print("\nBenutzer löschen:")
                delete_user(currentUserName)

            elif choice == "3":
                print("\nPasswort ändern:")
                change_password(currentUserName)

            elif choice == "4":
                print("\nBenutzernamen ändern:")
                change_user_name(currentUserName)

            elif choice == "5":
                give_user_list()

            elif choice == "0":     #the "0" choise is used for going to the main menu via breaking the loop of current menu. For more information, see the comments to the main menu in "menu_operations.py"
                condition = False

            else:
                print("Ungültige Eingabe. Bitte geben Sie eine Zahl zwischen 0 und 5 ein.\n")   #error message in case of invalid input

        except Exception as e:
            print(f"Ein Fehler ist aufgetreten: {e}. Bitte versuchen Sie es erneut oder wenden Sie sich an einen Administrator.\n") #error message for the exceptions that could potentially break the programm
