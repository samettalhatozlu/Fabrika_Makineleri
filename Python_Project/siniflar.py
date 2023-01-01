class Fabrika_Makineleri:
    def __init__(self, kullanim_alani, prensip, agirlik):
        self.kullanim_alani = kullanim_alani
        self.prensip = prensip
        self.agirlik = agirlik

    def bilgiyazdir(self):
        print(f"Alanı {self.kullanim_alani} olan ve çalışma prensibi {self.prensip} makine {self.agirlik} ağırlığındadır.")
    
    def calis(self):
        print(f"Alanı {self.kullanim_alani} olan ve çalışma prensibi {self.prensip} uygulanan ve  {self.agirlik} ağırlığında olan makine çalış.")

    def dur(self):
        print(f"Alanı {self.kullanim_alani} olan ve çalışma prensibi {self.prensip} uygulanan ve  {self.agirlik} ağırlığında olan makine dur.")


  

class Temizlik_Makinesi(Fabrika_Makineleri):
    def __init__(self, kullanim_alani, prensip, agirlik, ana_alet, kimyasal):
        self.ana_alet = ana_alet
        self.kimyasal = kimyasal
        super().__init__(kullanim_alani, prensip, agirlik)
    
    def bilgiyazdir(self):
        print(f"Alanı {self.kullanim_alani} olan ve çalışma prensibi {self.prensip} makine {self.agirlik} ağırlığındadır. Ayrıca ana kullanım aleti {self.ana_alet} olan makinede kimyasal olarak {self.kimyasal} maddesi kullanılmaktadır.")

    def yavasla(self):
        print(f"Kullanım alanı {self.kullanim_alani} olan makine yavaşlama moduna geç")
    
    def hizlan(self):
        print(f"Kullanım alanı {self.kullanim_alani} olan makine hızlanma moduna geç")



TemizlikMakinesi= Temizlik_Makinesi("Temizlik", "Yarı-Otomatik", "150 kg", "döner başlıklı fırçalar", "HR")
TemizlikMakinesi.bilgiyazdir()