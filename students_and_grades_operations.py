import json as j    #imported JSON-module; used for saving students' names, ids and grades (this file), as well as user data (username, password) (user_operations.py), as one of the easier options (see Studentendaten.json and/or Nutzerdaten.json respectively); json module imported as j for more readable code and shorter code lines

def give_student_list_sorted_alphabetically():  #function used for displaying list of students and their grades, in alphabetical order, in the terminal via for-loop and print commands
    students, grades = get_students_data()[1], get_students_data()[2]
    print("\nListe der Studenten (alphabetisch sortiert):")

    for student in sorted(students, key = str.lower):   #sorts students by the name, case-insensitive
        print(f"    {student}, Note: {grades[students.index(student)]:.2f}")
    print("")

def give_student_list_sorted_alphabetically_with_id():  #function used for displaying list of students and their id, in alphabetical order, in the terminal via for-loop and print commands
    id, students = get_students_data()[0], get_students_data()[1]
    print("\nListe der Studenten (alphabetisch sortiert):")

    for student in sorted(students, key = str.lower):   #sorts students by the name, case-insensitive
        print(f"    {student}, Matrikelnummer: {id[students.index(student)]:.2f}")
    print("")

def give_student_list_sorted_by_id():   #function used for displaying list of students, their grades and their ids, in order from the lowest to the highest id number, in the terminal via for-loop and print commands
    id, students, grades = get_students_data()
    print("\nListe der Studenten (nach Matrikelnummer sortiert):")

    for student in sorted(students, key=lambda student: id[students.index(student)]):   #Source: https://docs.python.org/3/howto/sorting.html
        print(f"    {student}, Note: {grades[students.index(student)]:.2f}, Matrikelnummer: {id[students.index(student)]}")
    print("")

def give_student_list_sorted_by_grades():   #function used for displaying list of students and their grades, in order from the highest (1.0) to the lowest (5.0) grade, in the terminal via for-loop and print commands
    students, grades = get_students_data()[1], get_students_data()[2]
    print("\nListe der Studenten (nach Noten sortiert):")

    for student in sorted(students, key=lambda student: grades[students.index(student)]):       #Source: https://docs.python.org/3/howto/sorting.html
        print(f"    {student}, Note: {grades[students.index(student)]:.2f}")
    print("")

def get_students_data():    #function for internal use only; used for getting students' data from the JSON file
    with open('Studentendaten.json', 'r') as f:     #json functionality in this project is explaint in the comments in "user_operations.py"
        data = j.load(f)
        id = data["id"]
        students = data["students"]
        grades = data["grades"]
    return id, students, grades

def rewrite_students_data(id, students, grades):    #function for internal use only; used for rewriting students' data into the JSON file
    with open('Studentendaten.json', 'w') as f:
        j.dump({"id": id, "students": students, "grades": grades}, f)

def add_student(currentUserName):   #function used for adding a new student to the list
    if str.lower(currentUserName) == str.lower("Lehrer"):  #allows access to the function only to the teacher; the case-insensitivity implies the possibility to add multiple teacher user with different upper-case/lower-case combination
        id, students, grades = get_students_data()
        condition = True

        while condition:
            newStudentId = input("\nBitte geben Sie die Matrikelnummer des neuen Studenten ein (exit zum Beenden): ")   #asks for the id of a new student

            if newStudentId == str.casefold("exit"):   #case-insensitive cancel-sequence
                condition = False

            else:
                try:    #since students' ids are saved as integers, the try-exept module is set up to prevent programm-breaking exceptions when changing the data type.
                    newStudentId = int(newStudentId)    #changes the id's data type to integer

                except ValueError:
                    print("\nUngültige Eingabe. Bitte geben Sie eine gültige Matrikelnummer ein.\n")    #error message in case of non-transferable to int data
                    return

                if newStudentId not in id:  #checks if such id already exists
                    newStudentName = input("\nBitte geben Sie den Namen des neuen Studenten ein: ") #asks for new student's name
                    id.append(newStudentId) #adds new student's id to the list
                    students.append(newStudentName) #adds new student's name to the list
                    grades.append(0.0)  #sets the new student's grade to 0.0

                    rewrite_students_data(id, students, grades) #updates students lists
                    print(f"Student {newStudentName} mit Matrikelnummer {newStudentId} wurde erfolgreich hinzugefügt.\n")   #success message

                    condition = False

                else:
                    print("\nEin Student mit dieser Matrikelnummer existiert bereits. Bitte versuchen Sie es erneut.\n")    #error message in case of existing id number

    else:
        print("\nSie haben keine Berechtigung, einen neuen Studenten hinzuzufügen. Bitte wenden Sie sich an den Lehrer.\n") #error message in case of unauthorised user

