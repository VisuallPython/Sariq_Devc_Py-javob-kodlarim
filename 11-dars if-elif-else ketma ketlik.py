            # 11-DARS. if(), elif(), else(). and va or operatorlari BIR NECHTA SHARTLARNI TEKSHIRISH.


  # Foydalanuvchidan yoshini so'rab, hayvonot bog'iga kirish chiptasi narhini chiqaruvchi dastur yozamiz.
    # 1-USUL
yosh = int(input('Yoshingiz nechida? '))
if yosh<=4:
    print('Sizga kirish bepul.')
elif yosh<=12:
    print('Sizga kirish 5000 so\'m')
else:
    print('Sizga kirish 10000 so\'m')

    # 2-USUL
    
# yosh = int(input('Yoshingizni kiriting \n >>>'))
# if yosh <= 4:
#     narx = 'bepul'
# elif yosh <= 12:
#     narx = 5000
# else: 
#     narx = 10000
# print(f'Sizga kirish {narx}')


# if yosh <= 4:
#     narx = 'bepul'
# elif yosh <= 12:
#     narx = 5000
# elif yosh <= 60:
#     narx = 10000
# else:             # bu yerda else qismi majburiy emas. Foydalanmasa ham mumkin.
#     narx = 7500   #Qariyalar uchun chegirma
# print(f'Sizga kirish {narx}')


        # AND, OR OPERATORLARI
    # or operatori (yoki)
# kun = input('Bugun qanday kun \n>>>')
# if kun.lower() == 'shanba' or kun.lower() == 'yakshanba':
#     print('Bugun dam olish kuni')
# else:
#     print('Bugun ish kuni.')


    # and operatori (va)
# kun = input('Bugun qaysi kun:\n>>>')
# havo = int(input('Havo harorati qanday:\n>>>'))
# if kun.lower() == 'yakshanba' and havo >= 30:
#     print('Cho\'milishga chiqamiz.')
# elif kun.lower() == 'yakshanba' and havo < 30:
#     print('Uyda dam olamiz.')

#   Shartlarni yozishda bir nechta and or operatorlarini aralashtirib ham yozish mumkin.
# kun = input('Bugun qanday kun: \n>>>')
# havo = int(input('Havo harorati qanday; \n>>>'))
# if (kun.lower() == 'shanba' or kun.lower() == 'yakshanba') and havo >= 30:
#     print('Cho\'milishga borsak bo\'ladi')
# elif (kun.lower() == 'shanba' or kun.lower() == 'yakshanba') and havo < 30:
#     print('Bugun uyda dam olar ekanmiz.')

#   true va false
# narx = 15000
# choy = True
# salat = False
# if choy and salat:
#     narx = narx + 10000
# elif choy or salat:
#     narx = narx + 5000
# print(f'Umumiy summa: {narx}')

#   if ni o'zidan foydalanib shart tekshirish
# narx = 15000
# choy = True
# salat = True
# non = False
# shashlik = True
# osh = False
# assorti = True
# if choy:
#     print('Choy oldilar')
#     narx = narx + 2000
# if salat:
#     print('Salat oldilar')
#     narx = narx + 2500
# if non:
#     print("Non oldilar")
#     narx = narx + 3000
# if shashlik:
#     print("Shashlik oldilar")
#     narx = narx + 10000
# if osh:
#     print("Osh oldilar")
#     narx = narx + 13000
# if assorti:
#     print('Assorti ham olishdi') 
#     narx = narx + 3500
# print(f'Jami summa: {narx}')        #Yuqoridagi dasturda har bir if alohida tekshiriladi va avvalgi yoki keyingi if ga bog'liq emas.


    #   RO'YXAT TARKIBINI TEKSHIRISH _ in OPERATORI
    # in operatori yordamida biz ro'yxatning tarkibida ma'lum bir element borligini tekshirishimiz mumkin.

# ruyxat = ['osh', 'somsa', 'lag\'mon', 'manti']
# print('shurva' in ruyxat)
# print('osh' in ruyxat)


# ruyxat = ['osh', 'somsa', 'lag\'mon', 'manti', 'norin']
# buyurtma = input('Nima buyurasiz? \n>>>>')
# if buyurtma.lower() == ruyxat:
#     print('Buyurtma qabul etildi!')
# else:
#     print('Bu taom bizda mavjud emas!')


    # not in OPERATORI_ not in operatori yordamida esa biror element ro'yxatda yo'qligini tekshirishimiz mumkin.

