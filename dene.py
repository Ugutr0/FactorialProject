def faktoriyel(n):
    if n < 0:
        return "Böyle bir faktöriyel yok."
    elif n == 0 or n == 1:
        return 1
    else:
        sonuc = 1
        for i in range(1, n + 1):
            sonuc *= i
        return sonuc


def program_baslat():
    while True:
        try:
            girdi = input(
                "Faktöriyelini hesaplamak istediğiniz sayıyı girin (örnek: 5!) veya çıkmak için 'çık' yazın: "
            ).strip()

            # Çıkış kontrolü
            if girdi.lower() == "çık":
                print("Programdan çıkılıyor. Görüşmek üzere!")
                break

            # Eğer tam sayı girilmişse, ama '!' eksikse
            if girdi.isdigit():
                print("Lütfen sayının sonuna '!' işareti ekleyin. (Örnek: 5!)")
                continue

            # Harf veya geçersiz giriş kontrolü
            if not girdi[:-1].isdigit() or not girdi.endswith("!"):
                print("Lütfen geçerli bir sayı girin. (Örnek: 5!)")
                continue

            # Sayıyı ayrıştır ve faktöriyel hesapla
            sayi = int(girdi[:-1])
            print(f"{girdi} = {faktoriyel(sayi)}")

        except Exception as e:
            print(f"Beklenmeyen bir hata oluştu: {e}")


# Programı başlat
program_baslat()
