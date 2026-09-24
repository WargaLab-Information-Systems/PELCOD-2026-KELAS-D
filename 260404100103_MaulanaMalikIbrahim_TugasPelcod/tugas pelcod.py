nama = input("Masukkan nama peserta:")
nilai_tugas = float(input("Masukkan nilai tugas: "))
nilai_kuis = float(input("masukkan nilai kuis:"))
nilai_ujian = float (input("masukkan nilai ujian:"))
kehadiran = float (input("masukkan persentase kehadiran (%): "))

##bobot : tugas 30%, kuis 20%, ujian 50%
nilai_akhir = (nilai_tugas * 0.3) + (nilai_kuis * 0.2) + (nilai_ujian * 0.5)

if kehadiran < 75:
    status = "tidak lulus"

elif nilai_akhir >= 85 and kehadiran >= 0.8:
    status = "lulus dengan predikat A"

elif nilai_akhir >= 75 and kehadiran >= 0.8:
    status = "lulus dengan predikat B"

elif nilai_akhir >= 65 and kehadiran >= 0.75:
    status = "lulus dengan predikat C"

else:
    status = "tidak lulus"

print( "\n" + "="*30)
print(" HASIL PENILAIAN PESERTA" )
print("="*30)
print(f"nama peserta              : {nama}")
print(f"nilai akhir               : {nilai_akhir:.2f}")
print(f"persentase kehadiran      : {kehadiran:.2f}%")
print(f"status kelulusan          : {status}")
print("="*30)
