# Program Penilaian Peserta (Student Grading System)

Program Python sederhana untuk menghitung nilai akhir peserta berdasarkan bobot komponen tertentu serta menentukan status kelulusan berdasarkan nilai akhir dan persentase kehadiran.

## Fitur Utama

- **Input Interaktif**: Menerima input nama, nilai tugas, nilai kuis, nilai ujian, dan persentase kehadiran dari pengguna.
- **Perhitungan Nilai Berbobot**:
  - Tugas: 30%
  - Kuis: 20%
  - Ujian: 50%
- **Evaluasi Kelulusan & Predikat**:
  - Memeriksa syarat minimum kehadiran (< 75% otomatis tidak lulus).
  - Menentukan predikat nilai (A, B, C) atau status tidak lulus berdasarkan kombinasi nilai akhir dan kehadiran.
- **Format Output Rapi**: Menampilkan ringkasan hasil penilaian dalam bentuk tabel teks yang terstruktur.

## Aturan Penilaian (Grading Rules)

1. **Kehadiran**: Jika persentase kehadiran di bawah 75% (`< 75`), peserta dinyatakan **tidak lulus** terlepas dari berapa nilai akhirnya.
2. **Predikat A**: Nilai akhir $\ge 85$ dan kehadiran $\ge 80\%$ (`0.8`).
3. **Predikat B**: Nilai akhir $\ge 75$ dan kehadiran $\ge 80\%$ (`0.8`).
4. **Predikat C**: Nilai akhir $\ge 65$ dan kehadiran $\ge 75\%$ (`0.75`).
5. **Tidak Lulus**: Jika tidak memenuhi ambang batas di atas.

*(Catatan: Pastikan memasukkan input kehadiran dalam bentuk persentase, misal `80` untuk 80%).*

## Cara Menjalankan Program

1. Pastikan Anda telah menginstal Python di komputer Anda.
2. Salin kode program ke dalam file baru, misalnya `penilaian.py`.
3. Jalankan perintah berikut di terminal atau command prompt:

```bash
python penilaian.py
```

4. Ikuti instruksi yang muncul di layar untuk memasukkan data peserta.