
import rafi053

# Data matriks untuk pengujian
matriks_A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matriks_B = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

print("=== PENGUJIAN MODUL rafi053 ===")

# 1. Menguji fungsi transpose
print("\n1. Hasil Transpose Matriks A:")
hasil_transpose = rafi053.transpose_matriks(matriks_A)
for baris in hasil_transpose:
    print(baris)

# 2. Menguji fungsi penjumlahan
print("\n2. Hasil Penjumlahan Matriks A dan B:")
hasil_jumlah = rafi053.penjumlahan_matriks(matriks_A, matriks_B)
for baris in hasil_jumlah:
    print(baris)

# 3. Menguji fungsi perkalian
print("\n3. Hasil Perkalian Matriks A dan B:")
hasil_kali = rafi053.perkalian_matriks(matriks_A, matriks_B)
for baris in hasil_kali:
    print(baris)