## PENJELASAN PROGRAM PENILAIAN PESERTA

# Input Data (Baris 1-5)
nama_peserta = input("Nama peserta : ")
nilai_tugas = float(input("Nilai tugas : "))
nilai_kuis = float(input("Nilai kuis  : "))
nilai_ujian = float(input("Nilai ujian : "))
kehadiran = float(input("Kehadiran   : "))

Users diminta memasukkan nama (string) dan empat nilai numerik (tugas,kuis,ujian,kehadiran). Fungsi float() 
digunakan agar input yang berupa angka desimal bisa diproses sebagai angka, bukan teks.

# Perhitungan Nilai Akhir (Baris 8)
nilai_akhir = (nilai_tugas * 0.30) + (nilai_kuis * 0.20) + (nilai_ujian * 0.50)

Nantinya nilai akhir akan dihitung dari rata-rata bobotnya:
1. tugas berkontribusi 30%
2. kuis berkontribusi 20%
3. ujian berkontribusi 50%

Contoh, Jika
tugas=80
kuis=90
ujian=75 --> (80*0.3)+(90*0.2)+(75*0.5) = 24+18+37.5
                                        =79.5

# Penetuan Status (Baris 10-19)
if kehadiran < 75:
    status = "Tidak Lulus"
elif nilai_akhir >= 85 and kehadiran >= 80:
    status = "Lulus dengan Predikat A"
elif nilai_akhir >= 75 and kehadiran >= 80:
    status = "Lulus dengan Predikat B"
elif nilai_akhir >= 65 and kehadiran >= 75:
    status = "Lulus dengan Predikat C"
else:
    status = "Tidak Lulus"

Logika ini dicek berurutan dari atas ke bawah (begitu satu kondisi terpenuhi, langsung berhenti)

1. Jika kehadiran dibawah 75% --> langsung "Tidak Lulus"
2. Jika lolos syarat kehadiran, bary di cek nilai akhir untuk menentukan predikat A,B,C --- masing-masing predikat punya ambang batas kehadiran sendiri;
Predikat A dan B butuh >80% dan predikat C cukup >75%
3. Jika tidak ada kondisi kelulusan yang cocok, misal nilai akhir di bawah 65 maka hasilnya "Tidak Lulus".

# Ouput (Baris 21-25)
print("\n=== HASIL PENILAIAN ===")
print(f"Nama        : {nama_peserta}")
print(f"Nilai Akhir : {nilai_akhir}")
print(f"Kehadiran   : {int(kehadiran)}%")
print(f"Status      : {status}")

Menampilkan hasil dalam format yang sudah rapih menggunakan f-string. int(kehadiran) membulatkan kehadiran ke bilangan bulat (misal 85.0-->85) agar tampilan lebih rapih tanpa desimal
