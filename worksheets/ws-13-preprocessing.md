# WS-13: Data Preprocessing

> **Bab 13 — Preprocessing & Persiapan Data untuk Analisis**

---

## Ringkasan Materi

### Data Refinement Pipeline

```
Raw Data → Cleaning → Transformation → Normalization → Processed Data → Analysis Ready
```

Setiap tahap memiliki tujuan berbeda. **Preprocessing bukan langkah teknis biasa** — setiap keputusan preprocessing adalah keputusan riset yang bisa mengubah kesimpulan.

### Empat Prinsip Preprocessing

| Prinsip | Deskripsi |
|---------|----------|
| **Consistency** | Metode sama untuk data yang sama |
| **Transparency** | Setiap langkah terdokumentasi |
| **Reproducibility** | Orang lain bisa mengulang dengan hasil sama |
| **Minimal Distortion** | Ubah sesedikit mungkin; jika normalisasi tidak perlu, jangan lakukan |

### Cleaning Triad

| Masalah | Strategi | Risiko |
|---------|---------|--------|
| **Missing values** | | |
| — Listwise deletion | Missing < 5%, random | Data loss |
| — Mean/median imputation | Sedikit missing, dist. normal | Mengurangi variabilitas |
| — Model-based imputation | Banyak missing, pola sistematis | Introduces dependency |
| — Flag & separate | Missing karena alasan substantif | Kompleksitas analisis |
| **Duplikat** | Identifikasi → verifikasi → hapus | False positive (data mirip ≠ duplikat) |
| **Error format** | Standardisasi tipe, encoding | Kehilangan informasi saat konversi |

### Normalisasi — Kapan & Metode Mana

| Metode | Formula | Output | Sensitif Outlier? |
|--------|---------|--------|-------------------|
| Min-max | (x-min)/(max-min) | [0, 1] | Ya |
| Z-score | (x-mean)/std | Unbounded | Lebih robust |
| Robust scaling | (x-median)/IQR | Unbounded | Paling robust |

**Kunci:** Parameter normalisasi harus dihitung dari **training set saja** — bukan seluruh data. Pelanggaran = **data leakage**.

### Data Leakage Prevention

Data leakage terjadi ketika informasi dari test set "bocor" ke preprocessing:
- Normalisasi parameter dari seluruh dataset ← **SALAH**
- Cross-validation dilakukan sebelum split ← **SALAH**
- Feature selection menggunakan label test set ← **SALAH**

### Jebakan Kognitif

1. "Preprocessing cuma teknis — tidak perlu detail" → bisa ubah kesimpulan
2. "Lebih banyak preprocessing = lebih bersih = lebih baik" → over-processing distorsi data
3. "Normalisasi selalu diperlukan" → belum tentu, tergantung metode analisis
4. "Imputation sama untuk semua situasi" → strategi harus sesuai konteks

---

## Template A.13 — Preprocessing Documentation Log

```
PREPROCESSING LOG

Dataset           : data_tiktokshop_clean.xlsx
Jumlah data awal  : 115 records responden

Cleaning:
| Masalah | Jumlah Kasus | Penanganan | Justifikasi |
|---------|-------------|------------|-------------|
| Missing | 0 Kasus     | N/A        | Google Forms diset "Wajib Diisi" (Required Items) pada semua indikator kuesioner. |
| Duplikat| 0 Kasus     | N/A        | Verifikasi berbasis kombinasi Cap Waktu dan ID baris menunjukkan tidak ada pengisian ganda. | 
| Tidak Lolos Screening   | 15 Kasus     | Eliminasi Total (Listwise Deletion) | Responden menjawab "Tidak" pada pertanyaan filter kelayakan ("Apakah Anda berbelanja di TikTok Shop dalam 3 bulan terakhir?"), sehingga tidak kompeten menilai usability sistem. | 

Transformation:
| Transformasi | Variabel | Detail | Alasan |
|-------------|----------|--------|--------|
| SUS Scoring | X1 (Live Shopping) & X2 (Product Reviews) | Mengikuti rumus baku Brooke (1996): Item ganjil (Skor - 1) dan Item genap (5 - Skor), lalu total dikali 2.5. | Mengubah nilai mentah skala Likert 1-5 menjadi metrik Usability terstandardisasi dengan range 0 - 100. |

Normalization:
  Metode    : Tidak memerlukan normalisasi tambahan (No Normalization).
  Alasan    : Variabel input hasil transformasi SUS sudah berada pada skala terstandar yang seragam (0 - 100). Algoritma Naïve Bayes berbasis probabilitas kepadatan frekuensi juga bersifat *distance-insensitive* (tidak sensitif terhadap magnitudo jarak), sehingga tidak membutuhkan scaling.
  Parameter : N/A (Dihitung dari: Tidak dilakukan normalisasi)

Leakage Check:
  [x] Parameter normalisasi dari training set saja
  [x] Tidak ada informasi test set dalam preprocessing
  [x] Cross-validation dilakukan setelah split

Jumlah data akhir : 100 records responden yang valid dan bersih.
Script tersedia   : [x] Ya → path:Menggunakan modul otomasi kalkulator SUS berbasis Python Pandas. | [ ] Belum
```

