# grades = {
#     "Ali": 85,
#     "Vali": 78,
#     "Hasan": 90
# }

# a=str(input("talaba ismini  kriting:"))
# b=int(input("talabani balini kriting:"))
# if a in grades:
#     grades[a]=b
# else:
#     grades[a]=b    
    
# print(grades)

# ===============================

# store = {
#     "olma": 5000,
#     "banan": 7000
# }

# a=str(input("mahsulot nomini kriting:"))


# if a in store:
#     print("bu mahsulot mavjud")
    
# else:
#     b=int(input("maxsulot narxini kriting:"))
#     store[a]=b
#     print(store)

# ==================================

# employees = {
#     "101": "Ali",
#     "102": "Bobur",
#     "103": "Madina"
# }

# a=str(input("xodim ID sini kriting:"))
# if a in employees:
#     employees.pop(a)
#     print("xodim ochirirldi:")
#     print(employees)
# else:
#     print("bunday ID topilmadi")
#     print(employees)

# =======================================

# prices = {
#     "Laptop": 700,
#     "Phone": 350,
#     "Camera": 500
# }

# a = max(prices.values())
# b = max(prices, key=prices.get)
# print(f"{b} narxi {a}")

# =================================

cart = {
    "olma": 3,
    "banan": 5,
    "uzum": 2
}

a=cart["olma"] + cart["banan"] + cart["uzum"]
print(f"jami mahsulotlar soni:{a}")