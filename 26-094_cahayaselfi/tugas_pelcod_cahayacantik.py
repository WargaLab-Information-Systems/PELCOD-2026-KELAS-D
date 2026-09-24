nama = input("Nama Peserta : ")
nilai_tugas = float(input("nilai tugas : "))
nilai_kuis = float(input("nilai kuis : "))
nilai_ujian = float(input("nilai ujian : "))
jumlah_kehadiran = float (input("jumlah kehadiran : "))

nilai_akhir = (nilai_tugas * 0.30) + (nilai_kuis * 0.20) + (nilai_ujian * 0.50)

if jumlah_kehadiran < 75:
    status = "Tidak Lulus"
elif nilai_akhir >= 85 and jumlah_kehadiran >= 80:
    status = "Lulus dengan Predikat A"
elif nilai_akhir >= 75 and jumlah_kehadiran >= 80:
    status = "Lulus dengan Predikat B"
elif nilai_akhir >= 65 and jumlah_kehadiran >= 75:
    status = "Lulus dengan Predikat C"
else:
    status = "Tidak Lulus"

print("\n===== HASIL PENILAIAN =====")
print(f"Nama         : {nama}")
print(f"Nilai Akhir  : {nilai_akhir}")
print(f"Kehadiran    : {jumlah_kehadiran}%")
print(f"Status       : {status}")
