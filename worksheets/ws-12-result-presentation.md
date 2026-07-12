# WS-12: Result Presentation & Visualization

> **Bab 12 — Penyajian Hasil & Visualisasi**

---

## Ringkasan Materi

### Data → Insight Model

```
Validated Data → Structured Presentation → Visualization → Pattern Recognition → Insight
```

Penyajian **mendahului** analisis. Tabel dan grafik membantu peneliti "melihat" data sebelum menghitung. Langsung ke uji statistik tanpa visualisasi berisiko kesimpulan yang secara teknis benar tapi kontekstual salah (Anscombe's Quartet, 1973).

### Tabel = Presisi, Grafik = Pola

Keduanya **saling melengkapi**:
- Tabel: angka presisi, self-contained (dipahami tanpa teks), sortable
- Grafik: pola visual, tren, perbandingan cepat

### Jenis Grafik Berdasarkan Tujuan

| Tujuan | Jenis Grafik |
|--------|-------------|
| Perbandingan antar-skenario | Bar chart (grouped/stacked) |
| Distribusi per-skenario | Box plot / violin plot |
| Tren temporal | Line chart |
| Korelasi dua variabel | Scatter plot |
| Proporsi (total = 100%) | Pie chart (hati-hati!) |

### Contoh Tabel Hasil yang Baik

| Model | Accuracy (%) | F1-Score (%) | Training Time (min) |
|-------|-------------|-------------|---------------------|
| BERT | 88.4 ± 1.2 | 87.1 ± 1.4 | 45.2 ± 3.1 |
| LSTM | 86.1 ± 1.8 | 84.5 ± 2.0 | 12.8 ± 1.2 |
| SVM | 82.3 ± 0.9 | 80.7 ± 1.1 | 0.3 ± 0.1 |

*N=10 per model. Mean ± std. Diurutkan berdasarkan Accuracy.*

### Visualization Bias — Yang Harus Dihindari

| Bias | Deskripsi | Dampak |
|------|----------|--------|
| Truncated axis | Y tidak dari 0 | Memperbesar perbedaan kecil |
| Inconsistent scale | Dua grafik skala beda | Perbandingan menyesatkan |
| Cherry-picked data | Hanya tampilkan yang "menang" | Selektif, tidak jujur |
| 3D effects | Efek 3D tanpa dimensi data ke-3 | Distorsi tanpa informasi |
| Missing error bar | Tidak ada variabilitas | Menyembunyikan ketidakpastian |

### Engineering vs Research Presentation

| Aspek | Engineering | Research |
|-------|-----------|---------|
| Tujuan grafik | Dashboard monitoring | Mendukung argumen ilmiah |
| Informasi wajib | KPI, threshold | Mean, std, CI, N, p-value |
| Bias handling | Less critical | Wajib dihindari (peer-review) |

---

## Template A.12 — Result Presentation Plan

```
RESULT PRESENTATION PLAN

Research Question : 1. Bagaimana pengaruh usability fitur Live Shopping dan Product Reviews secara eksplanatori terhadap Retensi Pengguna?
                    2. Bagaimana performa model Naïve Bayes dalam memprediksi Retensi Pengguna berbasis skor SUS?
Metrik Utama      : p-value (Eksplanatori), Accuracy (%), dan Macro-average F1-Score (Prediktif)

Tabel Hasil:
| Skenario | Metrik 1 (mean ± std) | Metrik 2 (mean ± std) | n |
| Klasifikasi Naïve Bayes (10-Fold CV) | 88.00 ± 0.00% | 0.47 ± 0.00 | 4 |
|          |                      |                      |   |

Visualisasi yang Direncanakan:
| # | Jenis Grafik | Pesan Utama | Metrik |
|---|-------------|-------------|--------|
| 1 | Bar Chart + Error Bar | Memperlihatkan stabilitas capaian akurasi Naïve Bayes di berbagai seed. | Mean Accuracy ± Std |
| 2 | Grouped Bar Chart | Membandingkan skor rata-rata SUS antara fitur Live Shopping vs Product Reviews. | Skor Rata-Rata SUS per Indikator |  

Bias Check:
  [x] Y-axis mulai dari 0 (atau dijustifikasi)
  [x] Error bar/CI ditampilkan
  [x] Semua data disertakan (tidak cherry-picked)
  [x] Tidak menggunakan 3D tanpa alasan
```

---

## Latihan 1 — Tabel Hasil

Buat tabel hasil eksperimen Anda (boleh dengan data simulasi jika belum punya data riil).

| Skenario | Rata-Rata Akurasi (mean ± std) | Rata-Rata Macro F1-Score | n |
|----------|----------------------|----------------------|---|
| *klasifikasi naive bayes* | *88.00 ± 0.00%* | *0.47. ± 0.00 * | *4 run* |
| | | | |
| | | | |

**Checklist tabel:**
- [x] Self-contained (judul jelas, satuan ada, N tercantum)
- [x] Mean ± std (bukan single number)
- [x] Diurutkan berdasarkan metrik utama
- [x] Format konsisten di semua baris

---

## Latihan 2 — Rencana Visualisasi

Rencanakan 2-3 grafik untuk menyajikan data dari Latihan 1. Setiap grafik = satu pesan.

| # | Jenis Grafik | Pesan | Data yang Digunakan |
|---|-------------|-------|---------------------|
| 1 | Bar Chart + Error Bar | Membuktikan akurasi Naïve Bayes konsisten secara mutlak di angka 88.00% di berbagai seed acak akibat imbas dominasi kelas mayoritas. | Mean Accuracy ± Std dari 4 nilai seed (42, 123, 999, 2026). |
| 2 | Grouped Bar Chart | Menunjukkan perbandingan skor rata-rata jawaban responden pada 10 butir pertanyaan instrumen SUS antara Fitur Live Shopping (X1) dan Product Reviews (X2) guna memetakan indikator mana yang paling menghambat usability.Nilai rata-rata per butir pertanyaan kuesioner  | Nilai rata-rata per butir pertanyaan kuesioner asli (N=100). |


---

## Latihan 3 — Bias Detection

Evaluasi visualisasi berikut untuk bias (skenario dari contoh):

**Skenario:** Metode A = 91.2%, Metode B = 90.8%. Bar chart dengan Y-axis mulai dari 90%.

| Pertanyaan | Jawaban |
|-----------|---------|
| Apakah Y-axis menyesatkan? | *Ya — Memulai sumbu Y dari 90% secara visual akan mendistorsi realita, membuat Metode A terlihat seolah-olah berkinerja dua kali lipat lebih baik dari B, padahal selisih aslinya hanya 0.4%.* |
| Apakah error bar ditampilkan? | Tidak, grafik batangan tunggal tanpa simpangan baku menyembunyikan variabilitas data sesungguhnya. |
| Apakah semua kondisi ditampilkan? | Tidak, rawan terjadi cherry-picking jika hanya menampilkan run terbaik. |
| Apa solusinya? | Sumbu Y wajib dimulai dari angka 0%, serta wajib menyematkan error bar untuk menunjukkan signifikansi tumpang tindih (overlap) antar kedua metode secara jujur.  |

**Evaluasi grafik Anda sendiri dari Latihan 2:**
- [x] Semua bias check lulus
- [ ] Ada yang perlu diperbaiki: Tidak ada, skala sumbu Y untuk akurasi model prediktif (0%-100%) dan skor rata-rata kuesioner dipastikan mulai dari angka 0 secara penuh.

---

## Refleksi

> Mengapa tabel dan grafik keduanya diperlukan — tidak cukup salah satu saja? Pernahkah Anda membuat grafik yang (tanpa sengaja) menyesatkan?

> Tabel dan grafik saling melengkapi karena melayani kebutuhan kognitif yang berbeda. Tabel menyediakan presisi numerik tingkat tinggi yang sangat dibutuhkan ketika pembaca atau dosen penguji Universitas Putra Bangsa ingin melihat angka pasti desimal dari nilai rata-rata skor SUS dan simpangan bakunya (sigma). Sebaliknya, grafik menyajikan pola, tren, dan perbandingan visual secara instan yang sulit ditangkap hanya dengan menatap deretan angka di dalam tabel. Jika hanya menyertakan tabel, pembaca akan kelelahan mencari pola; jika hanya menyertakan grafik, pembaca akan kehilangan akurasi nilai mutlaknya.

> Di masa lalu, saya terkadang tidak sengaja membuat grafik yang menyesatkan akibat menggunakan pengaturan default dari perangkat lunak spreadsheet yang otomatis memotong sumbu Y (truncated axis) agar grafik terlihat dinamis. Hal tersebut melanggar integritas riset karena memperbesar perbedaan kecil secara visual. Melalui workshop ini, saya menyadari bahwa kejujuran visual (seperti memulai sumbu dari angka 0 dan menyertakan error bar) jauh lebih utama demi menjaga objektivitas sebuah karya ilmiah.
