def letter_grade_to_gpa(letter_grade):
    grade_mapping = {'A': 4.0, 'A-': 3.67, 'B+': 3.33, 'B': 3.0, 'B-': 2.67, 'C+': 2.33, 'C': 2.0, 'C-': 1.67, 'D+': 1.33, 'D': 1.0, 'F': 0.0}
    return grade_mapping.get(letter_grade.upper(), 0.0)

def calculate_cumulative_gpa(course_grades):
    total_credit_hours = 0
    total_grade_points = 0

    for course, letter_grade in course_grades:
        credit_hours = 6 
        total_credit_hours += credit_hours
        total_grade_points += letter_grade_to_gpa(letter_grade) * credit_hours

    cumulative_gpa = total_grade_points / total_credit_hours
    return cumulative_gpa

sample_courses = [
    # Write your courses and their grades
    ('Programming Principles 1', 'A'),
    ('Programming Principles 2', 'A'),
    ('Calculus 1', 'A'),
    ('Calculus 2', 'A'),
    ('Ethics', 'B'),
    ('Discreate Structures', 'B'),
    ('Literature', 'B'),
    ('Linear Algebra', 'B+'),
    ('Digital Logic Design', 'A-'),
    ('Physics', 'C'),
    ('Computer Graphics', 'C+'),
    ('Artificial Intelligence', 'A'),
    ('Operting Systems', 'C+')
]

cumulative_gpa = calculate_cumulative_gpa(sample_courses)

print(f"The cumulative GPA for the provided courses is: {cumulative_gpa:.2f}")