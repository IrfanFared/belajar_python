#-didalam sebuah bahasa pemograman python kita bisa mengambil imput dari usser

nama = input("masuka nama ada:")

print(nama, "anda ganteng sekali pasti pacarnya chitoge")

umur = int(input("masukan umur anga:")) # -Irfan ini akan erro jika kita memasuakan data string karena kita membuat kode dimana mengsyaratakan data int makaa akan errro jika kita memasukaan data string
print("umur anda adalah :", umur)

#bagaimana dengan input data bolleaan 
#cara jika kita meminta imput data bolean kita perlu casting tipe data(convert),
#dari bolean ket int .karena angka 0 menghasilkan nilasi false dan angka 1 menghsilkan nilai tru

pertanyaan_pacar = bool(int(input('apakah kamu suka waguri jika iya ketik 1 jika tidak kerik 0')))

print(pertanyaan_pacar)

#-Irfan secara difault input dair kita bertipe string 