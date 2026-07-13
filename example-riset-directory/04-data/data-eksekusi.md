# data dan Struktur Data Responden (Tahap 4)

Dokumen ini berisi informasi mentah mengenai data kuesioner pengguna yang digunakan sebagai basis pengujian sistem dan antarmuka fitur TikTok Shop.

## 1. Ringkasan Data Mentah (Raw Dataset)
- **Nama File Sumber**: `data_115_responden_v2.csv`
- **Total Responden (N)**: 115 Baris
- **Total Kolom/Variabel**: 25 Pertanyaan/Parameter
- **Rentang Waktu Pengumpulan**: Juli 2026

## 2. Struktur Variabel Kuesioner

Data mentah ini dibagi menjadi tiga bagian utama berdasarkan tujuan evaluasi sistem:

### A. Identitas & Validasi Awal (3 Kolom)
1. `Cap waktu` (Timestamp pengisian)
2. `Nama` Responden
3. `Umur` Responden
4. `Apakah Anda berbelanja di TikTok Shop dalam 3 bulan terakhir?` (Validasi Filter Pengguna)

### B. Evaluasi Usability Fitur Live Shopping (10 Pertanyaan - Skala Likert 1-5)
Menggunakan instrumen System Usability Scale (SUS) untuk mengukur tingkat kemudahan, integrasi menu, kepercayaan diri pengguna, tingkat kerumitan, dan kebingungan sistem pada fitur *Live Shopping*.

### C. Evaluasi Usability Fitur Product Reviews (10 Pertanyaan - Skala Likert 1-5)
Menggunakan instrumen System Usability Scale (SUS) untuk mengukur konsumsi informasi ulasan, konsistensi rating bintang, tata letak posisi fitur, kemudahan filter, dan keakuratan informasi pada *Product Reviews*.

### D. Continuance Intention (1 Pertanyaan)
`Apakah Anda berniat untuk terus menggunakan, bertransaksi, atau mempertahankan aktivitas belanja Anda di platform TikTok Shop di masa yang akan datang?`

---

## 3. Contoh Cuplikan Data Mentah (Data Sample)

| No | Nama | Rentang Umur | Belanja 3 Bulan Terakhir? | Niat Pakai Live Shopping Lagi (Skala 1-5) | Fitur Rumit? (Skala 1-5) | Niat Kontinuitas Belanja |
|---|---|---|---|:---:|:---:|---|
| 1 | lita | 22 - 25 tahun | Tidak | 4 | 3 | (Kosong) |
| 2 | Rian | 22 - 25 tahun | Ya | 4 | 2 | Ya |
| 3 | Nyoman | 18 - 21 tahun | Ya | 3 | 3 | Tidak |
| 4 | Bagus | 18 - 21 tahun | Ya | 5 | 4 | Ya |

---

## 4. Rencana Pemrosesan ke Tahap Berikutnya (Tahap 5)
Data mentah ini akan diproses di folder output menggunakan perhitungan skor **System Usability Scale (SUS)** dengan rumus pembalik skor untuk pertanyaan genap (pertanyaan negatif) dan penjumlahan langsung untuk pertanyaan ganjil (pertanyaan positif) guna menghasilkan nilai *usability* akhir berskala 0–100.