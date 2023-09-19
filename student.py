import pickle
import course as crs


def add_course():


def check_file(filename):
    try:
        return load_file(filename)
    except FileNotFoundError:
        print("File doesn't exists so new file is created")
        return {}


def load_file(filename):
    with open(filename, 'rb') as file_read:
        return pickle.load(file_read)


def update_file(filename):
    with open(filename, 'wb') as file_write:
        pickle.dump(student_details, file_write)


if __name__ == '__main__':
    filename = 'studentDetails.pkl'
    course_list = crs.main()
    avl = crs.AVL()

    student_id = input("Enter the student id to proceed: ")      #unique id for student
    student_details = check_file(filename)
    
    if student_id in student_details:
        print(student_details[student_id])
    else:
        print(fr'Student id {student_id} has been created')
        student_details[student_id] = []
        update_file(filename)
    avl.get_all_course(course_list)
    print(student_details)



