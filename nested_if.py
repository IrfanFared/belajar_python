
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

nilai = 85

if nilai >= 70:
    if nilai >= 90:
        print("A")
    elif nilai >= 80:
        print("B")
    else:
        print("C")
else:
    if nilai >= 50:
        print("D")
    else:
        print("E")

#if kondisi_utama:
    # Blok kode jika kondisi_utama True
#    if kondisi_sub1:
        # Blok kode jika kondisi_utama DAN kondisi_sub1 True
 #   elif kondisi_sub2:
        # Blok kode jika kondisi_utama True, kondisi_sub1 False, tapi kondisi_sub2 True
#    else:
        # Blok kode jika kondisi_utama True, tapi kondisi_sub1 dan sub2 False
#else:
    # Blok kode jika kondisi_utama False