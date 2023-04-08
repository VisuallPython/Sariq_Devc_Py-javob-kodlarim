            # 10-dars. 'If' va 'else' Tarmoqlanish operatori


# mashinalar = ['audi', 'mersedes', 'kia', 'bmw', 'nexia', 'malibu']
# for mashina in mashinalar:
#     if mashina == 'bmw':
#         print(mashina.upper())
#     else:
#         print(mashina.title())


        # MATNLARNI SOLISHTIRISH

# Agar ikki qiymatning teng emasligini tekshirish talab qilinsa, != operatoridan foydalanilamiz. 

#   1-USUL:
# ism = input('Ismingiz kim?\n>>>')
# if ism.lower() != 'ali':              # shartda 'ali' kata harfda bo'lishi kk
#     print(f'Kechirasiz {ism.title()}, biz Alini kutyapmiz.')
# else:
#     print('Salom, Ali.')


#   2-USUL:
# ism = input('Ismingiz kim?\n>>>')
# if ism.title() == 'Ali':          # bunda esa katta bo'lishi kk
#     print('Salom, Ali.')
# else:
#     print(f'Uzur {ism.lower()}, biz Alini kutyapmiz.')


#   SONLARNI SOLISHTIRISH

# son = float(input('6*9 nechiga teng?\n>>>'))
# if son == 54: print('javob to\'g\'ri!')
# else: print('Javob xato!')

#   2-USUL: 
# son = float(input('6*9 nechiga teng?\n>>>'))
# if son != 54: 
#     print('Javob xato!')
# else: 
#     print('Javob to\'g\'ri!')


#   Yoshni aniqlash dasturi:
# yoshingiz = int(input('Yoshingiz nechida?\n>>>'))
# if yoshingiz >= 18: 
#     print('Xush kelibsiz.') 
# else:
#     print('Kirish mumkin emas.')  


#   Login tanlash dasturi:
# login = input('Login yarating: \n>>>')
# if len(login) < 5:
#     print('Kechirasiz login 5 yoki undan ortiq bo\'lishi kerak')
# else:
#     print('Qabul qilindi!')

#   Sonlarni solishtirishda arifmetik ifodalardan foydalanish:
# yilingiz = int(input('Tug\'ilgan yilingizni ayting \n>>>'))
# if 2023 - yilingiz < 18:
#     print(f'kechirasiz yoshingiz {2023-yilingiz} da ekan! \nKira olmaysiz.')
# else:
#     print(f'Yoshingiz {2023-yilingiz} da ekan.😊\nXush kelibsiz!')

#   Bir qator if va else  1-USUL:
# yosh = input('Yoshingiz nechida: ')
# if int(yosh) > 40: print('Xush kelibsiz')
# else: print('Afsuski mumkinmas.')

#   2-USUL:
# x, y = 30, 45
# print('x > y') if x > y else print('x < y')



""" AMALIYOT UCHUN MISOLLAR """
            
#   Yangi cars  degan ro'yxat tuzing, ro'yxat elementlarining birinchi harfini katta qilib konsolga chqaring. GM uchun ikkala harfni katta qiling.
# cars = ['toyota', 'hundai', 'mersedes', 'gm', 'captiva']
# for mashina in cars:
#     if mashina == 'gm':
#         print(mashina.upper())
#     else:
#         print(mashina.title())


#   Yuqoridagi mashqni teng emas (!=) operatori yordamida bajaring. 
# cars = ['toyota', 'hundai', 'mersedes', 'gm', 'captiva']
# for mashina in cars:
#     if mashina != 'gm':
#         print(mashina.title())
#     else:
#         print(mashina.upper())


#   Foydalanuvchi login ismini so'rang. Agar login admin bo'lsa, "Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?" xabarini konsolga chiqaring. Aks holda, "Xush kelibsiz, {foydalanuvchi_ismi}!"  matnini konsolga chiqaring.
# ism = input('Login kiriting? \n>>>')
# if ism.lower() == 'admin':
#     print(f'Xush kelibsiz, {ism.title()}. Foydalanuvchilar ro\'yxatini ko\'rasizmi? ')
# else:
#     print(f'Xush kelibsiz {ism}')


#   Foydalanuvchidan 2 ta son kiritishni so'rang. Agar ikki son bir-biriga teng bo'lsa, "Sonlar teng" ekan degan yozuvni konsolga chiqaring.
# age1 = input('1-sonni kiriting: \n>>>')
# age2 = input('2-sonni kiriting: \n>>>')
# if age1 == age2:
#     print('Sonlar teng.\n')
# else:
#     print('Sonlar teng emas.\n')


# #   Foydalanuvchidan istalgan son kiritishni so'rang. Agar son manfiy bo'lsa konsolga "Manfiy son", agar musbat bo'lsa "Musbat son" degan xabarni chiqaring. 
# son = input('Istalgan sonni kiriting: \n>>>')
# if int(son) > 0:
#     print(f'Son musbat!, kiritilgan son {son}')
# else:
#     print(f'Son manfiy!, kiritilgan son {son}')
    

# #   Foydalanuvchidan son kiritishni so'rang, agar son musbat bo'lsa uning ildizini hisoblab konsolga chiqaring. Agar son manfiy bo'lsa, "Musbat son kiriting" degan xabarni chiqaring. 
# son = int(input('Biror son kiriting:  '))
# from math import*
# if son > 0:
#     print(f'Sonning ildizi: {sqrt(son)}')
# else:
#     print('Musbat son kiriting!')