---

## Latihan 1 — Cleaning Plan

Periksa dataset Anda (atau dataset contoh) dan dokumentasikan masalah yang ditemukan.

| Masalah | Jumlah Kasus | Penanganan | Justifikasi |
|---------|-------------|------------|-------------|
| *Tidak Memenuhi Kriteria Target Responden* | *15 dari 115 (13.04%)* | *Listwise deletion (Dieliminasi secara total)* | *Responden tidak aktif bertransaksi di TikTok Shop dalam 3 bulan terakhir, sehingga tidak memiliki basis pengalaman aktual untuk mengevaluasi fitur Live Shopping dan Product Reviews.* |
| | | | |
| | | | |
| | | | |

**Jumlah data sebelum cleaning:* 115 * 
**Jumlah data setelah cleaning:* 100 * 
**Persentase data yang hilang/berubah:* 13.04% *
---

## Latihan 2 — Normalisasi Decision

Tentukan apakah data Anda perlu normalisasi, dan jika ya, metode apa yang tepat.

| Variabel | Range Asli | Distribusi | Outlier? | Metode Normalisasi | Alasan |
|----------|-----------|-----------|----------|-------------------|--------|
| *Skor SUS Fitur Live Shopping (X1)* | *45.0 – 82.5* | *Normal* | *Tidak* | *Tidak Perlu* | *Data sudah berada pada skala baku instrumentasi SUS (0–100) dan Naïve Bayes bekerja berbasis sebaran distribusi kelas, bukan jarak spasial. |
| Skor SUS Fitur Product Reviews (X2)  | 45.0 – 80.0  | Normal  | Tidak  | Tidak Perlu  | Data memiliki rentang batas logis yang sama persis dengan X1, sehingga bobot variabel sudah setara secara alami tanpa intervensi scaling.  |


**Apakah normalisasi diperlukan?** [ ] Ya / [x] Tidak
**Justifikasi:**
>Seluruh variabel prediktor (X1 dan X2) merupakan skor hasil kalkulasi kuesioner System Usability Scale (SUS) yang secara matematis sudah terikat (bounded) pada rentang nilai 0 hingga 100. Karena semua variabel masukan sudah berada pada skala ukur yang seragam, dan model klasifikasi yang digunakan adalah Naïve Bayes (bukan algoritma berbasis jarak seperti K-NN atau SVM), maka normalisasi tambahan seperti Min-Max atau Z-Score sama sekali tidak diperlukan dan justru berisiko menghilangkan variabilitas data asli..

**Leakage check:**
- [x] Parameter dihitung dari training set saja
- [x] Normalisasi diterapkan setelah train-test split

---

## Latihan 3 — Preprocessing Report

Buat ringkasan preprocessing lengkap — dokumentasi yang cukup bagi orang lain untuk mereplikasi.

```
PREPROCESSING SUMMARY

1. Dataset: data_115_responden_v2.csv
2. Data awal: 115 records, 25 features
3. Cleaning:
   - Missing values: 0 kasus, metode: N/A (Karena validasi "Required" di Google Forms)
   - Duplikat: 0 kasus, tindakan: N/A
   - Tidak Lolos Screening: 15 kasus, tindakan: Dieliminasi dari dataset (Listwise Deletion)
4. Transformation: Konversi jawaban skala Likert 1-5 menjadi nilai baku skor SUS skala 0-100 menggunakan formula Brooke (1996).
5. Normalisasi: Tidak dilakukan normalisasi (No Scaling), rentang skor SUS asli (0-100) dipertahankan penuh demi menjaga keaslian sebaran data.
6. Data akhir: 100 records, 2 features utama (SUS_LiveShopping & SUS_ProductReviews) dan 1 label target (Retensi).
7. Leakage check: [x] Lulus / [ ] Ada masalah
```

---

## Refleksi

> Apakah Anda pernah melakukan normalisasi "karena biasa dilakukan" tanpa mempertimbangkan apakah benar-benar diperlukan? Apa risiko over-preprocessing?

> Ya, pada proyek-proyek pemrograman atau tugas kuliah kecerdasan buatan sebelumnya, saya sering kali menerapkan normalisasi Min-Max secara otomatis "karena kebiasaan" atau sekadar mengikuti tutorial umum, tanpa memikirkan karakteristik dasar dari algoritma dan struktur data aslinya.

Risiko dari over-preprocessing (pemrosesan data yang berlebihan) adalah terjadinya distorsi atau hilangnya makna fisis substantif dari data asli.
> Risiko dari over-preprocessing (pemrosesan data yang berlebihan) adalah terjadinya distorsi nilai atau hilangnya makna fisis substantif dari data asli. Jika data yang sudah terstandardisasi secara alami (seperti skor SUS) dipaksa untuk di-scaling kembali, variabilitas asli antarreponden akan mengecil. Hal ini bisa menyembunyikan variasi penting yang dibutuhkan oleh algoritma Naïve Bayes untuk menghitung probabilitas posterior, yang pada akhirnya dapat mengaburkan kesimpulan akhir penelitian ilmiah di Universitas Putra Bangsa.
