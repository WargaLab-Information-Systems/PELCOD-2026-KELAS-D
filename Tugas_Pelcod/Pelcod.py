nama_peserta = input("Nama peserta : ")
nilai_tugas = float(input("Nilai tugas : "))
nilai_kuis = float(input("Nilai kuis  : "))
nilai_ujian = float(input("Nilai ujian : "))
kehadiran = float(input("Kehadiran   : "))

# Tugas (30%), Kuis (20%), Ujian (50%)
nilai_akhir = (nilai_tugas * 0.30) + (nilai_kuis * 0.20) + (nilai_ujian * 0.50)

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

print("\n=== HASIL PENILAIAN ===")
print(f"Nama        : {nama_peserta}")
print(f"Nilai Akhir : {nilai_akhir}")
print(f"Kehadiran   : {int(kehadiran)}%")
print(f"Status      : {status}")