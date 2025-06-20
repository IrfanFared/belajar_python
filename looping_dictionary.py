# didalam python kita juga bisa melakukan looping pada dictionary.

my_bioadata = {"Nama" : "irfan","Istri":"claudia"}


#ini digunakan hanya untuk perulangan key
for key in my_bioadata:
    print(f"{key}")

#atau bisa gunakan kata kunci .keys

for kunci in my_bioadata.keys():
    print(kunci)


#kalo ini digunakan untuk lopping value dengan .values

for value in my_bioadata.values():
    print(value)


#ada cara dimana kita bisa looping dengan key dan velue secara bersaman

for key, velue  in my_bioadata.items():
    print(f"ini adalah {key} dan {velue}")


#menghpus key pada dictionary

hapus_data_istri = my_bioadata.pop("Istri")
print(my_bioadata) # ini akan menghapus key pada dictionary 

#ada juga kta kunci .popitem yang menghapus ket terakhir

