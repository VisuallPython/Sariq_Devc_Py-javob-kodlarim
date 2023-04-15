        # 14-dars: Lug'at bilan ishlash

    # Sodda lug'at ko'rinishi;
# car = {'model':'Cobalt', 'rang':'Mokriviy asfalt', 'yili':'2015'}
# print(car['model'], car['rang'], car['yili'])
# print(car['model'])
# print(car['rang'], '\n')
# print(f"Mashina modeli {car['model']},\navtomabil rangi {car['rang']},\nmashina yili {car['yili']} ")


# talaba = {'ism':'sardor temirov', 'yosh':'20', 't_yili':'2003'}
# print(f"{talaba['ism'].title()}, {talaba['t_yili']} yil, {talaba['yosh']} yoshda.")


        # Yangi juftlik qo'shish
# talaba = {'ism':'sardor temirov', 'yosh':'20', 't_yili':'2003'}
# talaba['fakultet'] = 'ASU'
# talaba['kurs'] = '1- kurs'
# print(talaba)


# car = {
#     'zavot' : 'GM',
#     'model' : 'Malibu',
#     'rangi' : 'Mokriviy asfalt',
#     'uzatma_qutisi' : 'Avtomat',
#     'yili' : '2021',
#     'yurgan_yuli' : '10000 km'
#     }
# print(f"{car['zavot']}, {car['model']}, {car['rangi']}, {car['uzatma_qutisi']}, yili {car['yili']}, {car['yurgan_yuli']}")


    # get() METODI 01
# car = {
#     'zavot' : 'GM',
#     'model' : 'Malibu',
#     'rangi' : 'Mokriviy asfalt'
#     }
# narx = car.get('narx', 'Bunday kalit mavjud emas!')
# print(f"{car['zavot']}, {car['model']}, {car['rangi']}")
# print("narx: ", narx)
#             # Agar get() ichida comment qoldirmasak, Noune qiymat qaytaradi.


    # Bo'sh qiymat yaratish va uni to'ldirib borish.
# talaba = {}     # Lug'atlarda ro'yxat {} qavslarda yaratiladi
# talaba['ism'] = 'jovliyev shoxruh'
# talaba['yoshi'] = '18'
# talaba['kursi'] = '1- kurs'
# print(talaba, '\n')
# print(f"{talaba['ism'].title()} {talaba['yoshi']} yoshda, {talaba['kursi']}")
#         # lug'atning biri qiymatini yangilash
# talaba['kursi'] = '3- kurs'
# print(f"{talaba['ism'].title()} {talaba['yoshi']} yoshda, {talaba['kursi']}")


    # lugat ichidan elementlarni kalit so'z yordamida o'chirish
# car = {'model':'Malibu', 'rang':'qora', 'yili':'2022-yil'}
# del car['rang']     #rang kaliti bn qiymat o'chirildi.
# print(car)


    # Lug'atlarni bir nechta qatorda yozish
# mashinalar = {
#     'murod' : 'captiva',
#     'humoyun' : 'kia 5',
#     'sarvar' : 'malibu',
#     'shoxruh' : 'trecker'
# }
# print(mashinalar, '\n')
# print(mashinalar['humoyun'])

#     # get() metodi 02
# mashinalar = {
#     'murod' : 'captiva',
#     'humoyun' : 'kia 5',
#     'sarvar' : 'malibu',
#     'shoxruh' : 'trecker'
# }
# mashina1 = mashinalar.get('asil', 'Bunday kalit yo\'q.')
# print(mashina1)


        # AMALIY MISOLLAR YECHISH

#     #1-topshiriq
# otam = {'ism':'abdug\'affor', 't_yili':'1977-yil', 't_joyi':'surxondaryo viloyati'}
# onam = {'ism':'gulchexra', 't_yili':'1984-yil', 't_joyi':'surxondaryo viloyati'}
# ukam = {'ism':'bobur', 't_yili':'2011-yil', 't_joyi':'qumqo\'rg\'on tumani'}
# ukam2 = {'ism':'abdusamad', 't_yili':'2017-yil', 't_joyi':'qumqo\'rg\'on tumani'}
# singlim1 = {'ism':'marjona', 't_yili':'2005-yil', 't_joyi':'surxondaryo viloyati'}
# singlim2 = {'ism':'mahliyo', 't_yili':'2006-yil', 't_joyi':'surxondaryo viloyati'}
#
# print(f"Otamning ismi {otam['ism'].title()}, {otam['t_yili']} {otam['t_joyi'].capitalize()}da tug'ilgan. \n")
# print(f"Onamning ismi {otam['ism'].title()}, {onam['t_yili']} {onam['t_joyi'].capitalize()}da tug'ilgan. \n")
# print(f"Birinchi ukamning ismi {ukam['ism'].title()}, {ukam['t_yili']} {ukam['t_joyi'].capitalize()}da tug'ilgan. \n")
# print(f"Ikkinchi ukamning ismi {ukam2['ism'].title()}, {ukam2['t_yili']} {ukam['t_joyi'].capitalize()}da tug'ilgan. \n")
# print(f"Birinchi singliming ismi {singlim1['ism'].title()}, {singlim1['t_yili']} {singlim1['t_joyi'].capitalize()}da tug'ilgan. \n")
# print(f"Ikkinchi singliming ismi {singlim2['ism'].title()}, {singlim2['t_yili']} {singlim2['t_joyi'].capitalize()}da tug'ilgan. \n")


    #2-topshiriq
# sevimli_taomlar = {
#     'otam' : 'osh',
#     'onam' : 'manti',
#     'katta_singlim' : 'bilinchik',
#     'katta_ukam' : 'honim',
#     'kichik_singlim' : 'shirguruch'
# }
# print(f"Otamning sevimli taomi, {sevimli_taomlar['otam'].capitalize()}")
# print(f"Onamning sevimli taomi, {sevimli_taomlar['onam'].capitalize()}")
# print(f"Mahliyoning yoqtirgan taomi, {sevimli_taomlar['kichik_singlim'].capitalize()}")


    #3-4 topshiriq
    # Python izohli lug'ati
# py_lugat = {
#     'int':'butun son',
#     'float':'kasr son',
#     'bool':'shart operatori',
#     'string':"so'zlardan iborat matn turi",
#     'if':'qiymatni shart buyicha tekshirish',
#     'elsa':'if bajarilmagan holatdagi shartni bajaradi',
#     'for':'takrorlanish operatori',
#     'pop':'sonlarni darajaga oshiradi',
#     'max':'sonlarning eng kattasini aniqlaydi',
#     'min':'sonlarning eng kichigini aniqlaydi',
#     'title':'qatordagi barcha so\'zlarni katta harf qilib beradi'
# }
# kiritish = input('Kalit so\'z kiriting: ')
# print(f"{kiritish}: {py_lugat[kiritish]}")


    # 5-topshiriq




















