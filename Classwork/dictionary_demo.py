def main():
    #list [1, 2, 4, hey, .6, list_2]
    scores=[1,4,6,7,78]
    student_names=["Alice",'Bob','Jery','Jane','Bill']
    print(scores[3])
    for index in range(len(scores)):
        print(f'{student_names[index]}: {scores[index]}')
    #create a dictionary of names and scores
    student_scores={
        "Alice":87,
        'Bob':79,
        'Jery':94,
        'Sara':90
    }
    #print bob and Sara's scores
    print(student_scores['Bob'])
    print(student_scores['Sara'])
    #get all the keys and values from the student score dictionary
    print("\n\n")
    for student in student_scores:
            print(f"{student}: {student_scores[student]}")
    #declare a car dictionary
    car={"make": "ferarri", "model":"f-50", "year": 2021, "value":500000, "engine": 4.8}
    #get all the keys and values from the car dictionary
    print("\n\n")
    for key, value in car.items():
         print(f"{key}: {value}")
main()