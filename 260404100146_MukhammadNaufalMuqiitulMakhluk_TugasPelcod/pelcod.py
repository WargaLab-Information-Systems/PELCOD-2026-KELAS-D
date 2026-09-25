nama = input("Nama peserta   : ")
tugas = float(input("Nilai tugas    : "))
kuis = float(input("Nilai kuis     : "))
ujian = float(input("Nilai ujian    : "))
kehadiran = float(input("Kehadiran      : "))

# Menghitung nilai akhir
nilai_akhir = (tugas * 0.30) + (kuis * 0.20) + (ujian * 0.50)

if kehadiran < 75:
    status = "Tidak Lulus"
elif nilai_akhir >= 85 and kehadiran >= 80:
    status = "Lulus dengan Predikat A"
elif nilai_akhir >= 75 and kehadiran >= 80:
    status = "Lulus dengan Predikat B"
elif nilai_akhir >= 65 and kehadiran >= 75:
    status = "Lulus dengan Predikat C"
else:
    status = "Tidak Lulus"

# Hasil
print()
print("===== HASIL PENILAIAN =====")
print("Nama           :", nama)
print("Nilai Akhir    :", nilai_akhir)
print("Kehadiran      :", kehadiran, "%")
print("Status         :", status)