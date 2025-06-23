#fungsi dengan parameter
# jadi fungsi dengan parameter adalah fungsi yang bisa kita berikan nilai
# atau variabel yang akan digunakan di dalam fungsi tersebut
# untuk membuat fungsi dengan parameter kita bisa menambahkan parameter di dalam tanda kurung
# contoh untuk sytaksis
# def nama_fungsi(parameter1, parameter2):
#     # kode yang akan dijalankan
#     print(parameter1, parameter2)


# ini adalah contoh fungsi dengan parameter
def jumlah (nilai_pertama, nilai_kedua):
    if nilai_pertama <= nilai_kedua:
       total = nilai_pertama+ nilai_kedua
       print(total)
    else :
        print("gagal melakukan pertamabah")
# ini adalah contoh pemanggilan fungsi dengan parameter
# kita bisa memberikan nilai atau variabel sebagai parameter
jumlah(12,23)

def daftar_belanja(daftar_sayur):
    print(daftar_sayur)


def menghitung_penjumalahn(nilai):
    total = 0
    for list in nilai:
        total += list
    return total

# jika berbentuk lits kita bisa  deklarasikan list di dalam parameter
daftar_belanja(["bayam", "kangkung", "sawi", "wortel", "buncis"])   

nilai = [12,21,3,13,53,6,3,6]
hasil_fungsi = menghitung_penjumalahn(nilai)
print(hasil_fungsi)

