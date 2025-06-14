# didalam bahasa pemgraman python ada juga perulangan yang digunakan untuk mengulang kode tertentu selama kondisi tertentu bernilai benar.

#ada berbagai mcam perulangan yang ada di dalam bahasa pemograman python, salah satunya adalah perulangan for
# perulangan for adalah perulangan yang digunakan untuk mengulang kode tertentu selama kondisi tertentu bernilai benar.
# cara kerjanya adalah  

barang_impian = ["buku", "tablet", "istri cantik", ]

for i in barang_impian:
    print(f"Barang impian saya adalah {i}")


#di dalam pyton juga bisa perulang for denga mengunakan enumerate
barang_impian = ["buku", "tablet", "istri cantik", ]
for i, indek in  enumerate(barang_impian): 
    print(f"barang impian ke {i} {indek} yang saya beli dulu")