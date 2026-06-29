# # sana="24 mart 2026"
# sana=input(">>>")
# sana=sana.split(" ")
# x=sana[1]
# y=sana[0]
# b=sana[2]
# if x == "yanvar":
#     print(f"{y}.01.{b}")
# if x == "fevral":
#     print(f"{y}.02.{b}")
# if x == "mart":
#     print(f"{y}.03.{b}")
# if x == "aprel":
#     print(f"{y}.04.{b}")
# if x == "may":
#     print(f"{y}.05.{b}")
# if x == "iyun":
#     print(f"{y}.06.{b}")
# if x == "iyul":
#     print(f"{y}.07.{b}")
# if x == "avgust":
#     print(f"{y}.08.{b}")
# if x == "sentabr":
#     print(f"{y}.09.{b}")
# if x == "oktabr":
#     print(f"{y}.10.{b}")
# if x == "noyabr":
#     print(f"{y}.11.{b}")
# if x == "dekabr":
#     print(f"{y}.12.{b}")

# =====================================

# numbers=[3 , 7 ,2 ,6 ,5 ,2 ,5 ,9 ,65 ,3 ,1 ,4 , 0 ,65 ,3 ,7]

# numbers=set(numbers)
# numbers=tuple(numbers)
# a=0
# count=0
# for i in numbers:
#     a+=i
#     count+=1
# b=a / count
# print(f"{b}=> tuplening ichdagi qiymatlarning ortacha qiymati")

# ============================================================


# import json

# products = { "olma": 12000, "banan": 18000, "shaftoli": 15000, "uzum":20000}

# mahsulot = input(">> ")
# miqdor = int(input(">>"))

# if mahsulot in products:
#     f = open('exam.json', "w")
#     data = {"mahsulot":mahsulot, "miqdor":miqdor, "narx":miqdor*products[mahsulot]}
#     json.dump(data, f, indent=3)
#     f.close()



# ============================================================

# def eng_uzun_soz_top(str:str):
#     str=str.split(" ")
#     print(f"eng_uzun_soz={max(str)}")
#     return sorted(str)

# f=open("text.txt" , "w")

# matn=input("matn kriting:")
# natija=eng_uzun_soz_top(matn)
# for i in natija: 

#     f.write(i + " ")

# f.close()

# [============================================


def takrorlangan_son(lst):
   dkt = {}
   lst2=[]
   for i in lst:
      if i not in dkt:
         dkt[i] = 1
      else:
         dkt[i] += 1
   for i in dkt:
       
       lst2.append()
   return lst2


lst = [1,1,1, 2 ,3]
natija=takrorlangan_son(lst)
print(natija)

# ====================================

