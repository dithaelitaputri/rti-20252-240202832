# WS-16: Presentation & Defense (UAS)

> **Bab 16 — Presentasi & Pertahanan Ilmiah**

---

## Ringkasan Materi

### Scientific Defense Model

```
Research Work → Presentation → Questioning → Defense → Evaluation → Acceptance
```

### Presentasi ≠ Ringkasan Paper

| Paper | Presentasi |
|-------|-----------|
| Dibaca (self-paced) | Didengar (presenter-paced) |
| Detail lengkap | Ide kunci + highlight |
| Tabel numerik detail | Grafik visual + angka kunci |
| Pembaca bisa re-read | Audiens dengar sekali |

**Prinsip:** Presentasi membutuhkan **reformulasi**, bukan kompresi. Medium berbeda = pendekatan berbeda.

### Claim-Evidence-Reasoning (CER)

Setiap jawaban defense harus memiliki:
1. **Claim** — Pernyataan yang dijawab
2. **Evidence** — Data/fakta pendukung
3. **Reasoning** — Logika yang menghubungkan evidence ke claim

**Contoh:**
| Pertanyaan | Bad Answer | Good Answer (CER) |
|-----------|-----------|-------------------|
| "Kenapa hanya 3 dataset?" | "Tiga sudah cukup" | "3 dataset mewakili variasi: small-clean, medium-clean, medium-noisy [E]. Generalisasi perlu validasi lanjut — listed as limitation [R]" |
| "Hasil DS-3 menurun?" | "Itu outlier" | "Ya, karena distribusi heavy-tail melanggar asumsi Gaussian [E]. Ini menunjukkan boundary condition metode [R]" |
| "Effect size?" | "p=0.003, jadi signifikan" | "Cohen's d=1.2 (large effect) [E] — bukan hanya signifikan tapi substansial [R]" |

### Slide Design — One Slide, One Message

**Optimal 9-Slide Plan (15 menit):**

| # | Slide | Waktu | Pesan |
|---|-------|-------|-------|
| 1 | Title + context | 1 min | Apa ini tentang apa |
| 2 | Problem + motivation | 2 min | Mengapa penting |
| 3 | Gap + RQ | 1.5 min | Apa yang belum terjawab |
| 4 | Method overview | 2 min | Bagaimana dijawab (diagram) |
| 5 | Key result — tabel | 2 min | Temuan utama |
| 6 | Key result — grafik | 2 min | Pola visual |
| 7 | Interpretation + failure | 2 min | Apa artinya |
| 8 | Limitation + future | 1.5 min | Batasan & arah |
| 9 | Conclusion + contribution | 1 min | Closing message |

### Anticipatory Defense

Prediksi pertanyaan berdasarkan kategori:

| Kategori | Contoh Pertanyaan |
|---------|------------------|
| Problem | "Mengapa masalah ini penting?" |
| Gap | "Bagaimana dengan studi X yang sudah menjawab ini?" |
| Method | "Mengapa metode ini, bukan Y?" |
| Results | "Bagaimana menjelaskan anomali di DS-3?" |
| Generalization | "Apakah bisa diterapkan di domain lain?" |

### Tiga Prinsip Jawaban

1. **Direct** — Jawab dulu, elaborasi kemudian
2. **Data-based** — Tunjuk evidence spesifik
3. **Honest** — Akui limitasi jika memang ada

### Jebakan Kognitif

1. "Presentasi = semua yang ada di paper" → terlalu padat
2. "Slide cantik = presentasi bagus" → konten > estetika
3. "Tidak bisa jawab = gagal" → "I don't know, but..." menunjukkan kejujuran
4. "Tidak perlu latihan — saya paham riset saya" → latihan = menemukan celah

---

## Template A.16 — Defense Preparation Sheet

