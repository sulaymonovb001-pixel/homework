# a=[1, 2, 3]
# b=list(map(lambda x:x*3,a))
# print(b)

# ==============================

# v=[1, 2, 3, 4, 5]
# a=list(filter(lambda x:x%2 , v))
# print(a)

# ==============================

# a=["hi", "python"]
# b=list(map(lambda x:len(x) , a))
# print(b)

# ============================

# a=[0, 1, 0, -2, 5]
# b=list(filter(lambda x:x!=0 , a))
# print(b)

# ==================================

# a=[2, 5, -3]
# b=list(map(lambda x:x**2 , a))
# print(b)

# ===================================

# a=[3, -1, 0, -5, 2]
# b=list(filter(lambda x:x<0, a))
# print(b)

# ================================

# a=["a", "", "python", ""]
# b=list(filter(lambda x:x!='',a))
# print(b)

# =============================

# def x(y:int):
#     if y<0:
#         y=abs(y)
#         return y
#     else:
#         return y
# a=[-4, 0, 5]
# b=list(map(x,a))
# print(b)

# ======================

# a=["data science", "data analitika"]
# b=list(map(lambda x:x.upper(),a))
# print(b)

# =========================================

# a=[True, False, True]
# b=list(filter(lambda x :x, a))
# print(b)

# =================================

# a=['1','2','3']
# b=list(map(int,a))
# x=list(map(lambda x:x+x ,b))
# print(x[2])

# ================================

# a=[5, 12, 9, 30]
# b=list(filter(lambda x:x>10,a))
# print(b)

# ===================================

def scor(a:dict):
    b=[]
    for i in a:
        if i["score"]>0:
            b.append(i["score"])
    return b

        
a=[
  {"name": "Ali", "score": 65},
  {"name": "Vali", "score": 80},
  {"name": "Madina", "score": 72}
]
aa=scor(a)
stud=list(filter(lambda x:x>70 , aa))
g,b=stud
nat=[]
for i in a:
    if i["score"] == g:
        nat.append(i["name"])
        
for i in a:
    if i["score"] == b:
        nat.append(i["name"])
nat=str(nat)
print(nat)