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
  Runtime   : Python v3.10+ (Lingkungan eksekusi analisis  data statistik) RapidMiner Studio v9.10 (Naïve Bayes + 10-Fold CV)
  Framework : Jupyter Notebook / VS Code, Google Forms

Dependencies:
| Library | Version | Sumber | Hash/Checksum |
|Python Runtime|v3.10+ |Python Software Foundation | Lingkungan komputasi utama pengganti SPSS |
|  Pandas | v2.0+   | PyPI (pip) |  Naïve Bayes + CV  |
| Microsoft Excel | v2019+ | Microsoft |  Preprocessing data |
|Google Forms | - | Google | Kuesioner online |
|SciPy  | v1.10+ | PyPI (pip)  | Komputasi statistik inferensial & Uji Validitas Pearson  
|Pingouin |	v0.5+ |	PyPI (pip)	| Perhitungan Uji Reliabilitas Cronbach's Alpha|
| RapidMiner | v9.10 | RapidMiner Inc |Pemodelan prediktif Naïve Bayes + X-Validation |

Konfigurasi:
  Config file     : Dataset kuesioner
  Random seed     : Terkunci pada np.random.seed(42) di skrip Python untuk kepastian data instrumen.
  Hyperparameters : 10-Fold Cross Validation, signifikansi p < 0.05, ambang validitas R > 0.183 (N=115),
ambang reliabilitas Cronbach's Alpha >= 0.60, ambang batas SUS >= 70.

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
| Runtime | Python v3.10+ untuk otomasi pengujian statistik instrumen; RapidMiner Studio v9.10 untuk Naïve Bayes |
| Framework | Google Forms untuk pengumpulan data; Microsoft Excel untuk preprocessing |
| Random Seed | `np.random.seed(42)` pada Python, dan mengaktifkan kunci Local Seed pada operator pengacak data di RapidMiner |

**Dependencies (minimal 5):**

| Library | Version | Alasan Dibutuhkan |
|---------|---------|-------------------|
| Python Language | v3.10+ | Runtime utama mengeksekusi logika pemrograman pengganti peran software SPSS. |
| Pandas | v2.0+ | Membaca berkas `.xlsx`, menghitung total skor, dan transformasi matriks data kuesioner. |
| SciPy | v1.10+ | Menghitung koefisien korelasi Pearson Product Moment secara otomatis untuk uji validitas data. |
| Pingouin | v0.5+ | Melakukan kalkulasi metrik Cronbach's Alpha secara langsung guna menguji reliabilitas instrumen kuesioner. |
| RapidMiner Studio | v9.10 | Membangun model Naïve Bayes dengan pembagian sampel data menggunakan teknik 10-Fold Cross Validation. |
| Microsoft Excel | v2019+ | Preprocessing data — cleaning, pengkodean variabel, format dataset |
| Google Forms| - | Pengumpulan data kuesioner SUS dari 115 responden secara online |


---

## Latihan 2 — Repeatability Test Plan

Rancang tes repeatability sederhana: jalankan kode yang sama 3× di environment yang sama.

| Run | Seed | Metrik Utama | Hasil Sama? |
|-----|------|-------------|-------------|
| 1 | Python & RM Seed = 42 | Nilai Cronbach's Alpha & F1-score | — |
| 2 | Python & RM Seed = 42 | Nilai Cronbach's Alpha & F1-score | [x] Ya / [ ] Tidak |
| 3 | Python & RM Seed = 42 | Nilai Cronbach's Alpha & F1-score | [x] Ya / [ ] Tidak |

**Jika hasil berbeda, kemungkinan penyebab:**
> Nilai seed acak belum dikunci di baris kode teratas skrip Python, atau parameter pembagian data pada operator X-Validation di RapidMiner masih menggunakan *System Random* alih-alih *Local Seed*.

**Checklist kontrol yang sudah diterapkan:**
- [✅] random seed di-set di semua level
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
  Tools     : Python v3.10+, RapidMiner Studio v9.10, VS Code / Jupyter
  Hardware  : Minimal Intel Core i5, RAM 8 GB
  GPU       : Tidak diperlukan

## 2. Installation
> 1. Unduh dan instal Python v3.10 atau versi di atasnya.
  2. Jalankan perintah instalasi library dependency berikut di terminal:
pip install pandas numpy scipy pingouin openpyxl
  3. Install Microsoft Excel v2019 atau lebih baru
  4. Unduh dan instal RapidMiner Studio v9.10 dari situs resmi rapidminer.com.

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
    - Seed penguncian data  : np.random.seed(42)
- Batas signifikansi p   : p < 0.05
- Batas r-tabel valid   : R > 0.183 (Untuk nilai responden N=115)
- Batas reliabilitas    : Alpha >= 0.60
- Skema validasi model  : 10-Fold Cross Validation di RapidMiner


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