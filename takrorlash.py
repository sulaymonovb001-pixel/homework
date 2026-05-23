# lst = [True , 1 , False , "salom" , 0]
# for i in lst:
#     if str(i) == "True" or "False" == str(i):
#         print(i)

# ==============================================

# lst=["SAlom" , "dUNyo" , "pytoN"]
# count=0
# for i in lst:
#     for word in i:
#         if word.islower():
#             count+=1
# print(f"{count} ta kichik harf bor")
    
# ============================================

# lst=[12,32,643,321,8533,45,895]
# x=max(lst)
# print(x)

# ====================================

# lst=["salom","dunyo","pyton"]
# lst2=[]
# for i in lst:
#     lst2.append(i[::-1])
# print(lst2)

# =================================

# lst=["salom" , "pyton" , "bunyod" , "sulaymonov"]
# x=max(lst)
# print(x)

# ==========================================

# lst=[True , "salom" , 5 , 5.3 , False , "dunyo"]
# lst2=[]
# for i in lst:
#     lst2.append(type(i))
# print(lst2)

# ==================================================

lst=[2,54,63,1,6,9,4,2,5]
lst2=[]
for i in lst:
    if i %2==0:
        lst2.append(i)
        lst.remove(i)
for i in lst:
    x = i**3
    lst.append(x)
    lst.remove(i)
for i  in lst2:
    x = i**2
    lst2.append(x)
    lst2.remove(i)
print(lst)
print(lst2)