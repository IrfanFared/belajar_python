#jadi ini adalah contoh penggunaan dictionary dengan beberapa keys dan nested dictionary
# serta perbaikan dalam iterasi untuk efisiensi
# Perbaikan ini menghindari penggunaan indeks yang tidak perlu dan membuat kode lebih bersih
# Definisi dictionary dengan beberapa keys dan nested dictionary
# serta perbaikan dalam iterasi untuk efisiensi



biodata1 = {"nama": "irfan", "pacara": "claudia"}
biodata2 = {"nama": "budi", "pacara": "siti"}
biodata3 = {"nama": "candra", "pacara": "dina"}

biodata_mahasiswa = { # didalam dictionary ini, kita menyimpan biodata mahasiswa dengan beberapa keys
    "mhs1": biodata1,
    "mhs2": biodata2,
    "mhs3": biodata3
}

# Perbaikan utama: gunakan .items() untuk iterasi yang lebih efisien
for key, data in biodata_mahasiswa.items():
    nama = data['nama']
    pacara = data['pacara']
    
    # Contoh penggunaan data (bisa disesuaikan kebutuhan)
    print(f"Key: {key} | Nama: {nama} | Pacar: {pacara}")