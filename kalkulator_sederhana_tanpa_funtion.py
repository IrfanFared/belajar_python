print("kaklualator sederhana tanpa funtion")

operator = input("masukan operator + - * / : ")
angka1 = int(input("masukan angka pertama :"))
angka2 = int(input("masukan angka kedua : "))

if operator == "+":
    print(f"hasil penjumlahan {angka1} + {angka2} = {angka1 + angka2}")
elif operator == "-":
    print(f"hasil pengurangan {angka1} - {angka2} = {angka1 - angka2}")
else:
    print("operator tidak dikenal")