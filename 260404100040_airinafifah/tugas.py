# Sistem Penilaian Pelatihan Coding
# ---------------------------------------------------------------------------
# Nama      : Airin Afifah
# NIM       : 260404100040
# Tugas     : Pelatihan Coding
# ----------------------------------------------------------------------------

## Menyimpan data peserta
nama = input("Nama peserta : ")
nilai_tugas = float(input("Nilai tugas : "))
nilai_kuis = float(input("Nilai kuis : "))
nilai_ujian = float(input("Nilai ujian : "))
kehadiran = float(input("Kehadiran : "))

## Menghitung nilai akhir berdasarkan bobot
nilai_akhir = (nilai_tugas * 0.30) + (nilai_kuis * 0.20) + (nilai_ujian * 0.50)

## Menentukan status kelulusan
if kehadiran < 75:
    status = "Tidak Lulus"
elif nilai_akhir >= 85 and kehadiran >= 80:
    status = "inih kewren bangetsss dapet nilai A"
elif nilai_akhir >= 75 and kehadiran >= 80:
    status = "horew lulus nilai B"
elif nilai_akhir >= 65 and kehadiran >= 75:
    status = "ini juga kewren kok nilai C"
else:
    status = "Tidak Lulus"

## Menampilkan hasil penilaian
print("\n===== HASIL PENILAIAN =====")
print("Nama :", nama)
print("Nilai Akhir :", nilai_akhir)
print("Kehadiran :", str(kehadiran) + "%")
print("Status :", status)