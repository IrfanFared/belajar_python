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
# terkadan ada kassus dimana kita mengunakan backslas si mesin bingug yang dimana ini user pakai basckslas tapi kok ngak asa petik satu 
# untuk itu kita bisa gunakan mengunakan double backslas seperti contoh di bawhah ini

tanggal_lahir = "12\\12\\2006"
print(tanggal_lahir)
tanggal_lahir = "12\21\2008" #outpu bakal anomali
print(tanggal_lahir)

#bakslas + t = tab pada string
backslas_sebagai_tab = "tab\t menjauh \t\t lebih banyak tab"
print(backslas_sebagai_tab)

# fungsi backslas  menjadi backspace jika diletakan di depan huruf atau kata hanya mengunaka satu back slash di tambah huruf b

backslas_sebagai_backspace = "halao \bini_irfan"
print(backslas_sebagai_backspace)

#membuata baris ke-n mengunakan backslas + n

fungsi_backslash_untuk_membuat_newline = "ini adalah baris pertama. \n ini adalah baris kedua "
print(fungsi_backslash_untuk_membuat_newline)

#Raw string di gunakan  untu menghindaras kesalahn intrepretasi karakter backslas.
#kareana karakter backslass sangatlah unik 
# Raw string sangat berguna karena karak terkhusus seperti backslas diangga[ string  jika mengunakan raw string

raw_string = r"c\folder Irfan ganteng\fota nika bersama violet" 
print(raw_string)

#multilane stirng digunakan untuk membuat baris di banyak baris
#contoh

print("""" halo
Nama saya : Irfan
Saya pacarnya cludia
Saya suaminya violet
Hatiku hanya buat violet seorang saja ya 
      """)

#didalam bahasa pemograman python multiline dan raw string bisa di gabung jadi satu
#contoh 

print(
r"""
Halo kid
ini adalah foler foto papah sama mamah violet waktu muda c\foto waktu sma\
"""
)