def remove_student(currentUserName):    #function used for deleting a student from the list
    if str.lower(currentUserName) == str.lower("Lehrer"):  #see add_student
        id, students, grades = get_students_data()
        condition = True

        while condition:
            give_student_list_sorted_alphabetically_with_id()

            studentIdToRemove = input("\nBitte geben Sie die Matrikelnummer des Studenten ein, den Sie entfernen möchten (exit zum Beenden): ") #asks for id of student wich should be deleted

            if str.lower(studentIdToRemove) == str.lower("exit"):  #case-insensitive cancel-sequence
                condition = False

            else:
                try:    #see add_student
                    studentIdToRemove = int(studentIdToRemove)

                except ValueError:
                    print("\nUngültige Eingabe. Bitte geben Sie eine gültige Matrikelnummer ein.\n")    #error message in case described in add_student
                    return

                if studentIdToRemove in id: #checks if student with such id exists
                    removedStudentName = students[id.index(studentIdToRemove)]  #saves student's name so it can be accessed even after deletion in list for success message
                    id.pop(id.index(studentIdToRemove))         #deletes student's id...
                    students.pop(id.index(studentIdToRemove))   #..., name...
                    grades.pop(id.index(studentIdToRemove))     #... and grade from the lists

                    rewrite_students_data(id, students, grades) #updates lists
                    print(f"Student {removedStudentName} mit Matrikelnummer {studentIdToRemove} wurde erfolgreich entfernt.\n") #success message

                    condition = False

                else:
                    print("\nEs existiert kein Student mit dieser Matrikelnummer. Bitte versuchen Sie es erneut.\n")    #error message in case of non-existing student id

    else:
        print("\nSie haben keine Berechtigung, einen Studenten zu entfernen. Bitte wenden Sie sich an den Lehrer.\n")   #error message in case of an unauthorised user

def change_student_name(currentUserName):   #function used for changing student's name
    if str.lower(currentUserName) == str.lower("Lehrer"):  #see add_student
        id, students, grades = get_students_data()
        condition = True

        while condition:
            give_student_list_sorted_alphabetically_with_id()

            studentIdToChange = input("\nBitte geben Sie die Matrikelnummer des Studenten ein, dessen Namen Sie ändern möchten (exit zum Beenden): ")   #asks for an id number of the studen, who's name should be changed

            if str.lower(studentIdToChange) == str.lower("exit"):  #case-insensitive cancel-sequense
                condition = False

            else:
                try:    #see add_student
                    studentIdToChange = int(studentIdToChange)

                except ValueError:
                    print("\nUngültige Eingabe. Bitte geben Sie eine gültige Matrikelnummer ein.\n")
                    return

                if studentIdToChange in id:
                    newStudentName = input("\nBitte geben Sie den neuen Namen des Studenten ein: ") #asks for the student's new name
                    students[id.index(studentIdToChange)] = newStudentName  #changes student's name in the list

                    rewrite_students_data(id, students, grades) #updates students' lists
                    print(f"Der Name des Studenten mit Matrikelnummer {studentIdToChange} wurde erfolgreich zu {newStudentName} geändert.") #success message

                    condition = False

                else:
                    print("\nEs existiert kein Student mit dieser Matrikelnummer. Bitte versuchen Sie es erneut.\n")    #error message in case of non-existing id

    else:
        print("\nSie haben keine Berechtigung, den Namen eines Studenten zu ändern. Bitte wenden Sie sich an den Lehrer.\n")    #error message in case of unauthorised user

def change_student_id(currentUserName):     #function used for changing student's id number; has same functionality as previous function, will not be explained further
    if str.lower(currentUserName) == str.lower("Lehrer"):
        id, students, grades = get_students_data()
        condition = True

        while condition:
            give_student_list_sorted_alphabetically_with_id()

            studentIdToChange = input("\nBitte geben Sie die aktuelle Matrikelnummer des Studenten ein, dessen Matrikelnummer Sie ändern möchten (exit zum Beenden): ")

            if str.lower(studentIdToChange) == str.lower("exit"):
                condition = False

            else:
                try:
                    studentIdToChange = int(input("\nBitte geben Sie die aktuelle Matrikelnummer des Studenten ein, dessen Matrikelnummer Sie ändern möchten: "))

                except ValueError:
                    print("\nUngültige Eingabe. Bitte geben Sie eine gültige Matrikelnummer ein.\n")
                    return

                if studentIdToChange in id:
                    try:
                        newStudentId = int(input("\nBitte geben Sie die neue Matrikelnummer des Studenten ein: "))

                    except ValueError:
                        print("\nUngültige Eingabe. Bitte geben Sie eine gültige Matrikelnummer ein.\n")
                        return

                    if newStudentId not in id:
                        id[id.index(studentIdToChange)] = newStudentId

                        rewrite_students_data(id, students, grades)
                        print(f"Die Matrikelnummer des Studenten {students[id.index(studentIdToChange)]} wurde erfolgreich zu {newStudentId} geändert.")

                        condition = False

                    else:
                        print("\nEin Student mit dieser neuen Matrikelnummer existiert bereits. Bitte versuchen Sie es erneut.\n")

                else:
                    print("\nEs existiert kein Student mit dieser aktuellen Matrikelnummer. Bitte versuchen Sie es erneut.\n")

    else:
        print("\nSie haben keine Berechtigung, die Matrikelnummer eines Studenten zu ändern. Bitte wenden Sie sich an den Lehrer.\n")

