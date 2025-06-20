# latihab dictionary 
# mengisi tamplate ditictionary dari imput 
# beginilah contoh penggunaan dictionary untuk mengisi template biodata mahasiswa
# dengan input dari pengguna. Ini adalah cara yang efisien untuk mengumpulkan data
# dan menyimpannya dalam struktur yang mudah diakses.
# jadi ini adalah contoh penggunaan dictionary untuk mengisi template biodata mahasiswa


template_biodata = {
    "nama" : "kosong" ,
    "nomer" : "nomer kosong",
    "nama pacar": "nama kosong"
}

biodata_mahaiswa = dict.fromkeys(template_biodata.keys()) # dict form keys digunakan untuk membuat dictionary baru
# dengan keys yang sama dari template_biodata, tetapi dengan nilai None.
 
biodata_mahaiswa["nama"] = input("masukan nama anda") # input digunakan untuk mengambil input dari pengguna
# dan menyimpannya dalam dictionary biodata_mahaiswa dengan key yang sesuai.
biodata_mahaiswa["nomer"] = input("masukan nomer anda")
biodata_mahaiswa["nama pacar"] = input("masukan nama pacar")
#cara mengakses nilai dalam dictionary adalah dengan menggunakan key yang sesuai.
print(f"nama saya adalah {biodata_mahaiswa['nama']} dan nomer saya adalah [{biodata_mahaiswa['nomer']}] dan nama pacar saya adalah [{biodata_mahaiswa['nama pacar']}]")
print(biodata_mahaiswa)