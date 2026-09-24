data_peserta= ("alda")

print("data_peserta")
nama= input("data_peserta =")

nilai_tugas=int(input("nilai_tugas:"))
if nilai_tugas >= 75:
    print("lulus")
else: 
    print("tidak lulus")

nilai_kuis=75
nilai_kuis=int(input("nilai_kuis:"))
kuis=75
if kuis >=60:
    print("lulus")
else:
    print("tidak lulus")

nilai_ujian=90
nilai_ujian=int(input("nilai_ujian:"))
ujian=90
if ujian >70:
    print("lulus")
else :
    print("tidak lulus")

nilai_kehadiran=int(input("kehadiran:"))
if nilai_kehadiran >=85 :
    print("lulus")
else:
    print("tidak lulus")

nilai_akhir = (nilai_tugas*30/100)+(nilai_kuis *20/100)+(nilai_ujian +50/100)
print("nilai_akhir=",nilai_akhir)

nilai_tugas=80
if nilai_tugas <75:
    print("angka positif")
elif nilai_tugas >75:
    print("angka negatif")
else:
    print("angka 75")

nilai_kuis=75
if nilai_kuis <60:
    print("angka positif")
elif nilai_kuis >60:
    print("angka negatif")
else:
    print("angka 60")

nilai_ujian=90
if nilai_ujian<80:
    print("angka positif")
elif nilai_ujian >80:
    print("angka negatif")
else:
    print("angka 60")

nilai_kehadiran=85
if nilai_kehadiran <85:
    print("angka positif")
elif nilai_kehadiran >85:
    print("angka negatif")