```
DEFENSE PREPARATION

Slide Deck Plan:
  Total slides   : 11 Slides (9 konten + 1 title + 1 closing)
  Time per slide : ~1.5 - 2 menit
  Total time     : 15 menit

Slide Outline:
| # | Pesan Utama | Visual | Waktu |
|---|-------------|--------|-------|
| 1 | Judul & Konteks Evaluasi Fitur E-commerce | Judul Slide + Logo Universitas Putra Bangsa | 30s   |
| 2 | Masalah Retensi Gen Z & Ekspektasi UI/UX  | Diagram alur retensi konsumen digital       | 2min  |
| 3 | Celah Riset (Gap) & 2 Rumusan Masalah (RQ)| Tabel matriks posisi orisinalitas riset    | 2min  |
| 4 | Alur Metodologi (Kuesioner SUS & Naïve Bayes) | Flowchart sistem & parameter eksperimen   | 2min  |
| 5 | Temuan Utama Statistik Deskriptif SUS     | Tabel Skor SUS (X1=62.48, X2=63.18)       | 2min  |
| 6 | Hasil Prediksi Model Naïve Bayes (10-Fold) | Bar Chart Stabilitas Akurasi 88.00%       | 2min  |
| 7 | Interpretasi & Failure Analysis Logistik  | Narasi P-value > 0.05 & Class Imbalance   | 2min  |
| 8 | Batasan Penelitian & Agenda Mendatang     | Tabel matriks limitasi validitas          | 1min  |
| 9 | Kesimpulan Akhir & Kontribusi Praktis     | Poin konklusi jawaban RQ & Penutup       | 30s   |


Anticipatory Defense Matrix:
| Kategori | Pertanyaan Potensial | Jawaban (CER) |
|----------|---------------------|---------------|
| Problem  | Mengapa meneliti usability fitur spesifik, bukan platform keseluruhan? | Fitur Live Shopping dan Product Reviews adalah pendorong interaksi utama e-commerce saat ini [C]. Data transaksi menunjukkan mayoritas aktivitas Gen Z terpusat di dua fitur ini [E]. Mengevaluasi secara parsial memberikan rekomendasi perbaikan taktis yang lebih akurat daripada skala global [R]. |
| Gap      | Apa bedanya dengan riset kepuasan e-commerce yang melimpah? | Riset ini mengisi gap pengaruh teknis kegunaan langsung terhadap retensi [C]. Kebanyakan studi terdahulu hanya berfokus pada persepsi kepercayaan atau harga makro [E]. Mengawinkan SUS dan Naïve Bayes memetakan batas loyalitas berdasarkan kenyamanan operasional [R]. |
| Method   | Kenapa memakai Naïve Bayes jika terjadi class imbalance ekstrim? | Naïve Bayes efisien dalam menangani data survei dengan fitur independen berdistribusi normal [C]. Skor akurasi tetap tinggi konsisten di angka 88.00% di seluruh seed pengujian [E]. Pemilihan algoritma ini sengaja ditujukan untuk menguji ketangguhan probabilitas dasar tanpa manipulasi sintetik [R]. |
| Results  | Mengapa hasil regresi logistik menunjukkan p-value tidak signifikan (>0.05)? | Usability sistem bukan variabel penggerak retensi tunggal pada platform sosial [C]. Skor p-value X1=0.899 dan X2=0.644 membuktikan H0 tidak ditolak [E]. Gen Z memiliki toleransi kesalahan tinggi demi mengejar nilai ekonomi promosi dan hiburan belanja [R]. |
| Generalization | Apakah temuan mahasiswa UPB ini bisa berlaku umum untuk seluruh Gen Z nasional? | Skala generalisasi riset ini terbatas pada kelompok mahasiswa lokal [C]. Karakteristik data N=100 didominasi oleh kelas responden loyal homogen [E]. Hasil ini menjadi boundary condition yang dicatat dalam dokumen limitasi validitas eksternal [R]. |

Latihan:
  Latihan 1: [29 juni] — [Latihan mandiri menggunakan stopwatch, catatan: durasi awal 17 menit, slide hasil terlalu terburu-buru.]
  Latihan 2: [6 juli] — [Simulasi bersama partner belajar (Lia), catatan: durasi stabil 14.5 menit, intonasi CER pada slide failure analysis diperkuat.]
  
```

---

## Latihan 1 — Slide Outline

Rencanakan presentasi 15 menit untuk riset Anda.

| # | Pesan Utama | Visual yang Digunakan | Waktu |
|---|-------------|----------------------|-------|
| 1 | *Judul & Konteks Evaluasi Fitur E-commerce* | *Title slide formal dengan NIM 240202832* | *1.0 min* |
| 2 | *Masalah Retensi Gen Z & Ekspektasi UI/UX* | *Infografik tren penurunan pengguna pasca pemblokiran regulasi.* | *2 min* |
| 3 | *Celah Riset (Gap) & 2 Rumusan Masalah (RQ)* | *Peta konsep perbandingan literatur terdahulu.* | *1.5 min* |
| 4 | Alur Metodologi (Kuesioner SUS & Naïve Bayes) | Blok diagram pipeline data mentah hingga model siap uji di RapidMiner.| 2.0min |
| 5 | Temuan Utama Statistik Deskriptif SUS | Tabel ringkasan mean, median, simpangan baku skor baku SUS. | 2.0 min |
| 6 |  Hasil Prediksi Model Naïve Bayes (10-Fold) | Bar chart + error bar performa nilai akurasi lintas variasi benih acak. | 2.0 min |
| 7 | Interpretasi & Failure Analysis Logistik | Tangkapan layar ringkasan koefisien regresi biner dan nilai p-value. | 2.0 min |
| 8 | Batasan Penelitian & Agenda Mendatang | Tabel evaluasi ancaman internal, eksternal, dan statistikal. | 2.0 min |
| 9 | Kesimpulan Akhir & Kontribusi Praktis | Poin resume penutup berupa jawaban tegas atas target penelitian.| 2.0 min |

**Total waktu estimasi:** 15.0 menit

---

## Latihan 2 — Anticipatory Defense

Prediksi 5 pertanyaan yang mungkin diajukan penguji, lalu siapkan jawaban CER.

