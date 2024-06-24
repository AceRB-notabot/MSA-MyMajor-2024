import student
from datetime import datetime
"""
Funtion to write error log file
Input: Error message
Output None
"""
def write_to_error_log(error_message):
    try:
        #open log file
        log_file = open("error_log.txt", "a")
        #write error to my log file
        log_file.write(f"{datetime.now()}: {error_message}\n")
        #close log file
        log_file.close()
    except Exception as err:
        print(err)
    return

def load_students(file_name):
    #create an empty list to store student data
    list_of_students = []
    #open the file
    stu_file = open(file_name, "r")
    #ignore the header line of the file
    stu_file.readline()
    #read each line of the file with for loop
    line_number = 1
    for line_of_data in stu_file:
        #increment line number by 1
        line_number += 1
        #split each line at the comma
        student_data = line_of_data.split(",")
        #if not raise error and skip that line
        try:
            if len(student_data) != 6:
                raise Exception(f"There is an error in your data file at line {line_number}")
        except Exception as err:
            write_to_error_log(str(err))
            continue
        #get individua values from the resulting list
        try:
            first_name = student_data[0]
            last_name = student_data[1]
            major = student_data[2]
            credit_hours = float(student_data[3])
            gpa = float(student_data[4])
            id_number = int(student_data[5])
        except Exception as err:
            write_to_error_log(str(err))
        
        new_student = student.Student(first_name, last_name, major, credit_hours, gpa, id_number)
        #append each automobile to the list of automobiles
        list_of_students.append(new_student)
    #close file and return list of automobilesdddddddwd
    stu_file.close
    return list_of_students


def main():
    #load a list of automobiles from data in a file
    student_list = load_students("students.csv")

    #print info for each vehicle in a for loop
    for stu in student_list:
        stu.print_student_data()
main()