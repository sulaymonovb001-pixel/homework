# a=["olma","banan","olma","nok","banan"]
# print(tuple(set(a)))

# ============================================

# Filial1= ["non","sut","shakar","tuxum"]
# Filial2= ["sut","tuxum","choy"]
# Filial1=set(Filial1)
# Filial2=set(Filial2)
# a=Filial1.difference(Filial2)
# b=Filial2.difference(Filial1)
# c=Filial1.intersection(Filial2)
# print(a)
# print(b)
# print(c)

# ======================================

# a=["1234567890123","abc123","12345","9876543210000"]
# b=[]
# brak=[]
# for i in a:
#     x=len(i)
#     if x>=13:
#         if i.isalpha:
#             b.append(i)
#     else:
#         brak.append(i)
# print(f"Togri:{b}")
# print(f"Brak:{brak}")

# ==========================================

# a=[(41.3,69.2), (41.3,69.2), (41.4,69.1)]
# a=sorted(set(a))
# print(a)

# =======================================

# User1= ["Ali","Vali","Sardor"]
# User2= ["Ali","Jasur","Vali"]
# User1=set(User1)
# User2=set(User2)
# a=User1.difference(User2)
# b=User2.difference(User1)
# c=User1.intersection(User2)
# print(a)
# print(b)
# print(f"Umumiy:{c}")

# ===============================

# Kirganlar= [101,102,103,104]
# Chiqqanlar= [102,104]
# Kirganlar=set(Kirganlar)
# Chiqqanlar=set(Chiqqanlar)

# a=Kirganlar.difference(Chiqqanlar)
# print(a)

# ====================================

# a="Ali va Vali maktab uchun kitob bilan keldi"
# a=a.split(" ")

# for i in a:
#     if i == "va" or i == "bilan" or i == "uchun":
#         a.remove(i)
#         print(i)
# b=len(a)
# print(f"Tozalangan={a}")
# print(f"noyob soni={b}")

# ============================================

# togri= ("A","B","C","D")
# talaba= ["A","C","C","B"]
# xato_savollar = set()
# xato_soni = 0

# for i in range(len(togri)):
#     if togri[i] != talaba[i]:
#         xato_soni += 1
#         xato_savollar.add(i + 1)

# xato_foiz = int(xato_soni / len(togri) * 100)

# print("Xato_foiz =", xato_foiz)
# print("Xato_savollar =", xato_savollar)

# ==============================================

# Asosiy= ["song1","song2","song3"]
# Sevimli= ["song2","song4"]

# Asosiy=set(Asosiy)
# Sevimli=set(Sevimli)

# a=Asosiy.intersection(Sevimli)
# b=Sevimli.difference(Asosiy)
# print(f"umumiy:{a}")
# print(f"faqat sevimli{b}")

# ==================================

# lst = [(12000000, "18:00", 1), (5000000, "15:00", 2)]

# natija = []

# for i in lst:
#     if i[0] > 10000000:
#         natija.append(i)

# natija.sort(key=lambda x: x[1], reverse=True)

# print(natija)

# ================================

# a=[20,22,25,18,30,27,21]
# b=[]
# b=min(a)
# x=max(a)
# print(f"min,max={b}{x}")
# a=sorted(a)[4::]
# print(f"Yuqori_haroratlar={a}")

# ============================

# Kitoblar= ["Python asoslari","C dasturlash","Python OOP"]
# Kalit="Python"

# for i in Kitoblar:
#     if Kalit not in i:
#         Kitoblar.remove(i)

# print(Kitoblar)

# ====================================

# a=[("Ali",90), ("Vali",85), ("Sami",80), ("Jasur",75)]
# natija=[]

# for i in a:
#     if 90 <= i[1] <= 100:
#         natija.append((i[0], "Oltin"))
#     elif 85 <= i[1] < 90:
#         natija.append((i[0], "Kumush"))
#     elif 80 <= i[1] < 85:
#         natija.append((i[0], "Bronza"))

# print(natija)

# ===============================================

a=input("parol kriting")

b=len(a)

if b >= 8:
    if a in "!" or a in "@" or a in "#" or a in  "$" or a in  "%" or a in "^" or a in  "&" or a in "*" or a in  "?" or a in "_":
        print("parol togri kritildi")
    else:
        print("Maxsus belgi yetishmaydi")
else:
    print("Uzunligi 8 tadan kam","Raqam yetishmaydi")
    