def change_student_grade(currentUserName):  #function used for changing student's grade; has same functionality as previous function, will not be explained further
    if str.lower(currentUserName) == str.lower("Lehrer"):
        id, students, grades = get_students_data()
        condition = True

        while condition:
            give_student_list_sorted_alphabetically_with_id()

            studentIdToChange = input("\nBitte geben Sie die Matrikelnummer des Studenten ein, dessen Note Sie ändern möchten (exit zum Beenden): ")

            if str.lower(studentIdToChange) == str.lower("exit"):
                condition = False

            else:
                try:
                    studentIdToChange = int(input("\nBitte geben Sie die Matrikelnummer des Studenten ein, dessen Note Sie ändern möchten: "))

                except ValueError:
                    print("\nUngültige Eingabe. Bitte geben Sie eine gültige Matrikelnummer ein.\n")
                    return

                if studentIdToChange in id:
                    try:
                        newGrade = float(input("\nBitte geben Sie die neue Note des Studenten ein (zwischen 1.0 und 5.0): "))

                    except ValueError:
                        print("\nUngültige Eingabe. Bitte geben Sie eine gültige Note ein.\n")
                        return

                    if 1.0 <= newGrade <= 5.0:
                        grades[id.index(studentIdToChange)] = newGrade

                        rewrite_students_data(id, students, grades)
                        print(f"Die Note des Studenten {students[id.index(studentIdToChange)]} wurde erfolgreich zu {newGrade:.2f} geändert.")

                        condition = False

                    else:
                        print("\nUngültige Note. Bitte geben Sie eine Note zwischen 1.0 und 5.0 ein.\n")

                else:
                    print("\nEs existiert kein Student mit dieser Matrikelnummer. Bitte versuchen Sie es erneut.\n")

    else:
        print("\nSie haben keine Berechtigung, die Note eines Studenten zu ändern. Bitte wenden Sie sich an den Lehrer.\n")

def give_group_average_grade():             #function used for getting the group's average grade
    grades = get_students_data()[2]

    if len(grades) > 0:
        print(f"\nDie durchschnittliche Note der Gruppe beträgt: {(sum(grades) / len(grades)):.2f}\n")  #gives user group's average grade; reduced redundancy by using the operation itself, instead of saving it in the variable beforehands

    else:
        print("\nEs sind keine Noten vorhanden, um den Durchschnitt zu berechnen.\n")   #error message in case no grades are listed

def give_group_size():  #function used for getting the number of students in the group
    students = get_students_data()[1]
    print(f"\nDie Anzahl der Studenten in der Gruppe beträgt: {len(students)}\n")   #gives user the number of students

def void_grade(currentUserName):    #function used for resetting student's grade
    if str.lower(currentUserName) == str.lower("Lehrer"):  #see add_student
        id, students, grades = get_students_data()
        condition = True

        while condition:
            give_student_list_sorted_alphabetically_with_id()

            studentIdToVoid = input("\nBitte geben Sie die Matrikelnummer des Studenten ein, dessen Note Sie annullieren möchten (exit zum Beenden): ") #asks for id number of the student, who's note should be reset

            if str.lower(studentIdToVoid) == str.lower("exit"):    #case-insensitive cancel-sequence
                condition = False

            else:
                try:    #see add_student
                    studentIdToVoid = int(studentIdToVoid)

                except ValueError:
                    print("\nUngültige Eingabe. Bitte geben Sie eine gültige Matrikelnummer ein.\n")
                    return

                if studentIdToVoid in id:   #checks if given id exists within list
                    grades[id.index(studentIdToVoid)] = 0.0 #sets grade to 0

                    rewrite_students_data(id, students, grades) #updates lists
                    print(f"Die Note des Studenten {students[id.index(studentIdToVoid)]} mit Matrikelnummer {studentIdToVoid} wurde erfolgreich annulliert.")   #success message

                    condition = False

                else:
                    print("\nEs existiert kein Student mit dieser Matrikelnummer. Bitte versuchen Sie es erneut.\n")    #error message for non-existing id number

    else:
        print("\nSie haben keine Berechtigung, die Note eines Studenten zu annullieren. Bitte wenden Sie sich an den Lehrer.\n")    #error message for an unauthorised user

