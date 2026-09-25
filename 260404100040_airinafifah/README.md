# Sistem Penilaian Pelatihan Coding

| ---------------------- | --------------------------------- |
| **Nama**               | Airin Afifah                      |
| **NIM**                | 260404100040                      |
| **Mata Kuliah**        | Algoritma dan Pemrograman         |
| **Tugas**              | Tugas Individu — Pelatihan Coding |
| ---------------------- | --------------------------------- |

## Deskripsi Program

Program ini merupakan program Python sederhana yang digunakan untuk menentukan hasil penilaian dan status kelulusan seorang peserta.

Program menerima beberapa data dari pengguna, yaitu:
-Nama peserta
-Nilai tugas
-Nilai kuis
-Nilai ujian
-Persentase kehadiran

Setelah data dimasukkan, program menghitung nilai akhir berdasarkan bobot nilai tugas, kuis, dan ujian. Selanjutnya, program menentukan status kelulusan peserta berdasarkan nilai akhir dan persentase kehadiran.

### ⚖️ Bobot Nilai

| Komponen    | Bobot |
| ----------- | ----: |
| Nilai Tugas |   30% |
| Nilai Kuis  |   20% |
| Nilai Ujian |   50% |

### Kriteria Kelulusan

| Kondisi                              | Status      |
| ------------------------------------ | ----------- |
| Nilai akhir ≥ 85 dan kehadiran ≥ 80% | A           |
| Nilai akhir ≥ 75 dan kehadiran ≥ 80% | B           |
| Nilai akhir ≥ 65 dan kehadiran ≥ 75% | C           |
| Kehadiran < 75%                      | Tidak Lulus |
| Kondisi lainnya                      | Tidak Lulus |

## Cara Kerja Program

1. Memasukkan Nama Peserta
nama = input("nama peserta : ")

Program meminta pengguna memasukkan nama peserta. Data tersebut disimpan ke dalam variabel nama.

2. Memasukkan Nilai Tugas
nilai_tugas = float(input("nilai tugas : "))

Program meminta nilai tugas. Fungsi float() digunakan agar input dapat disimpan sebagai angka, termasuk jika terdapat nilai desimal.

3. Memasukkan Nilai Kuis
nilai_kuis = float(input("nilai kuis : "))

Nilai kuis dimasukkan oleh pengguna dan disimpan dalam variabel nilai_kuis.

4. Memasukkan Nilai Ujian
nilai_ujian = float(input("nilai ujian : "))

Nilai ujian dimasukkan oleh pengguna dan disimpan dalam variabel nilai_ujian.

5. Memasukkan Kehadiran
kehadiran = float(input("kehadiran : "))

Program meminta persentase kehadiran peserta dan menyimpannya dalam variabel kehadiran.

6. Menghitung Nilai Akhir
nilai_akhir = (nilai_tugas * 0.30) + (nilai_kuis * 0.20) + (nilai_ujian * 0.50)

Nilai akhir dihitung menggunakan bobot yang sudah ditentukan.

Nilai tugas dikalikan 0.30, nilai kuis dikalikan 0.20, dan nilai ujian dikalikan 0.50. Kemudian ketiga hasil tersebut dijumlahkan.

Rumusnya:

Nilai Akhir = (Nilai Tugas × 30%) + (Nilai Kuis × 20%) + (Nilai Ujian × 50%)

7. Mengecek Kehadiran
if kehadiran < 75:
    status = "Tidak Lulus"

Kondisi pertama mengecek apakah kehadiran kurang dari 75%.

Jika benar, status peserta langsung menjadi Tidak Lulus.

8. Menentukan Predikat A
elif nilai_akhir >= 85 and kehadiran >= 80:
    status = "inih kewren bangetsss dapet nilai A"

Jika kondisi sebelumnya tidak terpenuhi, program mengecek kondisi ini.

Peserta mendapatkan status A jika:

Nilai akhir minimal 85
Kehadiran minimal 80%

Operator and berarti kedua kondisi tersebut harus terpenuhi.

9. Menentukan Predikat B
elif nilai_akhir >= 75 and kehadiran >= 80:
    status = "horeww  lulus nilai B"

Peserta mendapatkan status B jika:

Nilai akhir minimal 75
Kehadiran minimal 80%

Kedua kondisi harus terpenuhi karena menggunakan operator and.

10. Menentukan Predikat C
elif nilai_akhir >= 65 and kehadiran >= 75:
    status = "ini juga kewren kok nilai C"

Peserta mendapatkan status C jika:

Nilai akhir minimal 65
Kehadiran minimal 75%
11. Kondisi Selain Itu
else:
    status = "Tidak Lulus"

else dijalankan jika semua kondisi sebelumnya tidak terpenuhi.

Artinya, peserta tidak memenuhi persyaratan untuk mendapatkan predikat A, B, atau C.

12. Menampilkan Hasil
print("hasil penilaian")
print("Nama :", nama)
print("Nilai Akhir :", nilai_akhir)
print("Kehadiran :", str(kehadiran) + "%")
print("Status :", status)

Bagian ini digunakan untuk menampilkan hasil program.

str(kehadiran) digunakan untuk mengubah nilai kehadiran menjadi teks sehingga dapat digabungkan dengan simbol %.

## Contoh Output

nama peserta : Airin Afifah
nilai tugas : 90
nilai kuis : 85
nilai ujian : 90
kehadiran : 90

hasil penilaian
Nama : Airin Afifah
Nilai Akhir : 89.0
Kehadiran : 90.0%
Status : inih kewren bangetsss dapet nilai A

## Konsep Python yang Digunakan

Program ini menggunakan beberapa konsep dasar Python:

* `input()` → menerima data dari pengguna.
* `float()` → mengubah input menjadi angka desimal.
* Variabel → menyimpan data peserta.
* Operator `*` → menghitung bobot nilai.
* Operator `+` → menjumlahkan nilai.
* Operator `<` dan `>=` → membandingkan nilai.
* Operator `and` → memastikan dua kondisi terpenuhi.
* `if` → mengecek kondisi pertama.
* `elif` → mengecek kondisi berikutnya.
* `else` → menangani kondisi yang tidak memenuhi seluruh syarat.
* `print()` → menampilkan hasil program.

## Penjelasan Singkat

Program dimulai dengan meminta pengguna memasukkan nama, nilai tugas, nilai kuis, nilai ujian, dan kehadiran. Setelah semua data dimasukkan, program menghitung nilai akhir menggunakan bobot masing-masing komponen.

Selanjutnya, program melakukan pengecekan kondisi menggunakan `if`, `elif`, dan `else`. Kehadiran diperiksa terlebih dahulu karena peserta yang memiliki kehadiran di bawah 75% langsung dinyatakan tidak lulus. Jika syarat tersebut tidak terpenuhi, program melanjutkan pengecekan untuk menentukan predikat A, B, atau C.

Setelah status ditentukan, program menampilkan nama peserta, nilai akhir, kehadiran, dan status kelulusan.