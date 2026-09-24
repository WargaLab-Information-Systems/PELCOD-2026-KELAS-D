# data peserta dan input nilai peserta
nama= input("nama peserta:")
nilai_tugas= float(input("nilai tugas:"))
nilai_kuis= float(input("nilai kuis:"))
nilai_ujian= float(input("nilai ujian:"))
nilai_kehadiran= float(input("nilai kehadiran :"))

# menghitung nilai akhir berdasarkan bobot
# ujian = 50% , nilai kuis = 20% , nilai tugas = 30%
nilai_akhir = (nilai_tugas * 0.30) + (nilai_kuis * 0.20) + (nilai_ujian * 0.50)

#status dan predikat
if nilai_kehadiran < 75 :
    status = "maaf anda tidak lulus."
elif nilai_kehadiran >= 80 and nilai_akhir >= 85:
    status = "selamat anda lulus, dengan predikat A"
elif nilai_kehadiran >= 80 and nilai_akhir >= 75:
    status ="selamat anda lulus, dengan predikat B"
elif nilai_kehadiran >= 75 and nilai_akhir >= 65:
    status = "selamat anda lulus, dengan predikat C"
else:
    status = "tidak lulus"

#hasil penelitian
print("----hasil penelitian----")
print(f"nama            : {nama}")
print(f"nilai akhir     : {nilai_akhir}")
print(f"kehadiran       : {nilai_kehadiran}")
print(f"status          : {status}")