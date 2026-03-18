import json as j

def give_student_list_sorted_alphabetically():
    students, grades = get_students_data()[1], get_students_data()[2]
    print("\nListe der Studenten (alphabetisch sortiert):")

    for student in sorted(students, key = str.lower):
        print(f"    {student}, Note: {grades[students.index(student)]:.2f}")
    print("")

def give_student_list_sorted_alphabetically_with_id():
    id, students = get_students_data()[0], get_students_data()[1]
    print("\nListe der Studenten (alphabetisch sortiert):")

    for student in sorted(students, key = str.lower):
        print(f"    {student}, Matrikelnummer: {id[students.index(student)]:.2f}")
    print("")

def give_student_list_sorted_by_id():
    id, students, grades = get_students_data()
    print("\nListe der Studenten (nach Matrikelnummer sortiert):")

    for student in sorted(students, key=lambda student: id[students.index(student)]):           #Source: https://docs.python.org/3/howto/sorting.html
        print(f"    {student}, Note: {grades[students.index(student)]:.2f}, Matrikelnummer: {id[students.index(student)]}")
    print("")

def give_student_list_sorted_by_grades():
    students, grades = get_students_data()[1], get_students_data()[2]
    print("\nListe der Studenten (nach Noten sortiert):")

    for student in sorted(students, key=lambda student: grades[students.index(student)]):       #Source: https://docs.python.org/3/howto/sorting.html
        print(f"    {student}, Note: {grades[students.index(student)]:.2f}")
    print("")

def get_students_data():
    with open('Studentendaten.json', 'r') as f:
        data = j.load(f)
        id = data["id"]
        students = data["students"]
        grades = data["grades"]
    return id, students, grades

def rewrite_students_data(id, students, grades):
    with open('Studentendaten.json', 'w') as f:
        j.dump({"id": id, "students": students, "grades": grades}, f)

def add_student(currentUserName):
    if currentUserName == str.lower("Lehrer"):
        id, students, grades = get_students_data()
        condition = True

        while condition:
            newStudentId = input("\nBitte geben Sie die Matrikelnummer des neuen Studenten ein (exit zum Beenden): ")

            if newStudentId == str.lower("exit"):
                condition = False

            else:
                try:
                    newStudentId = int(newStudentId)

                except ValueError:
                    print("\nUngültige Eingabe. Bitte geben Sie eine gültige Matrikelnummer ein.\n")
                    return

                if newStudentId not in id:
                    newStudentName = input("\nBitte geben Sie den Namen des neuen Studenten ein: ")
                    id.append(newStudentId)
                    students.append(newStudentName)
                    grades.append(0.0)

                    rewrite_students_data(id, students, grades)
                    print(f"Student {newStudentName} mit Matrikelnummer {newStudentId} wurde erfolgreich hinzugefügt.\n")

                    condition = False

                else:
                    print("\nEin Student mit dieser Matrikelnummer existiert bereits. Bitte versuchen Sie es erneut.\n")

    else:
        print("\nSie haben keine Berechtigung, einen neuen Studenten hinzuzufügen. Bitte wenden Sie sich an den Lehrer.\n")

def remove_student(currentUserName):
    if currentUserName == str.lower("Lehrer"):
        id, students, grades = get_students_data()
        condition = True

        while condition:
            give_student_list_sorted_alphabetically_with_id()

            studentIdToRemove = input("\nBitte geben Sie die Matrikelnummer des Studenten ein, den Sie entfernen möchten (exit zum Beenden): ")

            if studentIdToRemove == str.lower("exit"):
                condition = False

            else:
                try:
                    studentIdToRemove = int(studentIdToRemove)

                except ValueError:
                    print("\nUngültige Eingabe. Bitte geben Sie eine gültige Matrikelnummer ein.\n")
                    return

                if studentIdToRemove in id:
                    removedStudentName = students[id.index(studentIdToRemove)]
                    id.pop(id.index(studentIdToRemove))
                    students.pop(id.index(studentIdToRemove))
                    grades.pop(id.index(studentIdToRemove))

                    rewrite_students_data(id, students, grades)
                    print(f"Student {removedStudentName} mit Matrikelnummer {studentIdToRemove} wurde erfolgreich entfernt.\n")

                    condition = False

                else:
                    print("\nEs existiert kein Student mit dieser Matrikelnummer. Bitte versuchen Sie es erneut.\n")

    else:
        print("\nSie haben keine Berechtigung, einen Studenten zu entfernen. Bitte wenden Sie sich an den Lehrer.\n")

def change_student_name(currentUserName):
    if currentUserName == str.lower("Lehrer"):
        id, students, grades = get_students_data()
        condition = True

        while condition:
            give_student_list_sorted_alphabetically_with_id()

            studentIdToChange = input("\nBitte geben Sie die Matrikelnummer des Studenten ein, dessen Namen Sie ändern möchten (exit zum Beenden): ")

            if studentIdToChange == str.lower("exit"):
                condition = False

            else:
                try:
                    studentIdToChange = int(input("\nBitte geben Sie die Matrikelnummer des Studenten ein, dessen Namen Sie ändern möchten: "))

                except ValueError:
                    print("\nUngültige Eingabe. Bitte geben Sie eine gültige Matrikelnummer ein.\n")
                    return

                if studentIdToChange in id:
                    newStudentName = input("\nBitte geben Sie den neuen Namen des Studenten ein: ")
                    students[id.index(studentIdToChange)] = newStudentName

                    rewrite_students_data(id, students, grades)
                    print(f"Der Name des Studenten mit Matrikelnummer {studentIdToChange} wurde erfolgreich zu {newStudentName} geändert.")

                    condition = False

                else:
                    print("\nEs existiert kein Student mit dieser Matrikelnummer. Bitte versuchen Sie es erneut.\n")

    else:
        print("\nSie haben keine Berechtigung, den Namen eines Studenten zu ändern. Bitte wenden Sie sich an den Lehrer.\n")

