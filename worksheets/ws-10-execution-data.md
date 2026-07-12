# WS-10: Experiment Execution & Data Collection

> **Bab 10 — Eksekusi Eksperimen & Pengumpulan Data**

---

## Ringkasan Materi

### Experiment Execution Pipeline

```
Design → Execution Plan → Controlled Execution → Data Collection → Data Logging → Dataset for Analysis
```

### Multiple Run = Non-Negotiable

Single run **tidak pernah cukup** untuk klaim ilmiah. Minimum 5-10 run per skenario dengan seed berbeda. Multiple run menghasilkan:
- Mean, std, confidence interval
- Distribusi hasil → uji statistik
- Variabilitas → error bar di grafik

### Execution Plan

Setiap eksperimen harus memiliki plan sebelum eksekusi:
- Daftar skenario
- Jumlah run per skenario
- Random seed per run (pre-determined!)
- Urutan eksekusi (randomisasi/counterbalancing)
- Pre-execution checklist

### Data Logging Komprehensif

Setiap run menghasilkan log terstruktur:
1. **Identitas** — Run ID, timestamp, skenario
2. **Konfigurasi** — Semua parameter, seed, code version
3. **Hasil** — Semua metrik, output detail
4. **Metadata** — Waktu eksekusi, resource usage, warning/error

Format: CSV/JSON/database — **bukan stdout yang di-copy-paste**.

### Engineering vs Research Execution

| Aspek | Engineering | Research |
|-------|-----------|---------|
| Run | Sekali (deploy) | Multiple (min 5-10, seed berbeda) |
| Logging | Error log, access log | Semua parameter, metrik, metadata |
| Anomali | Bug → fix → redeploy | Investigasi → dokumentasi → analisis |
| Urutan | Tidak penting | Bisa bias — perlu randomisasi |

### Anomali = Dokumentasi, Bukan Hapus

Run gagal/anomali tidak boleh dihapus tanpa dokumentasi. Bisa jadi:
- **Bug** → fix & re-run (dokumentasikan!)
- **Batas kemampuan metode** → DNF = temuan
- **Data yang bias** jika hanya simpan run "berhasil"

### Jebakan Kognitif

1. "Satu angka cukup" → tanpa distribusi, tidak bisa diuji
2. "Seed tidak penting" → bahkan algoritma deterministik bisa dipengaruhi library stokastik
3. "Run gagal langsung hapus" → kehilangan temuan potensial
4. "Semua run harus hari ini" → thermal throttling, fatigue

---

## Template A.10 — Execution Plan & Data Log

```
EXECUTION PLAN

| Run # | Skenario | Seed | Parameter | Status | Waktu | Output File |
|-------|----------|------|-----------|--------|-------|-------------|
| Run # | Skenario | Seed | Parameter | Status | Waktu | Output File |
|-------|----------|------|-----------|--------|-------|-------------|
| 1     |Analisis Kausalitas Eksplanatori (Python) | 42 | Regresi Logistik Biner, alpha = 0.05 | Completed |
| 2     | Klasifikasi Prediktif (RapidMiner) - Run 1	| 42 |	Naïve Bayes, 10-Fold Cross Validation |	Completed |
| 3     | Klasifikasi Prediktif (RapidMiner) - Run 2 |	123 |	Naïve Bayes, 10-Fold Cross Validation	| Completed |
| 4     |Klasifikasi Prediktif (RapidMiner) - Run 3	| 999 |	Naïve Bayes, 10-Fold Cross Validation |	Completed |
| 5     | Klasifikasi Prediktif (RapidMiner) - Run 4  |	2026	 | Naïve Bayes, 10-Fold Cross Validation  |	Completed |

Jumlah runs per skenario :1 run untuk analisis statistik Python, 4 run dengan variasi seed berbeda untuk RapidMiner
Total runs               : 5 Run

DATA LOG (per run):
  Run ID    : RUN-TTSHOP-002
  Timestamp : 2026-05-18T16:20:45WIB
  Skenario  : Klasifikasi Prediktif Lapisan 1 (RapidMiner - Naïve Bayes)
  Input     : File data_tiktokshop_clean.xlsx (N=100, IV: Skor SUS Live Shopping & Product Reviews)
  Output    : Accuracy: 88.00%, Macro-average F1-score: 0.47, Precision: 88.00%, Recall: 100.00%
  Anomali   : Ditemukan 15 data responden tidak lolos kriteria screening awal.
  Catatan   : Evaluasi performa menggunakan skema 10-Fold Cross Validation dengan Local Seed dikunci pada angka 42. Distribusi kelas target Y bernilai Ya = 88 dan Tidak = 12 (terjadi class imbalance alami).
  
```

---

## Latihan 1 — Execution Plan

Susun execution plan untuk eksperimen Anda. Tentukan skenario, jumlah run, dan seed sebelum eksekusi.

