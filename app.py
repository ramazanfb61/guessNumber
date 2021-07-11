import random

ranNum = random.randint(1, 10)
print("Sayı Tahmin Etme Oyununa Hoşgeldin")
name = input("İsminizi Giriniz :")
print("Seninle Tanıştığıma Memnun Oldum", name, "\nHadi Başlayalım !!!")

# print("Doğru Cevap :",ranNum)

tahmin = int(input("Tahmini Sayıyı Gir :"))

if tahmin == ranNum:
   print("Doğru Cevap")
elif tahmin < ranNum:
      print("Tahmin Küçük")
elif tahmin > ranNum:
      print("Tahmin Büyük")

while tahmin != ranNum:
   tahmin = int(input("Tahmini Sayıyı Gir :"))
   if tahmin == ranNum:
      print("Doğru Cevap")
      break
   elif tahmin < ranNum:
      print("Tahmin Küçük")
   elif tahmin > ranNum:
      print("Tahmin Büyük")