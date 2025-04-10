from datetime import datetime

waktu = datetime.now ().strftime("%d %B %Y, %H:%M")

print ("Selamat Datang di Sekolah Tata Krama !")
nama = input("Masukin Nama Kamu : ")
katakotor = ["goblok", "bodoh", "anjing", "bangsat", "tolol", "tai", "g0blok", "gobl0k", "g0bl0k"]

kata = input("\nTulis Sesuatu Disini :\n")

katasopan = ""
katakasar = 0
for word in kata.split() :
  if word.lower() in katakotor :
    katasopan += "*" * len(word) + " "
    katakasar += 1
  else :
    katasopan += word + " "

print(f"\n{nama},Kamu Masih Gasopan di {waktu}, seharusnya :\n {katasopan}")

data = f"\nNama: {nama}\nWaktu: {waktu}\nJumlah Kata Kasar: {katakasar}\nTeks Disensor: {katasopan}\n\n"

with open("Sekolahtatakrama.txt", "a") as file :
  file.write(data)
