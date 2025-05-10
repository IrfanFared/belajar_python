def binary_search(arr, target):
    low = 0  # Indeks awal (0 = elemen pertama)
    high = len(arr) - 1  # Indeks akhir (9 = elemen terakhir)

    while low <= high:  # Selama masih ada area pencarian
        mid = (low + high) // 2  # Cari indeks tengah (// = pembagian bulat)
        if arr[mid] == target:  # Jika nilai tengah = target
            return mid  # Ketemu! Kembalikan indeks
        elif arr[mid] < target:  # Jika nilai tengah < target
            low = mid + 1  # Geser pencarian ke KANAN
        else:  # Jika nilai tengah > target
            high = mid - 1  # Geser pencarian ke KIRI
    return -1  # Tidak ditemukan

# Contoh penggunaan
data = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]  # List harus terurut!
target = 23

result = binary_search(data, target)
if result != -1:
    print(f"Angka {target} ditemukan di indeks {result}.")
else:
    print(f"Angka {target} tidak ditemukan.")