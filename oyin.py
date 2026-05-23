import random 

while 1:
    start = int(input("START >>> "))

    if start >= -100 and start <= 100:
        break
    else:
        print("START: -100 va 95 oralig'ida bo'lsin!")
        continue

while 1:
    stop = int(input("END >>> "))
    if stop >= 0 and stop <= 200:
        break
    else:
        print("STOP: -5 va 100 oralig'ida bo'lsin!")
        continue


natija = random.randint(start, stop)
count=0

print(f"START {start} dan {stop} gacha sonni top!")
x=int(input("urunishlar sonini kriting:"))
while 1:
    count+=1
    print(f"{count}-urinishingiz")
    a=int(input("Son kiriting: "))
    if a==natija:
        print("topdingiz")
        break
    elif a > natija:
        print("kichik")
    elif a < natija:
        print("katta")
    
    if count == x:
        print(f"To'g'ri javob: {natija} edi!")
        print("Yutqazdingiz!!!")
        break   
     

