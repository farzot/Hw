import os
os.system("cls")

class shape:#Object
    def __init__(self):
        print("Siz Shape clasidan object oldingiz")
    
    def draw(self,n):
        print(f"Shakllarni {n * '*'} orqali chizish")
    

class triangle(shape):
    def __init__(self):
        self.a = 0
        self.b = 0
        self.c = 0
        print("Uchburchak sinfi")
    def draw(self,a,b):
        for x in range(a):
            for j in range(b):
                if j == 0:
                    print("*",end = "")
                elif x == a-1:
                    print("*",end = " ")
                elif x == j:
                    print("*",end= "")
                else:
                    print("",end= "  ")
            print("")
class line(shape):
    def __init__(self):
        self.a = 0
        print("To'g'ri chiziq sinfi")
    def draw(self,a):
        for x in range(a):
            print("*",end= "")
class rectangle(shape):
    def __init__(self):
        self.a = 0
        self.b = 0
        print("To'rtburchak sinfi")
    def draw(self,a,b):
        for x in range(a):
            for j in range(b):
                if j == 0:
                    print("*",end = "")
                elif x == a-1:
                    print("*",end = " ")
                elif x == 0:
                    print("*",end = " ")
                elif j ==b-1:
                    print("*",end = " ")
                else:
                    print("",end= "  ")
            print("")
                
word = input("Shaklni kiriting: ")
match(word):
    case "triangle":
        uchburchak  = triangle()
        uchburchak.draw(9,9)
    case "line":
        chiziq = line()
        chiziq.draw(15)
    case "rectangle":
        rc =rectangle()
        rc.draw(10,10)
    