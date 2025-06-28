#anymous funtion atau lamda funtion adalah sebuah fungsi yang tidak memiliki nama
# dab bisanya digunakan untuk fungsi yang sedrhana atau fungsi yang hanya digunakan sekali
# kapan kita mengunakana anonymous funtion atau lamda funtion adalah ketika kita ingin membuat fungsi yang sederhan dan hanya digunakan sekali
# contoh sytaksis anonymous funtion atau lamda funtion adalah sebagai berikut

# lamda parameter : ekspresi

tambah = lambda a,b : a + b

tambah(5, 10)


"""
keuntungan mengunakan lamda
-kode yang ringka
-cocok di pakai di fungsi lain
-berguna sebagai fungsi sementara


"""
cewek_yang_menyukaiku = ["claudia","carmen", "violet", "syakirah"]

cewek_yang_menyukaiku.sort(key=lambda x : len(x))
print(cewek_yang_menyukaiku)

angka = [1, 2, 3, 4, 5, 6]
genap = list(filter(lambda x: x % 2 == 0, angka))
print(genap)  # Output: [2, 4, 6]
