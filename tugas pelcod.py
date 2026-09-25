nama = "Intan Dwi Lestari"
nilai_tugas = (80)
nilai_kuis = (75)
nilai_ujian = (90)
kehadiran = (85)

nilai_akhir = (nilai_tugas * 0.30) + (nilai_kuis * 0.20) + (nilai_ujian * 0.50)

if kehadiran < 75:
    status = "Tidak Lulus"
elif nilai_akhir > 85 and kehadiran >= 80:
    status = "Lulus Predikat A"
elif nilai_akhir >= 75 and kehadiran >= 80:
    status = "Lulus Predikat B"
elif nilai_akhir > 65 and kehadiran >= 75:
    status = "Lulus Predikat C"
else:
    status = "Tidak Lulus"

print("HASIL PENILAIAN")
print(f"Nama        : {nama}")
print(f"Nilai Akhir : {nilai_akhir:.2f}")
print(f"Kehadiran   : {kehadiran}%")
print(f"Status      : {status}")

