# students = {"Ali": 85, "Vali": 90, "Hasan": 78, "Husan": 88}
# search_name = "Vali"
# for i in students:
#     if i == search_name:
#         print(students[i])

# ==================================

# products = {"olma": 15000, "banan": 18000, "uzum": 22000}
# search_product = "banan"

# for i in products:
#     if i == search_product:
#         print(f"{products[i]}so'm")

# =============================================

# contacts = {"Ali": "+998901234567", "Vali": "+998911112233"}
# search_name = "Ali"

# for i in contacts:
#     if i == search_name:
#         print(contacts[i])

# =============================================

# ORTA

# =============================================

# salaries = {"Ali": 5000000, "Vali": 5500000, "Hasan": 6200000, "Madina": 4900000, "Rustam": 5800000}
# orta=0
# x=0
# for i in salaries:
#     x=x+salaries[i]

#     orta=orta+1
# natija=x/orta
# print(f"O'rtacha ish haqqi : {natija} so'm")

# =============================================

# students = {"Ali": 7, "Vali": 5, "Hasan": 12, "Madina": 9, "Husan": 6}
# bok=[]
# for name , book in students.items():
#     bok.append(book)
# a=max(bok)

# for name , book in students.items():
#     if book == a:
#         print(f"{name} - {book} ta kitob")

# ================================================

# teams = {
#     "Real Madrid": "Vinicius Jr.",
#     "Barcelona": "Pedri",
#     "Manchester City": "Erling Haaland",
#     "Bayern Munich": "Harry Kane"
# }
# search_team = "Manchester City"

# for i in teams:
#     if i == search_team:
#         print(f"{search_team} jamoasining eng yaxshi o'yinchisi: {teams[i]}")

# =====================================

# salaries = {"Dasturchi": 7000000, "Menejer": 8500000, "HR": 6000000}
# a=[]
# b=[]

# for name , salary in salaries.items():
#     a.append(name)
#     if name == "Dasturchi":
#         salary = salary + 700000
#         b.append(salary)
#     elif name == "Menejer":
#         salary = salary + 850000
#         b.append(salary)
#     else:
#         salary = salary + 600000
#         b.append(salary)
# natija=dict(zip(a,b))
# print(natija)

# =========================================

# stock = {"olma": 10, "banan": 0, "uzum": 5, "nok": 0, "shaftoli": 3}
# a=[]
# for name , i in stock.items():
#     if i == 0:
#         a.append(name)
# print(f"tugagan maxsulotlar => {a}")

# =====================================

# movies = {"Titanic": 195, "Avatar": 162, "Interstellar": 169, "The Irishman": 209}
# b=[]
# for name , i in movies.items():
#     b.append(i)

# x=max(b)

# for name ,y in movies.items():
#     b=name
#     if y == x:
#         print(f"eng uzoq davom etgan film {b} daqiqasi:{x}")

# ====================================================

grades = {
    "Ali": {"Matematika": 85, "Fizika": 90, "Ingliz tili": 78},
    "Vali": {"Matematika": 88, "Fizika": 85, "Ingliz tili": 82},
    "Hasan": {"Matematika": 92, "Fizika": 80, "Ingliz tili": 85}
}
lst=[]

for i,a in grades.items():
    for x,y in a.items():
        if x == "Matematika":
            lst.append(y)
            
lst=max(lst)

for i,a in grades.items():
    for x,y in a.items():
        if y == lst:
            print(f"matematikadan eng alochi oquvchu => {i} ball => {lst}")

# fizika

lst1=[]
for i,a in grades.items():
    for x,y in a.items():
        if x == "Fizika":
            lst1.append(y)
            
lst1=max(lst1)

for i,a in grades.items():
    for x,y in a.items():
        if y == lst1:
            print(f"Fizikadan eng alochi oquvchu => {i} ball => {lst}")


# ingiliz tili

lst2=[]
for i,a in grades.items():
    for x,y in a.items():
        if x == "Ingliz tili":
            lst2.append(y)
            
lst2=max(lst2)

for i,a in grades.items():
    for x,y in a.items():
        if y == lst2:
            print(f"Ingliz tilidaN eng alochi oquvchu => {i} ball => {lst}")