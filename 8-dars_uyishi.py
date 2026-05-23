f=open("text.txt")
# brand={}
# for i in f.read().split("\n"):
#     x=i.split(",")[-4]
#     if x in brand:
#         brand[x]+=1
#     else:
#         brand[x]=1
# print(brand)
# eng_kop_brand = max(brand, key=brand.get)
# print(eng_kop_brand)
# print(brand[eng_kop_brand])


# -------------------------------------------------

country_count = {}

eng_kop_brand = "Ford"

for i in f.read().split("\n")[1:]:
    data = i.split(",")

    brand = data[4]
    country = data[7]

    if brand == eng_kop_brand:

        if country in country_count:
            country_count[country] += 1
        else:
            country_count[country] = 1

print(country_count)

eng_kop_davlat = max(country_count, key=country_count.get)
eng_kam_davlat = min(country_count, key=country_count.get)

f.close()