# ruyxat = ['osh', 'somsa', 'lag\'mon', 'manti', 'norin']
# print('qaynatma' not in ruyxat)
# print('somsa' not in ruyxat)

# ruyxat = ['osh', 'somsa', 'lag\'mon', 'manti', 'norin']
# buyurtma = input('Nima buyurasiz? \n>>>>')
# if buyurtma.lower() not in ruyxat:
#     print('Bu taom bizda yo\'q ekan.')
# else:
#     print("Qabul qilindi")

#   Ikki ro'yxatning tarkibi quyidagicha tekshiriladi:
# ruyxat = ['osh', 'somsa', 'lag\'mon', 'manti', 'norin']
# buyurtmalar = ['qaynatma', 'qovurdoq', 'osh', 'norin']
# for taom in buyurtmalar:
#     if taom in ruyxat:
#         print(f'Ro\'yxatda {taom} bor.')
#     else:
#         print(f'Ro\'yxatda {taom} yo\'q ekan')


#   RO'YXAT BO'SH EMASLIGINI TEKSHIRISH
# ruyxat = ['osh', 'somsa', 'lag\'mon', 'manti', 'norin', 'biqtirma']
# buyurtmalar = ['qaynatma', 'qovurdoq', 'osh', 'norin', 'manti']
# if buyurtmalar:
#     for taom in buyurtmalar:
#         if taom in ruyxat:
#             print(f'Ro\'yxatda {taom} bor')
#         else:
#             print(f'Ro\'yxatda {taom} yo\'q.')
# else:
#     print("Buyurtmalar yo'q")


            # AMALIYOT_ Misollar yechish
#   Foydalanuvchidan juft son kiritishni so'rang. Agar foydalanuvchi juft son kiritsa "Rahmat!", agar toq son kiritsa "Bu son juft emas" degan xabarni chiqaring.
# son = int(input("Juft son kiriting: \n>>>>"))
# if son%2 == 0:
#     print("Raxmat")
# else:
#     print("Bu son juft emas!")

#   Foydalanuvchi yoshini so'rang, va muzeyga kirish uchun chipta narhini chiqaring:
# yosh = int(input("Yoshingizni kiriting: "))
# if yosh<=4 or yosh>=60:
#     print('Kirish sizga bepul.')
# elif yosh <= 18:
#     print('Sizga kirish 10000 so\'m')
# elif yosh > 18:
#     print('Sizga kirish 20000 so\'m')

#   Foydalanuvchidan ikita son kiritishni so'rang, sonlarni solishtiring va ularning teng yoki katta/kichikligi haqida xabarni chiqaring
# son1 = int(input("1-sonni kiriting: "))
# son2 = int(input("2-sonni kiriting: "))
# if son1 == son2:
#     print(f'Ular teng: {son1}={son2}')
# elif son1 > son2:
#     print(f'{son1} > {son2}')
# else:
#     print(f'{son1} < {son2}')


# mahsulot = ['anor', 'limon', 'Mandarin', 'go\'sht', 'somsa', 'guruch', 'muzqaymoq', 'olma', 'shakar', 'un', 'shokolad', 'qahva']
# savat = []
# print('Savatga kamida 5 ta mahsulot kiriting!')   
# mah1 = savat.append(input('1-mahsulotni kiriting: '))
# mah2 = savat.append(input('2-mahsulotni kiriting: '))
# mah3 = savat.append(input('3-mahsulotni kiriting: '))
# mah4 = savat.append(input('4-mahsulotni kiriting: '))
# mah5 = savat.append(input('5-mahsulotni kiriting: '))
# if savat:
#     for tovar in savat:
#         if tovar in mahsulot:
#             print(f'Do\'konimizda {tovar} bor')
#         else:
#             print(f'Do\'konimizda {tovar} yo\'q.')
# else: 
#     print('Savat bo\'sh.')



