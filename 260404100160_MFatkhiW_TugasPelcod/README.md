# Penjelasan Program pelcod.py

Program ini berfungsi untuk menghitung nilai akhir peserta berdasarkan nilai tugas, nilai kuis, dan nilai ujian. Setelah itu, program juga menghitung persentase kehadiran dan menentukan status kelulusan berdasarkan aturan yang telah dibuat.

## 1. Tujuan Program

Program ini dibuat untuk:
- menerima data peserta,
- menghitung nilai akhir sesuai bobot yang ditentukan,
- menghitung persentase kehadiran,
- menentukan kelulusan dan predikat berdasarkan nilai serta kehadiran,
- menampilkan hasil penilaian ke layar.

## 2. Input yang Dimasukkan

Program meminta user untuk memasukkan beberapa data, yaitu:
- Nama peserta
- Nilai tugas
- Nilai kuis
- Nilai ujian
- Jumlah kehadiran (0-16)

Berikut bentuk inputnya:

```python
nama_peserta = input("Masukkan Nama Peserta: ")
nilai_tugas = float(input("Masukkan Nilai Tugas: "))
nilai_kuis = float(input("Masukkan Nilai Kuis: "))
nilai_ujian = float(input("Masukkan Nilai Ujian: "))
kehadiran = int(input("Masukkan Jumlah Kehadiran (0-16): "))
```

## 3. Perhitungan Nilai Akhir

Pada program ini, nilai akhir dihitung dengan bobot sebagai berikut:
- Nilai tugas = 30%
- Nilai kuis = 20%
- Nilai ujian = 50%

Rumus yang digunakan:

```python
nilai_akhir = (nilai_tugas * 30/100) + (nilai_kuis * 20/100) + (nilai_ujian * 50/100)
```

Artinya:
- nilai tugas memiliki bobot 30%
- kuis memiliki bobot 20%,
- ujian memiliki bobot 50%,

## 4. Perhitungan Persentase Kehadiran

Program menghitung presentase kehadiran dengan membandingkan jumlah kehadiran terhadap total 16 pertemuan.

```python
kehadiran_persen = (kehadiran / 16) * 100
```

Contoh:
- jika kehadiran = 12, maka

```python
(12 / 16) * 100 = 75%
```

Persentase inilah yang dipakai untuk menentukan apakah peserta memenuhi syarat kehadiran.

## 5. Logika Penentuan Status Kelulusan

Program menggunakan struktur `if`, `elif`, dan `else` untuk mengecek kelulusan.

### Kondisi pertama
```python
if kehadiran_persen < 75:
    grade = "Tidak Lulus karena kehadiran kurang dari 75%"
```

Jika persentase kehadiran kurang dari 75%, maka peserta otomatis dinyatakan tidak lulus meskipun nilai akhir tinggi.

### Kondisi kedua
```python
elif nilai_akhir >= 85 and kehadiran_persen >= 80:
    grade = "Lulus dengan predikat A"
```

Jika nilai akhir minimal 85 dan kehadiran minimal 80%, peserta dinyatakan lulus dengan predikat A.

### Kondisi ketiga
```python
elif nilai_akhir >= 75 and kehadiran_persen >= 80:
    grade = "Lulus dengan predikat B"
```

Jika nilai akhir minimal 75 dan kehadiran minimal 80%, peserta dinyatakan lulus dengan predikat B.

### Kondisi keempat
```python
elif nilai_akhir >= 65 and kehadiran_persen >= 75:
    grade = "Lulus dengan predikat C"
```

Jika nilai akhir minimal 65 dan kehadiran minimal 75%, peserta dinyatakan lulus dengan predikat C.

### Kondisi terakhir
```python
else:
    grade = "Tidak Lulus"
```

Jika peserta tidak memenuhi syarat-syarat di atas, maka statusnya adalah tidak lulus.

## 6. Output Program

Setelah semua perhitungan selesai, program menampilkan hasilnya dengan format seperti berikut:

```python
print("\nHasil Penilaian:")
print(f"Nama Peserta: {nama_peserta}")
print(f"Nilai Tugas: {nilai_tugas}")
print(f"Nilai Kuis: {nilai_kuis}")
print(f"Nilai Ujian: {nilai_ujian}")
print(f"Persentase Kehadiran: {kehadiran} ({kehadiran_persen:.2f}%)")
print(f"Nilai Akhir: {nilai_akhir:.2f}")
print(f"Status Kelulusan: {grade}")
```

Output yang tampil meliputi:
- nama peserta,
- nilai tugas,
- nilai kuis,
- nilai ujian,
- persentase kehadiran,
- nilai akhir,
- status kelulusan.

## 7. Kesimpulan

Program ini adalah contoh sederhana pemrograman Python untuk mengevaluasi hasil belajar peserta. Dengan kombinasi antara perhitungan bobot nilai dan aturan kehadiran, program dapat menentukan apakah peserta lulus atau tidak dan memberikan predikat yang sesuai.

## 8. Catatan

Program ini masih sederhana dan belum dilengkapi dengan validasi input yang ketat, misalnya:
- nilai tidak boleh negatif,
- kehadiran tidak boleh lebih dari 16,
- input harus berupa angka.

Namun secara umum, program ini sudah dapat menjalankan fungsi utama penilaian dan keputusan kelulusan dengan baik.
