from user_operations import login, user_operations_menu as menu_users                   #login function imported from the subprogramm (needed for propper functionality of the programm); function for the "user" submenu imported (imported as menu_users for shorter lines and better readability)
from students_and_grades_operations import students_operations_menu as menu_students    #function for the "students" submenu imported (imported as menu_students for the same reasons)

def main_menu():    #function for initialisation of the main menu
    current_user = login()  #logs user in (for explanation of the function see "user_operations.py") and saves username for checking permissions

    if str.lower(current_user) == str.lower("exit"):   #case-insensitive cancel-sequence (I just love this wording)
        print("Programm wird beendet. Auf Wiedersehen!")    #logout message

    else:
        condition = True    #explained in "user_operations.py"

        while condition:    #same here
            try:            #and here
                choice = input("\nWillkommen zum Hauptmenü!\nHier können Sie in die folgende Untermenüs wechseln:\n1: Benutzerverwaltungsmenü\n2: Studentenverwaltungsmenü\n0: Programm beenden\nGeben Sie die Nummer der gewünschten Operation ein: ")     #asks for the users choice, in which submenu they want to go. Another long line...

                if choice == "1":
                    menu_users(current_user)    #function explained in "user_operations.py"

                elif choice == "2":
                    menu_students(current_user) #function explained in "students_and_grades_operations.py"

                elif choice == "0":     #in this case, opposed to the functions in "user_operations.py" and "students_and_grades_operations.py", "0" input is used for logout, because it is already the main menu
                    print("Programm wird beendet. Auf Wiedersehen!")    #logout message
                    condition = False

                else:
                    print("Ungültige Eingabe. Bitte geben Sie eine Zahl zwischen 0 und 2 ein.\n")   #and of course an error message for those who loves to try not intended inputs :)

            except Exception as e:
                print(f"Ein Fehler ist aufgetreten: {e}. Bitte versuchen Sie es erneut oder wenden Sie sich an einen Administrator.\n")     #for explanation see "user_operations.py"
