# while 1:   
#     try:
#         son = int(input("Son kiriting: "))
#         nat=(100 / son)
#     except ZeroDivisionError:
#         print("xato 0 kiritib bolmaydi")
#     except ValueError:
#         print("xato harf kritib bolmaydi")
#     else:
#         print(f"natija=>{nat}")
#         break
#     finally:
#         print("dastur tugadi")

# ==================================

# while 1:   
#     try:
#         son = int(input("Yoshingizni kiriting: "))
#         nat=son
#     except ValueError:
#         print("xato string kritib bolmaydi")
#     else:
#         print(f"yoshinngiz=>{nat}")
#         break
#     finally:
#         print("dastur tugadi")
# =============================================

# while 1:
#     try:
#         mevalar = ["olma", "banan", "gilos"]
#         n = int(input("Indeks kiriting: "))
#     except ValueError:
#         print("string kiritmang!!!")
#     except IndexError:
#         print("xato index kritingiz!!!")
#     else:
#         print(mevalar[n])
#         break
#     finally:
#         print("dastur tugad!!!")

# ===============================

# while  1:
#     try:
#         a=[10, 20, 30, 40]
#         b=int(input("indeks kriting"))
#         a[b]
#     except IndexError:
#         print("hato indeks kritingiz")
#     except ValueError:
#         print("hato string yozmang")
#     else:
#         print(f"natija => {a[b]}")
#         break
#     finally:
#         print("dastur tugad")

# ===================================

# while 1:
    # try:
    #     a={
    #         "Ali": 85, 
    #         "Vali": 90, 
    #         "Hasan": 78
    #        }
    #     b=input("ism kriting")
    #     for i in a:
    #         if i == b:
    #             name=i
    # except KeyError:
    #     print("xato bunday ism yoq")
    # else:
    #     print(f"natija => {name}")
    #     break
    # finally:
    #     print("dastur tugad")

# ======================================

# while 1:
#     try:
#         a=int(input("son kriting"))
#         b=a/100
#     except ZeroDivisionError:
#         print("0 ga bolinmaydi")
#     except ValueError:
#         print("Notogri son")
#     else:
#         print("Natija:", b)
#         break
#     finally:
#         print("---- dastur tugad ----")

# ===============================================

# while True:
#     try:
#         a = float(input("1-son: "))
#         b = float(input("2-son: "))
#         op = input("Amal (+ - * /): ")

#         if op == "+":
#             res = a + b
#         elif op == "-":
#             res = a - b
#         elif op == "*":
#             res = a * b
#         elif op == "/":
#             res = a / b
#         else:
#             raise ValueError("Notogri amal")

#     except ZeroDivisionError:
#         print("0 ga bolinmaydi")
#     except ValueError as e:
#         print("Xato:", e)
#     else:
#         print("Natija:", res)
#         break
#     finally:
#         print("---- dastur tugad ----")

# ================================================