# mahsulot = ['anor', 'limon', 'mandarin', 'go\'sht', 'somsa', 'guruch', 'muzqaymoq', 'olma', 'shakar', 'un', 'shokolad', 'qahva']
# print('5 ta mahsulot kiriting!') 
# savat = []
# savat.append(input('1-mahsulotni kiriting: '))
# savat.append(input('2-mahsulotni kiriting: '))
# savat.append(input('3-mahsulotni kiriting: '))
# savat.append(input('4-mahsulotni kiriting: '))
# savat.append(input('5-mahsulotni kiriting: '))
  
# bor_mahsulotlar = []
# mavjud_emas =[]
# for tovar in savat:
#     if tovar in  mahsulot:
#         bor_mahsulotlar.append(tovar)
#     else:
#         mavjud_emas.append(tovar)
# if mavjud_emas:
#     print("Quyidagilar mavjud emas!")
#     for tovar in mavjud_emas:
#         print(tovar)
# else:
#     print('Do\'konda hamma mahsulot mavjud! ')

        # 2-USUL: 

# maxsulotlar = ['olma', 'guruch', 'qalam', 'uzum', 'ruchka', 'piyola', 'choynak', 'qalampir', 'kartoshka']      
# savat = []
# for n in range(1, 6):
#     maxsulot = savat.append(input(f'{n} - maxsulotni qo\'shing \n>>>'))

# bor_mahsulotlar = []
# mavjud_emas = []    
# for tovar in savat:
#     if tovar in maxsulotlar:
#         bor_mahsulotlar.append(tovar)
#     else:
#         mavjud_emas.append(tovar)
# if mavjud_emas:
#     print('Do\'konimizda quyidagilar yo\'q:')
#     for narsalar in mavjud_emas:
#         print(narsalar)
# else:
#     print('Hammasi mavjud.')


#   foydalanuvchilar degan ro'yxat tuzing, va kamida 5 ta login qo'shing.
# foydalanuvchilar = ['anvar', 'sobir', 'ilhom', 'murod', 'kamol', 'otabek']
# login = input('Yangi login tanlang: >>>')
# if login.lower() in foydalanuvchilar:
#     print('Bu login band. Yangi login tanlang!')
# else:
#     print('Xush kelibsiz!')


#   Foydalanuvchidan biror butun son kiritishni so'rang. Foydalanuvchi kiritgan sonni 2 da 10 gacha bo'lgan sonlardan qay biriga qoldiqsiz bo'linishini konsolga chiqaring. 
# butun_son = int(input('Ixtiyoriy butun son kiriting: >>>'))
# if butun_son % 2 == 0:
#     print(f'{butun_son} 2 ga qoldiqsiz bo\'linadi.')
# if butun_son % 3 == 0:
#     print(f'{butun_son} 3 ga qoldiqsiz bo\'linadi.')
# if butun_son % 4 == 0:
#     print(f'{butun_son} 4 ga qoldiqsiz bo\'linadi.')
# if butun_son % 5 == 0:
#     print(f'{butun_son} 5 ga qoldiqsiz bo\'linadi.')  
# if butun_son % 6 == 0:
#     print(f'{butun_son} 6 ga qoldiqsiz bo\'linadi.')  
# if butun_son % 7 == 0:
#     print(f'{butun_son} 7 ga qoldiqsiz bo\'linadi.')     
# if butun_son % 8 == 0:
#     print(f'{butun_son} 8 ga qoldiqsiz bo\'linadi.')  
# if butun_son % 9 == 0:
#     print(f'{butun_son} 9 ga qoldiqsiz bo\'linadi.') 
 
 
 
 
 
# # Maxsulot xarid qilish va uni saralash dasturi!
#
# maxsulotlar = ['olma', 'anor', 'piyoz', 'guruch', 'lavlagi', 'qalampir', 'no\'xat', 'gilos', 'piyola']
# son = int(input("Nechta maxsulot kiritasiz: "))
#
# savat = []
# for tartib in range(1, son+1):
#     savat.append(input(f'{tartib} - maxsulotni kiriting >>>'))
#
# bor_maxsulotlar = []
# mavjud_emas = []
#
# for tovar in savat:
#     if tovar in maxsulotlar:
#         bor_maxsulotlar.append(tovar)
#     else:
#         mavjud_emas.append(tovar)
#
# if mavjud_emas:
#     print(f'Bizda quyidagi maxsulotlar yo\'q.')
#     for yuq_max in mavjud_emas:
#         print(yuq_max)
# else:
#     print('Hamma maxsulot bizda mavjud.')