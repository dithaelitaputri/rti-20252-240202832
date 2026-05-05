# WS-04: Research Question & Hypothesis

> **Bab 4 — Research Question, Contribution & Hypothesis**

---

## Ringkasan Materi

### RQ Bukan Pertanyaan Biasa

Research Question yang baik secara implisit mengandung cetak biru eksperimen: subjek, baseline, metrik, domain, dataset.

| Kualitas | Contoh |
|----------|--------|
| **Buruk** | "Bagaimana pengaruh deep learning terhadap deteksi malware?" |
| **Baik** | "Apakah CNN menghasilkan F1-Score lebih tinggi dari RF pada CIC-MalMem-2022?" |

Perbedaan: RQ yang baik menyebutkan **metode spesifik**, **metrik terukur**, **baseline**, dan **dataset**.

### Tiga Jenis RQ

| Jenis | Pola | Kebutuhan |
|-------|------|-----------|
| **Comparison** | A vs B → mana lebih baik? | ≥ 2 metode, metrik sama |
| **Improvement** | A' vs A → modifikasi lebih baik? | Pre/post, bukti perbaikan |
| **Exploratory** | Faktor X₁...Xₙ → pengaruh terhadap Y? | Multi-variabel, korelasi/regresi |

### Contribution Statement

Tiga jenis kontribusi: **Improvement** (metode terbukti lebih baik), **Comparison** (perbandingan sistematis yang belum ada), **Novel Approach** (pendekatan baru). Kontribusi harus terhubung langsung dengan gap — kontribusi tanpa gap = klaim tanpa justifikasi.

### Hypothesis H₀ / H₁

- **H₀** (Null) = Tidak ada perbedaan signifikan — asumsi default, harus dibuktikan salah
- **H₁** (Alternative) = Ada perbedaan signifikan — diterima hanya jika H₀ ditolak
- Harus **falsifiable**, mengandung **metrik terukur**, dirumuskan **SEBELUM eksperimen**

### Rantai Operasionalisasi

```
RQ → Variable → Metric → Data → Analysis
```

Jika rantai ini tidak lengkap, RQ belum mature. Bi-directional: RQ yang tidak bisa jadi hipotesis testable harus direvisi mundur.

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan pertanyaan | Apa yang harus dibangun? | Apa yang harus dibuktikan? |
| Bentuk jawaban | Sistem yang berfungsi | Bukti empiris terukur |
| Sukses diukur oleh | User satisfaction, uptime | Signifikansi statistik, effect size |
| Jika gagal | Debug dan perbaiki | Laporkan, analisis mengapa |

### Istilah Penting

- **Research Question (RQ)** — Pertanyaan spesifik: variabel terukur + metrik + konteks
- **Contribution Statement** — Apa yang diketahui setelah riset selesai yang sebelumnya belum ada
- **H₀ / H₁** — Null vs Alternative Hypothesis
- **Falsifiability** — Kondisi hipotesis ditolak harus bisa didefinisikan sebelum eksperimen
- **Operationalization** — Proses mewujudkan konsep abstrak menjadi variabel terukur

---

## Template A.4 — RQ-Contribution-Hypothesis

```
RQ-CONTRIBUTION-HYPOTHESIS

Gap Statement  : Kesenjangan antara pengalaman penggunaan (usability) yang dirasakan dengan keputusan untuk melanjutkan penggunaan platform (retensi), serta terbatasnya kajian yang menganalisis pengaruh usability pada level fitur spesifik (live shopping dan product reviews) terhadap retensi dalam konteks social commerce.

Research Question:
  Tipe         : [x] Comparison  [ ] Improvement  [x] Exploratory
  Formulasi    : Bagaimana pengaruh usability level fitur (live shopping dan product reviews) terhadap retensi pengguna TikTok Shop pada Generasi Z, dan bagaimana pola prediksinya menggunakan Naïve Bayes?
  Variabel IV  : Usability Fitur Live Shopping dan Usability Fitur Product Reviews.
  Variabel DV  : Retensi Pengguna
  Metrik       : Skor System Usability Scale (SUS), Accuracy, Precision, Recall, dan F1-Score.
  Dataset      : 115 responden Generasi Z pengguna TikTok Shop.
  Baseline     : Ambang kelayakan SUS (>70) dan performa model klasifikasi (macro-average F1-score).

Quality Check RQ:
  [x] Variabel spesifik
  [x] Metrik jelas
  [x] Baseline ada
  [x] Konteks disebutkan
  [x] Memerlukan eksperimen (bukan hanya survei literatur)

Contribution Statement:
  Apa yang baru diketahui : Usability pada level fitur ternyata tidak berpengaruh signifikan terhadap retensi pengguna di social commerce, dan pendekatan prediktif (Naïve Bayes) memberikan insight pola perilaku yang tidak terjelaskan oleh model regresi linier.
  Jenis kontribusi        : [ ] Improvement  [x] Comparison  [x] Novel approach
  Gap yang diisi          : Mengisi celah keterpisahan antara pendekatan eksplanatori (regresi) dan prediktif (machine learning) dalam analisis retensi pengguna.

Hypothesis Pair:
  H₀ : Usability fitur live shopping dan product reviews tidak memiliki pengaruh signifikan terhadap retensi pengguna TikTok Shop.
  H₁ : Usability fitur live shopping dan product reviews memiliki pengaruh signifikan terhadap retensi pengguna TikTok Shop.
  Threshold              : Signifikansi p < 0,05 untuk regresi dan akurasi model klasifikasi.  
  Justifikasi threshold  : Standar umum dalam penelitian kuantitatif untuk menolak $H_0$ dan menguji performa model prediktif.
```

