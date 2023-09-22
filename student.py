import pickle
import course as crs
import pandas as pd
from tabulate import tabulate as table
import re


def student_login():
    student_id = input("Enter the student id to proceed: ")  # unique id for student

    if student_id in student_details:
        show_options(student_id)
        update_file(filename)
    else:
        print(f'Student id {student_id} has been created')
        student_details[student_id] = []
        show_options(student_id)
        update_file(filename)


def admin_login():
    display_course(df)
    select_course = input("Please select the course code to generate roster: ").upper()
    student_list = [student for student in student_details if select_course in student_details[student]]
    display_course(pd.DataFrame(student_list, columns=["Student ID"]))

def display_course(dataFrame):
    print(table(dataFrame, headers="keys", tablefmt="outline", showindex=False))


def show_options(id):
    options, msg, user_input = ["add", "drop", "view"], '', ''
    print(f"Welcome user {id}. Please select an option below to continue.")
    for item in options:
        msg += f'-> {item}\n'
    msg += "You selected: "
    while user_input.lower() not in options:
        if user_input:
            print("Select a valid option to continue e.g.if you want to add a course please enter add")
        user_input = input(msg)

    choice = user_input.lower()
    if choice == "add":
        add_course(id)

    elif choice == "drop":
        drop_course(id)
    else:
        view_course(id)


def check_overlap(schd1, schd2):
    enrolled_schedule = re.split("\s", schd1)
    schd1_date = re.findall("..", enrolled_schedule[0])
    schd1_time = re.split("-", enrolled_schedule[1])

    chosen_schedule = re.split("\s", schd2)
    schd2_date = re.findall("..", chosen_schedule[0])
    schd2_time = re.split("-", chosen_schedule[1])

    for date in schd1_date:
        if date in schd2_date and (schd1_time[0] <= schd2_time[0] <= schd1_time[1] or
                                   schd1_time[0] <= schd2_time[1] <= schd1_time[1]):
            return False
    return True


def add_course(id):
    courses_enrolled = student_details[id]
    add_choice, flag = '', 0
    add_df = df[~df["Code"].isin(courses_enrolled)]
    display_course(add_df)
    while add_choice.upper() not in add_df["Code"].values:
        if add_choice:
            print("Entered course code is not valid")
        add_choice = input("Please select the course code which you want to enroll -> ")
    add_choice = add_choice.upper()

    #check course overlap
    for x in courses_enrolled:
        if not check_overlap(((df[df["Code"] == x]["Schedule"]).values[0]), ((add_df[add_df["Code"] == add_choice]["Schedule"]).values[0])):
            flag = 1
            break
    if flag == 0:
        print(f"Course {add_choice} has been successfully enrolled")
        student_details[id].append(add_choice)
    else:
        print("Course cannot be enrolled since it overlaps with other course")


def drop_course(id):
    courses_enrolled = student_details[id]
    drop_df = df[df["Code"].isin(courses_enrolled)]
    display_course(drop_df)
    drop_choice = ''
    while drop_choice.upper() not in courses_enrolled:
        if drop_choice:
            print("Entered course code is not valid")
        drop_choice = input("Please select the course code which you want to drop -> ")
    drop_choice = drop_choice.upper()
    student_details[id].remove(drop_choice)
    print(f"Course {drop_choice} has been successfully dropped")


def view_course(id):
    courses_enrolled = student_details[id]
    view_df = df[df["Code"].isin(courses_enrolled)]
    display_course(view_df)


def check_file(filename):
    try:
        return load_file(filename)
    except FileNotFoundError:
        print("File doesn't exists so new file has been created")
        return {}


def load_file(filename):
    with open(filename, 'rb') as file_read:
        return pickle.load(file_read)


def update_file(filename):
    with open(filename, 'wb') as file_write:
        pickle.dump(student_details, file_write)


if __name__ == '__main__':
    filename = 'studentDetails.pkl'
    login_option = ["student", "admin"]
    login_as = ''
    course_list = crs.main()
    df = pd.DataFrame(course_list, columns=["Code", "Title", "Schedule"])
    student_details = check_file(filename)

    while login_as.lower() not in login_option:
        if login_as:
            print("Please select either student or admin to continue e.g., enter 'student'")
        login_as = input("How would you like to login (student/admin): ")
    login_as = login_as.lower()

    if login_as == 'student':
        student_login()
    else:
        admin_login()






