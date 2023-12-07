import Model.model_exam
def TakeExam() :
    studentName = input("enter student's name: ")
    examID = input("enter exam's ID: ")
    lesson = input("enter the lesson's name: ")
    date = input("date: ")
    score = input("score: ")
    rank = input("rank: ")

    #bayad log in yadesh bemuneh
    #teacher name

    examRes = Model.model_exam(studentName , examID , lesson , date , score , rank )
    f = open("C:/Users/ASUS/Desktop/schooool/studentinfo.txt" , "w")
    f.write("Student's name: " + studentName + "\n")
    f.write("Lesson: " + lesson + "\n")
    f.write("Date: " + date + "\n")
    f.write("Score: " + score + "\n")
    f.write("Rank: " + rank + "\n")
    f.close()
#complete
TakeExam()