# =============================================================================
# Sistem Penilaian dan Kelulusan Peserta Pelatihan Coding
# Nama    : Ega Cairigio Meifirdo
# NIM     : 260404100109
# =============================================================================

# ──────────────────────────────────────────────
# KONSTANTA BOBOT PENILAIAN
# ──────────────────────────────────────────────
BOBOT_TUGAS = 0.30   # 30%
BOBOT_KUIS = 0.20   # 20%
BOBOT_UJIAN = 0.50   # 50%

# ──────────────────────────────────────────────
# KONSTANTA BATAS KELULUSAN
# ──────────────────────────────────────────────
BATAS_KEHADIRAN_MINIMUM = 75    # kehadiran < 75% -> langsung Tidak Lulus
BATAS_KEHADIRAN_BC = 80    # kehadiran >= 80% -> syarat Predikat A / B
BATAS_NILAI_A = 85
BATAS_NILAI_B = 75
BATAS_NILAI_C = 65


# ──────────────────────────────────────────────
# INPUT DATA PESERTA
# ──────────────────────────────────────────────
print("=" * 40)
print("   Tugas Individu - Pelatihan Coding")
print("=" * 40)

nama_peserta = input("Nama peserta  : ")
nilai_tugas = float(input("Nilai tugas   : "))
nilai_kuis = float(input("Nilai kuis    : "))
nilai_ujian = float(input("Nilai ujian   : "))
kehadiran = float(input("Kehadiran (%) : "))


# ──────────────────────────────────────────────
# PERHITUNGAN NILAI AKHIR
# ──────────────────────────────────────────────
nilai_akhir = (
    (nilai_tugas * BOBOT_TUGAS) +
    (nilai_kuis  * BOBOT_KUIS)  +
    (nilai_ujian * BOBOT_UJIAN)
)


# ──────────────────────────────────────────────
# PENENTUAN STATUS KELULUSAN
# ──────────────────────────────────────────────
if kehadiran < BATAS_KEHADIRAN_MINIMUM:
    # Aturan no. 5 - kehadiran < 75% -> langsung Tidak Lulus
    status = "Tidak Lulus"

elif nilai_akhir >= BATAS_NILAI_A and kehadiran >= BATAS_KEHADIRAN_BC:
    # Aturan no. 1
    status = "Lulus dengan Predikat A"

elif nilai_akhir >= BATAS_NILAI_B and kehadiran >= BATAS_KEHADIRAN_BC:
    # Aturan no. 2
    status = "Lulus dengan Predikat B"

elif nilai_akhir >= BATAS_NILAI_C and kehadiran >= BATAS_KEHADIRAN_MINIMUM:
    # Aturan no. 3
    status = "Lulus dengan Predikat C"

else:
    # Aturan no. 4
    status = "Tidak Lulus"


# ──────────────────────────────────────────────
# TAMPILAN HASIL AKHIR
# ──────────────────────────────────────────────
print()
print("=" * 30)
print("     HASIL PENILAIAN")
print("=" * 30)
print(f"Nama         : {nama_peserta}")
print(f"Nilai Akhir  : {nilai_akhir:.1f}")
print(f"Kehadiran    : {kehadiran:.0f}%")
print(f"Status       : {status}")
print("=" * 30)
