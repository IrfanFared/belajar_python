def tambah (a,b):
    return a+b

def kurang (a,b):
    return a-b
def kali (a,b):
    return a*b
def bagi (a,b):
    return a/b

print("kakaluator sederhana")
print("1. tambah")
print("2. kurang")
print("3. kali")
print("4. bagi")
pilihan = int(input("masukkan pilihan 1/2/3/4 : "))

angka1 = int(input("masuskan angka pertama : "))
angka2 = int(input("masukan angka kedua:  "))

if pilihan == 1 :
    print(f"hasil penjumlahan {angka1} + {angka2} = {tambah (angka1,angka2)}")
elif pilihan == 2 :
    print(f"hasil pengurangan {angka1} - {angka2} = {kurang (angka1,angka2)}")
elif pilihan == 3 :
    print(f"hasil perkalian {angka1} * {angka2} = {kali (angka1,angka2)}")
elif pilihan == 4 :     
    print(f"hasil pembagian {angka1} / {angka2} = {bagi (angka1,angka2)}")
else:
    print("tidak ada pilihan")
