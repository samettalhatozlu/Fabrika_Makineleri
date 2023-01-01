from siniflar import Fabrika_Makineleri

for i in range(15):
    freze0 = input("Freze'nin kullanım alanı nedir?")
    freze1 = input("Freze'nin çalışma prensibi nedir?")
    freze2 = input("Freze'nin ağırlığı nedir?")
    torna0 = input("Torna'nın kullanım alanı nedir?")
    torna1 = input("Torna'nın çalışma prensibi nedir?")
    torna2 = input("Torna'nın ağırlığı nedir?")
    cnc0 = input("CNC'nin kullanım alanı nedir?")
    cnc1 = input("CNC'nin çalışma prensibi nedir?")
    cnc2 = input("CNC'nin ağırlığı nedir?")
    forklift0 = input("Forklift'in ağırlığı kaç kg'dır?")
    forklift1 = input("Forklift'in çalışma prensibi nedir?")
    forklift2 = input("Forklift'in ağırlığı nedir?")
    pres0 = input("Pres'in çalışma prensibi nedir?")
    pres1 = input("Pres'in çalışma prensibi nedir?")
    pres2 = input("Pres'in ağırlığı nedir?")
    break
#3. satırdan 19. satıra olan kısımda projede istenilen 5. maddedeki bir döngü içerisinde oluşturulacak beş nesnenin özellikleri kullanıcıdan
# girdi olarak alınma işlemi gerçekleştirilmiştir.


freze = Fabrika_Makineleri({freze0}, {freze1}, {freze2})
torna = Fabrika_Makineleri({torna0}, {torna1}, {torna2})
cnc = Fabrika_Makineleri({cnc0},{cnc1},{cnc2})
forklift = Fabrika_Makineleri({forklift0},{forklift1},{forklift2})
pres = Fabrika_Makineleri({pres0},{pres1},{pres2})
#24. ve 28. maddelerde nesne oluşturma işlemi gerçekleştirilmiştir.

YeniAnaNesneler = {"nesne1":freze, "nesne2": torna, "nesne3": cnc, "nesne4": forklift, "nesne5": pres}
#31. satırda nesne oluşturma işlemi gerçekleştirilmiştir.

from siniflar import Temizlik_Makinesi

for i in range(25):
    Temizlik_Makinesi2_0 = input("Temizlik_Makinesi2'nin kullanım alanı nedir?")
    Temizlik_Makinesi2_1 = input("Temizlik_Makinesi2'nin çalışma prensibi nedir?")
    Temizlik_Makinesi2_2 = input("Temizlik_Makinesi2'nin ağırlığı nedir?")
    Temizlik_Makinesi2_3 = input("Temizlik_Makinesi2'nin ana aleti nedir?")
    Temizlik_Makinesi2_4 = input("Temizlik_Makinesi2'nin kimyasalı nedir?")
    Temizlik_Makinesi3_0 = input("Temizlik_Makinesi3'ün kullanım alanı nedir?")
    Temizlik_Makinesi3_1 = input("Temizlik_Makinesi3'ün çalışma prensibi nedir?")
    Temizlik_Makinesi3_2 = input("Temizlik_Makinesi3'ün ağırlığı nedir?")
    Temizlik_Makinesi3_3 = input("Temizlik_Makinesi3'ün ana aleti nedir?")
    Temizlik_Makinesi3_4 = input("Temizlik_Makinesi3'ün kimyasalı nedir?")
    Temizlik_Makinesi4_0 = input("Temizlik_Makinesi4'ün kullanım alanı nedir?")
    Temizlik_Makinesi4_1 = input("Temizlik_Makinesi4'ün çalışma prensibi nedir?")
    Temizlik_Makinesi4_2 = input("Temizlik_Makinesi4'ün ağırlığı nedir?")
    Temizlik_Makinesi4_3 = input("Temizlik_Makinesi4'ün ana aleti nedir?")
    Temizlik_Makinesi4_4 = input("Temizlik_Makinesi4'ün kimyasalı nedir?")
    Temizlik_Makinesi5_0 = input("Temizlik_Makinesi5'in kullanım alanı nedir?")
    Temizlik_Makinesi5_1 = input("Temizlik_Makinesi5'in çalışma prensibi nedir?")
    Temizlik_Makinesi5_2 = input("Temizlik_Makinesi5'in ağırlığı nedir?")
    Temizlik_Makinesi5_3 = input("Temizlik_Makinesi5'in ana aleti nedir?")
    Temizlik_Makinesi5_4 = input("Temizlik_Makinesi5'in kimyasalı nedir?")
    Temizlik_Makinesi6_0 = input("Temizlik_Makinesi6'nın kullanım alanı nedir?")
    Temizlik_Makinesi6_1 = input("Temizlik_Makinesi6'nın çalışma prensibi nedir?")
    Temizlik_Makinesi6_2 = input("Temizlik_Makinesi6'nın ağırlığı nedir?")
    Temizlik_Makinesi6_3 = input("Temizlik_Makinesi6'nın ana aleti nedir?")
    Temizlik_Makinesi6_4 = input("Temizlik_Makinesi6'nın kimyasalı nedir?")
    break

