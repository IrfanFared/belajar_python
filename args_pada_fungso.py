# args adalah fungsi yang digunakan untuk mengirimkan banyak parameter ke dalam sebuah fungsi
# args adalah sebuah tuple yang berisi semua paramter yang dikirimkan ke dalam fungsi
# args bisa digunakan untuk mengirimkan banyak parameter ke dalam sebuah fungsi
# args menampung tipe data yang berbeda-beda

#untuk sytax args kita harus menambahkan tanda * di depan nama parameter

def faktorial(*args: int) -> int:
    hasil = 1
    for angka in args:
        if angka < 0:
            raise ValueError("angka tidak boleh negatif")
        elif angka == 0:
            hasil *= 1
        hasil *= angka
    return hasil

# contoh penggunaan fungsi faktorial
try:
    print(faktorial(5, 4, 3))  # Output: 60
    print(faktorial(0, 1, 2))  # Output: 2
    print(faktorial(-1, 2))  # Akan menimbulkan ValueError
except ValueError as e:
    print(e)



def sapa_nama(*daftar_nama):
    if not daftar_nama:
        print("tamu tidak dikenali")
    elif len(daftar_nama) == 1:
        print(f"helo cuy {daftar_nama[0]}")
    else :
        daftar_nama = ",".join(daftar_nama [:-1])
        print(f"halo selamat datang {daftar_nama} dan {daftar_nama[-1]}")

sapa_nama("irfan","caludia","kecoak")
