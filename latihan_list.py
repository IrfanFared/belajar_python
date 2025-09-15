#kata kunci enumerate
# digunakan untuk mengembalikan indeks dari elemen yang sedang diulang.# Ini sangat berguna ketika kita ingin mengetahui posisi elemen dalam daftar atau koleksi lainnya.


daftar_biodata = []

while True:
    Nama = input("masukan nama anda: ")
    umur = input("masukan umur anda : ")
 
    list_biodata = [Nama,umur]
    daftar_biodata.append(list_biodata)
    for index, i in enumerate(daftar_biodata):
        print(f"nomer biodata ke {index+1} dengan {i[0]} dan umur {i[1]}")

    finish = input("apakah anda ingin lajut atau tidak ")

    if finish == "no":
     break
 
print("progam selesai")
print(daftar_biodata)

     
  
