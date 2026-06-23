# WS-07: Experimental Design & Validity

> **Bab 7 — Experimental Design & Validity**

---

## Ringkasan Materi

### Correlation ≠ Causality

Kausalitas membutuhkan 3 syarat:
1. **Covariance** — X dan Y bergerak bersama
2. **Temporal precedence** — X berubah sebelum Y
3. **Elimination of alternatives** — Tidak ada faktor lain yang menjelaskan Y

Controlled experiment adalah satu-satunya metode yang bisa membuktikan kausalitas.

### Empat Jenis Validitas

| Jenis | Pertanyaan | Ancaman Umum |
|-------|-----------|-------------|
| **Internal** | Apakah hubungan IV→DV nyata? | Confounding variable, selection bias |
| **External** | Apakah bisa digeneralisasi? | Dataset terlalu spesifik |
| **Construct** | Apakah mengukur konsep yang benar? | Metrik tidak sesuai |
| **Conclusion** | Apakah kesimpulan statistik valid? | Sample size kecil, uji salah |

Internal dan external validity sering berkonflik: semakin terkontrol (internal kuat) → semakin artificial (external lemah).

### Tiga Tipe Eksperimen dalam Riset TI

| Tipe | Deskripsi | Kapan Digunakan |
|------|----------|----------------|
| **Comparison Study** | Metode A vs B pada kondisi identik | Membandingkan pendekatan berbeda |
| **Ablation Study** | Full system → lepas komponen satu per satu | Mengukur kontribusi tiap komponen |
| **Parameter Study** | Variasikan satu parameter, amati dampak | Uji sensitifitas/robustness |

### Fairness dalam Perbandingan

Perbandingan yang adil = **kondisi identik** untuk semua metode: dataset sama, preprocessing sama, tuning effort sebanding, environment sama, metrik sama.

Contoh tidak adil: Transformer (30 fitur tambahan + Bayesian optimization) vs RF (default params) → hasilnya misleading.

### Threats to Validity = Diidentifikasi Sebelum Eksperimen

Ancaman validitas harus diidentifikasi **sebelum** eksperimen dan mitigasinya dirancang sebagai bagian dari desain — bukan ditulis sebagai boilerplate setelah selesai.

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan testing | Memastikan sistem memenuhi requirement | Membuktikan hubungan kausal antar variabel |
| Baseline | Versi sebelumnya (last release) | Metode tervalidasi dari literatur |
| Kegagalan | Bug → fix → release | H₀ tidak ditolak → tetap kontribusi ilmiah |
| Sukses | 100% test pass | Evidence valid — mendukung atau menolak hipotesis |

### Istilah Penting

- **Causality** — Hubungan sebab-akibat (covariance + temporal + elimination)
- **Controlled Experiment** — Ubah satu variabel, kontrol sisanya, amati efek
- **Fairness** — Semua metode diuji pada kondisi yang benar-benar identik
- **Threats to Validity** — Faktor yang bisa melemahkan kesimpulan jika tidak dimitigasi
- **Conclusion Validity** — Validitas statistik: power, sample size, uji yang tepat

---

## Template A.7 — Desain Eksperimen Lengkap

```
EXPERIMENT DESIGN

Research Question : Bagaimana pengaruh usability fitur live shopping dan 
product reviews terhadap retensi pengguna TikTok Shop 
pada Generasi Z, dan bagaimana pola prediksinya 
menggunakan Naïve Bayes?
Hypothesis        : 
H₀: Usability fitur live shopping dan product reviews 
    tidak berpengaruh signifikan terhadap retensi 
    pengguna TikTok Shop pada Generasi Z.
H₁: Usability fitur live shopping dan product reviews 
    berpengaruh signifikan terhadap retensi pengguna 
    TikTok Shop pada Generasi Z.
Tipe Eksperimen   : [x] Comparison  [ ] Ablation  [ ] Parameter

Kondisi Eksperimen:
| Kondisi | Deskripsi | IV Value | CV Settings |
|---------|-----------|----------|-------------|
| Control |  Regresi Logistik Biner |  Skor SUS | 115 responden Gen Z |
| Treatment | Model machine learning untuk klasifikasi dan pola prediksi retensi. | Algoritma Naïve Bayes | Dataset 115 responden Gen Z, 10-Fold Cross Validation |

Fairness Checklist:
  [x] Dataset identik untuk semua kondisi
  [x] Preprocessing setara
  [x] Tuning effort setara
  [x] Environment identik
  [x] Metrik evaluasi sama

Threat Analysis:
| Threat Type | Ancaman Spesifik | Mitigasi |
|-------------|-----------------|----------|
| Internal    |  Responden mengisi kuesioner secara asal-asalan |     Melakukan logic check (cleaning data) dan uji validitas-reliabilitas kuesioner. |
| External    |  Hasil penelitian hanya mencerminkan perilaku Gen Z di area kampus tertentu. |  Memastikan kriteria sampling (purposive sampling) menyasar Gen Z yang aktif belanja di TikTok Shop secara luas. |
| Construct   |  Metrik usability (SUS) dianggap tidak cocok untuk platform social commerce. | Menggunakan instrumen SUS baku yang sudah tervalidasi secara global untuk pengujian sistem software/e-commerce. |
| Conclusion  | Ukuran sampel (115 responden) dianggap terlalu kecil untuk pemodelan Naïve Bayes. | Menggunakan metode evaluasi 10-Fold Cross-Validation untuk meminimalkan bias pembagian data data train-test. |

Statistical Plan:
  Uji statistik   : Analisis Regresi Logistik Biner & Evaluasi Klasifikasi (Confusion Matrix).
  Justifikasi      : Regresi untuk menguji signifikansi hubungan sebab-akibat (H₁), Confusion Matrix untuk menguji performa prediksi AI.
  Alpha            : 0,05 (Tingkat kepercayaan 95%)
  Effect size min  : Nagelkerke R² untuk regresi logistik dan macro-average F1-score untuk  Naïve Bayes.
```

