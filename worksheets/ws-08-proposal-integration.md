# WS-08: Proposal Integration (UTS)

> **Bab 8 — Proposal & Checkpoint**

---

## Ringkasan Materi

### Proposal = Satu Argumen Utuh

Proposal riset bukan kumpulan bab yang independen. Ia adalah **satu argumen** yang mengalir dari masalah ke rencana solusi. Jika satu koneksi putus, seluruh proposal kehilangan koherensi.

### Integration Map — 6 Koneksi Kritis

```
Problem (Bab 2) → Gap (Bab 3) → RQ & H (Bab 4) → Metrik (Bab 5) → Sistem (Bab 6) → Eksperimen (Bab 7)
```

| Koneksi | Pertanyaan Verifikasi |
|---------|----------------------|
| Problem → Gap | Apakah gap muncul dari analisis literatur terhadap masalah? |
| Gap → RQ | Apakah RQ langsung menjawab gap yang teridentifikasi? |
| RQ → Metrik | Apakah setiap variabel di RQ punya metrik terdefinisi? |
| Metrik → Sistem | Apakah setiap metrik bisa diukur oleh komponen sistem? |
| Sistem → Eksperimen | Apakah desain eksperimen menggunakan sistem sebagai instrumen? |

### Koherensi Vertikal + Horizontal

- **Vertikal** — Alur logis atas-ke-bawah (problem → experiment)
- **Horizontal** — Konsistensi terminologi (nama variabel di RQ = di hipotesis = di metrik = di desain)

### Jebakan Kognitif

| Jebakan | Deskripsi |
|---------|----------|
| "Selling" Introduction | Menulis promosi, bukan menyajikan data dan gap |
| Copy-paste Methodology | Menyalin deskripsi tekstbook tanpa menyesuaikan ke RQ |
| Optimistic Timeline | Meremehkan waktu implementasi; selalu tambah buffer 30-50% |
| No Possibility of Failure | Mengimplikasikan hasil pasti sukses — proposal jujur mengakui H₀ mungkin tidak ditolak |

### Struktur Proposal

1. **Pendahuluan** — Latar belakang + problem statement (Bab 1-2)
2. **Tinjauan Pustaka** — Literature review + gap + baseline (Bab 3)
3. **RQ / Kontribusi / Hipotesis** — (Bab 4)
4. **Metodologi** — Metrik + sistem + desain eksperimen (Bab 5-7)
5. **Timeline & Output**

### Istilah Penting

- **Integration Map** — Diagram 6 koneksi kritis antar komponen proposal
- **Vertical Coherence** — Alur logis atas-ke-bawah
- **Horizontal Coherence** — Konsistensi terminologi di semua bagian
- **Checkpoint** — Titik self-assessment sebelum transisi dari desain ke eksekusi

---

## Template A.8 — Integration Checklist

```
PROPOSAL INTEGRATION CHECKLIST

Koneksi Vertikal (Flow Atas-Bawah):
  [x] Problem → Gap: Usability fitur TikTok Shop 
      terdokumentasi marginal-low (SUS 52 & 53) dari 
      jurnal referensi, dan gap muncul dari literatur 
      yang belum menganalisis usability per fitur
  [x] Gap → RQ: langsung menanyakan pengaruh 
      usability level fitur dan kemampuan prediksi 
      Naïve Bayes terhadap retensi
  [x] RQ → Hypothesis: H₀ dan H₁ memprediksi 
      ada / tidaknya pengaruh signifikan usability 
      terhadap retensi, terhubung langsung ke RQ
  [x] Hypothesis → Metric: metrik mengukur variabel dalam hipotesis
  [x] Metric → System: Skor SUS dari kuesioner 
      menghasilkan IV, label retensi menghasilkan DV, 
      SPSS dan RapidMiner menghitung metrik
  [x] System → Experiment: Kuesioner SUS menjadi 
      instrumen pengujian Kondisi A (regresi) 
      dan Kondisi B (Naïve Bayes)

Koneksi Horizontal (Konsistensi):
  [x] Istilah sama di semua bagian
  [x] Variabel di RQ = variabel di hipotesis = metrik di desain
  [x] Scope tidak berubah dari masalah ke eksperimen

Rubrik Self-Assessment:
| Kriteria | 1 (Lemah) | 2 (Cukup) | 3 (Baik) | Skor |
|----------|-----------|-----------|----------|------|
| Koherensi |  Koneksi antar bagian terputus atau tidak logis  |  Sebagian besar koneksi ada tapi ada yang lemah | Semua koneksi dari problem sampai eksperimen terhubung logis dan bisa ditelusuri |  3  |
| Specificity | Variabel dan metrik masih abstrak  | Sebagian variabel terdefinisi tapi belum semua numerik | Semua variabel, metrik, dan metode terdefinisi numerik dan spesifik |  3 |
| Feasibility |Penelitian sulit dijalankan dengan sumber daya yang ada | Bisa dijalankan tapi ada tantangan yang belum diantisipasi |  Penelitian bisa dijalankan dengan tools yang tersedia, tantangan sudah diidentifikasi|  2 |
| Rigor     |  Hipotesis tidak testable, ancaman validitas tidak diidentifikasi | Hipotesis testable tapi ancaman validitas belum semua dimitigasi | Hipotesis testable dan terhubung ke RQ, semua ancaman validitas diidentifikasi beserta mitigasinya |  3 |
```

