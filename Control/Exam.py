import Model.Exam
def TakeExam() :
    studentName = input("enter student's name: ")
    examID = input("enter exam's ID: ")
    lesson = input("enter the lesson's name: ")
    date = input("date: ")
    score = input("score: ")
    rank = input("rank: ")
    teacherName = input("enter teacher's name: ")

    examRes = Model.Exam(studentName , examID , lesson , date , score , rank , teacherName)
    f = open("C:/Users/ASUS/Desktop/schooool/studentinfo.txt" , "w")
    f.write("Lesson: " + lesson + "\n")
    f.write("Date: " + date + "\n")
    f.write("Score: " + score + "\n")
    f.write("Rank: " + rank + "\n")
    f.close()
