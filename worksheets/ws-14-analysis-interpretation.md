# WS-14: Analysis, Interpretation & Failure Analysis

> **Bab 14 — Analisis Data, Interpretasi & Failure Analysis**

---

## Ringkasan Materi

### Data → Knowledge Model

```
Data → Analysis → Interpretation → Explanation → Knowledge
```

Tiga level yang berbeda:
- **Analysis** — "Apa yang terjadi?" (deskriptif + inferensial)
- **Interpretation** — "Apa artinya?" (konteks RQ + literatur)
- **Failure Analysis** — "Mengapa tidak berhasil?" (boundary conditions)

### Beyond p-value

**Statistical significance ≠ practical significance.** Selalu laporkan:
1. p-value (signifikansi statistik)
2. Effect size (besarnya efek)
3. Confidence interval (rentang ketidakpastian)

| Effect Size (Cohen's d) | Interpretasi |
|-------------------------|-------------|
| < 0.2 | Small |
| 0.2 – 0.8 | Medium |
| > 0.8 | Large |

### Pemilihan Uji Statistik

| Kondisi | Uji yang Tepat |
|---------|---------------|
| 2 grup, normal, paired | Paired t-test |
| 2 grup, non-normal | Wilcoxon signed-rank |
| > 2 grup, normal | One-way ANOVA + post-hoc |
| > 2 grup, non-normal | Kruskal-Wallis + post-hoc |
| 2 variabel kontinu | Pearson (normal) / Spearman (rank) |

### Failure Analysis as Contribution

Hipotesis yang ditolak adalah **temuan yang berharga**:

| Dataset | New (F1) | Baseline (F1) | p-value | Cohen's d |
|---------|---------|--------------|---------|-----------|
| DS-1 (small, clean) | 94.2±1.1 | 89.3±1.5 | <0.001 | **3.7** |
| DS-4 (medium, noisy) | 78.3±3.2 | 82.1±2.8 | 0.008 | **-1.3** |
| DS-5 (large, noisy) | 71.6±4.1 | 80.5±3.0 | <0.001 | **-2.5** |

**Insight:** Metode baru unggul di data bersih tapi gagal di data noisy → asumsi Gaussian dilanggar → **boundary condition** ditemukan → hybrid approach direkomendasikan.

**Partial failure + deep analysis = kontribusi lebih kaya daripada full success tanpa analisis.**

### Limitation Types

| Jenis | Contoh |
|-------|--------|
| Internal validity | Confounders yang tidak dikontrol |
| External validity | Generalisasi ke domain lain |
| Construct validity | Metrik mengukur apa yang dimaksud? |
| Statistical limitation | Sample size, asumsi distribusi |

### Jebakan Kognitif

1. "Signifikan statistik = penting secara praktis" → cek effect size
2. "Hipotesis tidak didukung → cari sudut baru" → p-hacking
3. "Kegagalan tidak perlu dilaporkan detail" → missed insight
4. "Limitasi cukup disebutkan, tidak perlu dianalisis" → kedalaman hilang

---

## Template A.14 — Analysis & Interpretation Report

```
ANALYSIS & INTERPRETATION

1. Statistik Deskriptif:
   | Skenario | Mean | Std | Median | Min | Max | n |
   |X1: SUS Live Shopping | 62.48 | 8.46 | 62.50  | 45.0| 82.5|100|
   |X2: SUS Product Reviews| 63.18 | 8.05 | 62.50  | 45.0| 80.0|100|

2. Uji Hipotesis:
   Uji yang digunakan  : Regresi Logistik Biner (Binary Logistic Regression)
   Justifikasi          : Variabel independen berupa data kontinu (skor SUS), sedangkan variabel dependen berupa data kategorikal biner (Retensi Pengguna: "Ya" atau "Tidak").
   Hasil: 
   - X1 (Live Shopping)  : p-value = 0.899, Koefisien = -0.0046
   - X2 (Product Reviews): p-value = 0.644, Koefisien = -0.0183
   LLR p-value          : 0.8918 (Model secara simultan tidak signifikan mempengaruhi target)

3. Keputusan:
   [ ] H₀ ditolak → H₁ diterima
   [x] H₀ tidak ditolak (Pengaruh Usability Fitur terhadap Retensi tidak signifikan secara statistik).

4. Interpretasi:
   Hubungan ke RQ       : Peningkatan skor usability SUS pada kedua fitur secara parsial tidak mendorong peningkatan probabilitas Retensi Pengguna Gen Z secara signifikan.
   Practical significance: Secara praktis, kegunaan (usability) sistem bukan satu-satunya penentu mutlak retensi; faktor eksternal lain seperti promo harga, algoritma konten, atau tren produk memiliki andil yang lebih kuat.
   Perbandingan literatur: Berbeda dengan teori umum Brooke (1996) yang menyatakan usability linier dengan loyalitas, pada ekosistem social commerce Gen Z, faktor kenyamanan antarmuka tergeser oleh ketergantungan utilitas hiburan.

5. Limitation:
   | Jenis | Ancaman | Dampak | Mitigasi |
   |-------|---------|--------|----------|
   | Statistical | Imbalance target class (88 Ya vs 12 Tidak). | Logistik biner kesulitan memisahkan batas keputusan (decision boundary) secara tajam. | Melaporkan kondisi apa adanya sebagai cerminan loyalitas organik pengguna platform saat ini. |

   | Construct | Ukuran sampel terbatas (N=100). | Power of test dalam mendeteksi efek kecil berkurang. | Menyarankan perluasan jangkauan sampel multi-kampus pada penelitian selanjutnya. |

6. Failure Analysis (jika H₀ tidak ditolak):
   Penyebab potensial  : Tingginya dominasi kelas mayoritas (88% pengguna menjawab 'Ya' untuk retensi) menyebabkan variansi data terpusat, sehingga model regresi mendeteksi variasi skor SUS tidak sensitif terhadap perubahan status loyalitas.
   Boundary condition   : Kerangka pengujian SUS ini bekerja optimal pada platform yang belum mapan. Pada TikTok Shop yang sudah menjadi bagian dari gaya hidup harian Gen Z, usability rendah tidak langsung menurunkan retensi mereka.
   Insight              : Usability yang berada pada kategori "Marginal OK" (Skor ~62) sudah cukup bagi pengguna untuk bertahan, didorong oleh tingginya nilai ekonomi/hiburan yang diperoleh.
```

---

## Latihan 1 — Pemilihan Uji Statistik

Tentukan uji statistik yang tepat untuk eksperimen Anda.

| Pertanyaan | Jawaban |
|-----------|---------|
| Berapa grup yang dibandingkan? | *Usability yang berada pada kategori "Marginal OK" (Skor ~62) sudah cukup bagi pengguna untuk bertahan, didorong oleh tingginya nilai ekonomi/hiburan yang diperoleh.* |
| Apakah data berpasangan (paired)? | Tidak |
| Apakah distribusi normal? (uji normalitas) | Variabel independen berdistribusi normal, namun variabel dependen bersifat kategorikal dikotomus (biner). |
| **Uji yang dipilih:** | Regresi Logistik Biner (Binary Logistic Regression) |
| **Justifikasi:** | Tepat digunakan ketika variabel terikat merupakan variabel dummy biner (Ya/Tidak) dan ingin mengukur probabilitas perpindahan keputusan berdasarkan skor skala kontinu. |

**Effect size yang akan dilaporkan:** [x] Pseudo R-squared (Nagelkerke/McFadden) / [ ] Eta-squared / [ ] Lainnya: ____

---

## Latihan 2 — Interpretasi Hasil

Gunakan data berikut (atau data riil Anda) untuk berlatih interpretasi.

**Data:**
| Model | Accuracy (mean ± std) | n |
|-------|----------------------|---|
| A | 89.2 ± 1.5 | 10 |
| B | 87.8 ± 2.1 | 10 |

p = 0.045, Cohen's d = 0.74, CI 95% = [0.03, 2.77]

| Aspek | Interpretasi |
|-------|-------------|
| Signifikansi statistik | *Nilai p-value X1 (0.899) dan X2 (0.644) > 0.05. Secara statistik, tidak terdapat bukti yang cukup untuk menyatakan bahwa tingkat usability fitur Live Shopping maupun Product Reviews memprediksi keputusan Retensi Gen Z secara nyata pada tingkat signifikansi alpha = 5%.* |
| Effect size | *Nilai Pseudo R-squared sebesar 0.0031 menunjukkan bahwa variasi kegunaan sistem hanya mampu menjelaskan 0.31% dari variabilitas keputusan retensi pengguna, mengonfirmasi efek yang sangat kecil (weak effect).* |
| Practical significance | Pengguna Gen Z tetap menggunakan platform bukan karena aplikasi tersebut sangat mudah digunakan (skor SUS hanya berada di rentang rata-rata ~62-63), melainkan karena nilai manfaat lain, seperti murahnya harga barang atau keunikan interaksi belanja langsung. |
| Hubungan ke RQ | Menjawab RQ-1 bahwa kegunaan kedua fitur tersebut belum mampu menjadi stimulan penggerak retensi pengguna secara mandiri. |
| Perbandingan literatur |Hasil ini memperkaya khazanah riset perilaku konsumen digital bahwa loyalitas social commerce lebih didorong oleh pemenuhan aspek kepuasan hedonik dibandingkan aspek teknis kegunaan antarmuka semata. |

---

## Latihan 3 — Failure Analysis

Latih kemampuan failure analysis: hipotesis TIDAK didukung. Apa yang bisa dipelajari?

**Skenario:** Metode baru Anda mendapat F1 = 83.2%, baseline = 84.7%. p = 0.12 (tidak signifikan).

| Pertanyaan | Jawaban |
|-----------|---------|
| Apakah ini "gagal"? | *Bukan gagal. Hasil di mana H0 tidak ditolak adalah temuan ilmiah yang valid dan jujur. Menolak mitos bahwa "aplikasi harus selalu mendapat skor SUS tinggi agar pengguna tidak pindah" justru merupakan kontribusi riil riset ini. |
| Kemungkinan penyebab? | *Adanya bias sebaran kelas respons (Class Imbalance) di mana 88 dari 100 responden sudah terlanjur loyal memilih "Ya", sehingga fluktuasi skor SUS tidak terlihat pengaruhnya pada kelompok minoritas yang memilih "Tidak".* |
| Boundary condition? | *Model evaluasi usability murni ini mencapai batas kegunaannya ketika diterapkan pada aplikasi yang memiliki efek ketergantungan sosial tinggi (high social attachment) di kalangan mahasiswa Universitas Putra Bangsa.* |
| Insight yang bisa diambil? | *Ada batasan toleransi kesalahan antarmuka pengguna (usability tolerance). Selama aplikasi masih fungsional (OK), pengguna tidak akan berpaling jika alternatif nilai ekonomis produk tetap tinggi.* |
| Apakah layak dilaporkan? Mengapa? | *Sangat Layak. Melaporkan hasil apa adanya menjauhkan peneliti dari praktik manipulasi data (p-hacking) dan memberikan rambu-rambu penting bagi pengembang aplikasi bahwa strategi retensi tidak boleh hanya fokus pada perbaikan UI/UX saja.* |

**Limitation terkait:**
| Jenis | Ancaman | Dampak |
|-------|---------|--------|
| *Statistical* | *Hanya 5 run per skenarioo* | *Power test rendah dan estimasi variabilitas performa model menjadi kurang stabil.* |
| Construct | Penggunaan metrik F1-score tunggal tanpa melihat Confusion Matrix menyeluruh. |  Potensi bias evaluasi tersembunyi jika terjadi ketimpangan distribusi kelas data (class imbalance). |
| External Validity | Eksperimen hanya dievaluasi pada 1 jenis karakteristik dataset lokal.  | Generalisasi model di domain atau arsitektur dataset lain yang lebih variatif belum teruji sepenuhnya. |

---

## Refleksi

> Apakah "failure" dalam riset benar-benar gagal, atau justru kontribusi? Bagaimana failure analysis mengubah cara Anda melihat hasil negatif?

> Failure atau tidak terdukungnya hipotesis di dalam riset ilmiah bukanlah sebuah kegagalan personal maupun kegagalan sistem, melainkan sebuah bentuk kontribusi pengetahuan yang baru. Hasil negatif memberi tahu dunia akademik mengenai adanya kondisi batas (boundary conditions) di mana suatu teori umum ternyata tidak berlaku pada ruang lingkup atau populasi tertentu.


> Melalui failure analysis, saya belajar melihat hasil negatif bukan sebagai sesuatu yang harus disembunyikan atau dimanipulasi, melainkan sebagai peluang emas untuk menggali anomali secara kritis. Hal ini membuktikan integritas ilmiah saya sebagai mahasiswa Universitas Putra Bangsa yang melaporkan kebenaran data lapangan apa adanya secara objektif, rasional, dan bertanggung jawab.