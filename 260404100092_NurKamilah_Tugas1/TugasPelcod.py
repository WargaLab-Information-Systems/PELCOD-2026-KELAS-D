nama_peserta = "Seokjin"
nilai_tugas = 80
nilai_kuis = 75
nilai_ujian = 90
kehadiran = 85

nilai_akhir = (nilai_tugas*0.30) + (nilai_kuis*0.20) + (nilai_ujian*0.50)

if kehadiran < 75:
    status = "tidak lulus"
elif nilai_akhir >= 85 and kehadiran >= 80:
    status = "Lulus dengan Predikat A"
elif nilai_akhir >= 75 and kehadiran >= 80:
    status = "Lulus dengan Predikat B"
elif nilai_akhir >= 65 and kehadiran >= 75:
    status = "Lulus dengan Predikat A"
else : 
    status = "tidak lulus"



print("---Hasil Penilaian---")
print("Nama         : ", nama_peserta)
print("Nilai Akhir  : ", nilai_akhir)
print("Kehadiran    : ", kehadiran)
print("Status       : ", status)
