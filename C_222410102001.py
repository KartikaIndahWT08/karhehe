# QUIZ 01 ALGORITMA & PEMROGRAMAN 10 Oktober 2022

import random as rd #import library random dan membuat nama alias menjadi rd agar lebih mudah dipanggil
angka = rd.randint(0, 100) #untuk membuat angka random dari 0-100 menggunakan library random yang telah di import

batas = 10 #membatasi looping atau counter

#judul game tebak angka
print('!','='*20,'!') #print 1 tanda seru (!) di awal setelah 20 tanda sama dengan (=) dan 1 tanda seru (!) di akhir untuk pembatas atas judul game
print(' '*2," GAME TEBAK ANGKA ",' '*2) #print judul "GAME TEBAK ANGKA" dengan jeda dua spasi di awal dan jeda 2 spasi di akhir
print('!','='*20,'!') #print 1 tanda seru (!) di awal setelah 20 tanda sama dengan (=) dan 1 tanda seru (!) di akhir untuk pembatas bawah judul game sehingga judul game seperti dikotaki

for percobaan in range(batas):
  jawaban = int(input(f'\n[Percobaan {percobaan + 1}] Masukkan angka: ')) #input untuk memasukkan angka kita setelah itu variabel percobaaan ditambah 1 untuk counter batas percobaan jika percobaan = 10 maka looping berhenti

  if jawaban == angka: #membandingkan jawaban dengan angka random
        print('Selamat, tebakanmu benar!') #jika benar maka akan di print "Selamat, tebakanmu benar!"
        break
  else: #kondisi ketika jawaban salah
    print('Tebakanmu terlalu','kecil' if jawaban < angka else 'besar') #maka akan di print "Tebakanmu terlalu kecil" jika jawaban < angka random dan akan di print "Tebakanmu terlalu besar" jika jawaban > angka random
else:
    print(f'\nSayang sekali, kamu sudah salah menebak sebanyak {batas}x!') # ketika  variabel percobaan = 10 dan belum menemukan angka yang benar maka akan di print
    print("Angka yang benar adalah ",angka) # print angka random yang sebenarnya