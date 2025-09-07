"""
Nama  : Muhammad Irfan pratama
NIM   : 25031554135
kelas : 2025A

Maaf sebelumnya bu atik 
saya mengerjakan tugas saya sekalian eksperimen if else mengunakan for in(iterasi)

"""

list_empat_angka_yang_memenuhi_4_kondisi = [1,3,2,12]


for i in list_empat_angka_yang_memenuhi_4_kondisi:
    value = i
    if value %2:
        if value**3 != 27 :
            value = value + 4 #assigment 1
            print(f"nilai {value} memenuhi kondisi pertama")
        else:
            value = value / 1.5 #assigment 2
            print(f"nilai {value} memenuhi kondisi kedua")
    else:
        if value <= 10:
            value = value * 2 #assigment 3
            print(f"nilai {value} memenuhi kondisi ketiga")
        else:
            value = value - 2 # asigment 4
            print(f"nilai {value} memenuhi kondisi keempat")
            
print(f"nilai angka yang memenuhi 4 kondisi if else di atas adalah {list_empat_angka_yang_memenuhi_4_kondisi} ")
