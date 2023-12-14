
def show() :
    f = open("C:/Users/ASUS/Desktop/school/studentinfo.txt", "w")
    lines = f.readlines()
    f.close()
    print(lines)
    for line in lines :
        print(line)