def get_students_note():    #function used for viewing certain student's graade
    id, students, grades = get_students_data()  #see add_student
    condition = True

    while condition:
        give_student_list_sorted_alphabetically_with_id()

        studentIdToCheck = input("\nBitte geben Sie die Matrikelnummer des Studenten ein, dessen Note Sie überprüfen möchten (exit zum Beenden): ") #asks for id number of the student who's grade should be accessed

        if str.lower(studentIdToCheck) == str.lower("exit"):   #case-insensitive cancel-sequence
            condition = False

        else:
            try:    #see add_student
                studentIdToCheck = int(studentIdToCheck)

            except ValueError:
                print("\nUngültige Eingabe. Bitte geben Sie eine gültige Matrikelnummer ein.\n")
                return

            if studentIdToCheck in id:  #checks if given student's id exists within list
                print(f"\nDie Note des Studenten {students[id.index(studentIdToCheck)]} mit Matrikelnummer {studentIdToCheck} beträgt: {grades[id.index(studentIdToCheck)]:.2f}\n") #success message; displays student's grade
                condition = False

            else:
                print("\nEs existiert kein Student mit dieser Matrikelnummer. Bitte versuchen Sie es erneut.\n")    #error message in case of non-existing id number

def students_operations_menu(currentUserName):  #function for the students operations menu, which is one of the two submenus in the main menu (see menu_operations.py); available for all users, but with different permissions
    condition = True

    while condition:
        choice = input("\nWillkommen zum Studentenverwaltungsmenü!\nHier können Sie folgende Operationen durchführen:\n1: Student hinzufügen\n2: Student entfernen\n3: Namen eines Studenten ändern\n4: Matrikelnummer eines Studenten ändern\n5: Note eines Studenten ändern\n6: Note eines Studenten annullieren\n7: Note eines Studenten überprüfen\n8: Durchschnittsnote der Gruppe berechnen\n9: Anzahl der Studenten in der Gruppe anzeigen\n10: Liste der Studenten anzeigen\n0: Zum Hauptmenü\nGeben Sie die Nummer der gewünschten Operation ein: ")   #asks for the users choice of operation. This one is gotta be the longest line in the whole programm

        try:    #try-except block used to catch any unexpected errors and avoid crashing the program; also gives the user a chance to try again in case of an error
            #next lines are the implementation of the choices in the menu, calling for the function chosen by the user. All functions are explained above
            if choice == "1":
                print("\nStudent hinzufügen:")
                add_student(currentUserName)

            elif choice == "2":
                print("\nStudent entfernen:")
                remove_student(currentUserName)

            elif choice == "3":
                print("\nNamen eines Studenten ändern:")
                change_student_name(currentUserName)

            elif choice == "4":
                print("\nMatrikelnummer eines Studenten ändern:")
                change_student_id(currentUserName)

            elif choice == "5":
                print("\nNote eines Studenten ändern:")
                change_student_grade(currentUserName)

            elif choice == "6":
                print("\nNote eines Studenten annullieren:")
                void_grade(currentUserName)

            elif choice == "7":
                print("\nNote eines Studenten überprüfen:")
                get_students_note()

            elif choice == "8":
                print("\nDurchschnittsnote der Gruppe berechnen:")
                give_group_average_grade()

            elif choice == "9":
                print("\nAnzahl der Studenten in der Gruppe anzeigen:")
                give_group_size()

            elif choice == "10":
                cond = True

                while cond:
                    choice_list = input("\nMöchten Sie die Liste der Studenten alphabetisch sortiert (1), nach Matrikelnummer sortiert (2) oder nach Noten sortiert (3) anzeigen? Geben Sie die entsprechende Zahl ein: ")

                    if choice_list == "1":
                        give_student_list_sorted_alphabetically()
                        cond = False

                    elif choice_list == "2":
                        give_student_list_sorted_by_id()
                        cond = False

                    elif choice_list == "3":
                        give_student_list_sorted_by_grades()
                        cond = False

                    else:
                        print("\nUngültige Eingabe. Bitte geben Sie 1, 2 oder 3 ein.\n")

            elif choice == "0":     #the "0" choise is used for going to the main menu via breaking the loop of current menu. For more information, see the comments to the main menu in "menu_operations.py"
                condition = False

            else:
                print("Ungültige Eingabe. Bitte geben Sie eine Zahl zwischen 0 und 10 ein.\n")  #error message in case of invalid input

        except Exception as e:
            print(f"Ein Fehler ist aufgetreten: {e}. Bitte versuchen Sie es erneut oder wenden Sie sich an einen Administrator.\n") #error message for the exceptions that could potentially break the programm
