# pengertiana continou dalam  bahasa pemograman python adalah kata kunci yang digunakan untuk melanjutkan ke perulangan berikutnya.
# contoh penggunaan continou dalam bahasa pemograman python adalah sebagai berikut:
# for i in range(10):
#     if i == 5:
#         continue
#     print(i)


angka = 0

while angka < 10:
    angka +=1
    print(f"perulangan ke {angka}")
    if angka == 5:
        print("angka 5 tidak di print")
        continue
    print("angka di print") # jadi jika kondi angka == 5 maka angka 5 tidak di print
print("progam selesai")
