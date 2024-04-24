# -----------------------------------------------------------------
#
# Title: Assignment05.py
# Desc: This assignment demonstrates assignment04 and builds on it to use
#       data processing using dictionaries and exception handling.
# Change Log: (Who, When, What)
# TMcGrew, 2024-04-21, Created script reusing code from my Assignment04
# TMcGrew, 2024-04-22, reworked all the list of lists to be list of dictionaries
#       with same functionality
# TMcGrew, 2024-04-23, reworked to save and read from a JSON file instead of a CSV,
#       put more descriptive type hints on the dict and list when declared. Reworked it
#       again to now use json module to read/write to the JSON file.
# TMcGrew, 2024-04-24, added error handling with try except finally on file read,
#       user entering first/last name, and when dictionary rows are written into file.
#       Took out where on option 3 it wouldn't save to file if student_first name was empty
#       and prompted you to go to option 1.  Doesn't matter now as always something to write
#       to file as list of dictionaries loaded upon start.  If nothing entered it just
#       resaves that info.
#
# ------------------------------------------------------------------

# imports

import json
from json import JSONDecodeError

# -- data -- #

# constants

MENU: str = "--- Course Registration Program --- \n"
MENU += "Select from the following menu: \n"
MENU += "1. Register a Student for a Course \n"
MENU += "2. Show current data \n"
MENU += "3. Save data to a file \n"
MENU += "4. Exit the program \n"
MENU += "-------------------------------"

FILE_NAME: str = "Enrollments.json"

# variables

student_first_name: str = ""
student_last_name: str = ""
course_name: str = ""
json_data: str = ""  # don't need this if using json module or you could but it should be a list then
file = None
menu_choice: str = ""
student_data: dict[str, str] = {}  # one row of student data now a dict instead of a list
students: list[dict[str, str]] = []  # table of student data (list of dictionaries)

try:

    # When the program starts, read the file data into a list of dictionaries (table)
    file = open(FILE_NAME, "r")
    # Extract the data from the file
    students = json.load(file)  # must import json above
    # now students contains the parsed JSON data as a Python list of dictionaries
    # students is the list and student are the dictionaries.

except FileNotFoundError as e:
    print("Text file must exist before running this script!\n")
    print("-- Technical Error Message -- ")
    print(e, e.__doc__, type(e), sep='\n')
    print("Creating file since it doesn't exist")
    file = open(FILE_NAME, "w")
    json.dump(students, file) #putting empty list in upon creation
except JSONDecodeError as e:
    print("-- Technical Error Message -- ")
    print(e, e.__doc__, type(e), sep='\n')
    print("Data in file isn't valid. Resetting it...")
    file = open(FILE_NAME, "w")
    json.dump(students, file) #putting empty list in upon creation
except Exception as e:
    print("There was a non-specific error!\n")
    print("-- Technical Error Message -- ")
    print(e, e.__doc__, type(e), sep='\n')
finally:
    if file.closed == False:
        file.close()

# -- present and process the data -- #

while (menu_choice != "4"):
    # Present the menu of choices
    menu_choice = input(MENU + '\n Your selection?: ')

    if (menu_choice == '1'):

        # variables capturing the input asked from the user
        try:
            student_first_name = input("Please enter your first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should not contain numbers.")

            student_last_name = input("Please enter your last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")

            course_name = input("Please enter the course name: ")

            # Add the student data to a dictionary using the student_data variable,
            # then add that dictionary to the students list to create a table of data
            # (a dictionary inside of a list).
            student_data = \
                {"FirstName": student_first_name, "LastName": student_last_name, "CourseName": course_name}
            students.append(student_data)

            # notify user to pick '3' now to fully register by saving it to a file
            print("\nThank you! Please now select '3' to save the registration to a file.\n")

        except ValueError as e:
            print(e)  # Prints the custom message
            print("-- Technical Error Message -- ")
            print(e.__doc__)
            print(e.__str__())
        except Exception as e:
            print("There was a non-specific error!\n")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep='\n')

        continue

    elif (menu_choice == '2'):

        # Present the current data
        for student in students:
            print(f"{student['FirstName']} {student['LastName']} is registered for {student['CourseName']}.")

        print("\nPlease now select '3' to save the registrations you entered to a file.\n")
        continue

    elif (menu_choice == '3'):

        try:
            # Save the data to a file
            # open() function to open a file in the desired mode ("w" for writing, "a' to append).
            file = open(FILE_NAME, "w")
            json.dump(students, file)
            # closes the file to save the information
            file.close()

            # shows user what it just wrote to the file
            for student in students:
                print(f"{student['FirstName']} {student['LastName']} is fully registered for {student['CourseName']}.")

            # print a line to get space after printing info and before menu again
            print('\n')

            continue

        except TypeError as e:
            print("Please check that the data is a valid JSON format\n")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep='\n')
        except Exception as e:
            print("-- Technical Error Message -- ")
            print("Built-In Python error info: ")
            print(e, e.__doc__, type(e), sep='\n')
        finally:
            if file.closed == False:
                file.close()

    # Stop the loop
    elif (menu_choice == '4'):
        exit()
        # break? or continue? or exit()?

    else:
        # spacing
        print()
        # They they picked something other than the options given
        print("Please pick one of the options.")
        # spacing
        print()
        continue
