# =========================================================================
# File Module : gyoga112.py
# Nama        : Gyoga Syaputra
# NPM         : 2515061112
# Deskripsi   : Modul Aljabar Matriks (Perkalian, Transpose, Trace, Determinan)
# =========================================================================

def perkalian_matriks(matriks_A, matriks_B):
    """Fungsi untuk mengalikan dua matriks (Matrix Operations)."""
    baris_A = len(matriks_A)
    kolom_A = len(matriks_A[0])
    baris_B = len(matriks_B)
    kolom_B = len(matriks_B[0])

    if kolom_A != baris_B:
        return "Error: Syarat perkalian gagal (Kolom A != Baris B)."

    hasil = [[0 for _ in range(kolom_B)] for _ in range(baris_A)]

    for i in range(baris_A):
        for j in range(kolom_B):
            for k in range(kolom_A):
                hasil[i][j] += matriks_A[i][k] * matriks_B[k][j]
    return hasil

def transpose_matriks(matriks):
    """Fungsi untuk melakukan transpose matriks (baris menjadi kolom)."""
    baris = len(matriks)
    kolom = len(matriks[0])
    
    hasil = []
    for j in range(kolom):
        baris_baru = []
        for i in range(baris):
            baris_baru.append(matriks[i][j])
        hasil.append(baris_baru)
    return hasil

def trace_matriks(matriks):
    """
    Fungsi The Trace Operator (Materi 46).
    Menghitung jumlah elemen pada diagonal utama matriks persegi.
    """
    baris = len(matriks)
    kolom = len(matriks[0])

    if baris != kolom:
        return "Error: Trace hanya bisa dihitung pada matriks persegi (n x n)."

    total_trace = 0
    for i in range(baris):
        total_trace += matriks[i][i] 
    
    return total_trace

def determinan_2x2(matriks):
    """
    Fungsi Matrix Determinants (Materi 35).
    Menghitung determinan khusus untuk matriks ordo 2x2.
    """
    baris = len(matriks)
    kolom = len(matriks[0])

    if baris != 2 or kolom != 2:
        return "Error: Fungsi ini khusus untuk matriks ordo 2x2."
    
    a = matriks[0][0]
    b = matriks[0][1]
    c = matriks[1][0]
    d = matriks[1][1]
    
    return (a * d) - (b * c)

def cetak_matriks(matriks):
    """Fungsi pembantu untuk menampilkan list 2D menjadi bentuk matriks."""
    if isinstance(matriks, str) or isinstance(matriks, int) or isinstance(matriks, float):
        print(matriks)
    else:
        for baris in matriks:
            print(baris)
