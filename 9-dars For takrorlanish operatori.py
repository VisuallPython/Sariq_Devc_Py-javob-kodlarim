#             9-Dars. For takrolanish operatori!
            
#   Keling quyidagi misolni ko'ramiz. Bizda mehmonlar ro'yxati bor, biz har bir mehmonning ismini yangi qatordan chiqarmoqchimiz.
# mehmonlar = ['Asil', 'Murod', 'Humoyu', 'Kamol', 'Jahongir']
# for mehmon in mehmonlar:
#     print("Salom mening do\'stim, ", mehmon)


#   for qanday ishlaydi, misol:
# dustlar = ['Asil', 'Murod', 'Humoyu', 'Kamol', 'Jahongir']
# for mehmon in dustlar:
#     print(f' Hurmatli do\'stim {mehmon}, sizni va oilangizni naxor oshga taklif qilaman!')
#     print('\nHurmat bilan Temirov Sardor oilasi!')

#   koddagi xatoliklar:
# mehmonlar = ['Ali','Vali','Hasan', 'Husan','Olim']
# for mehmon in mehmonlar:
#     print(mehmon)
#     print(mehmonlar)  # bu qator tsikl tashqarisida bo'lishi kerak edi;

#   to'g'ri kod quyidagicha bo'ladi. 
# mehmonlar = ['Ali','Vali','Hasan', 'Husan','Olim']
# for mehmon in mehmonlar:
#     print(mehmon)
# print(mehmonlar)


#   Misol_1:
# for son in range(1,11):
#     print(f'{son} ning kvadrati, {son**2} ga teng;')

#   Misol_2:
# sonlar = list(range(11))
# sonlar_kvadrati = []
# for son in sonlar:
#     sonlar_kvadrati.append(son**2)
# print(sonlar)
# print(sonlar_kvadrati)

#   Misol_3:    Sonning kunini hisoblash!
# sonlar_kubi = []
# sonlar = list(range(11))
# for son in sonlar:
#     sonlar_kubi.append(son**3)
# print(sonlar)
# print(sonlar_kubi)


#         for va input()
# dustlarim = []
# print('5 ta eng yaqin do\'stingiz kim?')
# for n in range(1, 6):
#     dustlarim.append(input(f'{n} - do\'stingizni ismi: '))
# print(dustlarim)


#             AMALIYOT

#   Kamida 5 elementdan iborat ismlar degan ro'yxat tuzing, va ro'yxatdagi har bir ismga takrorlanuvchi xabar yozing;
# ismlar = ['Asilbek', 'Haydar', 'Komil', 'Murod', 'Sardor', 'Kamron']
# for ism in ismlar:
#     print(f'Assalomu alaykum {ism}')

#   Yuoqirdagi tsikl tugaganidan so'ng, ekranga "Kod n marta takrorlandi" degan xabarni chiqaring (n o'rniga kod necha marta takrorlanganini yozing)
# ismlar = ['Asilbek', 'Haydar', 'Komil', 'Murod', 'Sardor', 'Kamron', 'Adhambek']
# for ism in ismlar:
#     print(f'Assalomu alaykum {ism}')
# print(f'Kod 7 marta takrorlandi!')

#   10 dan 100 gacha bo'lgan toq sonlar ro'yxatini tuzing. Ro'yxatning xar bir elementining kubini yangi qatordan konsolga chiqaring.
# sonlar = list(range(11, 101, 2))
# for son in sonlar:
#     print(son**3)

#   Foydalanuvchidan 5 ta eng sevimli kinolarini kiritshni so'rang, va kinolar degan ro'yxatga saqlab oling. Natijani konsolga chiqaring.
# kinolar = []
# print("5 ta eng sevimli kinongizni kiriting!")
# for kino in range(1, 6):
#     kinolar.append(input(f'{kino} - sevimli kinongiz: '))
# print(kinolar)

#   Foydalanuvchidan bugun nechta odam bilan uchrashganini (suhbatlashganini) so'rang, va har bir suhbatlashgan odamning ismini birma-bir so'rab ro'yxatga yozing. Ro'yxatni konsolga chiqaring.
# uchrashuvlar = []
# soni = int(input('Bugun nechta inson bilan uchrashdingiz? -->>'))
# for uchrashuv in range(1, soni+1):
#     uchrashuvlar.append(input(f'{uchrashuv} - suxbat qilgan odamiz kim edi: '))
# print(uchrashuvlar)