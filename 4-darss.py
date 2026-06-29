# logins = ["aziz", "ali", "aziz", "dilshod", "aziz", "madina"]
# logins=set(logins)
# a=len(logins)
# print(logins)
# print(f"yagona loginlar soni:{a}")

# ==========================================================

# old_customers = {"Ali", "Aziz", "Madina"}
# new_customers = {"Madina", "Bekzod", "Aziz", "Lola"}
# all=[]
# for i in new_customers:
#     if i not in old_customers:
#         all.append(i)
# print(all)

# =====================================================

# branch1 = ("olma", "banan", "shaftoli")
# branch2 = ("banan", "olma", "uzum")
# branch3 = ("shaftoli", "anjir", "banan")

# all=branch1+branch2+branch3
# print(set(all))

# =====================================

# user1 = {"coding", "music", "travel"}
# user2 = {"reading", "coding", "travel"}

# a=user1.intersection(user2)
# print(a)

# =-=========================================

# frontend = {"Aziz", "Ali", "Madina"}
# backend = {"Madina", "Dilshod", "Aziz"}

# a=frontend.intersection(backend)
# print(a)

# ============================================

# phones = ["+998901112233", "+998901112233", "+998909998877", "+998909998877", "+998901231212"]
# a=phones
# phones=set(phones)
# new=[]
# for i in phones:
#     if a.count(i)>1:
#         new.append(i)
# print(new)

# ================================================================

# files = ["data.csv", "report.pdf", "image.jpg", "data2.csv", "summary.pdf"]
# new=[]
# for i in files:
#     i=i.split(".")
#     new.append(i[1])
# print(set(new))

# ==========================================================

# emails = ["a@gmail.com", "b@gmail.com", "a@gmail.com", "c@gmail.com"]
# emails=set(emails)
# a=list(emails)
# print(a)

# ========================================================

# school1 = {"Matematika", "Fizika", "Informatika"}
# school2 = {"Fizika", "Ingliz tili", "Informatika"}

# a=school1.difference(school2)
# print(a)
# ================================================

# api1 = ["UZB", "RUS", "ENG", "GER"]
# api2 = ["ENG", "FRA", "TUR", "RUS"]

# all=api1+api2
# print(set(all))
# =====================================

# user1 = {8, 9, 10, 11, 14}
# user2 = {9, 10, 12, 14, 16}
# user3 = {10, 14, 15, 17}

# x=user1.intersection(user2,user3)
# print(x)

# ====================================

# store_a = ["laptop", "mouse", "keyboard", "monitor"]
# store_b = ["tablet", "keyboard", "monitor"]
# new=[]
# for i in store_a:
#     if store_b.count(i) == 0:
#         new.append((i))
# print(sorted(new))

# ==============================================

# students = [
#     ("Ali", "Matematika", "Ingliz tili", "Fizika"),
#     ("Madina", "Fizika", "Kimyo", "Matematika"),
#     ("Aziz", "Tarix", "Matematika", "Kimyo")
# ]
# natija=set()
# for i in students:
#     for x in i[1::]:
#         natija.add(x)
# print(natija)

# ============================================

# orders = ["osh", "lag'mon", "osh", "manti", "manti", "shashlik"]
# print(set(orders))

# =====================================================

# friends_ali = {"aziz", "madina", "bekzod", "lola"}
# friends_aziz = {"madina", "lola", "umar"}

# a=friends_ali.intersection(friends_aziz)
# print(a)

# ==================================================

# it = ("developer", "tester", "designer")
# marketing = ("designer", "copywriter", "analyst")
# finance = ("analyst", "accountant")

# all=it+marketing+finance
# all=set(all)
# print(all)

# =================================================

# price_source1 = {100, 200, 300, 400}
# price_source2 = {300, 400, 500, 600}

# a=price_source1.symmetric_difference(price_source2)
# print(a)

# =================================================

# aziz_courses = {"Python", "SQL", "Git"}
# ali_courses = {"Python", "HTML", "CSS"}
# a=aziz_courses.symmetric_difference(ali_courses)
# print(a)

# ==================================

