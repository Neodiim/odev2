
def harf_mi(karakter):
   
    if karakter.isalpha():
        return True
    else:
        return False

def buyukten_kucuge_cevir(harf):
   
    return harf.lower()

def frekans_analizi(metin):
    metin = metin.upper()
    harfler = [harf for harf in metin if harf.isalpha()]

   
    frekanslar = {}
    toplam_harfler = len(harfler)

   
    for harf in harfler:
        if harf in frekanslar:
            frekanslar[harf] += 1
        else:
            frekanslar[harf] = 1


    for harf, sayi in frekanslar.items():
        frekanslar[harf] = (sayi / toplam_harfler) * 100

    return frekanslar

def benim_bilgilerim():
    
    ad = "Ömer Faruk" 
    soyad = "Yüksel"  
    ogrenci_no = "211213034"  
    notum = "Birine hayallerini sormak, onun ruhunu anlamak için en iyi yöntemdir."  
    print(f"Ad: {ad}\nSoyad: {soyad}\nÖğrenci Numarası: {ogrenci_no}\nNot: {notum}")

if __name__ == "__main__":
    benim_bilgilerim()
    metin = input("Lütfen bir metin girin: ")
    karakter = input("Lütfen bir karakter girin: ")
    buyuk_harf = input("Lütfen bir büyük harf girin: ")

    frekanslar = frekans_analizi(metin)
    print("\nMetnin harf frekansları:")
    for harf, frekans in frekanslar.items():
        print(f"{harf}: %{frekans:.2f}")

   
    if harf_mi(karakter):
        print(f"{karakter} bir harftir.")
    else:
        print(f"{karakter} bir harf değildir.")

    kucuk_harf = buyukten_kucuge_cevir(buyuk_harf)
    print(f"Büyük harften küçük harfe çevrilmiş hali: {kucuk_harf}")
