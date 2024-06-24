import student

def main():
    student_1 = student.Student("Jimothy", "Henri", "Engineering", 97, 3.97, 390490)
    student_2 = student.Student("Eliza", "Jonns", "Education", 56, 4.35, 345487)
    student_list = []
    student_list.append(student_1)
    student_list.append(student_2)
    
    for stu in student_list:
        print(stu.print_student_data())
main()