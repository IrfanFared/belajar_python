a = 10
b = 9

c = a | b
print(c) #asilnya adalah 1011 dalam biner, yang sama dengan 11 dalam desimal.
print(format(a,"08b"))
#Kenapa hasilnya 00001010?

#10 dalam biner adalah 1010
#Karena kita minta 8 digit ("08b")
#Sistem akan menambah 0000 di depan
#Sehingga menjadi 00001010
print("AND (&) - Menghasilkan 1 jika kedua bit adalah 1")
a = 12  # 1100
b = 10  # 1010
c = a & b
print(f"a =       {format(a,'08b')} ({a})")
print(f"b =       {format(b,'08b')} ({b})")
print(f"a & b =   {format(c,'08b')} ({c})")
# Output: 
# a =       00001100 (12)
# b =       00001010 (10)
# a & b =   00001000 (8)

print("OR (|) - Menghasilkan 1 jika salah satu bit adalah 1")
a = 12  # 1100
b = 10  # 1010
c = a | b
print(f"a =       {format(a,'08b')} ({a})")
print(f"b =       {format(b,'08b')} ({b})")
print(f"a | b =   {format(c,'08b')} ({c})")
# Output:
# a =       00001100 (12)
# b =       00001010 (10)
# a | b =   00001110 (14)

print("XOR (^) - Menghasilkan 1 jika bit berbeda")
a = 12  # 1100
b = 10  # 1010
c = a ^ b
print(f"a =       {format(a,'08b')} ({a})")
print(f"b =       {format(b,'08b')} ({b})")
print(f"a ^ b =   {format(c,'08b')} ({c})")
# Output:
# a =       00001100 (12)
# b =       00001010 (10)
# a ^ b =   00000110 (6)