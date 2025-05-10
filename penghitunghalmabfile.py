import os
from PyPDF2 import PdfReader

def hitung_halaman(pdf_file):
    """Menghitung jumlah halaman dalam sebuah file PDF"""
    reader = PdfReader(pdf_file)
    return len(reader.pages)

# Folder tempat PDF berada (Ganti dengan lokasi folder PDF kamu)
folder_pdf = r"C:\Users\Acer\Downloads\printy3"

# Variabel untuk menyimpan total halaman
total_halaman = 0

# Loop semua file dalam folder
print("Menghitung jumlah halaman untuk setiap file PDF...\n")
for file in os.listdir(folder_pdf):
    if file.endswith(".pdf"):  # Pastikan hanya membaca file PDF
        file_path = os.path.join(folder_pdf, file)
        jumlah_halaman = hitung_halaman(file_path)
        total_halaman += jumlah_halaman  # Tambahkan ke total halaman
        print(f"{file}: {jumlah_halaman} halaman")

# Menampilkan total semua halaman
print("\n========================================")
print(f"Total seluruh halaman dari semua file PDF: {total_halaman} halaman")
print("========================================")