Temizlik_Makinesi2 = Temizlik_Makinesi({Temizlik_Makinesi2_0},{Temizlik_Makinesi2_1},{Temizlik_Makinesi2_2},{Temizlik_Makinesi2_3},{Temizlik_Makinesi2_4})
Temizlik_Makinesi3 = Temizlik_Makinesi({Temizlik_Makinesi3_0},{Temizlik_Makinesi3_1},{Temizlik_Makinesi3_2},{Temizlik_Makinesi3_3},{Temizlik_Makinesi3_4})
Temizlik_Makinesi4 = Temizlik_Makinesi({Temizlik_Makinesi4_0},{Temizlik_Makinesi4_1},{Temizlik_Makinesi4_2},{Temizlik_Makinesi4_3},{Temizlik_Makinesi4_4})
Temizlik_Makinesi5 = Temizlik_Makinesi({Temizlik_Makinesi5_0},{Temizlik_Makinesi5_1},{Temizlik_Makinesi5_2},{Temizlik_Makinesi5_3},{Temizlik_Makinesi5_4})
Temizlik_Makinesi6 = Temizlik_Makinesi({Temizlik_Makinesi6_0},{Temizlik_Makinesi6_1},{Temizlik_Makinesi6_2},{Temizlik_Makinesi6_3},{Temizlik_Makinesi6_4})

YeniCocukNesneler = {"cnesne1":Temizlik_Makinesi2, "cnesne2":Temizlik_Makinesi3, "cnesne3":Temizlik_Makinesi4, "cnesne4":Temizlik_Makinesi5, "cnesne5":Temizlik_Makinesi6}

for i in range(15):
    print(freze.bilgiyazdir())
    print(torna.bilgiyazdir())
    print(cnc.bilgiyazdir())
    print(forklift.bilgiyazdir())
    print(pres.bilgiyazdir())
    print(freze.dur())
    print(torna.dur())
    print(cnc.dur())
    print(forklift.dur())
    print(pres.dur())
    print(freze.calis())
    print(torna.calis())
    print(cnc.calis())
    print(forklift.calis())
    print(pres.calis())
#72. satırdan 87. satıra kadar olan kısımda projede istenilen 6. maddedeki metotların çalıştırılması işlemi gerçekleştirilmiştir.

for i in range(10):
    print(Temizlik_Makinesi2.yavasla())
    print(Temizlik_Makinesi2.hizlan())
    print(Temizlik_Makinesi3.yavasla())
    print(Temizlik_Makinesi3.hizlan())
    print(Temizlik_Makinesi4.yavasla())
    print(Temizlik_Makinesi4.hizlan())
    print(Temizlik_Makinesi5.yavasla())
    print(Temizlik_Makinesi5.hizlan())
    print(Temizlik_Makinesi6.yavasla())
    print(Temizlik_Makinesi6.hizlan())
    
#by Samet Talha Tozlu