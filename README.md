**Student Enrollment and Course Registration**

The objective of this project is to develop a system dedicated to the management of student enrollment and course registration. This codebase has been collaboratively contributed by members of **Group 4**, comprising Tansu Diri, Chandrika Kolluri, and Vignesh Pugalenthi.

A notable feature of our project is the utilization of Python dictionaries (resembling hashmaps) to efficiently store and manage student data, coupled with the implementation of an AVL tree data structure to organize and maintain course-related information.

Here are the steps to execute the code

`Student Login`
- User can log in as a student
  >How would you like to login (student/admin): _student_

- Enter the unique ID of the student, if the ID is not found, the system will automatically create a new student ID for that entered ID.
  >Enter the student id to proceed: _vp001_

- The user is presented with a range of operations, including:
  > -> add \
    -> drop \
    -> view
  
  - **Add:** This operation facilitates the process of enrolling in a course
    > You selected: _add_ \
    #displaying available courses \
    Please select the course code which you want to enroll -> _csc501_ \
    Course CSC501 has been successfully enrolled

  - **Drop:** Use this operation to withdraw or de-enroll from a course.
    > You selected: _drop_ \
    #displaying enrolled courses \
    Please select the course code which you want to drop -> _csc501_ \
    Course CSC501 has been successfully dropped

  - **View:** This operation allows users to access and view their current schedule.
    > You selected: _view_ \
  +--------+------------------+------------------+\
| Code   | Title            | Schedule         | \
+========+==================+================+ \
| CSC500 | Research Methods | TuTh 16:00-17:15 | \
+--------+------------------+------------------+
  
`Admin Login`
- User can log in as an admin
  >How would you like to login (student/admin): _admin_

- Select the course code which will list all the enrolled students
  > Please select the course code to generate roster: csc500 \
+--------------+ \
| Student ID   | \
+==============+ \
| vp001        | \
| vp002        | \
| vp003        | \
+--------------+ \

  



    

