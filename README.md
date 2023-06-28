# vinkay
This is our vinkay project
def GPA():
    courses = int(input("How many courses did you do this semester?: "))
    grade_points = []
    course_unit = []
    grade_point = dict([('A', 5), ('B', 4),('C',3), ('D',2),('E',1), ('F',0)])
    sum_wgp = 0
    for i in range(1,courses+1):
        course_unit_student = int(input(f"Enter the number of units for course {i}: "))
        course_unit.append(course_unit_student)
        grade_student = input(f"Enter your grade for course {i}: ").upper()
        while grade_student not in grade_point.keys():
            print("ERROR: Wrong grade! Please try again")
            grade_student = input(f"Enter your grade for course {i}: ").upper()
        grade_points.append(grade_point[grade_student])

        wgp = course_unit[i-1] * grade_points[i-1]
        sum_wgp += wgp

    gpa = (sum_wgp)/sum(course_unit)

    print(f"You have {grade_points.count(0)} carryover(s) in this semester.")
    print(f"Your GPA for this semester is: {round(gpa, 2)}")
    return round(gpa,2), sum_wgp, sum(course_unit)