| Run # | Skenario | Seed | Parameter Kunci | Status |
|-------|----------|------|----------------|--------|
|  1  | Analisis Kausalitas Eksplanatori (Python)| 42 |Regresi Logistik Biner, alpha = 0.05 | Completed |
|  2  | Klasifikasi Prediktif (RapidMiner) - Run 1 |  42 | Naïve Bayes, 10-Fold Cross Validation. | Completed |
|  3  | Klasifikasi Prediktif (RapidMiner) - Run 2 |  123 | Naïve Bayes, 10-Fold Cross Validation. | Completed |
|  4  | Klasifikasi Prediktif (RapidMiner) - Run 3 |  999 | Naïve Bayes, 10-Fold Cross Validation. | Completed |
|  5  | Klasifikasi Prediktif (RapidMiner) - Run 4 |  2026 | Naïve Bayes, 10-Fold Cross Validation. | Completed |

**Total skenario:** 2 Skenario Utama (1 Eksplanatori & 1 Prediktif)
**Run per skenario:** 1 run untuk analisis statistik Python, 4 run dengan variasi seed berbeda untuk RapidMiner
**Total run keseluruhan:** 5 Run

---

## Latihan 2 — Data Log Terstruktur

Desain format data log untuk eksperimen Anda. Tentukan field apa saja yang akan dicatat.

**Identitas:**
| Field | Contoh |
|-------|--------|
| Run ID | RUN-TTShop-001|
| Timestamp | 2026-05-18T16:15:00 |
| Skenario ID | SKN-02-NaïveBayes  |

**Konfigurasi:**
| Field | Contoh |
|-------|--------|
| Seed |42 / 123 / 999 / 2026 |
| Tool Version | RapidMiner Studio v9.10 / Python Runtime v3.10+ |
| Input Dataset | data_tiktokshop_clean.xlsx (N=100) |

**Hasil:**
| Metrik | Tipe Data | Range Valid |
|--------|----------|-------------|
| p-value Fitur Live Shopping (X1) | float | 00.0 – 1.00 |
| p-value Fitur Product Reviews (X2)| float |  00.0 – 1.00|
|Accuracy |float |0.0% – 100.0%|
|Macro-average F1-score |float |0.00 – 1.00|

**Format output:** [x] CSV / [x] JSON / [ ] Database / [ ] Lainnya: ____

---

## Latihan 3 — Anomaly Protocol

Rencanakan bagaimana menangani anomali. Untuk setiap jenis, tentukan langkah yang diambil.

| Jenis Anomali | Contoh | Tindakan |
|---------------|--------|----------|
| Data tidak lolos kriteria | Responden mengisi "Tidak" pada filter belanja 3 bulan terakhir. | Langsung keluarkan dari dataset utama (Listwise Deletion) sebelum masuk ke proses pengolahan skor SUS agar tidak membiaskan hasil riset. Ditandai sebagai kegagalan kriteria penyaringan kuesioner. |
| Hasil ekstrem | Nilai akurasi model Naïve Bayes selalu stagnan di angka 88% di seluruh nilai seed pengujian. | Investigasi distribusi kelas target Y. Hal ini wajar terjadi karena efek Class Imbalance yang dominan (88 responden menjawab 'Ya' dari total 100 data). Catat kondisi ini sebagai karakteristik data lapangan asli. |
| Inkonsistensi data | Nilai target kelas Y bernilai kosong (Missing Value). | Lakukan pembersihan baris data secara total agar distribusi probabilitas Naïve Bayes tetap berjalan presisi. |


**Prinsip:** Detect → Investigate → Document → Decide

---

## Refleksi

> Pernahkah Anda melaporkan hasil riset/tugas dari single run? Apa risikonya? Bagaimana multiple run mengubah kepercayaan terhadap hasil?

**Pengalaman sebelumnya:**
> Ya, pada tugas-tugas kuliah pemrograman atau basis data sebelumnya, saya sering kali melaporkan performa sistem atau akurasi hanya dari satu kali pengujian (single run). Risikonya adalah angka tersebut bisa jadi merupakan faktor kebetulan (keberuntungan acak dari pemisahan dataset) sehingga tidak mewakili kestabilan aslinya saat diuji ulang dengan kondisi data berbeda.

**Yang akan dilakukan berbeda:**
> Pada riset kali ini, saya menerapkan prinsip kontrol pengujian berganda (multiple runs) dengan mengunci variasi nilai random seed (42, 123, 999, dan 2026) baik di level lingkungan eksekusi Python maupun pada pemisahan data di operator 10-Fold Cross Validation RapidMiner. Dengan cara ini, keabsahan nilai evaluasi performa model Naïve Bayes terbebas dari unsur manipulasi atau bias sebaran data tunggal, sehingga hasil penelitian ini menjadi sepenuhnya kredibel dan sahih untuk dipertahankan di depan dosen penguji Universitas Putra Bangsa.