---

## Latihan 1 — Dari Gap ke RQ

Gunakan gap yang ditemukan di WS-03. Transformasikan menjadi Research Question.

**Gap dari WS-03:** Hubungan antara usability dan retensi yang belum konsisten dan jarangnya analisis pada level fitur spesifik dalam social commerce.

**RQ versi pertama (tulis bebas):**
> "Apakah persepsi usability fitur live shopping dan product reviews berpengaruh terhadap retensi pengguna Generasi Z di TikTok Shop, dan sejauh mana algoritma Naïve Bayes dapat memprediksi pola retensi tersebut?"

**Evaluasi RQ:**

| Komponen | Ada? | Isi |
|----------|------|-----|
| Metode spesifik | *Ya* | Naïve Bayes dan Regresi Logistik. |
| Metrik terukur | Ya | Skor SUS, Accuracy, Precision, Recall, F1-Score. |
| Baseline | Ya | Ambang SUS >70 dan macro-average F1-score |
| Dataset/konteks | Ya | 115 responden Generasi Z pengguna TikTok Shop. |

**Tipe RQ:** [x] Comparison / [ ] Improvement / [x] Exploratory

**RQ versi revisi (setelah evaluasi):**
> Bagaimana pengaruh usability fitur live shopping dan product reviews terhadap retensi pengguna Generasi Z di TikTok Shop menggunakan metrik SUS, dan seberapa akurat algoritma Naïve Bayes memprediksi retensi tersebut dibandingkan baseline performa klasifikasi?

---

## Latihan 2 — Hypothesis Pair

Rumuskan pasangan hipotesis dari RQ di Latihan 1.

| Komponen | Isi |
|----------|-----|
| H₀ | *Tidak ada pengaruh signifikan antara usability fitur terhadap retensi pengguna TikTok Shop.* |
| H₁ | Terdapat pengaruh signifikan antara usability fitur terhadap retensi pengguna TikTok Shop. |
| Metrik | Skor SUS dan Koefisien Regresi Logistik (p-value). |
| Threshold | p< 0,05> |
| Justifikasi threshold | |

**Apakah hipotesis ini falsifiable?** [x] Ya / [ ] Tidak
> Bagaimana cara membuktikannya salah? Jika hasil olah data statistik menunjukkan nilai signifikansi ($p-value$) lebih besar dari 0,05, maka hipotesis $H_1$ dinyatakan salah (ditolak) dan $H_0$ gagal ditolak.

---

## Latihan 3 — Rantai Operasionalisasi

Lengkapi rantai dari RQ hingga metode analisis.

| Tahap | Isi |
|-------|-----|
| RQ | *Bagaimana pengaruh usability fitur terhadap retensi pengguna TikTok Shop?* |
| Variable (IV) | *Skor Usability fitur live shopping dan product reviews.* |
| Variable (DV) | Status Retensi Pengguna (Kategorik: Ya/Tidak) |
| Metric | Skor SUS (0-100) dan probabilitas Naïve Bayes. |
| Data source | Kuesioner primer 115 responden Generasi Z. |
| Analysis method | Regresi Logistik Biner dan Klasifikasi Naïve Bayes. |

**Apakah rantai lengkap?** [x] Ya / [ ] Tidak
> Jika tidak, tahap mana yang perlu direvisi? ______________

---

## Refleksi

> Ambil satu judul skripsi/paper yang pernah dibaca. Coba ekstrak RQ-nya. Apakah RQ tersebut memenuhi semua komponen (metode, metrik, baseline, konteks)? Jika tidak, apa yang hilang?

**Judul:** Jika hasil olah data statistik menunjukkan nilai signifikansi ($p-value$) lebih besar dari 0,05, maka hipotesis $H_1$ dinyatakan salah (ditolak) dan $H_0$ gagal ditolak.
**RQ yang diekstrak:** Bagaimana pengaruh usability level fitur terhadap retensi pengguna TikTok Shop pada Generasi Z, dan bagaimana pola prediksinya menggunakan Naïve Bayes?
**Komponen yang hilang:** Tidak ada yang hilang; RQ ini sudah mencakup subjek (Gen Z), domain (social commerce), metode (Naïve Bayes), dan metrik (SUS & Prediksi) secara eksplisit.