---

## Latihan 1 — Desain Eksperimen

Susun desain eksperimen berdasarkan RQ, variabel, dan sistem dari WS-04 sampai WS-06.

**RQ:** Bagaimana pengaruh usability fitur live shopping dan product reviews terhadap retensi pengguna TikTok Shop pada Generasi Z, dan bagaimana pola prediksinya menggunakan Naïve Bayes?
**Tipe eksperimen:** [x] Comparison / [ ] Ablation / [ ] Parameter

| Kondisi | Deskripsi | IV Value | CV Settings |
|---------|-----------|----------|-------------|
| Control | Pengujian statistik regresi untuk dasar penentuan pengaruh. | Regresi Logistik Biner | Dataset 115 responden Gen Z, alpha = 0,05, instrumen SUS baku |
| Treatment | Pemodelan klasifikasi untuk memprediksi pola retensi pengguna | Algoritma Naïve Bayes | Dataset 115 responden, skema evaluasi 10-Fold Cross Validation |

---

## Latihan 2 — Fairness Checklist

Evaluasi apakah desain eksperimen di Latihan 1 sudah fair.

| Kriteria | Status | Detail |
|----------|--------|--------|
| Dataset identik |  ✅  | Kedua metode diuji menggunakan dataset yang sama, yaitu data dari 115 responden Gen Z TikTok Shop. |
| Preprocessing setara | ✅  | Skala input data untuk kedua metode disamakan (skor SUS 0-100 dan label biner). |
| Tuning effort setara | ✅ | Kedua model dijalankan pada parameter standar tanpa optimasi berlebih di salah satu model. |
| Environment identik | ✅  | Pemrosesan statistik dan data mining dilakukan menggunakan tools standar (SPSS dan RapidMiner). |
| Metrik evaluasi sama | ✅  | Keduanya melihat luaran prediksi keputusan retensi (Ya/Tidak). |

**Ada yang tidak fair?** [ ] Ya / [x] Tidak
> Jika ya, bagaimana cara memperbaikinya? ________________

---

## Latihan 3 — Threat Analysis

Identifikasi ancaman validitas untuk desain eksperimen ini.

| Threat Type | Ancaman Spesifik | Mitigasi |
|-------------|-----------------|----------|
| Internal | *Responden mengisi asal asalan* | *Logic check saat cleaning data + uji validitas & reliabilitas sebelum analisis utama* |
| External | Sampel hanya Gen Z tertentu, tidak mewakili seluruh Gen Z Indonesia. | Nyatakan keterbatasan ini secara jujur di bagian limitasi penelitian. |
| Construct | SUS dianggap tidak cocok untuk social commerce. | SUS sudah tervalidasi global untuk software/e-commerce (Brooke, 1996) |
| Conclusion | Class imbalance: 101 Ya vs 14 Tidak membuat akurasi menyesatkan. | Gunakan macro-average F1-score sebagai metrik utama, bukan hanya accuracy. |

**Ancaman mana yang paling sulit dimitigasi?** External Validity
**Mengapa?**
> Karena penelitian kuantitatif berbasis kuesioner online dengan 115 sampel memiliki keterbatasan geografis dan demografis, sehingga sangat sulit mengklaim bahwa hasil ini mewakili seluruh Generasi Z di Indonesia tanpa melakukan sampling berskala nasional.

---

## Refleksi

> Sebuah paper melaporkan "metode kami mengalahkan semua baseline." Apa 3 pertanyaan pertama yang harus diajukan untuk mengevaluasi klaim ini?

**Jawaban:**
1. Apakah dataset dan preprocessing yang digunakan sama adilnya antara metode baru dan metode baseline?
2.Apakah metode baseline sudah di-tuning dengan maksimal, atau sengaja dibiarkan memakai parameter default agar terlihat kalah?
3. Metrik apa yang digunakan untuk mengklaim kemenangan tersebut? Apakah menang di Akurasi tapi sebenarnya kalah di F1-Score karena datanya timpang?
