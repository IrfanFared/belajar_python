# cara membuat list di dalam python
list_kosong = []

#data tipen number
kupulan_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#data tipe string
kumpulan_string = ["Irfan", "claudia"]

# kumpulan data bolean 

kumpulan_data_bollean = [True,False,True,False]
 
 #kumpulan data capuran
kumpulan_data_campuaran = [1, "irfan", True, 2.5]

#cara cepat membuat list

data_range = range(1, 10)
print(list(data_range))

# membuat list dengan foor loop 

list_dengan_for_loop =  [i**10 for i in range(1,20)]
print(list_dengan_for_loop)

#membuat list dengan if

list_dengan_if = [i for i in range(1,20) if i % 2 == 0]

#Mengambil data di list

nama = ["irfan","claudia","dewi","dewa","dewo"]
data1 = nama[1]
print(data1)

#mengambil panjang data atau jumlah data di list
panjang_data = len(nama)
print(panjang_data)

# menambahakan data pada list ke n
#list.insert(index, nilai)

nama.insert(1,"irfan ganten")
