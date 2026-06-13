# =========================================================================
# File Utama  : matriks.py
# Deskripsi   : File pengujian untuk mengimpor modul gyoga112
# =========================================================================

import gyoga112

# Inisialisasi Matriks untuk Pengujian
Matriks_X = [
    [1, 2],
    [3, 4]
]

Matriks_Y = [
    [5, 6],
    [7, 8]
]

Matriks_Persegi_3x3 = [
    [4, 2, 1],
    [0, 5, 3],
    [1, 1, 6]
]

print("=== PENGUJIAN MODUL STRUKTUR DATA (GYOGA SYAPUTRA) ===\n")

# 1. Uji Perkalian Matriks
print("1. Perkalian Matriks X dan Y:")
hasil_kali = gyoga112.perkalian_matriks(Matriks_X, Matriks_Y)
gyoga112.cetak_matriks(hasil_kali)

# 2. Uji Transpose Matriks
print("\n2. Transpose Matriks X:")
hasil_transpose = gyoga112.transpose_matriks(Matriks_X)
gyoga112.cetak_matriks(hasil_transpose)

# 3. Uji The Trace Operator 
print("\n3. Trace Matriks Persegi 3x3 (Jumlah diagonal utama: 4+5+6):")
hasil_trace = gyoga112.trace_matriks(Matriks_Persegi_3x3)
gyoga112.cetak_matriks(hasil_trace)

# 4. Uji Determinan 
print("\n4. Determinan Matriks X (1x4 - 2x3):")
hasil_determinan = gyoga112.determinan_2x2(Matriks_X)
gyoga112.cetak_matriks(hasil_determinan)
