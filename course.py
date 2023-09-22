class Node:
    def __init__(self, val, name, schd):
        self.course_code = val
        self.course_name = name
        self.course_schedule = schd
        self.left = None
        self.right = None
        self.height = 1


class AVL:

    def insert_node(self, root, code, name, schd):
        if root is None:
            return Node(code, name, schd)
        elif code < root.course_code:
            root.left = self.insert_node(root.left, code, name, schd)
        else:
            root.right = self.insert_node(root.right, code, name, schd)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)

        # Case 1 - Left Left
        if balance > 1 and code < root.left.course_code:
            return self.right_rotate(root)

        # Case 2 - Right Right
        if balance < -1 and code > root.right.course_code:
            return self.left_rotate(root)

        # Case 3 - Left Right
        if balance > 1 and code > root.left.course_code:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Case 4 - Right Left
        if balance < -1 and code < root.right.course_code:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def left_rotate(self, z):

        y = z.right
        x = y.left

        # Perform rotation
        y.left = z
        z.right = x

        # Update heights
        z.height = 1 + max(self.get_height(z.left),
                           self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left),
                           self.get_height(y.right))

        return y

    def right_rotate(self, z):

        y = z.left
        x = y.right

        # Perform rotation
        y.right = z
        z.left = x

        # Update heights
        z.height = 1 + max(self.get_height(z.left),
                           self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left),
                           self.get_height(y.right))

        return y

    def get_height(self, root):
        if root is None:
            return 0
        return root.height

    def get_balance(self, root):
        if root is None:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    def get_all_course(self, root, courses):
        if not root:
            return
        self.get_all_course(root.left, courses)
        courses.append([root.course_code, root.course_name, root.course_schedule])
        self.get_all_course(root.right, courses)
        return courses


def main():
    course = AVL()
    list_courses = []
    head = course.insert_node(None, 'CSC500', 'Research Methods', 'TuTh 16:00-17:15')
    head = course.insert_node(head, 'CSC501', 'Design and Analysis of Algorithm', 'TuTh 14:30-15:45')
    head = course.insert_node(head, 'CSC581', 'Advanced Software Engineering', 'Mo 12:30-2:30')
    head = course.insert_node(head, 'CSC595', 'Special topics in Computer Science', 'TuTh 12:30-14:30')
    return course.get_all_course(head, list_courses)


