def en_iyi_pazarlama_secimi(max_butce, kampanya_listesi):
    kampanya_sayisi = len(kampanya_listesi)
    
    # DP tablosu oluşturuyoruz
    dp_tablo = [[0] * (max_butce + 1) for _ in range(kampanya_sayisi + 1)]

    for i in range(1, kampanya_sayisi + 1):
        maliyet, tahmini_getiri = kampanya_listesi[i - 1]

        for mevcut_butce in range(max_butce + 1):
            if maliyet <= mevcut_butce:
                dp_tablo[i][mevcut_butce] = max(dp_tablo[i - 1][mevcut_butce], 
                                                 tahmini_getiri + dp_tablo[i - 1][mevcut_butce - maliyet])
            else:
                dp_tablo[i][mevcut_butce] = dp_tablo[i - 1][mevcut_butce]
    
    return dp_tablo[kampanya_sayisi][max_butce]

# Örnek Kullanım
kampanyalar = [(10, 50), (20, 60), (30, 90)]  # (maliyet, getiri)
butce = 50

maks_getiri = en_iyi_pazarlama_secimi(butce, kampanyalar)
print("Seçilen Kampanyalar ile Maksimum Getiri:", maks_getiri)
