            # 8-dars LISTS


# cars = ['Volvo', 'Bmw', 'Lasetti', 'Audi', 'Cobalt', 'Mersedes Benz']
# cars.sort()
# print(cars)

# # Ikkita kod teng ahamiyatli!

# cars = ['Volvo', 'Bmw', 'Lasetti', 'Audi', 'Cobalt', 'Mersedes Benz']
# cars.sort(reverse=1)  # reverse=0 bo'lsa alifbo tartibida taxlaydi aks xolda 1 yoki -1 ga teng bo'lsa alifboga teskari ravishda taxlanadi.
# print(cars)


# shaharlar = ['Toshkent', 'Surxondaryo', 'Navoi', 'Berlin', 'Angliya']
# shaharlar.sort()
# print(shaharlar)


# shaharlar = ['Toshkent', 'Surxondaryo', 'Navoi', 'Berlin', 'Angliya']
# shaharlar.sort(reverse = True)  # True yoki 1 ishlatiladi
# print(shaharlar)


# # Ro'yxat ichidagi elementlarning ketma-ketligini buzmagan holda ro'yxatni tartiblash:
# noutbuk = ['igravoy', 'Atom', 'offis', 'stol kompyuter', 'shaxsiy', 'netbook', ]
# a = sorted(noutbuk)     #ro'yxat 'sorted' ichida bo'lishi kerak
# print(a, '\n')
# print(noutbuk)


# # Ro'yxat ichidagi elementlarning ketma-ketligini buzmagan holda ro'yxatni teskari tartiblash:
# noutbuk = ['igravoy', 'Atom', 'offis', 'stol kompyuter', 'shaxsiy', 'netbook', ]
# a = sorted(noutbuk, reverse=True)     #ro'yxat 'sorted' ichida bo'lishi kerak
# print(a, '\n')
# print(noutbuk)


# Yuoqridagi ikki usul bilan sonli ro'yxatlarni ham tartiblashimiz mumkin:

# sonlar = [1, 4, 5, 2, 6, 9, 11, 21, 16]
# sonlar.sort()
# print(sonlar)


# sonlar = [1, 4, 5, 2, 6, 9, 11, 21, 16]
# sonlar.sort()
# print(sonlar)
# print(sorted(sonlar, reverse=1))

# sonlar = [1, 4, 5, 2, 6, 9, 11, 21, 16]
# print(sonlar)
# sonlar.reverse()
# print(sonlar)


# mevalar = ['olma', 'behi', 'shaftoli', 'zardoli', 'ananas']
# print(mevalar)
# mevalar.reverse()
# print(mevalar)


# # Ro'yxatning uzunligini aniqlash
# mevalar = ['olma', 'behi', 'shaftoli', 'zardoli', 'ananas', 'qulipnay']
# a = len(mevalar)
# print('R\'yxat elementlari soni: ', a, 'ta.')


#         range() metodi!
# sonlar = list(range(1,11))
# print(sonlar)


#         range() yordamida qadamni ham berishimiz mumkin:
        
# Toq sonloar chiqaradi:
# sonlar = list(range(1, 20, 2))  #Toq sonlar chiqadi
# print(sonlar)
#         # listni teskari holatda ko'rish->
# sonlar.reverse()
# print(sonlar)


#             Juft sonni chiqaradi:
# sonlar = list(range(0, 21, 2))
# print(sonlar)
# sonlar.reverse()
# print(sonlar)

#             Agar sonlar ketma-ketligi 0 dan boshlansa, range(0,10) emas range(10) deb yozsak ham bo'laveradi.
# raqamlar = list(range(15))
# print(raqamlar)

#             SONLI RO'YXAT USTIDA SODDA AMALLAR 
# narxlar = [110, 200, 320, 98, 55, 452]
# a = max(narxlar)
# b = min(narxlar)
# c = sum(narxlar)
# print(f' Eng qimmat: {a}. Eng arzon: {b}. Yig\'indisi: {c}')


#             RO'YXATNI KESISH
# mashinalar = ['Bmw', 'Tayoto', 'Malibu', 'Mersedes', 'Hundai', 'Kia']
# mening_mash = mashinalar[1:4]    # 1-indeskdan boshlab 3 ta element ajratib olamiz
# print('1: ', mashinalar)
# print('2: ' ,mening_mash)


# avto = ['Bmw', 'Tayoto', 'Malibu', 'Mersedes', 'Hundai', 'Kia', 'Cobalt']
# avto1 = avto[2:]
# avto2 = avto[:5]
# print('1: ', avto1)
# print('2: ', avto2)


#             RO'YXATDAN NUSXA OLISH
# sonlar = [1, 2, 3, 4, 5] # donlar degan ro'yxat yaratamiz
# sonlar2 = sonlar # sonlar2 degan ro'yxatni sonlar ga tenglaymiz
# sonlar2.append(6) # sonlar2 ga 6 sonini qo'shamiz
# sonlar2.append(7) # sonlar2 ga 7 sonini qo'shamiz
# print("Bu sonlar ro'yxati:", sonlar)
# print("Bu sonlar2 ro'yxati:", sonlar2)


