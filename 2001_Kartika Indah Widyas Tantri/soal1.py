#KARTIKA INDAH WIDYAS TANTRI / 222410102001

print('!','='*20,'!')
print(' '*7," SOAL 1 ",' '*7)
print('!','='*20,'!')
def main():

    jumlah = int(input("Masukkan jumlah kata : "))

    for i in range(jumlah):
        in_str = input("Masukkan kata ke-{0} : ".format(i+1))

        print("\nHasil : ")
        temp_arr = [i for a,i in enumerate(in_str)]
        for y in range(len(temp_arr)-1):
            banding = ""
            if ord(temp_arr[y]) > ord(temp_arr[y+1]):
                banding = "lebih"
                selisih = ord(temp_arr[y]) - ord(temp_arr[y+1])
            elif ord(temp_arr[y]) < ord(temp_arr[y+1]):
                banding = "kurang"
                selisih = ord(temp_arr[y+1]) - ord(temp_arr[y])

            print("{char1} {banding} dari {char2}, selisihnya adalah {selisih}".format(char1 = temp_arr[y], char2 = temp_arr[y+1], banding = banding, selisih = selisih))
        print()

if __name__ == '__main__' :
    main()