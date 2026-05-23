# def count_passing_students(grades: list[int], passingGrade: int):
#     for i in grades:
#         if i <= passingGrade:
#             grades.remove(i)
#     return len(grades)
# grades = [45, 60, 75, 30, 90]
# passingGrade = int(input("kirish ball:"))
# natija=count_passing_students(grades,passingGrade)
# print(natija)

# =====================================================


# def ends_with_gram(words: list[str]) -> list[str]:
#     result = []
#     for i in words:
#         if i.lower().endswith("gram"):
#             result.append(i)
#     return result

# words = ["telegram", "Instagram", "hello", "program", "diagram", "world"]
# print(ends_with_gram(words))

# ======================================================

# def get_top_user(data: list[tuple[str, int]]) -> str:
#     if not data:
#         return ""

#     users = {}

#     for userid, value in data:
#         if userid not in users:
#             users[userid] = value
#         else:
#             users[userid] += value

#     max_score = max(users.values())
    
#     for k, v in users.items():
#         if v == max_score:
#             return k, v

# if "name" == "main":
#     data = [
#         ("user1", 50),
#         ("user2", 60),
#         ("user1", 40),
#         ("user3", 30)
#     ]

#     print(get_top_user(data))

# ==============================================

def format_date(date: str):
    # date = 12.12.2026
    res = ""
    if date[3:5] == "01":
        res = date.replace(date[2:6], " Yanvar ",) + " yil."
    elif date[3:5] == "02":
        res = date.replace(date[2:6], " Fevral ",) + " yil."
    elif date[3:5] == "03":
        res = date.replace(date[2:6], " Mart ",) + " yil."
    elif date[3:5] == "04":
        res = date.replace(date[2:6], " Aprel ",) + " yil."
    elif date[3:5] == "05":
        res = date.replace(date[2:6], " May ",) + " yil."
    elif date[3:5] == "06":
        res = date.replace(date[2:6], " Iyun ",) + " yil."
    elif date[3:5] == "07":
        res = date.replace(date[2:6], " Iyul ",) + " yil."
    elif date[3:5] == "08":
        res = date.replace(date[2:6], " Avgust ",) + " yil."
    elif date[3:5] == "09":
        res = date.replace(date[2:6], " Sentabr ",) + " yil."
    elif date[3:5] == "10":
        res = date.replace(date[2:6], " Oktabr ",) + " yil."
    elif date[3:5] == "11":
        res = date.replace(date[2:6], " Noyabr ",) + " yil."
    elif date[3:5] == "12":
        res = date.replace(date[2:6], " Dekabr ",) + " yil."
    else:
        return "Bunday oy mavjud emas!\n"
    return res