def change_student_id(currentUserName):
    if currentUserName == str.lower("Lehrer"):
        id, students, grades = get_students_data()
        condition = True

        while condition:
            give_student_list_sorted_alphabetically_with_id()

            studentIdToChange = input("\nBitte geben Sie die aktuelle Matrikelnummer des Studenten ein, dessen Matrikelnummer Sie ändern möchten (exit zum Beenden): ")

            if studentIdToChange == str.lower("exit"):
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

def change_student_grade(currentUserName):
    if currentUserName == str.lower("Lehrer"):
        id, students, grades = get_students_data()
        condition = True

        while condition:
            give_student_list_sorted_alphabetically_with_id()

            studentIdToChange = input("\nBitte geben Sie die Matrikelnummer des Studenten ein, dessen Note Sie ändern möchten (exit zum Beenden): ")

            if studentIdToChange == str.lower("exit"):
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

def give_group_average_grade():
    grades = get_students_data()[2]

    if len(grades) > 0:
        averageGrade = sum(grades) / len(grades)
        print(f"\nDie durchschnittliche Note der Gruppe beträgt: {averageGrade:.2f}\n")

    else:
        print("\nEs sind keine Noten vorhanden, um den Durchschnitt zu berechnen.\n")

def give_group_size():
    students = get_students_data()[1]
    print(f"\nDie Anzahl der Studenten in der Gruppe beträgt: {len(students)}\n")

def void_grade(currentUserName):
    if currentUserName == str.lower("Lehrer"):
        id, students, grades = get_students_data()
        condition = True

        while condition:
            give_student_list_sorted_alphabetically_with_id()

            studentIdToVoid = input("\nBitte geben Sie die Matrikelnummer des Studenten ein, dessen Note Sie annullieren möchten (exit zum Beenden): ")

            if studentIdToVoid == str.lower("exit"):
                condition = False

            else:
                try:
                    studentIdToVoid = int(input("\nBitte geben Sie die Matrikelnummer des Studenten ein, dessen Note Sie annullieren möchten: "))

                except ValueError:
                    print("\nUngültige Eingabe. Bitte geben Sie eine gültige Matrikelnummer ein.\n")
                    return

                if studentIdToVoid in id:
                    grades[id.index(studentIdToVoid)] = 0.0

                    rewrite_students_data(id, students, grades)
                    print(f"Die Note des Studenten {students[id.index(studentIdToVoid)]} mit Matrikelnummer {studentIdToVoid} wurde erfolgreich annulliert.")

                    condition = False

                else:
                    print("\nEs existiert kein Student mit dieser Matrikelnummer. Bitte versuchen Sie es erneut.\n")

    else:
        print("\nSie haben keine Berechtigung, die Note eines Studenten zu annullieren. Bitte wenden Sie sich an den Lehrer.\n")

def get_students_note():
    id, students, grades = get_students_data()
    condition = True

    while condition:
        give_student_list_sorted_alphabetically_with_id()

        studentIdToCheck = input("\nBitte geben Sie die Matrikelnummer des Studenten ein, dessen Note Sie überprüfen möchten (exit zum Beenden): ")

        if studentIdToCheck == str.lower("exit"):
            condition = False

        else:
            try:
                studentIdToCheck = int(studentIdToCheck)

            except ValueError:
                print("\nUngültige Eingabe. Bitte geben Sie eine gültige Matrikelnummer ein.\n")
                return

            if studentIdToCheck in id:
                condition = False
                print(f"\nDie Note des Studenten {students[id.index(studentIdToCheck)]} mit Matrikelnummer {studentIdToCheck} beträgt: {grades[id.index(studentIdToCheck)]:.2f}\n")

            else:
                print("\nEs existiert kein Student mit dieser Matrikelnummer. Bitte versuchen Sie es erneut.\n")

def students_operations_menu(currentUserName):
    condition = True

    while condition:
        choice = input("\nWillkommen zum Studentenverwaltungsmenü!\nHier können Sie folgende Operationen durchführen:\n1: Student hinzufügen\n2: Student entfernen\n3: Namen eines Studenten ändern\n4: Matrikelnummer eines Studenten ändern\n5: Note eines Studenten ändern\n6: Note eines Studenten annullieren\n7: Note eines Studenten überprüfen\n8: Durchschnittsnote der Gruppe berechnen\n9: Anzahl der Studenten in der Gruppe anzeigen\n10: Liste der Studenten anzeigen\n0: Zum Hauptmenü\nGeben Sie die Nummer der gewünschten Operation ein: ")

        try:
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

            elif choice == "0":
                condition = False

            else:
                print("Ungültige Eingabe. Bitte geben Sie eine Zahl zwischen 0 und 10 ein.\n")

        except Exception as e:
            print(f"Ein Fehler ist aufgetreten: {e}. Bitte versuchen Sie es erneut oder wenden Sie sich an einen Administrator.\n")
