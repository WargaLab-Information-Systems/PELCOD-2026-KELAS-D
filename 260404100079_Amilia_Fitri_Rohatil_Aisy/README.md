# Sistem Penilaian dan Kelulusan Mahasiswa

Dokumentasi dan penjelasan untuk skrip Python sederhana yang digunakan untuk menghitung nilai akhir serta menentukan status kelulusan peserta pelatihan *coding*.

---

## 📋 Deskripsi Proyek

Proyek ini bertujuan untuk mengolah data penilaian peserta pelatihan berdasarkan beberapa komponen:
* **Nilai Tugas** (Bobot 30%)
* **Nilai Kuis** (Bobot 20%)
* **Nilai Ujian** (Bobot 50%)
* **Kehadiran** (Persentase %)

Program menentukan status kelulusan peserta berdasarkan kriteria nilai akhir dan batas minimum kehadiran yang dipersyaratkan.

---

## ⚙️ Cara Kerja Program

Program ini bekerja melalui 4 tahapan utama:

1. **Input Data**
   * Mengambil nama peserta (`string`).
   * Mengambil input angka untuk nilai tugas, kuis, ujian, dan persentase kehadiran (`float`).

2. **Kalkulasi Nilai Akhir**
   * Menghitung nilai akhir menggunakan formula berikut:
     $$\text{Nilai Akhir} = (\text{Tugas} \times 0.30) + (\text{Kuis} \times 0.20) + (\text{Ujian} \times 0.50)$$

3. **Evaluasi Logika Kelulusan (`if-elif-else`)**
   * **Aturan Utama (Syarat Kehadiran Mutlak):** Jika kehadiran $< 75\%$, peserta otomatis **Tidak Lulus** tanpa memandang seberapa tinggi nilai akhirnya.
   * **Predikat A:** Nilai Akhir $\ge 85$ **DAN** Kehadiran $\ge 80\%$.
   * **Predikat B:** Nilai Akhir $\ge 75$ **DAN** Kehadiran $\ge 80\%$.
   * **Predikat C:** Nilai Akhir $\ge 65$ **DAN** Kehadiran $\ge 75\%$.
   * **Tidak Lulus:** Semua kondisi yang tidak memenuhi syarat di atas.

4. **Output Hasil**
   * Menampilkan ringkasan hasil penilaian berisi nama, nilai akhir, persentase kehadiran, dan status kelulusan peserta.

---

## 🚀 Cara Menjalankan Program

### Prasyarat
* Python versi 3.x atau yang lebih baru sudah terpasang di komputer Anda.

### Langkah-langkah
1. Simpan kode ke dalam sebuah file, contohnya `main.py`.
2. Buka Terminal atau Command Prompt (CMD).
3. Jalankan perintah berikut:
   ```bash
   python main.py
   ```
4. Masukkan input sesuai instruksi pada layar.

---

## 💡 Contoh Penggunaan

### Contoh Input:
```text
Nama Peserta: Amar
Nilai Tugas: 80
Nilai kuis: 75
Nilai ujian: 90
Kehadiran: 85
```

### Contoh Output:
```text
HASIL PENILAIAN
Nama        : Amar
Nilai Akhir : 83.5
Kehadiran   : 85%
Status      : Lulus dengan Predikat B
```