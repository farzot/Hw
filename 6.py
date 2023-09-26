import os
os.system("cls")
class Plastic_carta:
    def __init__(self,name,__karta_raqam,_karta_muddati):
        self.name=name
        self.__karta_raqam=__karta_raqam
        self._karta_muddati=_karta_muddati
        self.__parol=1111
    def __changing_parol(self):
        default_parol=int(input("Eski parolni kiriting--> " ))
        __new_parol=int(input("Yangi parolni kiriting--> "))
        if default_parol==self.__parol:
            self.__parol==__new_parol
            print("Parol o'zgartirildi! ")
        else:
            print("Iltimos eski parolni to'g'ri kiriting! ")
    def get_changing(self):
        return self.__changing_parol
    def show(self):
        print(f"\tName: {self.name}\tKarta raqam: {self.__karta_raqam}\tKarta muddati: {self._karta_muddati}\tParol: {self.__parol}\n")


plastics=[]
n=int(input("How many object you want to enter --> "))
for x in range(n):
    i=1
    nm=input(f"{i}) Name--> ")
    kr=int(input(f"{i}) Number of carta--> "))
    km=input(f"{i}) Deadline of carta-->")
    plastics.append(Plastic_carta(nm,kr,km))
    i+=1
for x in plastics:
    plastics[0].get_changing()
for x in plastics:
    x.show()



        
