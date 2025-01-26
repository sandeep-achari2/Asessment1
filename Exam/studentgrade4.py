
def student_details():   #taking input details
    name=input("enter student name: ")
    subject1=int(input("enter Sub1 marks: "))
    subject2=int(input("enter Sub2 marks: "))
    subject3=int(input("enter Sub3 marks: "))
    subject4=int(input("enter Sub4 marks: "))
    subject5=int(input("enter Sub5 marks: ")) 
    if subject1>100 or subject2>100 or subject3>100 or subject4>100 or subject5>100: #if marks are greater than 100 print it is incorrect
        print("enter correct marks for grading")
        exit()
    return {name,subject1,subject2,subject3,subject4,subject5}

def marks_grading():   #evaluating marks,grading and percentage    
    (name,subject1,subject2,subject3,subject4,subject5)=student_details()
    total_marks=subject1+subject2+subject3+subject4+subject5
    print("Total marks:",total_marks)
    percentage=total_marks//5
    print("Percentage:",percentage)
    if percentage>89:
        return "A Grade"
    elif percentage>79:
        return "B Grade"
    elif percentage>59:
        return "C Grade"
    else:
        return "fail"
    
def main():  # main function
    print("Student Grade Calculation")
    print(marks_grading()) #calling function to print details
    
main()