# Nama :Muhammad Irfan Pratama
# Kelas  : 2025A
# NIM     : 25031554135

# Tulislah syntax untuk algoritma tersebut dengan for-loop dan while-loop
#while loop ada di file terpisah bu Atik


# mengunakan for-loop
list_angka = [100, 15, 125, 58, 330, 15,6,253,423,6]

maks = 0

for angka in list_angka:
    if angka > maks:
        maks = angka
    elif angka <= maks:
        continue
print(f"Bilangan maksimal akhir  {maks}")



