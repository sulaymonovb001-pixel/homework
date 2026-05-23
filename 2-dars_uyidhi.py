
# n=int(input("son kriting:"))
# n+=1
# m=1
# x = 1
# b=0
# e=0
# while m<n:
#     x = m ** m
#     print(f"{m} ^ {m} = {x} ")
#     e = b+x
#     b=e
#     print(f"{x} + {b} = {e} ")
#     m+=1

# ======================================
# n=0
# while n<=200:
#     print(n)
#     if n == 16:
#         print(f"sizning yoshingiz:{n}")
#         break
#     n+=1
      
# ==========================================


# n=100
# while n <= 999:
#     birlar=n%10
#     onlar=n//100
#     yuzlar=n%100//10
#     if birlar == onlar or birlar == yuzlar or onlar == yuzlar:
#         print(n)
#     n+=1

# ===========================================================

# import random 
# x=int(input("son kriting"))
# natija = random.randint(1,x)
# count =0
# print("son topish oyni boshlandi=>")
# while (x):
#     n=int(input("son kriting"))
#     if n == natija:
#         print("winner")
#         break
#     elif n<natija:
#         print("KATTA")
#     else:
#         print("KICHIK") 
#     count +=1    
    
#     if count == 3:
#         print("looser")
#         break

# =============================================

# yosh = int(input("Yoshni kiriting: "))
# yil = int(input("Obuna yillari sonini kiriting: "))

# narx = 15
# chegirma = 0

# if yosh > 50:
#     chegirma += 0.20
#     print("Yosh bo'yicha chegirma: 20%")
# else:
#     print("Yosh bo'yicha chegirma: 0%")

# if yil > 5:
#     chegirma += 0.15
#     print("Obuna davomiyligi bo'yicha chegirma: 15%")
# elif yil > 3:
#     chegirma += 0.10
#     print("Obuna davomiyligi bo'yicha chegirma: 10%")
# else:
#     print("Obuna davomiyligi bo'yicha chegirma: 0%")

# yakuniy = narx - (narx * chegirma)

# print(f"Asosiy narx: ${narx}")
# print(f"Yakuniy narx: ${yakuniy:.2f}")

# ========================================================

# import re

# while True:
#     parol = input("Parol kiriting: ")

#     xato = False
#     if len(parol) < 8:
#         print("Parol juda qisqa.")
#         xato = True

#     if not any(harf.isupper() for harf in parol):
#         print("Parolda katta harf yetishmayapti.")
#         xato = True

#     if not any(harf.isdigit() for harf in parol):
#         print("Parolda raqam yetishmayapti.")
#         xato = True

#     if not re.search(r'[@#$]', parol):
#         print("Parolda maxsus belgi (@, #, $) yetishmayapti.")
#         xato = True

#     if not xato:
#         print("Parol kuchli!")
#         break

# 5-masalada CHATGPTdan yordam soradm !!!

# ==============================================================

