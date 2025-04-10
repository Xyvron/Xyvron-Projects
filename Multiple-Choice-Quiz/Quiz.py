#(main.py)#

from Question import Question
from datetime import datetime

waktuselesai = datetime.now().strftime("%d %B %Y, %H:%M")

soal = [
  "\nSiapa tokoh yang dikenal sebagai “Bapak Proklamator Indonesia”?\n(a) Soeharto\n(b) Soekarno\n(c) Habibie\n\n",
  "\nApa hasil dari 15 % 4 (modulus)?\n(a) 3\n(b) 1\n(c) 4\n\n",
  "\nBahasa pemrograman yang sering digunakan dalam pengembangan AI adalah…\n(a) C++\n(b) Python\n(c) Java\n\n",
  "\nManakah yang termasuk hewan mamalia?\n(a) Ikan Hiu\n(b) Katak\n(c) Lumba-lumba\n\n",
  "\nApa fungsi dari perintah print() dalam Python?\n(a) Menghitung Angka\n(b) Menampilkan output ke layar\n(c) Menghapus file\n\n"
]

kuncijawaban = [
  Question(soal[0], "b"),
  Question(soal[1], "a"),
  Question(soal[2], "b"),
  Question(soal[3], "c"),
  Question(soal[4], "b")
]

opsijawaban = ["a","b","c"]


def quiz_rahasia (kuncijawaban) :
  print("Halo, Selamat Datang di Kuis Rahasia!")
  skor = 0
  try :
    nama = input("Masukan nama kamu: ")

    for no, jawab in enumerate(kuncijawaban) :
      print(f"\n\nSoal {no+1}")
      coba = input(f"{jawab.prompt}\n> ")
      if coba.lower() == jawab.answer :
        print("\n✅ Benar!")
        skor += 1
      elif coba.lower() != jawab.answer and coba.lower() in opsijawaban:
        print(f"❌ Salah. Jawaban benar: {jawab.answer}")
      else :
        print ("\nJawabanmu Tidak Valid")
  except :
    print("\nInput Gak Valid My Friend!")
    
  print("\n🧠 Kuis selesai!")
  print(f"\nNama: {nama}\nSkor: {skor} dari   {len(kuncijawaban)}\nWaktu: {waktuselesai} ")
  print(f"\nHasil kamu telah disimpan ke file 'hasil_kuis.txt' ")
  with open("hasil_kuis.txt", "a") as file:
    file.write(f"Nama: {nama}\nSkor: {skor}/{len(kuncijawaban)}\nWaktu: {waktuselesai}\n\n")

quiz_rahasia(kuncijawaban)

#(Question.py)#

class Question :
  def __init__  (self, prompt, answer) :
    self.prompt = prompt
    self.answer = answer
