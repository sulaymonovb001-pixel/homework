# a=[10000, 25000, 5000]
# nat=list(map(lambda x:x+x/100*12 , a))
# print(nat)

# =========================================

# a=["Ali, ali@gmail.com", "Vali, vali123@mail.ru", "Aziza, aziza@outlook.com"]
# nay=list(map(str.lower,a))
# print(nay)

# =================================================

# a=[("Burger", False), ("Salad", True), ("Soup", True), ("Steak", False)]

# nat = list(filter(lambda x: x[1]==True, a))

# print(nat)

# ===================================================

# a=[55, 60, 75, 90, 45]
# nat=list(filter(lambda x:x>=60 , a))
# print(nat)

# ============================================

# a=["+998901234567", "+375291234567", "+998991112233", "0901234567"]
# nat=list(filter(lambda x:x.startswith("+998") , a))
# print(nat)

# ==================================================

# a=[120, 350, 210, 500, 90]
# nat=list(map(lambda x:x/30 , a))
# print(nat) 

# ==========================================

# a=[15000, 23000, 5000, 125000]

# nat=[f"{price:,} so'm".replace("," , ",") for price in a]
# print(nat)

# =============================================

# a=[("Ali", "IT"), ("Vali", "HR"), ("Aziza", "IT"), ("Nodir", "Finance")]
# nat=list(filter(lambda x:x[1] == "IT" , a))
# print(nat)

# ======================================================

# a=[("Olma", 10000), ("Banan", 12000), ("Uzum", 15000)]
# nat=list(map(lambda x:x[1]-(x[1]/10),a))

# print(nat)

# ===============================================

a="Python dasturlash tili juda kuchli va sodda"
nat=list(filter(lambda x:len(x)>5 , a ))
print(nat)