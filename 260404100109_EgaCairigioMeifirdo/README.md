# 📋 Sistem Penilaian dan Kelulusan Peserta Pelatihan Coding

> **Tugas Individu — Pelatihan Coding**
> Mata Pelajaran : Pemrograman Dasar (Python)

| Info       | Detail                     |
|------------|----------------------------|
| **Nama**   | Ega Cairigio Meifirdo      |
| **NIM**    | 260404100109               |
| **File**   | `penilaian_peserta.py`     |
| **Bahasa** | Python 3                   |

---

## 📌 Deskripsi Program

Program ini merupakan sistem sederhana untuk **menghitung nilai akhir** dan **menentukan status kelulusan** peserta pelatihan coding berdasarkan bobot penilaian dan persentase kehadiran yang telah ditentukan.

---

## ⚙️ Cara Kerja Program

### 1. Rumus Nilai Akhir

Program menghitung nilai akhir menggunakan rumus berbobot berikut:

```
Nilai Akhir = (Nilai Tugas × 30%) + (Nilai Kuis × 20%) + (Nilai Ujian × 50%)
```

| Komponen      | Bobot |
|---------------|-------|
| Nilai Tugas   | 30%   |
| Nilai Kuis    | 20%   |
| Nilai Ujian   | 50%   |

---

### 2. Logika Penentuan Status

Program menggunakan `if`, `elif`, dan `else` dengan alur berikut:

```
Kehadiran < 75%
    └─► TIDAK LULUS (langsung, tanpa cek nilai)

Kehadiran >= 75%
    ├─► Nilai Akhir >= 85 DAN Kehadiran >= 80%  → Lulus dengan Predikat A
    ├─► Nilai Akhir >= 75 DAN Kehadiran >= 80%  → Lulus dengan Predikat B
    ├─► Nilai Akhir >= 65 DAN Kehadiran >= 75%  → Lulus dengan Predikat C
    └─► (selain kondisi di atas)                → Tidak Lulus
```

| Status                   | Syarat Nilai Akhir | Syarat Kehadiran |
|--------------------------|--------------------|------------------|
| Lulus dengan Predikat A  | ≥ 85               | ≥ 80%            |
| Lulus dengan Predikat B  | ≥ 75               | ≥ 80%            |
| Lulus dengan Predikat C  | ≥ 65               | ≥ 75%            |
| Tidak Lulus              | Tidak memenuhi syarat di atas         |
| Tidak Lulus *(paksa)*    | Kehadiran < 75% (nilai apapun)        |

---

## 🚀 Cara Menjalankan Program

### Persyaratan
- Python 3 sudah terinstall di komputer

### Langkah-langkah

1. Buka terminal / command prompt
2. Masuk ke folder program:
   ```bash
   cd 260404100109_EgaCairigioMeifirdo
   ```
3. Jalankan program:
   ```bash
   python penilaian_peserta.py
   ```

---

## 💡 Contoh Penggunaan

### Input
```
========================================
   Tugas Individu - Pelatihan Coding
========================================
Nama peserta  : Amar
Nilai tugas   : 80
Nilai kuis    : 75
Nilai ujian   : 90
Kehadiran (%) : 85
```

### Proses Perhitungan
```
Nilai Akhir = (80 × 0.30) + (75 × 0.20) + (90 × 0.50)
            = 24.0 + 15.0 + 45.0
            = 84.0
```

### Output
```
==============================
     HASIL PENILAIAN
==============================
Nama         : Amar
Nilai Akhir  : 84.0
Kehadiran    : 85%
Status       : Lulus dengan Predikat B
==============================
```

---

## 🗂️ Struktur File

```
260404100109_EgaCairigioMeifirdo/
├── penilaian_peserta.py   ← Program utama
└── README.md              ← Dokumentasi ini
```

---

## 🧱 Konsep Python yang Digunakan

| Konsep               | Implementasi dalam Program                          |
|----------------------|-----------------------------------------------------|
| Variabel             | `nama_peserta`, `nilai_tugas`, `nilai_akhir`, dll.  |
| Tipe Data            | `str` untuk nama, `float` untuk nilai & kehadiran   |
| Operator Aritmatika  | `*` dan `+` untuk menghitung nilai akhir berbobot   |
| Operator Logika      | `and` untuk gabungan kondisi nilai & kehadiran      |
| Percabangan          | `if`, `elif`, `else` untuk menentukan status        |
| Konstanta            | `BOBOT_TUGAS`, `BATAS_NILAI_A`, dll. (UPPER_CASE)  |
| f-string             | Format output `f"Nilai Akhir : {nilai_akhir:.1f}"`  |
| Fungsi Built-in      | `input()`, `float()`, `print()`                     |

---

*Dibuat untuk memenuhi Tugas Individu Pelatihan Coding — 2026*
