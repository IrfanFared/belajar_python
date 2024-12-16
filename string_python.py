#string merupakan  kumpulan karakter yang di apit ''  atau ""

#cara membuata string
nama = "Irfan"
kelas = '12 A'

#cara membuat multilane string

Perkenalan_diri = """
Halo nama saya Irfan saya berasal dari kota Jepara
saya suka mactha dan suka claudia
"""

print(Perkenalan_diri)


#menguakan tanda \(slas) untuk supaya dimana ada kasu kita membutuhkann tanda ' 
jadwal_piket = 'Irfan piket hari Jum\'at' # ini memimalisri si mesin bigung 
print(jadwal_piket)

# didalam bahasa pemoraman python backslash adalah notasi uni 
# terkadan ada kassus dimana kita mengunakan backslas si mesin bingu yang dimana ini user pakai basckslas tapi kok ngak asa petik satu 
# untuk itu kita bisa gunakan mengunakan double backslas seperti contoh di bawhah ini

tanggal_lahir = "12\\12\\2006"
print(tanggal_lahir)
tanggal_lahir = "12\21\2008" #outpu bakal anomali
print(tanggal_lahir)

#bakslas + t = tab pada string
backslas_dengan_tab = "tab\t menjauh \t\t lebih banyak tab"
print(backslas_dengan_tab)