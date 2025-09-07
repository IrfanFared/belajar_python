# password asli
Pasword_asli = "irfan"

# password tebakan
pasword_tebakan = "irfan"

persen_kemiripan = 0

# Menggunakan enumerate untuk mendapatkan indeks dan nilai sekaligus
for indeks, char_asli in enumerate(Pasword_asli):
    # Pastikan tebakan punya panjang yang sama atau lebih
    if indeks < len(pasword_tebakan):
        # Membandingkan karakter di indeks yang sama
        if char_asli == pasword_tebakan[indeks]:
            persen_kemiripan += 1
    # Jika tebakan lebih pendek, berhenti
    else:
        break

print(persen_kemiripan)