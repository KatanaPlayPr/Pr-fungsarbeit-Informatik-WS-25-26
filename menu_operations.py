from user_operations import login, user_operations_menu as menu_users
from students_and_grades_operations import students_operations_menu as menu_students

def main_menu():
    current_user = login()
    if current_user == str.lower("exit"):
        print("Programm wird beendet. Auf Wiedersehen!")
    else:
        condition = True
        while condition:
            try:
                choice = input("\nWillkommen zum Hauptmenü!\nHier können Sie in die folgende Untermenüs wechseln:\n1: Benutzerverwaltungsmenü\n2: Studentenverwaltungsmenü\n0: Programm beenden\nGeben Sie die Nummer der gewünschten Operation ein: ")
                if choice == "1":
                    menu_users(current_user)
                elif choice == "2":
                    menu_students(current_user)
                elif choice == "0":
                    print("Programm wird beendet. Auf Wiedersehen!")
                    condition = False
                else:
                    print("Ungültige Eingabe. Bitte geben Sie eine Zahl zwischen 0 und 2 ein.\n")
            except Exception as e:
                print(f"Ein Fehler ist aufgetreten: {e}. Bitte versuchen Sie es erneut oder wenden Sie sich an einen Administrator.\n")
