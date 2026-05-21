grades = ['A', 'B', 'C', 'D', 'E', 'F']     # Possible grades
grades_strength = {'A': 5, 'B': 4, 'C': 3, 'D': 2, 'E': 1, 'F': 0}      # Grade strength
cumulative_unit = 0
total_grade_point = 0

course_grades = []      # List to contain tuples of grades and unit


def calculate_gpa(courses_grades):
    """Calculates the GPA on 5 unit scale."""
    global cumulative_unit
    global total_grade_point

    for grading in courses_grades:
        # courses_grade is a list of tuples with each having two values, 
        # the first would be the grade, and the second would be the unit.
        cumulative_unit += grading[1]

        total_grade_point += grades_strength[grading[0]] * grading[1]

    gpa = round(total_grade_point / cumulative_unit, 2)

    print('Your GPA for the semester is ' + str(gpa) + '/5.0.')


try:
    course_no = int(input('How many gradable courses did you offer: '))

    i = 0
    while i < course_no:
        try:
            grade_unit_list = []
            course_grade = input('%d. Enter grade (A, B, C, D, E, or F): ' % (i + 1)).title()

            if course_grade not in grades:
                print('Invalid input.')
                continue

            grade_unit_list.append(course_grade)

            course_unit = int(input('%d. Enter course unit: ' % (i + 1)))

            # List of individual grade and unit of courses
            grade_unit_list.append(course_unit)

            # List to tuple
            grade_unit_list_tuple = tuple(grade_unit_list)

            # List of all tuples containing grades and units
            course_grades.append(grade_unit_list_tuple)

            i += 1
        except ValueError:
            print('Invalid input!')
            continue

    calculate_gpa(course_grades)

except ValueError:
    print('Invalid input!')

