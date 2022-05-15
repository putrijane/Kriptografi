def cipher_encryption():
    msg = input("Enter Plain Text: ").replace(" ", "").upper()
    # print(msg)
    key = input("Enter keyword: ").upper()

    # menetapkan angka ke kata kunci
    kywrd_num_list = keyword_num_assign(key)

    # mencetak key
    for i in range(len(key)):
        print(key[i], end=" ", flush=True)
    # for
    print()
    for i in range(len(key)):
        print(str(kywrd_num_list[i]), end=" ", flush=True)
    # for
    print()
    print("-------------------------")

    # jika karakter tidak cocok dengan seluruh grid dengan sempurna
    extra_letters = len(msg) % len(key)
    # print(extraLetters)
    dummy_characters = len(key) - extra_letters
    # print(dummyCharacters)

    if extra_letters != 0:
        for i in range(dummy_characters):
            msg += "."
    # if

    # print(msg)

    #menghitung nomor pada baris
    num_of_rows = int(len(msg) / len(key))

    # Convert message ke dalam grid / membuat grid
    arr = [[0] * len(key) for i in range(num_of_rows)]
    #menulis message ke dalam grid
    z = 0
    for i in range(num_of_rows):
        for j in range(len(key)):
            arr[i][j] = msg[z]
            z += 1
        # for
    # for

    for i in range(num_of_rows):
        for j in range(len(key)):
            print(arr[i][j], end=" ", flush=True)
        print()
    # for

    # mendapatkan lokasi dari angka tersebut
    num_loc = get_number_location(key, kywrd_num_list)

    print(num_loc)

    # proses cipher, akan dituliskan huruf perkolom sesuai dengan urutan proses sebelumnya (cipher : SGTRL)
    cipher_text = ""
    k = 0
    for i in range(num_of_rows):
        if k == len(key):
            break
        else:
            d = int(num_loc[k])
        # if
        for j in range(num_of_rows):
            cipher_text += arr[j][d]
        # for
        k += 1
    # for

    print("Cipher Text: {}".format(cipher_text))

#jika dalam grid sudah terisi semua oleh cipher, maka akan dilanjut dengan dummy character
def get_number_location(key, kywrd_num_list):
    num_loc = ""
    for i in range(len(key) + 1):
        for j in range(len(key)):
            if kywrd_num_list[j] == i:
                num_loc += str(j)
            # if
        # for
    # for
    return num_loc

#didefinisikan sesuai urutan abjad 
def keyword_num_assign(key):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    kywrd_num_list = list(range(len(key)))
    # print(kywrdNumList)
    init = 0
    for i in range(len(alpha)):
        for j in range(len(key)):
            if alpha[i] == key[j]: #jika ada alfabet yang sama maka akan diurutkan dari kiri ke kanan sesuai pada grid
                init += 1
                kywrd_num_list[j] = init
            # if
        # inner for
    # for
    return kywrd_num_list


def cipher_decryption():
    msg = input("Enter Cipher Text: ").replace(" ", "").upper()
    # print(msg)
    key = input("Enter keyword: ").upper()

    # menetapkan angka ke kata kunci
    kywrd_num_list = keyword_num_assign(key)
    
    #menghitung nomor pada baris
    num_of_rows = int(len(msg) / len(key))

    # mendapatkan lokasi dari angka tersebut
    num_loc = get_number_location(key, kywrd_num_list)

    # melakukan konversi message ke dalam grid
    arr = [[0] * len(key) for i in range(num_of_rows)]

    # decipher
    plain_text = ""
    k = 0
    itr = 0

    # print(arr[6][4])
    # itr = len(msg)
    # mulai dari kolom bernomor 1 dan memasukkan ciphertext
    for i in range(len(msg)):
        d = 0
        if k == len(key):
            k = 0
        else:
            d: int = int(num_loc[k])
        for j in range(num_of_rows):
            arr[j][d] = msg[itr]
            # print("j: {} d: {} m: {} l: {} ". format(j, d, msg[l], l))
            itr += 1
        if itr == len(msg):
            break
        k += 1
    print()

    #mengekstrak plaintext dari grid per satu baris (satu per satu, baris pertama, baris kedua, dst) 
    for i in range(num_of_rows):
        for j in range(len(key)):
            plain_text += str(arr[i][j])
        # for
    # for

    print("Plain Text: " + plain_text)


def main():
    choice = int(input("1. Encryption\n2. Decryption\nChoose(1,2): "))
    if choice == 1:
        print("Encryption")
        cipher_encryption()
    elif choice == 2:
        print("Decryption")
        cipher_decryption()
    else:
        print("Invalid Choice")


if __name__ == "__main__":
    main()