# -Irfan di dalam sebuah bahasa pemograman python kiata bisa mengubah tipe data 
# kala di bahasa pemograman python nama casting tipe data

nilai_siswa = 12
print(nilai_siswa,type(nilai_siswa))


#ini adalah cara mengubah dtipe data di bahasa pemograman python
nilai_siswa_to_string = str(nilai_siswa)
print(type(nilai_siswa_to_string))

nilai_siswa_to_float = float(nilai_siswa)
print(type(nilai_siswa_to_float))

nilai_siswa_to_bollean = bool(nilai_siswa)
print(nilai_siswa_to_bollean,type(nilai_siswa_to_bollean)) #akan false jika nilai 0 akana tru jika nila selain o

nilai_ujian = 12.9

nilai_akhir = int(nilai_ujian) #jika kita mengubah tipe data dari float ke int maka anggka setelah koma akan di abaikan alias diaggap tidak ada
print(nilai_akhir,type(nilai_ujian))