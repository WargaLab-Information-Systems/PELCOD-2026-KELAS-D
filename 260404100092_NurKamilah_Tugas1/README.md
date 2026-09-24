nama_peserta = "Seokjin" ##input nama peserta, menggunakan tipe data string karna berupa haruf dan menggunakan tanda kutip
nilai_tugas = 80  ##input nilai tugas menggunakan tipe data integer
nilai_kuis = 75  ##input nilai kuis menggunakan tipe data integer
nilai_ujian = 80  ##input nilai ujian menggunakan tipe data integer
kehadiran = 85  ##input kehadiran menggunakan tipe data integer

nilai_akhir = (nilai_tugas*0.30) + (nilai_kuis*0.20) + (nilai_ujian*0.50)
## hitung nilai akhir menggunakan operator aritmatika, nilai tugas dikali bobot nilai tugas,berlaku juga untuk nilai kuis dan nilai ujian

if kehadiran < 75:
    status = "tidak lulus" ##jika kehadiran kurang dari 75, maka tidak memenuhi syarat kelulusan dan status menjadi tidak lulus
elif nilai_akhir >= 85 and kehadiran >= 80:
    status = "Lulus dengan Predikat A"  ##jika nilai akhir lebih atau sama dengan 85 dan kehadiran lebih atau sama dengan 80, status nya adalah lulus dengan predikat A
elif nilai_akhir >= 75 and kehadiran >= 80:
    status = "Lulus dengan Predikat B"
elif nilai_akhir >= 65 and kehadiran >= 75:
    status = "Lulus dengan Predikat C"
else : ### jika semua syarat di atas tidak terpenuhi status akan dinyatakan tidak lulus
    status = "tidak lulus"


### hasil output dari program di atas
## menampilkan judul "hasil penilaian", nama peserta, nilai akhir, kehadiran, dan status
print("---Hasil Penilaian---") 
print("Nama         : ", nama_peserta)
print("Nilai Akhir  : ", nilai_akhir)
print("Kehadiran    : ", kehadiran)
print("Status       : ", status)