---

## Latihan 1 — Kompilasi Proposal Mini

Kumpulkan hasil dari WS-02 sampai WS-07 menjadi satu ringkasan proposal.

| Komponen | Sumber | Isi (1-2 kalimat) |
|----------|--------|-------------------|
| Problem Statement | WS-02 | Usability fitur live shopping dan product reviews TikTok Shop berada di kategori marginal-low (skor SUS 52 dan 53), sehingga pengguna Generasi Z berpotensi tidak bertahan menggunakan platform karena kualitas pengalaman fitur yang belum memadai. |
| Gap | WS-03 | Belum ada studi yang menganalisis usability pada level fitur live shopping dan product reviews secara terpisah, dan belum ada yang menggabungkan pendekatan eksplanatori dan prediktif secara komplementer dalam analisis retensi pengguna TikTok Shop. |
| RQ | WS-04 | Bagaimana pengaruh usability fitur live shopping dan product reviews terhadap retensi pengguna TikTok Shop pada Generasi Z, dan seberapa akurat algoritma Naïve Bayes memprediksi pola retensi tersebut dibandingkan baseline regresi logistik? |
| Hipotesis | WS-04 | H₀: Skor SUS fitur live shopping dan product reviews tidak berpengaruh signifikan terhadap label retensi pengguna TikTok Shop Generasi Z (p ≥ 0,05). H₁: Skor SUS fitur live shopping dan product reviews berpengaruh signifikan terhadap label retensi pengguna TikTok Shop Generasi Z (p < 0,05). |
| Variabel & Metrik | WS-05 | IV = skor SUS fitur live shopping dan product reviews (skala ratio 0–100); DV = label retensi pengguna (nominal: Ya/Tidak); CV = dataset 115 responden yang sama, instrumen SUS baku Brooke (1996), threshold p < 0,05; Metrik = p-value, Nagelkerke R², accuracy, macro-average F1-score. |
| Sistem | WS-06 | Kondisi A (baseline): kuesioner SUS → skor IV → regresi logistik biner di SPSS → output p-value dan koefisien. Kondisi B (intervention): kuesioner SUS → skor IV → Naïve Bayes di RapidMiner dengan 10-Fold CV → output confusion matrix dan F1-score. |
| Desain Eksperimen | WS-07 | Comparison study: Kondisi A = regresi logistik biner sebagai pendekatan eksplanatori standar; Kondisi B = Naïve Bayes sebagai pendekatan prediktif. Keduanya menggunakan dataset identik dari 115 responden Gen Z agar perbandingan fair. |

---

## Latihan 2 — Integration Checklist

Verifikasi 6 koneksi kritis. Isi dengan merujuk tabel di Latihan 1.

