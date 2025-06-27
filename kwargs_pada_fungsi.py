# apa kwargs
# kwargs adalah singkatan dari keyword arguments yang digunakan untuk mengirimakan argemunt ke dalam fungsi
# dengan nama pareneternya 
# kwargs adalah sebuah dictionary yang berisi pasangan nama parameter dan nilai argumen  yang diberikan
# kwargs ini sama seperti args hanya saja bisa ditambahkan key
# kalo kita menulis args dengan bitang satung di dalam kurung sedankan jika kwargs bisa mengunakan bintang 2



def formulir (**kwaargs):
    for key , value in kwaargs.items():
        print(f"urutan ke {key} fasil pengisian formulir")


formulir(nama = "irfan", umur = 12)