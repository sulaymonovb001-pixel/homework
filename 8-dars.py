f=open("text.txt")
# # for i in f.read().split():
# #     if i[::-1].lower() == i.lower():
# #         print(i)

# # ==========================================

# country={}
# card=[]
# # for i in f.read().split("\n"):
# #     i=i.split(",")[-1]
# #     if i not in country:
# #         country[i] = 1
# #     else:
# #         country[i] +=1
# # print(country)

# # for i in f.read().split("\n"):
# #     y=i.split(",")[1]
# #     x=i.split(",")[-1]
# #     if i == "visa":
# #         card.append(sorted(x))
# #     print(x)\

# # =====================================

# karta_raqam=[]
# davlatt=[]
# valyute=[]
# korxona=[]

# for i in f.read().split("\n"):
#     x=i.split(",")[0]
#     d=i.split(",")[-1]
#     v=i.split(",")[2]
#     k=i.split(",")[4]
#     if '0' in x and '1' in x and '2' in x and '3' in x and '4' in x and '5' in x and '6' in x and '7' in x and '8' in x  and '9' in x:
#         karta_raqam.append(x)
#         davlatt.append(d)
#         valyute.append(v)
#         korxona.append(k)
# print(f"karta raqami:{karta_raqam}")
# print(f"davlat:{davlatt}")
# print(f"valyutasi:{valyute}")
# print(f"korxonasi:{korxona}")
# f.close() 


f=open("text.txt")

# for i in f.read().split("\n"):
#     for x in i.split(",")[-2].split("-"):
#         # if x[0].isalpha() or x[1].isalpha():
#         #     continue
#         # else:
#         #     break
#         if x[0].isdigit() and x[1].isdigit():
#             break
#     else:
#         print(i)

# =================================================
country={}
for i in f.read().split("\n"):
    x =i.split(",")[0]
    g=x.split(".")[-1]

    if g not in country:
        country[g] = 1
    else:
        country[g] +=1
print(country)
f.close()
