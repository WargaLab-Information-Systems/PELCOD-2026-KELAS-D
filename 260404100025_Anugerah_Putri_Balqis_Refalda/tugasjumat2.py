data_peserta=(input("data peserta:"))
nilai_tugas=int(input("nilai tugas:"))
nilai_kuis=int(input("nilai kuis:"))
nilai_ujian=int(input("nilai ujian:"))
nilai_kehadiran=int(input("nilai kehadiran:"))

print("---HASIL PENILAIAN----\n")

print("nama  :",data_peserta)
nilai_akhir=(nilai_tugas*30/100)+(nilai_kuis*20/100)+(nilai_ujian*50/100)
print("nilai akhir=", nilai_akhir)
print("kehadiran =",nilai_kehadiran, "%")

if nilai_kehadiran <75:
    print("status = tidak lulus")
elif nilai_akhir >= 85 and nilai_kehadiran>=80:
    status="lulus dengan predikat A"
elif nilai_akhir>= 75 and nilai_kehadiran>=80:
    status="lulus dengsn prdikat B"
elif nilai_akhir>=65 and nilai_kehadiran>=75:
    status="lulus dengan predikat C"
else:
    status ="tidak lulus"

print("status=",status)


