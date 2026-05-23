def soz(a:str):
    a = a.split()
    new = {}
    for i in a:
        new[i] = a.count(i)
    print(new)


# def harf(a:str):

#     if a.isalpha :
#         new = {}
#         for i in a:
#             new[i] = a.count(i)
#             if new[i]==1:
#                 print(new)
#             break
# natija=harf(input(">>>"))
# print   

def oy (a:str):
    b=a[4:6:]   # 12.12.2010
    x=a[:2:]
    f=a[5::]
    oy= ""
    if  b <=12 and a>0:
        if b == "01":
            oy = "yanvar"
        if b == "02":
            oy = "fevral"
        if b == "03":
            oy = "mart"
        if b == "04":
            oy = "aprel"
        if b == "05":
            oy = "may"
        if b == "06":
            oy = "iyun"
        if b == "07":
            oy = "iyul"
        if b == "08":
            oy = "avgust"
        if b == "09":
            oy = "sentabr"
        if b == "10":
            oy = "oktabr"
        if b == "11":
            oy = "noyabr"
        if b == "12":
            oy = "dekabr"
    print(f"{x}{oy}{f}yil")





def count_passing_students(grades: list[int], passingGrade: int):
    for i in grades:
        if i <= passingGrade:
            grades.remove(i)
    return grades
grades = [45, 60, 75, 30, 90]
passingGrade = int(input("kirish ball"))
natija=count_passing_students(grades,passingGrade)