| # | Kategori | Pertanyaan | Claim | Evidence | Reasoning |
|---|----------|-----------|-------|----------|-----------|
| 1 | *Problem* | *Mengapa fokus pada retensi pengguna Gen Z?* | *Gen Z adalah motor penggerak utama volume transaksi perdagangan sosial saat ini.* | *Data demografi riset menunjukkan 100% sampel aktif bertransaksi rutin.* | *Mempertahankan segmen pasar ini menentukan keberlanjutan bisnis platform jangka panjang.* |
| 2 | *Method* | *Mengapa formula konversi SUS dari Brooke (1996) harus dikali 2.5?* | *Perkalian tersebut memetakan skor mentah likert ke dalam rentang standar persentil.* | *Formula baku: Total Skor x 2.5 menghasilkan rentang nilai 0 - 100.* | *Standardisasi ini mempermudah interpretasi kategori adopsi sistem secara objektif dan universal.* |
| 3 | Results | Mengapa sebaran skor standar deviasi SUS berkisar di angka  8? | Variabilitas penilaian responden terhadap kegunaan fitur relatif seragam. | Nilai sigma Live Shopping = 8.46 dan Product Reviews = 8.05. | Sebaran yang sempit membuktikan tidak adanya jawaban ekstrem dari 100 sampel bersihan. |
| 4 | Failure | Mengapa akurasi Naïve Bayes konstan di 88.00% tanpa fluktuasi? | Terjadi fenomena bias kelas mayoritas organik dalam dataset lapangan. | Distribusi label target bernilai 88 respons "Ya" dan hanya 12 respons "Tidak". |Algoritma memprediksi struktur kelas dominan dengan sempurna sehingga nilai ragamnya nol. |
| 5 | General | Apa rekomendasi konkret bagi manajemen aplikasi dari hasil riset ini? | Pengembang tidak perlu merombak total antarmuka UI/UX fitur saat ini. | Rata-rata skor SUS (~62) terbukti sudah cukup menjaga keputusan retensi beli ulang konsumen. | Anggaran pengembangan sebaiknya dialokasikan pada subsidi voucher belanja atau peningkatan performa live streaming. |

---

## Latihan 3 — Simulasi Q&A

Minta teman/kolega mengajukan 3 pertanyaan tentang riset Anda. Catat pertanyaan dan evaluasi jawaban Anda.

| # | Pertanyaan | Jawaban Saya | Evaluasi |
|---|-----------|-------------|---------|
| *1* | *"Mengapa tidak melakukan teknik oversampling (SMOTE) untuk mengatasi ketimpangan kelas target?"* | *Karena riset ini mengutamakan analisis eksplanatori jujur terhadap kondisi distribusi data alami di lapangan tanpa intervensi sintetik. Hal ini dijelaskan sebagai karakteristik sampel pada Bab 4 halaman 12."* | *[✓] Direct [✓] Data-based [✓] Honest* |
| 2 |Bagaimana cara menjamin bahwa 100 responden ini mengisi kuesioner secara sungguh-sungguh? | Kami menerapkan pertanyaan filter kelayakan (screening questions) di awal formulir serta mengaktifkan fitur required untuk mencegah adanya butir jawaban yang terlewat. |[ ✓] Direct [ ✓] Data-based [✓] Honest |
| 3 | Apakah skor SUS 62.48 sudah cukup membuat aplikasi dikategorikan ramah pengguna? | Belum optimal secara mutlak. Berdasarkan skala penilaian Bangor et al. (2008), nilai tersebut berada pada batas bawah kategori 'Marginal OK'. Masih terdapat ruang perbaikan pada indikator konsistensi navigasi. | [✓] Direct [✓] Data-based [✓] Honest |


**Pertanyaan yang paling sulit dijawab:**
> Mempertahankan argumentasi logis mengapa nilai p-value regresi yang tidak signifikan (>0.05) tetap merupakan temuan ilmiah yang berharga dan valid untuk dipublikasikan.

**Apa yang perlu disiapkan lebih baik:**
> Membawa salinan cetak tabel referensi konversi SUS menurut matriks skala Bangor dan Brooke agar bisa langsung ditunjukkan sebagai evidence visual pendukung saat sesi tanya jawab sidang.

---

## Refleksi

> Dari seluruh proses WS-01 sampai WS-16 — dari paradigma riset hingga presentasi — bagian mana yang paling mengubah cara Anda berpikir tentang riset? Apa satu hal yang akan selalu Anda terapkan di riset berikutnya?

**Insight terbesar:**
> Paradigma terbesar yang berubah adalah pemahaman bahwa riset ilmiah bukan sekadar mencari hasil yang "selalu sukses" atau membuktikan hipotesis "pasti diterima". Riset sejati adalah sebuah argumen logis yang jujur. Temuan failure analysis—seperti tidak signifikannya pengaruh usability akibat dominasi kelas retensi organik—ternyata memiliki nilai kontribusi akademis yang sangat kaya jika dianalisis secara mendalam menggunakan kerangka Claim-Evidence-Reasoning (CER).

**Yang akan selalu diterapkan:**
> Saya akan selalu menerapkan prinsip kejujuran data dan pemakaian tabel limitasi penelitian secara transparan sejak awal. Mengetahui batas kemampuan model atau sampel riset bukan sebuah kelemahan, melainkan wujud integritas ilmiah tertinggi saya sebagai peneliti mahasiswa di Universitas Putra Bangsa.
