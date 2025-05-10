import os
import PyPDF2

def cari_kata_kunci_di_folder(folder_path, kata_kunci):
    # List semua file PDF di folder
    semua_file = [f for f in os.listdir(folder_path) if f.lower().endswith('.pdf')]

    if not semua_file:
        print("Tidak ada file PDF di folder ini.")
        return

    for nama_file in semua_file:
        path_lengkap = os.path.join(folder_path, nama_file)
        halaman_ditemukan = []

        try:
            with open(path_lengkap, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                jumlah_halaman = len(pdf_reader.pages)

                for i in range(jumlah_halaman):
                    halaman = pdf_reader.pages[i]
                    teks = halaman.extract_text()

                    if teks and kata_kunci.lower() in teks.lower():
                        halaman_ditemukan.append(i + 1)

            if halaman_ditemukan:
                print(f'📄 "{nama_file}" → Kata kunci "{kata_kunci}" ditemukan di halaman: {halaman_ditemukan}')
            else:
                print(f'📄 "{nama_file}" → Kata kunci tidak ditemukan.')

        except Exception as e:
            print(f'❌ Gagal membaca "{nama_file}": {e}')

# === Contoh penggunaan ===
folder_path = r'C:\Users\Acer\Downloads\printy3'  # Ganti dengan path ke folder PDF kamu
kata_kunci = 'saltpeter'          # Ganti dengan kata kunci yang kamu cari

cari_kata_kunci_di_folder(folder_path, kata_kunci)
