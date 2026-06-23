# WS-09: Implementation & Environment

> **Bab 9 — Implementasi Riset & Kontrol Lingkungan**

---

## Ringkasan Materi

### Implementasi Riset ≠ Coding Biasa

Tujuan implementasi riset bukan membuat software yang berfungsi, melainkan membangun **instrumen pengukuran yang konsisten**. Setiap modul harus di-mapping ke variabel (dari Bab 6), parameter harus config-driven, dan logging aktif dari hari pertama.

### Reproducible Implementation Model

```
Design → Implementation → Environment Setup → Execution Consistency → Reproducibility → Trustworthy Result
```

Setiap transisi memiliki syarat:
- Design → Implementation: kode sesuai mapping variabel-ke-komponen
- Implementation → Environment: versi, dependency, seed, path, OS eksplisit
- Environment → Consistency: seed terkunci, urutan deterministik
- Consistency → Reproducibility: dokumentasi lengkap
- Reproducibility → Trust: siapa pun ikuti dokumentasi → hasil sama/serupa

### Repeatability vs Reproducibility

| Level | Peneliti | Environment | Hasil |
|-------|---------|-------------|-------|
| **Repeatability** | Sama | Sama | Sama persis |
| **Reproducibility** | Berbeda | Berbeda (ikuti docs) | Sama/serupa |

Capai **repeatability** dulu, baru **reproducibility**.

### Engineering vs Research Perspective

| Aspek | Engineering | Research |
|-------|-----------|---------|
| Tujuan | Sistem berfungsi untuk user | Instrumen pengukuran konsisten |
| Dependency | Update ke terbaru | Lock di versi spesifik |
| Testing | Unit, integration, E2E | Repeatability test (run ulang → sama?) |
| Dokumentasi | User guide, API docs | Environment spec, execution steps, expected output |
| Config | Default masuk akal | Setiap parameter eksplisit & adjustable |

### Jebakan Kognitif

1. Menunda environment setup → bug sulit dilacak
2. Tidak pakai version control → hasil tidak bisa direkonstruksi
3. Menolak Docker/container → "di laptop saya bisa" saat review
4. 3× hasil sama ≠ repeatable (bisa cache/state tersimpan)

### Istilah Penting

- **Environment Specification** — Deskripsi lengkap: hardware, OS, runtime, library + versi, config, seed
- **Dependency** — Komponen eksternal yang harus di-lock versinya
- **Config-driven** — Parameter dieksternalisasi ke file konfigurasi, bukan hardcode

---

## Template A.9 — Dokumentasi Setup Eksperimen

```
EXPERIMENT SETUP DOCUMENTATION

Hardware:
  CPU     : Minimal Intel Core i5 generasi 8 ke atas 
  RAM     : Minimal 8 GB 
  GPU     : Tidak diperlukan 
  Storage : Minimal 10 GB 

Software:
  OS        : Windows 10/11 (64-bit)
  Runtime   : SPSS Statistics v26 (regresi logistik biner)
              RapidMiner Studio v9.10 (Naïve Bayes + 10-Fold CV)
  Framework : Google Forms, Microsoft Excel v2019+

Dependencies:
| Library | Version | Sumber | Hash/Checksum |
|SPSS Statistics|v26 |IBM |Regresi logistik |
|  RapidMiner | v9.10   | RapidMiner Inc |  Naïve Bayes + CV  |
| Microsoft Excel | v2019+ | Microsoft |  Preprocessing data |
|Google Forms | - | Google | Kuesioner online |
|SPSS Amos  | v26 | IBM  | Uji validitas &  |

Konfigurasi:
  Config file     : Dataset kuesioner
  Random seed     : Tidak berlaku untuk regresi logistik 
                    (deterministik). Naïve Bayes menggunakan seed default RapidMiner
  Hyperparameters : 10-Fold Cross Validation, 
                    threshold p < 0,05, ambang SUS ≥ 70

Reproducibility Check:
  [x] Dependency terdokumentasi (requirements.txt / lock file)
  [x] Seed ditetapkan di semua level (Python, NumPy, framework)
  [x] Config di version control
  [x] README instruksi reproduksi lengkap
```

---

## Latihan 1 — Environment Specification

Dokumentasikan environment untuk eksperimen Anda (boleh environment saat ini atau yang direncanakan).

| Komponen | Spesifikasi |
|----------|------------|
| CPU | Minimal Intel Core i5 generasi 8 ke atas atau setara |
| RAM | Minimal 8 GB |
| GPU | Tidak diperlukan — analisis berbasis statistik dan probabilistik |
| OS | Windows 10/11 64-bit |
| Runtime | SPSS Statistics v26 untuk regresi logistik; RapidMiner Studio v9.10 untuk Naïve Bayes |
| Framework | Google Forms untuk pengumpulan data; Microsoft Excel untuk preprocessing |
| Random Seed | Tidak berlaku untuk regresi logistik. Naïve Bayes menggunakan seed default RapidMiner dengan 10-Fold CV |

