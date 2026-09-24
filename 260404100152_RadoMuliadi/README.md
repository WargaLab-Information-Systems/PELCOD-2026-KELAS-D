# 🎓 Panduan Program Penilaian Peserta Coding (Versi Super Pemula)

Halo! Selamat datang! Artikel ini bakal ngejelasin cara kerja program Python kamu dengan cara yang sangat simpel dan gampang dibayangkan. 

---

## 💡 Apa sih Kegunaan Program Ini?

Bayangin kamu lagi jadi **guru** di kelas coding. Program ini tugasnya mirip seperti **kalkulator pintar** yang membantu kamu untuk:
1. Nanya nama dan nilai siswa.
2. Hitung gabungan nilainya otomatis.
3. Cek apakah siswanya rajin masuk kelas atau tidak.
4. Nentuin apakah siswanya **Lulus** (dapat nilai A, B, atau C) atau **Tidak Lulus**.

---

## 🧱 Bagian-Bagian Penting di Dalam Kode

Mari kita bedah kodenya satu per satu:

### 1. Nanya-nanya ke Pengguna (`input`)
```python
nama_peserta = input("Nama peserta   : ")
nilai_tugas = float(input("Nilai tugas    : "))
...
```
* **Apa maksudnya?** 
  Program bakal memunculkan pertanyaan di layar dan nungguin kamu mengetik jawaban.
* **Kenapa pakai `float(...)`?** 
  Supaya komputer tahu bahwa jawaban yang kamu ketik itu berupa **angka yang bisa ada komanya** (misal: `85.5`), bukan sekadar tulisan biasa.

---

### 2. Menyiapkan "Bumbu" Resep (`BOBOT`)
```python
BOBOT_TUGAS = 0.30
BOBOT_KUIS = 0.20
BOBOT_UJIAN = 0.50
```
* **Apa maksudnya?**
  Nilai akhir itu tidak cuma ditambah begitu saja, tapi ada porsinya masing-masing:
  * 📝 **Tugas:** menyumbang $30\%$ ($0.30$) dari total nilai.
  * ✏️ **Kuis:** menyumbang $20\%$ ($0.20$) dari total nilai.
  * 🧪 **Ujian:** menyumbang $50\%$ ($0.50$) dari total nilai (paling besar!).

---

### 3. Menghitung Nilai Akhir
```python
nilai_akhir = (nilai_tugas * BOBOT_TUGAS) + (nilai_kuis * BOBOT_KUIS) + (nilai_ujian * BOBOT_UJIAN)
```
* **Cara kerjanya:**
  Komputer mengalikan setiap nilai dengan porsi bobotnya, lalu semuanya dijumlahkan untuk dapat satu **Nilai Akhir**.

---

### 4. Aturan Kelulusan (`if`, `elif`, `else`)
Bagian ini seperti **pos pemeriksaan tempat wisata**:

```python
if kehadiran < 75:
    status = "Tidak Lulus"
```
* 🛑 **Aturan Utama (Syarat Absen):** Jika hadirnya kurang dari $75\%$, komputer langsung bilang **"Tidak Lulus"** tanpa peduli berapa pun nilai ujiannya.

```python
elif nilai_akhir >= 85 and kehadiran >= 80:
    status = "Lulus dengan Predikat A"
```
* 🌟 **Predikat A:** Jika nilai akhir minimal $85$ **DAN** hadirnya minimal $80\%$.

```python
elif nilai_akhir >= 75 and kehadiran >= 80:
    status = "Lulus dengan Predikat B"
```
* 👍 **Predikat B:** Jika nilai akhir minimal $75$ **DAN** hadirnya minimal $80\%$.

```python
elif nilai_akhir >= 65 and kehadiran >= 75:
    status = "Lulus dengan Predikat C"
```
* 👌 **Predikat C:** Jika nilai akhir minimal $65$ **DAN** hadirnya minimal $75\%$.

```python
else:
    status = "Tidak Lulus"
```
* ❌ **Lainnya:** Kalau tidak memenuhi kriteria di atas, berarti **Tidak Lulus**.

---

### 5. Menampilkan Hasil ke Layar (`print`)
```python
print(f"Nama         : {nama_peserta}")
print(f"Nilai Akhir  : {nilai_akhir:.1f}")
...
```
* **Apa maksudnya?**
  Komputer mencetak hasil akhirnya ke layar.
* **Trik Rahasia `{nilai_akhir:.1f}`:**
  Tulisan `:.1f` memberi tahu komputer: *"Tolong tampilkan angkanya dengan **1 angka saja di belakang koma** ya!"* (Misal: `82.33333` berubah jadi `82.3`).

---

## 🚀 Contoh Hasil Saat Program Dijalankan

```text
Nama peserta   : Budi
Nilai tugas    : 80
Nilai kuis     : 90
Nilai ujian    : 85
Kehadiran (%)  : 85

===== HASIL PENILAIAN =====
Nama         : Budi
Nilai Akhir  : 84.5
Kehadiran    : 85%
Status       : Lulus dengan Predikat B
```

🎉 **Selamat!** Sekarang kamu sudah paham bagaimana logika program sederhana ini bekerja!