# date and time 

import datetime
hari_ini = datetime.date.today()
print(hari_ini)

import datetime as dt
hari_ini = dt.date.today()
print(hari_ini)

print(f"hari ini adalaha hari{hari_ini:%A}") # maksu dari %A adalah nama hari dalam seminggu
#output = hari ini adalaha hari Monday

import datetime as dt

tanggal = int(input("masukan tanngal lahir anda  "))
bulan = int(input("masukan bulan lahir anda      "))
tahun = int(input("masukan tahun lahir anda      "))

tanggal_lahir = dt.date(tahun, bulan, tanggal)
print(f"tannggal lahir anda andalah {tanggal_lahir}")

# di  dalam bahasa pemogramn python kita bisa menghitung umur mengunakan dt time
# contoh penggunaannya adalah sebagai berikut
import datetime as dt
tanggal_lahir = dt.date(2006, 12, 12)
hari_ini = dt.date.today()
umur = hari_ini - tanggal_lahir
print(f"umur anda adalah {umur.days} hari")

# mecari panjang umur dalam bentukk tahun
umur_dalam_tahun = umur.days // 365 # arti dari // adalah pembagian bulat
print(f"umur anda adalah {umur_dalam_tahun} tahun")

# mencari sisa bulan dari umur
sisa_hari = umur.days % 365
sisa_bulan = sisa_hari // 30
print(f"umur anda adalah {sisa_bulan} bulan")



