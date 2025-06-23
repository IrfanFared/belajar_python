# apa itu default fungsi di python
# # default argument adalah nilai yang sudah ditentukan sebelumnya untuk parameter fungsi
# jika kita tidak memberikan nilai pada parameter tersebut saat memanggil fungsi, makan nilai default akan digunakan

# bagaumana untu sytaksis default argument
# def nama_fungsi(parameter1=nilai_default1, parameter2=nilai_default2):
#contoh

def biodata  (nama,pacar = "claudia"):
  
    print(f"halo{nama} dan pacar saya adalh {pacar}")

biodata("irfan") # jika mengisi parameter kedua makan akan otomatis mengunakan parameter default
