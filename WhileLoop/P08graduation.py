student_name = input()

exclusion_counter = 0
year_counter = 0
grades_counter = 0

while True:
    grade = float(input())

    if grade < 4:
        exclusion_counter += 1
        if exclusion_counter > 1:
            print(f'{student_name} has been excluded at {year_counter +1 } grade')
            break
        continue

    year_counter += 1
    grades_counter += grade

    if year_counter == 12:
        average_grade = f'{grades_counter/12:.2f}'
        print(f'{student_name} graduated. Average grade: {average_grade}')
        break