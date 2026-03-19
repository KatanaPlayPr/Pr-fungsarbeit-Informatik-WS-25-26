12.03.2026, 09:43: testing user management operations. Expected output: list of users, successful creation/deletion/password change messages; loop for creation/deletion
should allow to try false inputs; loop for creation/deletion should terminate on 'exit'; loop for login should allow re-login after operations; loop for login should
terminate on 'exit'. Additional test cases: try to create a user with an existing username; try to delete a non-existing user; try to change password with wrong current
password; try to login with wrong credentials. Actual reults: list of users displayed; successful creation/deletion/password change messages displayed; loop for
creation/deletion allows to try false inputs and terminates on 'exit'; loop for login allows re-login after operations and terminates on 'exit'; trying to create a user
with an existing username shows an error message; trying to delete a non-existing user shows an error message; trying to change password with wrong current password
shows an error message; trying to login with wrong credentials shows an error message.  Bug found: if two users have the same password, the user created later cannot log
in.     Bug fixed by checking the index of the username and comparing the password at that index.

16.03.2026, 12:09: testing user management operations menu.     Expected output: login and password requested, loop allows to try false inputs and terminates on 'exit',
successful login message, menu options displayed, successful operation messages.    Actual results: login and password requested; loop allows to try false inputs and
terminates on 'exit'; successful login message displayed; menu options displayed; successful operation messages displayed.

16.03.2026, 12:32: testing student management operations.   Expected output: list of students, successful creation/deletion messages; loop for creation/deletion should
allow to try false inputs; loop for creation/deletion should terminate on 'exit'.   Additional test cases: try to create a student with an existing ID; try to delete a
non-existing student.   Actual results: list of students displayed; successful creation/deletion messages displayed; loop for creation/deletion allows to try false inputs
and terminates on 'exit'; trying to create a student with an existing ID shows an error message; trying to delete a non-existing student shows an error message.

17.03.2026, 22:29: testing student management operations menu.     Expected output: login and password requested, loop allows to try false inputs and terminates on 'exit',
successful login message, menu options displayed, successful operation messages.    Actual results: login and password requested; loop allows to try false inputs and
terminates on 'exit'; successful login message displayed; menu options displayed; successful operation messages displayed.

18.03.2026, 13:10: testing main menu.     Expected output: login and password requested, loop allows to try false inputs and terminates on 'exit', successful login message,
menu options displayed. The main menu should allow to access the user management and student management menus, and should allow to log out. The user management menu and
the student management menu changed so they should not ask for login again when accessed from the main menu, also blocking the possibility to log out from the user management
menu and the student management menu, allowing to go back to the main menu instead.    Actual results: login and password requested; loop allows to try false inputs and
terminates on 'exit'; successful login message displayed; menu options displayed; main menu allows to access the user management and student management menus, and allows to
log out; user management menu and student management menu do not ask for login again when accessed from the main menu, and do not allow to log out from their menus, allowing
to go back to the main menu instead. Overall, the main menu and its submenus work as expected.

To-do: implement all of the functionality into main. Overall state 18.03.2026, 13:50: ready for submission.
Done.

18.03.2026, 16:35: testing the main file.   Expected output: equivalent to the main_menu function of the menu_operations.py.    Actual results: programm runs as intended.

State: 18.03.2026, 16:40: programm lacks descriptions and documentations, othervise ready for submission.

State: 19.03.2026, 11:08: almost ready

19.03.2026, 12:01: Bug found: exit sequences do not work as intended, because of a wrong comparison condition.      Bug fixed. sequences work as intended.
