# Nama :Muhammad Irfan Pratama
# Kelas  : 2025A
# NIM     : 25031554135

# Tulislah syntax untuk algoritma tersebut dengan for-loop dan while-loop

#dengan mengunakan while-loop

list_Bilangan = [1044, 125, 2325, 328, 230, 15,21,1,32,89]

maks = 0
n = 0

while n < len(list_Bilangan):
    angka = list_Bilangan[n]

    if angka > maks:
        maks = angka
    elif angka <= maks:
        continue

    n += 1

print(f"Bilangan maksimal  akhir  {maks}")