| Koneksi | Status | Bukti |
|---------|--------|-------|
| Problem → Gap | ✅ | Masalah usability marginal-low ditemukan dari jurnal referensi, dan gap muncul karena belum ada studi yang menganalisis usability per fitur secara terpisah. |
| Gap → RQ | ✅ | RQ langsung menanyakan pengaruh usability pada level fitur dan kemampuan prediksi Naïve Bayes |
| RQ → Hypothesis | ✅ | H₀ dan H₁ memprediksi ada atau tidaknya pengaruh signifikan usability terhadap retensi, yang merupakan inti dari RQ. |
| Hypothesis → Metric | ✅ | H₀/H₁ diuji menggunakan p-value (threshold 0,05) untuk regresi, dan macro-average F1-score untuk Naïve Bayes — keduanya mengukur variabel dalam hipotesis secara langsung. |
| Metric → System | ✅ | Skor SUS dihasilkan oleh kuesioner (komponen IV), label retensi dihasilkan oleh modul klasifikasi (komponen DV), dan semua metrik dihitung otomatis oleh SPSS dan RapidMiner. |
| System → Experiment | ✅ | Desain eksperimen menggunakan output kuesioner SUS sebagai input Kondisi A (regresi) dan Kondisi B (Naïve Bayes), sehingga sistem benar-benar menjadi instrumen pengujian. |

**Koneksi mana yang paling lemah?** Metric → System
**Bagaimana cara memperkuatnya?**
>Karena penelitian ini berbasis kuesioner dan bukan sistem software yang dibangun sendiri, perlu dijelaskan secara eksplisit bahwa SPSS dan RapidMiner berperan sebagai "komponen sistem" yang menghasilkan metrik  bukan sekadar alat bantu analisis.

**Konsistensi horizontal — apakah istilah dan scope konsisten?** [x] Ya / [ ] Tidak
> Jika tidak, di bagian mana terjadi inkonsistensi? _________

---

## Latihan 3 — Rubrik Self-Assessment

Evaluasi proposal mini menggunakan rubrik.

| Kriteria | Skor (1-3) | Justifikasi |
|----------|-----------|-------------|
| Koherensi | 3 | Alur dari problem → gap → RQ → hipotesis → metrik → sistem → eksperimen sudah terhubung dengan logis dan tidak ada koneksi yang putus. |
| Specificity | 3 | Semua variabel, metrik, dan metode sudah terdefinisi secara spesifik dan numerik — skor SUS 0–100, threshold p < 0,05, 115 responden, 10-Fold CV. |
| Feasibility | 2 | Penelitian berbasis kuesioner dan tools yang tersedia (SPSS dan RapidMiner), namun ketidakseimbangan kelas data (101 vs 14) menjadi tantangan nyata yang perlu diantisipasi. |
| Rigor | 3 | Ancaman validitas sudah diidentifikasi sejak awal (internal, external, construct, conclusion) beserta mitigasinya, dan metrik evaluasi dipilih berdasarkan karakteristik data. |

**Skor total:** 11 / 12

**Apakah proposal siap untuk fase eksekusi?** [x] Ya / [ ] Belum
> Jika belum, apa yang perlu diperbaiki? __________________

---

## Refleksi

> Dari seluruh proses WS-01 sampai WS-08, bagian mana yang paling mudah dan paling sulit? Mengapa? Apa yang akan dilakukan berbeda jika mengulang dari awal?

**Bagian termudah:** Latihan 1 - Karena semua komponen sudah dikerjakan di WS sebelumnya, yang perlu dilakukan hanya merangkum dan memastikan semuanya terhubung. Prosesnya seperti menyusun puzzle yang potongannya sudah tersedia.
**Bagian tersulit:** Latihan 2 — Integration Checklist, Memverifikasi bahwa setiap koneksi benar-benar terhubung secara logis  bukan hanya terlihat nyambung  membutuhkan pemahaman mendalam tentang seluruh alur penelitian dari awal sampai akhir.
**Yang akan dilakukan berbeda:**
> Jika mengulang dari awal, topik penelitian akan ditetapkan lebih awal sejak WS-01 agar semua latihan dari awal sampai akhir langsung mengacu pada satu topik yang sama. Dengan demikian tidak perlu melakukan penyesuaian saat topik berganti di WS-04, dan seluruh alur penelitian bisa lebih konsisten sejak hari pertama.
