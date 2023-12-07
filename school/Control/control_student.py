import Model.model_student




 #ATTENTION
def show() :
    f = open("C:/Users/ASUS/Desktop/Programs/26mordad/13mehr/studentinfo.txt", "w")
    lines = f.readlines()
    f.close()
    print(lines)
    for line in lines :
        print(line)