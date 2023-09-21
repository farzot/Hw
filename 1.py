#Exercise-1

# class Kitob():
#     def __init__(self,nomi,muallifi,narxi,nashryoti):
#         self.nomi = nomi
#         self.muallifi = muallifi
#         self.narxi = narxi 
#         self.nashiryoti = nashryoti
#     def kiritish(self):
#         self.nomi = input("Kitob nomini kirtiting: ")
#         self.muallifi = input("Kitob mallifini kiriting: ")
#         self.narxi = input("Kitob narxini kiriting: ")
#         self.nashiryoti = input("Kitob nashryotini kiriting:")
#     def chiqarish(self):
#         print(f"Kitob nomi: {self.nomi}")
#         print(f"Kitob muallifi: {self.muallifi}")
#         print(f"Kitob narxi: {self.narxi}")
#         print(f"Kitob nashryoti: {self.nashiryoti}")

# kitoblar = []
# for _ in range(3):
#     kitob = Kitob("","","","")
#     kitob.kiritish()
#     kitoblar.append(kitob)
# for kitob in kitoblar:
#     if kitob.nashiryoti[0].upper() in "ABCDEFGH":
#         kitob.chiqarish()

#exercise-2

# import os
# class Laptop:
#     def __init__(self,nomi,rami,narxi,pros):
#         self.nomi = nomi 
#         self.rami = rami
#         self.narxi = narxi 
#         self.pros = pros

#     def inputchik(self):
#         self.nomi = input("Enter name of Compyuter: ")
#         self.rami = int(input("Enter RAM of Compyuter: "))
#         self.narxi = int(input("Enter price of Compyuter: "))
#         self.pros = input("Enter protsession of Compyuter: ")

#     def outputchik(self):
#         print(f"Kompiyuter nomi: {self.nomi}")
#         print(f"Kompiyuter RAMi: {self.rami}")
#         print(f"Kompiyuter narxi: {self.narxi}")
#         print(f"Kompiyuter protsessori: {self.pros}")

# cam = []
# for _ in range(5):
#     compyuter = Laptop("",0,0,"")
#     compyuter.inputchik()
#     cam.append(compyuter)
# for compyu in cam:
#     if compyuter.rami > 4 and compyuter.rami < 16:
#         compyu.outputchik()

