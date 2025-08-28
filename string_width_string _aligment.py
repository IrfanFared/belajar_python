# with dan multilane string adalah fitur yang memungkinkan kita untuk menulis string dalam beberapa baris


# didalam bahasa pemograman python ada yang namanya  multilane string 
nama = "Irfan"
no_absen = 21
kelas = "XII"
umur = 21

print(f"\n nama saya adalah {nama},\n no absen saya adalah {no_absen},\n kelas saya adalah {kelas},\n umur saya adalah {umur}")


# didalam bahasa pemograman python ada yang namanya multilane string mengunakan kutip 3
nama = "Irfan"  
no_absen = 21
kelas = "XII"   
umur = 21
print(f"""
nama saya adalah {nama},    
no absen saya adalah {no_absen},
kelas saya adalah {kelas},
umur saya adalah {umur}
""")

import textwrap
text = """Irfan adalah orang yanga sangat tampan dan ganteng.
di sukai banyak oranga jadinya dia jadi sombong dan angkuh.
tapi dia tetap baik dan ramah kepada semua oranga"""
print(textwrap.fill(text, width=100))

#text wrap adalah fungsi yang digunakan untuk membungkus teks menjadi beberapa baris dengan lebar tertentu

text= "halo  semua nama saya irfan.Hari ini saya mencoba untuk selalu bertanya ketika dosen menjelaskan materi"
print(textwrap.fill(text,width = 10))

print("Irfan pacarnya violet evergarden \n irfan ganteng gg cuy")