# scope adalah cakupan dimana varibale bisa diakses/dikenali di suatu progam

#global scope


"""
definisi global scope adalah cakupan diman varibel dapat diakses dari seluruh bagian progam, termasuk di dalam fungsi. varibel yang dideklarasika diluar fungsi atau blok kode lainya akan memeiliki global scope.
ini berarti variabel tersebut dapa diakses dan digunakan di mana saja dalam progam, termsuk di dalam fungsi.
"""
# global scope

x = 12

def tambah ():
    hasil = x +1
    return hasil

tambah()
print(x) # bisa diakses dimanapun

"""
definisi local scope adalah variabel yang hanya bisa diakses di fungsi itu sendiri
tidak bisa diakses di luar fungsi
"""

def tambah1 ():
    y = 1
    hasil = y +1
    return hasil

tambah1()
print(y) # tidak bisa di akses diluar fungsi

#jika variabel local dan global sama makan yang akan diprioritaskan mesin scope lokal

#Mengubah Global dari Dalam Fungsi: Pakai global

x = 10

def ubah():
    global x
    x = 20  # mengubah x global

ubah()
print(x)  # Output: 20

"""
kenap kita harus mengunakan scope
-bikin kode tidak konflik
-bikin kode terstruktur
-menghidari bug berlebih
"""
