import math

def  Mencari_panjang_vektor(x1,x2,y1,y2):
    deltaX_pangkat2 = (x2 - x1)**2
    deltaY_pangkat_2 = (y2 - y1)**2
    
    Hasil_perhitungan_jarak = math.sqrt(deltaX_pangkat2 + deltaY_pangkat_2)
    return Hasil_perhitungan_jarak


print(Mencari_panjang_vektor(1,5,1,4))
