class Musteri:
    def __init__(self, musteri_id, sehir, talep_puani, sure_gereksinimi):
        self.musteri_id = musteri_id
        self.sehir = sehir
        self.talep_puani = talep_puani
        self.sure_gereksinimi = sure_gereksinimi

class Temsilci:
    def __init__(self, temsilci_id, sehir, max_calisma_suresi):
        self.temsilci_id = temsilci_id
        self.sehir = sehir
        self.max_calisma_suresi = max_calisma_suresi

def temsilci_atama_sistemi(musteriler, temsilciler):
    sehire_gore_temsilciler = {}

    # Temsilcileri şehir bazında gruplayalım
    for temsilci in temsilciler:
        if temsilci.sehir not in sehire_gore_temsilciler:
            sehire_gore_temsilciler[temsilci.sehir] = []
        sehire_gore_temsilciler[temsilci.sehir].append(temsilci)

    dp_cache = {}

    def max_puan_hesapla(musteri_index):
        if musteri_index >= len(musteriler):
            return 0
        if musteri_index in dp_cache:
            return dp_cache[musteri_index]

        mevcut_musteri = musteriler[musteri_index]
        atama_yapmadan_devam = max_puan_hesapla(musteri_index + 1)  # Alternatif atama

        en_iyi_sonuc = atama_yapmadan_devam

        if mevcut_musteri.sehir in sehire_gore_temsilciler:
            for temsilci in sehire_gore_temsilciler[mevcut_musteri.sehir]:
                if temsilci.max_calisma_suresi >= mevcut_musteri.sure_gereksinimi:
                    temsilci.max_calisma_suresi -= mevcut_musteri.sure_gereksinimi
                    yeni_sonuc = mevcut_musteri.talep_puani + max_puan_hesapla(musteri_index + 1)
                    temsilci.max_calisma_suresi += mevcut_musteri.sure_gereksinimi
                    en_iyi_sonuc = max(en_iyi_sonuc, yeni_sonuc)

        dp_cache[musteri_index] = en_iyi_sonuc
        return en_iyi_sonuc

    return max_puan_hesapla(0)

# Örnek Kullanım
musteri_listesi = [
    Musteri(1, "İstanbul", 10, 2),
    Musteri(2, "Ankara", 20, 1),
    Musteri(3, "İstanbul", 15, 3)
]

temsilci_listesi = [
    Temsilci(1, "İstanbul", 5),
    Temsilci(2, "Ankara", 3)
]

maks_puan = temsilci_atama_sistemi(musteri_listesi, temsilci_listesi)
print("Toplam Maksimum Hizmet Puanı:", maks_puan)
