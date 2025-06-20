biodata = {"nama": "irfan","nomer" : "23"}


#jika kita ingin mencopy data dictionary tanpa mengubah asal variabel

biodata_new = biodata.copy

#menghpus key pada dictionary

hapus_data_istri = biodata.pop("Istri")
print(biodata) # ini akan menghapus key pada dictionary 

#ada juga kta kunci .popitem yang menghapus ket terakhir