# sonlar = [1, 2, 3, 4]
# sonlar2 = sonlar[:]
# sonlar2.append(5)
# sonlar2.append(6)
# print('Bu sonlar ro\'yxat: ', sonlar)
# print('Bu sonlar2 ro\'yxat: ',sonlar2)


#             TUPLES - O'ZGARMAS RO'YXAT
            
# toys = ('bus','car','bear','dino','snake','lizard')
# print(toys[0])
# print(toys[-1])
# print(toys[2:5])
 
#     Tuple e'lon qilishda kvadrat qavslar [] o'rniga oddiy qavslar () ishlatiladi:
# harflar = ('a', 'b', 's', 'd')
# harflar[0] = 'l'
# print(harflar)      # tuple turida o'chirish, qo'shish mumkin emas!

# uyin = ('kontr', 'need for', 'horizon 5', 'call of duty', 'sniper')
# uyin2 = list(uyin)  # tuple endi oddiy list ga almashdi.
# uyin2.append('velopoyga')
# uyin2.remove('kontr')
# print(uyin2)




#             AMALIY MISOLLAR
            
#   O'zingizga ma'lum davlatlarning ro'yxatini tuzing va ro'yxatni konsolga chiqaring:
#   Ro'yxatning uzunligini konsolga chiqaring:
# davlat = ['Hindiston', 'Turkiya', 'Amerika', 'Xitoy', 'Yaponiya']
# print(davlat)
# print('Ro\'yxat uzunligi: ', len(davlat))

#   sorted() funktsiyasi yordamida ro'yxatni tartiblangan holda konsolga chiqaring.
# davlat = ['Hindiston', 'Turkiya', 'Amerika', 'Xitoy', 'Yaponiya']
# sort = sorted(davlat)
# print(sort)

#   sorted() yordamida ro'yxatni teskari tartibda konsolga chiqaring:
# davlat = ['Hindiston', 'Turkiya', 'Amerika', 'Xitoy', 'Yaponiya']
# sort = sorted(davlat, reverse=1)
# print(sort)

#   Asl ro'yxatni qaytadan konsolga chiqaring
#   reverse() metodi yordamida ro'yxatni ortidan boshlab chiqaring
# davlat = ['Hindiston', 'Turkiya', 'Amerika', 'Xitoy', 'Yaponiya']
# print(davlat)
# davlat.reverse()
# print(davlat)

#   sort() metodi yordamida ro'yxatni avval alifbo bo'yicha, keyin esa alifboga teskari tartibda konsolga chiqaring.
# davlat = ['Hindiston', 'Turkiya', 'Amerika', 'Xitoy', 'Yaponiya']
# davlat.sort()
# print(davlat)
# davlat.reverse()
# print(davlat)

#   120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzing:
#   Ro'yxatdagi sonlar yig'indisini hisoblang va konsolga chiqaring
# sonlar = list(range(120, 1200, 2))
# print('Juft sonlar: ', sonlar)
# print('Umumiy summa: ', sum(sonlar))

#   Ro'yxatdagi eng katta va eng kichik son o'rtasidagi ayirmani hisoblang va konsolga chiqaring
# sonlar = list(range(120, 1200))
# e_katta = max(sonlar)
# e_kichik = min(sonlar)
# ayirma = e_katta - e_kichik
# print("E_katta va e_kichik sonlar ayirmasi: ", ayirma)

#   Ro'yxatdagi elementlar sonini hisoblang
# sonlar = list(range(120, 1200, 2))
# qiymat = len(sonlar)
# print(qiymat)

#   Ro'yxatning boshidan, o'rtasidan va oxiridan 20 ta qiymatni konsolga chiqaring
# sonlar = list(range(120, 1200, 2))
# print('\nBoshidan: ', sonlar[:20])
# print('\nO\'rtasidan: ', sonlar[520:550])
# print('\nOxiridan: ', sonlar[-20:])


#   taomlar degan ro'yxat yarating va ichiga istalgan 5ta taomni kiriting
#   nonushta degan yangi ro'yxatga taomlardan nusxa oling
# taomlar = ['osh', 'manti', 'honim', 'qozonkabob']
# nonuchta = taomlar[:]
# print(taomlar)
# print(nonuchta)

#   #Yangi ro'yxatda faqat nonushtaga yeyiladigan taomlarni qoldiring, va qo'shimcha 2 ta taom qo'shing
# taomlar = ['osh', 'manti', 'honim', 'qozonkabob']
# nonushta = taomlar[:]
# nonushta.remove('honim')
# nonushta.remove('qozonkabob')
# nonushta.append('qovurdoq')
# nonushta.append('shirguruch')
# print('Nonushta: ', nonushta)
# print('taomlar: ', taomlar)

#   Yuqoridagi nonushta ro'yxatini o'zgarmas ro'yxatga aylantiring va nonushta[0] = "qaymoq va non" deb qiymat berib ko'ring.
# taomlar = ['osh', 'manti', 'honim', 'qozonkabob']
# nonushta = taomlar[:]
# nonushta.remove('honim')
# nonushta.remove('qozonkabob')
# nonushta.append('qovurdoq')
# nonushta.append('shirguruch')
# nonushta = tuple(nonushta)
# nonushta[0] = 'qaymoq va sut'
# print(nonushta)       