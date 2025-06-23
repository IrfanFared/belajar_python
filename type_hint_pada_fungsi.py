from typing import Union

#type  hint (type anotation) adalah sebuah fitu di python yang memukinkan kita untuk
# - menambahkan keteranagan pada parameter  atau memberi tanda tipe data parameter
 # type hint anotation juga digunakan untu return value

# ini adalah sebuah contoh dari type hint 

def biodata (nama : str, nomer : int) -> str: # sebuah tanda pana tidak  tapi lebih baik dikasi saja karean memudah python dan  pembaca memahami kode
            return f"halo nama saya {nama} dan {nomer} " # setelah pana dikasih none jika tidak mengmbaikan nilai

# fungsi type anotatio 1.memudahkan untuk debug dan pembacaan bagi komputer,2.memudahkan untu kerja tim


# type hint di python bisa juga untuk memberi tanda pada parameter dengan lebih dari dua tipe data
# mengunakan kata kunci union tapi kita harus import dulu package union contoh import ada pada line atas

def biodata_new (umur : Union[int,float] ) -> int :
        return f"halo  saya {umur} "

#ada cara lain juga ketika kita ingin memberi tanda parameter untuk lebih dari dua tipe data

def tampila ( isi : int | float | str):
        print(f"{isi}")

