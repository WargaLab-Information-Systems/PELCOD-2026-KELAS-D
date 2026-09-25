#Penilaian dan Kelulusan Mahasiswa

#Data Mahasiswa
nama = ("Fenny Eka Saputri")

nilai_tugas = (80)
nilai_kuis = (75)
nilai_ujian = (90)
kehadiran = (85)

nilai_akhir = (nilai_tugas*0.30) + (nilai_kuis*0.20) + (nilai_ujian*0.50)

if kehadiran < 75:
    status = "Tidak Lulus"
elif nilai_akhir > 85 and kehadiran >=80:
    status = "lulus predikat A"
elif  nilai_akhir >= 75 and kehadiran >= 80:
    status = "lulus predikat B"
elif nilai_akhir_akhir > 65 and kehadiran >=75:
    status = "lulus predikat C"
else:
    status = "tidak lulus"

print("hasil penilaian")
print(("Nama          :", nama))
print(("Nilai Akhir :",nilai_akhir))
print(("Kehadiran :",str(kehadiran) + "%"))
print(("Status :",status))