**Dependencies (minimal 5):**

| Library | Version | Alasan Dibutuhkan |
|---------|---------|-------------------|
| SPSS Statistics | v26 | Menjalankan regresi logistik biner dan uji signifikansi p-value |
| RapidMiner Studio | v9.10 | Membangun model Naïve Bayes dan evaluasi 10-Fold Cross Validation |
| Microsoft Excel | v2019+ | Preprocessing data — cleaning, pengkodean variabel, format dataset |
| Google Forms| - | Pengumpulan data kuesioner SUS dari 115 responden secara online |
| SPSS Amos | v26 | Uji validitas Pearson dan reliabilitas Cronbach's Alpha sebelum analisis utama |

---

## Latihan 2 — Repeatability Test Plan

Rancang tes repeatability sederhana: jalankan kode yang sama 3× di environment yang sama.

| Run | Seed | Metrik Utama | Hasil Sama? |
|-----|------|-------------|-------------|
| 1 | Default RapidMiner | Macro-average F1-score | — |
| 2 | Default RapidMiner | Macro-average F1-score | [x] Ya / [ ] Tidak |
| 3 | Default RapidMiner | Macro-average F1-score | [x] Ya / [ ] Tidak |

**Jika hasil berbeda, kemungkinan penyebab:**
> Pengacakan partisi data pada operator X-Validation di RapidMiner tidak dikunci menggunakan Local Seed (masih menggunakan sistem acak dinamis), atau adanya perubahan urutan baris data pada file excel sebelum di-import..

**Checklist kontrol yang sudah diterapkan:**
- [✅] Random seed di-set di semua level
- [✅] Tidak ada background process yang mengganggu
- [✅] Cache dibersihkan antar-run
- [✅] Config file yang sama untuk semua run

---

## Latihan 3 — README Eksperimen

Tulis README minimum untuk eksperimen Anda (6 komponen wajib).

```
# Judul Eksperimen: Analisis Usability Fitur Live Shopping 
  dan Product Reviews terhadap Retensi Pengguna TikTok Shop pada Generasi Z Menggunakan Naïve Bayes

## 1. Environment
>  OS        : Windows 10/11 64-bit
  Tools     : SPSS Statistics v26, RapidMiner Studio v9.10,
              Microsoft Excel v2019+
  Hardware  : Minimal Intel Core i5, RAM 8 GB
  GPU       : Tidak diperlukan

## 2. Installation
> 1. Install SPSS Statistics v26 dari IBM
  2. Install RapidMiner Studio v9.10 dari rapidminer.com
  3. Install Microsoft Excel v2019 atau lebih baru
  4. Tidak diperlukan instalasi library tambahan

## 3. Data
> Sumber  : Kuesioner online via Google Forms
  Format  : File .xlsx (Microsoft Excel)
  Ukuran  : 115 responden, 23 indikator pertanyaan SUS
  Isi     : Skor SUS fitur live shopping (10 item), 
            skor SUS fitur product reviews (10 item), 
            dan label retensi pengguna 

## 4. Execution
> Langkah 1 — Buka file dataset .xlsx di Microsoft Excel,
              lakukan cleaning data dan hitung skor SUS 
              per fitur menggunakan rumus baku Brooke (1996)
  Langkah 2 — Import dataset ke SPSS, jalankan analisis 
              regresi logistik biner dengan skor SUS sebagai 
              IV dan label retensi sebagai DV
  Langkah 3 — Import dataset ke RapidMiner, bangun model 
              Naïve Bayes dengan 10-Fold Cross Validation, 
              jalankan dan catat hasilnya


## 5. Configuration
>  File config  : Dataset kuesioner (data_tiktokshop.xlsx)
  Parameter    : 
    - Threshold signifikansi  : p < 0,05
    - Ambang kelayakan SUS    : ≥ 70
    - Fold CV                 : 10-Fold Cross Validation
    - Metrik utama            : Macro-average F1-score


## 6. Expected Output
> 1. File Output SPSS (*.spv): Menampilkan tabel "Variables in the Equation" dengan nilai Sig. (p-value) < 0,05 untuk uji kausalitas, serta nilai Nagelkerke R Square.
2. Performance Vector RapidMiner: Menampilkan Confusion Matrix dengan format:
   - Accuracy: ~85%
```

---

## Refleksi

> Apakah eksperimen Anda saat ini bisa direproduksi oleh orang lain tanpa bantuan Anda? Komponen apa yang masih hilang?

**Level saat ini:** [✅] Repeatability / [ ] Reproducibility / [ ] Belum keduanya
**Komponen yang belum terdokumentasi:**
> 1. File dataset mentah yang telah disamarkan (.xlsx) belum di-upload ke repository umum.
> 2. Petunjuk filtering data untuk mengeliminasi 115 responden yang tidak konsisten belum dituliskan secara langkah-per-langkah.
> 3. File ekspor proses workflow RapidMiner (.rmp) belum dilampirkan agar orang lain tinggal melakukan klik run secara instan.