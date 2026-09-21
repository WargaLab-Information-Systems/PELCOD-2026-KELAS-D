nama_peserta = input("Masukkan Nama Peserta: ")
nilai_tugas = float(input("Masukkan Nilai Tugas: "))
nilai_kuis = float(input("Masukkan Nilai Kuis: "))
nilai_ujian = float(input("Masukkan Nilai Ujian: "))
kehadiran = int(input("Masukkan Jumlah Kehadiran (0-16): "))

nilai_akhir = (nilai_tugas * 30/100) + (nilai_kuis * 20/100) + (nilai_ujian * 50/100)
kehadiran_persen = (kehadiran / 16) * 100

if kehadiran_persen < 75:
    grade = "Tidak Lulus karena kehadiran kurang dari 75%"
elif nilai_akhir >= 85 and kehadiran_persen >= 80:
    grade = "Lulus dengan predikat A"
elif nilai_akhir >= 75 and kehadiran_persen >= 80:
    grade = "Lulus dengan predikat B"
elif nilai_akhir >= 65 and kehadiran_persen >= 75:
    grade = "Lulus dengan predikat C"
else:
    grade = "Tidak Lulus"

print("\nHasil Penilaian:")
print(f"Nama Peserta: {nama_peserta}")
print(f"Nilai Tugas: {nilai_tugas}")
print(f"Nilai Kuis: {nilai_kuis}")
print(f"Nilai Ujian: {nilai_ujian}")
print(f"Persentase Kehadiran: {kehadiran} ({kehadiran_persen:.2f}%)")
print(f"Nilai Akhir: {nilai_akhir:.2f}")
print(f"Status Kelulusan: {grade}")