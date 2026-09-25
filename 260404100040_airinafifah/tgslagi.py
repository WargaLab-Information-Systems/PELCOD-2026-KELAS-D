# Sistem Penilaian Peserta Pelatihan Coding
# --------------------------------------------------------
# Nama                   :Airin Afifah
# NIM                    :260404100040
# Mata Kuliah           :Algoritma dan Pemrograman
# Tugas                 :Tugas Individu — Pelatihan Coding
# --------------------------------------------------------

nama = input("nama peserta : ")
nilai_tugas = float(input("nilai tugas : "))
nilai_kuis = float(input("nilai kuis : "))
nilai_ujian = float(input("nilai ujian : "))
kehadiran = float(input("kehadiran : "))
nilai_akhir = (nilai_tugas * 0.30) + (nilai_kuis * 0.20) + (nilai_ujian * 0.50)

if kehadiran < 75:
    status = "Tidak Lulus"
elif nilai_akhir >= 85 and kehadiran >= 80:
    status = "enih kewren bangetsss dapet nilai A"
elif nilai_akhir >= 75 and kehadiran >= 80:
    status = "horeww  lulus nilai B"
elif nilai_akhir >= 65 and kehadiran >= 75:
    status = "ini juga kewren kok nilai C"
else:
    status = "Tidak Lulus"

print("hasil penilaian")
print("Nama :", nama)
print("Nilai Akhir :", nilai_akhir)
print("Kehadiran :", str(kehadiran) + "%")
print("Status :", status)