#KARTIKA INDAH WIDYAS TANTRI / 222410102001

# kiri = ['q', 'w', 'e', 'r', 't', 'a', 's', 'd', 'f', 'g', 'z', 'x', 'c', 'v', 'b']
# kanan = ['y', 'u', 'i', 'o', 'p', 'h', 'j', 'k', 'l', 'n', 'm']
print('!','='*20,'!')
print(' '*7," SOAL 3 ",' '*7)
print('!','='*20,'!')

KIRI = ['q', 'w', 'e', 'r', 't', 'a', 's', 'd', 'f', 'g', 'z', 'x', 'c', 'v', 'b']
KANAN = ['y', 'u', 'i', 'o', 'p', 'h', 'j', 'k', 'l', 'n', 'm']

def isKanan(ch):
    if(ch in KANAN):
        return True
    return False

def isKiri(ch):
    if(ch in KIRI):
        return True
    return False

def isNyaman(nyaman, char1 = '', char2 = '', sisi = ''):
    print(nyaman)
    if(nyaman):
        print("Penjelasan: Setiap karakater selalu bergantian tangan.")
    else:
        print('Penjelasan: Karakter yang berdempetan yakni "{char1}" dan "{char2}" berada di satu tangan ({sisi})'.format(char1 = char1, char2 = char2, sisi = sisi))

def main():
    in_str = input("Masukkan Kata/kalimat : ")

    nyaman = True

    temp_arr = [i for a,i in enumerate(in_str)]
    for y in range(len(temp_arr)-1):
        if isKanan(temp_arr[y]):
            if isKanan(temp_arr[y+1]):
                nyaman = False
                isNyaman(nyaman, temp_arr[y], temp_arr[y+1], 'Kanan')
                break
        elif isKiri(temp_arr[y]):
            if isKiri(temp_arr[y+1]):
                nyaman = False
                isNyaman(nyaman, temp_arr[y], temp_arr[y+1], 'Kiri')
                break

    if(nyaman):
        isNyaman(nyaman)

if __name__ == '__main__' :
    main()
