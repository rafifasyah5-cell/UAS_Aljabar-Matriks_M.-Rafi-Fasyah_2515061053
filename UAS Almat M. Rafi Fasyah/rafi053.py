

def transpose_matriks(matriks):
    """Fungsi untuk melakukan transpose matriks (mengubah baris menjadi kolom)."""
    baris = len(matriks)
    kolom = len(matriks[0])
    
    hasil = [[0 for _ in range(baris)] for _ in range(kolom)]
    
    for i in range(baris):
        for j in range(kolom):
            hasil[j][i] = matriks[i][j]
            
    return hasil


def penjumlahan_matriks(matriks1, matriks2):
    """Fungsi untuk menjumlahkan dua buah matriks dengan ordo yang sama."""
    if len(matriks1) != len(matriks2) or len(matriks1[0]) != len(matriks2[0]):
        return "Error: Ordo matriks tidak sama, penjumlahan tidak dapat dilakukan."
    
    baris = len(matriks1)
    kolom = len(matriks1[0])
    
    hasil = [[0 for _ in range(kolom)] for _ in range(baris)]
    
    for i in range(baris):
        for j in range(kolom):
            hasil[i][j] = matriks1[i][j] + matriks2[i][j]
            
    return hasil


def perkalian_matriks(matriks1, matriks2):
    """Fungsi untuk menghitung perkalian antar dua matriks."""
    if len(matriks1[0]) != len(matriks2):
        return "Error: Jumlah kolom matriks pertama tidak sama dengan jumlah baris matriks kedua."
    
    baris_m1 = len(matriks1)
    kolom_m1 = len(matriks1[0])
    kolom_m2 = len(matriks2[0])
    
    hasil = [[0 for _ in range(kolom_m2)] for _ in range(baris_m1)]
    
    for i in range(baris_m1):
        for j in range(kolom_m2):
            for k in range(kolom_m1):
                hasil[i][j] += matriks1[i][k] * matriks2[k][j]
                
    return hasil