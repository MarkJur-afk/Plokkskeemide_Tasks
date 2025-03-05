# from time import *
# print("Enter numbers: a b c")
# a = float(input("Number a: "))
# b = float(input("Number b: "))
# c = float(input("Number c: "))

# if a > 0 and b > 0 and c > 0:
#     summ = a + b + c
#     print(f"Sum of your numbers is {summ}!")

#V5 3 task
# from ast import While


for õ in range (20):
     print(f"Sooritab eksamit {õ+1}, õpilane")
     for e in range (3):
         print(f"{e+1}. eksaam")

# print()
#V4 task2
vastus = 0
P = int(input("Siseta numbrid: "))
while True:
     arv = float(input("Siseta arv: "))
     if arv<0:
         vastus += arv
     P -= 1
     if P == 0:
         break
print(vastus)


vastus = 0
P = int(input("Siseta numbrid: "))
for i in range (P):
     arv = float(input("Siseta arv: "))
     if arv<0:
         vastus += arv
print(vastus)


#V1 task4
from time import * 

maht=int(input("Enter the number of cutlets on your scovoroda: "))
cutlets = int(input("Enter the number of cutlets: "))
aeg = 1
lahen = cutlets // maht
jaak = cutlets%maht
if jaak>0: 
    lahen+=1
print(f"Praeme. Tuleb {lahen}")
for l in range (lahen):
    if jaak>0 and l==lahen-1:
        print(f"Panni peal on {jaak} kotlet.")
    else:
        print(f"Panni peale on {maht} kotlet")
    print(f"{l+1}. lahenemine Praeme esimene pool ")
    sleep(aeg)
    print("Umberpooramine")
    print(f"{l+1}. lahenemine Praeme teine pool")
    sleep(aeg)
    print(f"Valmis!")

for i in range(1, cutlets + 1):
     print(f"robot put coltlet {i} on the grill.")
    
     print(f"First storona {i}...")
     time.sleep(time)
     print(f"swipe {i}.")
    
     print(f"Second {i}...")
     time.sleep(time)  
     print(f"Cotlets {i} ready!")

print("all cotlets is ready")

