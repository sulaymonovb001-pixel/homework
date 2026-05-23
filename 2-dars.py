# son1=int(input("1-son kriting:"))
# son2=int(input("2-son kriting:"))
# if son1>son2:
#     print("1-son katta")
# else:
#     print("2-son katta")

# =====================================

# parol=input("parolni kriting:")
# paroll="admin123"
# if parol == paroll:
#     print("togri")
# else:
#     print("notogri")

# ==================================

# harf=input("harf kriting:")
# if harf.islower():
#     print("kichik harf")
# else:
#     print("katta harf")

# ===============================

# harf=input("harf kriting:")

# if harf in "aeuio":
#     print("kichik unli")
# elif harf in "AEIOU":
#     print("katta unli")
# elif harf.isalpha:
#     print("undosh")

# ===================================

# son=int(input("son kriting:"))
# if son<=10 and son>=0:
#     print("kichik")
# elif son>=11 and son<=100:
#     print("orta")
# else:
#     print("katta")

#  =============================

# email=input("email kiriting:")
# if email in "@":
#     print("EMAIL")
# else:
#     print("EMAIL EMAS")

# =================================

# baho=int(input("bahoyingizni  kriting:"))
# if baho >=0  and baho<=49:
#     print("F")
# elif baho >=50 and baho<=69:
#     print("C")
# elif baho >70 and baho <=89:
#     print("b")
# elif baho>=90 and baho <=100:
#     print("A")
# else:
#     print("bunday baho yoq")

# ====================================

# son= int (input("1-son kriting:"))
# son1=int (input("2-sonni  kriting:"))
# amal=input("belgi kriting :")

# if amal in '-':
#     javob =son - son 
#     print(f"{son} - {son1} = {javob}")
# elif amal in '+':
#     javob =son + son 
#     print(f"{son} + {son1} = {javob}")
# elif amal in '*':
#     javob =son * son 
#     print(f"{son} * {son1} = {javob}")
# elif amal in '/':
#     javob =son /son 
#     print(f"{son} / {son1} = {javob}")
# else:
#     print("notogori belgi kritingiz (+-/*) kirita olasiz")

# ==============================================================

# son =int(input("son kriting:"))
# count=0
# for i in range (1,son+1):
#     count=count+i
# print(f"sonlar yigindisi:{count}")

# =========================================

# import random 

# natija = random.randint(1,100)

# while (1):
#     n=int(input("son kriting"))
#     if n == natija:
#         print("TOPDINGIZ")
#         break
#     elif n<natija:
#         print("KATTA")
#     else:
#         print("KICHIK")

# ==========================================

# import random 

# count=0
# for i in range(0,5):
#     natija = random.randint(1,10)
#     count=+natija
# print(count)    

# =========================================

# odam=int(input("nechta odam bor:"))

# for i in range (odam):
#     yosh=int(input("yoshingizni kriting:"))
#     if  yosh<12:
#         print("Animatsiya yoki Oila janridagi kino  koring")
#     elif yosh>12 and yosh<=18:
#         print("Action yoki Sarguzasht janridagi kinoni koring")
#     elif yosh>18 and yosh<=60:
#         print("Drama yoki Komediya janridagi kino koring")
#     elif yosh>60:
#         print("Dokumental yoki Klassik janridag kino koring")
#     i=+1

# ==================================================================
# - Foydalanuvchidan uchta mahsulot narxini so'rang.
# - Agar jami narx $100 dan ortiq bo'lsa, 10% chegirma bering.
# - Agar jami narx $200 dan ortiq bo'lsa, 15% chegirma bering.
# - Agar jami narx $500 dan ortiq bo'lsa, 20% chegirma bering.
# - Chegirma (agar bo'lsa) bilan yakuniy narxni chop eting.
# jami = 0
# natija = 0
# chegirma = 0
# for i in range(3):
#     m = int(input(f"{i+1}-Mahsulotni qiymatini kiriting: "))
#     jami += m

# if jami >= 100 and jami <= 200:
#     natija = jami * 0.90
#     chegirma = 10
#     print(f"Narx: {natija} | {chegirma}")
# elif jami >= 200 and jami <= 500:
#     natija = jami * 0.85
#     chegirma = 15
#     print(f"Narx: {natija} | {chegirma}")
# elif jami >= 500:
#     natija = jami * 0.80
#     chegirma = 20
#     print(f"Narx: {natija} | {chegirma}")
# else:
#     print(f"Narx: {natija} | CHEGIRMA YO'Q!")

# =========================================================

# while 1:
#     tanlov = input("Selsiyni kiritinhg: ")

#     if tanlov == "exit":
#         print("DASTUR TUGADI!")
#         break

#     if tanlov.isdigit() or tanlov[0] == "-" and tanlov[1:].isdigit():
#         c = int(tanlov)
#         f = c * (9/5) + 32
#     else:
#         print("Noto'g'ri qiymat!")
#         continue

#     if f <= 32:
#         print(f"Selsius {c} | Farangeyt - {f:.2f} | Muzlash!")
#     elif f >= 32 and f <= 85:
#         print(f"Selsius {c} | Farangeyt - {f:.2f} | Yaxshi kun!")
#     else:
#         print(f"Selsius {c} | Farangeyt - {f:.2f} | Issiq!")

# ======================================================================

import random 

while 1:
    start = int(input("START >>> "))

    if start >= -100 and start <= 95:
        break
    else:
        print("START: -100 va 95 oralig'ida bo'lsin!")
        continue

while 1:
    stop = int(input("END >>> "))
    if stop >= -5 and stop <= 100:
        break
    else:
        print("STOP: -5 va 100 oralig'ida bo'lsin!")
        continue


natija = random.randint(start, stop)
count=0

print(f"START {start} dan {stop} gacha sonni top!")

while 1:
    count+=1
    print(f"{count}-urinishingiz")
    a=int(input("Son kiriting: "))
    if a==natija:
        print("topdingiz")
        break
    elif natija >= a and natija <= a+5 or natija <= a and natija >= a-5:
        print("Issiq")
    elif natija >= a and natija <= a+20 or natija <= a and natija >= a-20:
        print("Iliq")
    else:
        print("Sovuq")
    
    if count == 7:
        print(f"To'g'ri javob: {natija} edi!")
        print("Yutqazdingiz!!!")
        break   
     

