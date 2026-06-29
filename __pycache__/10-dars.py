# import json

# data = {"ism": "O'tkir", "ball": 4.9, "kurs": 2}

# # 1. Oddiy konvertatsiya
# s1 = json.dumps(data)
# print(s1)
# # {"ism": "O\u2019tkir", ...}  ← ensure_ascii=True (default)

# # 2. O'zbek harflar bilan
# s2 = json.dumps(data, ensure_ascii=False)
# print(s2)
# # {"ism": "O'tkir", "ball": 4.9, "kurs": 2}  ← To'g'ri!

# # 3. Chiroyli formatlash
# s3 = json.dumps(data, indent=2, ensure_ascii=False)
# print(s3)
# # {
# #   "ism": "O'tkir",
# #   "ball": 4.9,
# #   "kurs": 2
# # }

# # 4. Kalitlarni tartiblash
# s4 = json.dumps(data, sort_keys=True, indent=2)
# print(s4)  # Kalitlar alifbo tartibida


# ================================================================

# import json

# talabalar = [
#     {"id": 1, "ism": "Alisher", "ball": 4.5, "guruh": "A1"},
#     {"id": 2, "ism": "Malika",  "ball": 4.8, "guruh": "A1"},
#     {"id": 3, "ism": "Sardor",  "ball": 3.9, "guruh": "B2"},
# ]

# with open("talabalar.json", "w", encoding="utf-8") as f:
#     json.dump(talabalar, f, indent=4, ensure_ascii=False)

# print(f"{len(talabalar)} ta talaba saqlandi")

# =====================================================

