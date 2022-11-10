#KARTIKA INDAH WIDYAS TANTRI / 222410102001

# Pak Budi adalah seorang peternak Sapi. Setiap Sapi memiliki waktu masing-masing untuk menjadi Dewasa. Rincian nya sebagai berikut :
# 1.Sapi Warrior    : 690 hari
# 2.Sapi Mage       : 420 hari
# 3.Sapi Assasin    : 530 hari
# 4.Sapi Nolep      : 330 hari
print('!','='*20,'!')
print(' '*7," SOAL 2 ",' '*7)
print('!','='*20,'!')
def main():
    jumlah_data = int(input("Masukkan jumlah sapi : "))
    jumlah_hari = 0

    for i in range(jumlah_data):
        inp = int(input("Masukkan kode sapi : "))
        if(inp == 1):
            jumlah_hari += 690
        elif(inp == 2):
            jumlah_hari += 420
        elif(inp == 3):
            jumlah_hari += 530
        elif(inp == 4):
            jumlah_hari += 330

    tahun = jumlah_hari // 365

    bulan = (jumlah_hari - tahun * 365) // 30

    hari = (jumlah_hari - tahun * 365 - bulan * 30)

    print("Jumlah hari yang diperlukan ialah : {0} Tahun, {1} Bulan, dan {2} Hari".format(tahun, bulan, hari))
if __name__ == '__main__' :
    main()