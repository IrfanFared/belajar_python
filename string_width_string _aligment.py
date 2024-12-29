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
text = """Irfan adalaha oranga yanga sangant tampan dan ganteng.
di sukai banyak oranga jadinya dia jadi sombong dan angkuh.
tapi dia tetap baik dan ramah kepada semua oranga"""
print(textwrap.fill(text, width=50))