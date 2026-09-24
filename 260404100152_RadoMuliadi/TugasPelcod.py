"""
Program Sistem Penilaian dan Kelulusan Peserta Pelatihan Coding
Menghitung nilai akhir dan menentukan status kelulusan berdasarkan
nilai tugas, kuis, ujian, dan persentase kehadiran.
"""

# ===== INPUT DATA PESERTA =====
nama_peserta = input("Nama peserta   : ")
nilai_tugas = float(input("Nilai tugas    : "))
nilai_kuis = float(input("Nilai kuis     : "))
nilai_ujian = float(input("Nilai ujian    : "))
kehadiran = float(input("Kehadiran (%)  : "))

# ===== BOBOT PENILAIAN =====
BOBOT_TUGAS = 0.30
BOBOT_KUIS = 0.20
BOBOT_UJIAN = 0.50

# ===== PERHITUNGAN NILAI AKHIR =====
nilai_akhir = (nilai_tugas * BOBOT_TUGAS) + (nilai_kuis * BOBOT_KUIS) + (nilai_ujian * BOBOT_UJIAN)

# ===== PENENTUAN STATUS KELULUSAN =====
if kehadiran < 75:
	# Kehadiran di bawah 75% langsung dinyatakan Tidak Lulus
	status = "Tidak Lulus"
elif nilai_akhir >= 85 and kehadiran >= 80:
	status = "Lulus dengan Predikat A"
elif nilai_akhir >= 75 and kehadiran >= 80:
	status = "Lulus dengan Predikat B"
elif nilai_akhir >= 65 and kehadiran >= 75:
	status = "Lulus dengan Predikat C"
else:
	status = "Tidak Lulus"

# ===== MENAMPILKAN HASIL =====
print("\n===== HASIL PENILAIAN =====")
print(f"Nama         : {nama_peserta}")
print(f"Nilai Akhir  : {nilai_akhir:.1f}")
print(f"Kehadiran    : {kehadiran:.0f}%")
print(f"Status       : {status}")
