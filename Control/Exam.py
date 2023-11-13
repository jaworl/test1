import Model.Exam
def TakeExam() :
    studentName = input("enter student's name: ")
    lesson = input("enter the lesson's name: ")
    date = input("date: ")
    score = input("score: ")
    rank = input("rank: ")

    examRes = Model.Exam(studentName , lesson , date , score , rank)
    f = open("C:/Users/ASUS/Desktop/Programs/26mordad/13mehr/studentinfo.txt" , "w")
    f.write("Lesson: " + lesson + "\n")
    f.write("Date: " + date + "\n")
    f.write("Score: " + score + "\n")
    f.write("Rank: " + rank + "\n")
    f.close()

TakeExam()