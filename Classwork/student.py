#create a student class
class Student():
    #define the constructor
    def __init__(self, first_name, last_name, major, credit_hours, gpa, id_number):
        #assign class properties values
        self.__first_name = first_name
        self.__last_name = last_name
        self.__major = major
        self.__credit_hours = credit_hours
        self.__gpa = gpa
        self.__id_number = id_number

    #create get and set methods for class properties
    def get_first_name(self):
        return self.__first_name
    def set_first_name(self, new_first_name):
        if new_first_name == "":
            print("Error: Must be the new first name")
            return
        self.__first_name = new_first_name
    def get_last_name(self):
        return self.__last_name
    def set_first_name(self, new_last_name):
        if new_last_name == "":
            print("Error: Must be the new last name")
            return
        self.__last_name = new_last_name
    def get_major(self):
        return self.__major
    def set_major(self, new_major):
        if new_major == "":
            print("Error: Enter a new major")
            return
        self.__major = new_major
    def get_credit_hours(self):
        return self.__credit_hours
    def set_credit_hours(self, new_credit_hours):
        if new_credit_hours != float or new_credit_hours != int:
            print("Error: Enter the new credit hours as a number")
            return
        self.__credit_hours = new_credit_hours
    def get_gpa(self):
        return self.__gpa
    def set_gpa(self, new_gpa):
        if new_gpa != float or new_gpa != int:
            print("Error: New GPA must be a number")
            return
        self.__gpa = new_gpa
    def get_id_number(self):
        return self.__id_number
    
    def get_class_level(self):
        if self.__credit_hours in range (0, 31):
            student_class = "Freshman"
        elif self.__credit_hours in range (31, 61):
            student_class = "Sophmore"
        elif self.__credit_hours in range (61, 91):
            student_class = "Junior"
        elif self.__credit_hours >= 91:
            student_class = "Senior"
        return student_class
    
    def update_credit_hours(self, hours):
        try:
            self.__credit_hours += float(hours)
        except:
            print("Error: The hours to be added must be a number")
    
    def print_student_data(self):
        student_class = self.get_class_level()
        print(f"{self.__first_name} {self.__last_name} Major:{self.__major}\nStudent Class:{student_class} Credits:{self.__credit_hours}\n GPA:{self.__gpa} Student ID:{self.__id_number}")