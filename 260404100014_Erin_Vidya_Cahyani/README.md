
##  Kode Program (`main.py`)

python
# Input data peserta
nama = input("Nama peserta : ")
nilai_tugas = float(input("Nilai tugas : "))
nilai_kuis = float(input("Nilai kuis  : "))
nilai_ujian = float(input("Nilai ujian : "))
kehadiran = float(input("Kehadiran   : "))

# Menghitung nilai akhir berdasarkan bobot
nilai_akhir = (nilai_tugas * 0.30) + (nilai_kuis * 0.20) + (nilai_ujian * 0.50)

# Menentukan status dan predikat kelulusan
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

# Menampilkan hasil penilaian
print("\n=== HASIL PENILAIAN ===")
print(f"Nama        : {nama}")
print(f"Nilai Akhir : {nilai_akhir}")
print(f"Kehadiran   : {int(kehadiran)}%")
print(f"Status      : {status}")
```

---

##  Rumus & Aturan Penilaian

### 1. Bobot Perhitungan Nilai Akhir
$$\text{Nilai Akhir} = (\text{Tugas} \times 30\%) + (\text{Kuis} \times 20\%) + (\text{Ujian} \times 50\%)$$

### 2. Syarat Kelulusan & Predikat
* **Syarat Mutlak**: Jika kehadiran **kurang dari 75%**, peserta **otomatis Tidak Lulus** (tanpa melihat nilai akhir).
* **Predikat A**: Nilai Akhir $\ge 85$ **DAN** Kehadiran $\ge 80\%$.
* **Predikat B**: Nilai Akhir $\ge 75$ **DAN** Kehadiran $\ge 80\%$.
* **Predikat C**: Nilai Akhir $\ge 65$ **DAN** Kehadiran $\ge 75\%$.
* **Tidak Lulus**: Jika nilai atau kehadiran tidak memenuhi syarat di atas.

---

## Cara Menjalankan Program

### Prasyarat
Pastikan komputer kamu sudah terinstal **Python 3**.

### Langkah-Langkah:
1. Simpan kode program di atas ke dalam file berformat `.py`, misalnya `main.py`.
2. Buka **Terminal** (Mac/Linux) atau **Command Prompt / PowerShell** (Windows).
3. Jalankan perintah berikut:
   ```bash
   python main.py
   ```
4. Masukkan data sesuai petunjuk di layar.


## Contoh Penggunaan

### Input yang Diisi:
```text
Nama peserta : Amar
Nilai tugas : 80
Nilai kuis  : 75
Nilai ujian : 90
Kehadiran   : 85
```

### Output yang Dihasilkan:
```text
=== HASIL PENILAIAN ===
Nama        : Amar
Nilai Akhir : 83.5
Kehadiran   : 85%
Status      : Lulus dengan Predikat B
```

1. **`input()`**: Digunakan untuk meminta ketikan teks dari pengguna melalui layar terminal.
2. **`float()`**: Mengubah teks input angka menjadi desimal (berkoma) agar bisa dihitung secara akurat secara matematis.
3. **`if` - `elif` - `else`**: Struktur percabangan/keputusan. Program mengecek syarat dari atas ke bawah secara berurutan.
4. **`and`**: Operator logika yang mewajibkan **kedua kondisi sekaligus** terpenuhi.
5. **`f"..."` (f-string)**: Cara praktis dan rapi untuk menyisipkan nilai variabel ke dalam teks output.