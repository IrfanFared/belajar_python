
#Nested if dalam bahasa pemrograman Python adalah konsep di mana satu pernyataan if diletakkan di dalam pernyataan if lainnya. Ini memungkinkan pengembang untuk membuat keputusan bertingkat, 
# di mana keputusan pertama dapat mempengaruhi keputusan kedua. 
#if kondisi_pertama:
    # Blok kode jika kondisi_pertama True
    #if kondisi_kedua:
        # Blok kode jika kondisi_kedua True
    #else:
        # Blok kode jika kondisi_kedua False
#else:
    # Blok kode jika kondisi_pertama False

gaji = 10000000

if gaji > 1000000:
    print("gaji anda di atas rata-rata")
    if gaji > 2000000:
        print("gaji anda di atas rata-rata tinggi")
else:
        print("gaji anda di bawah rata-rata")
