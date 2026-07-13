# Tahap 3 — Perhitungan Analisis Deskriptif Skor SUS

**Status:** Selesai — matriks perhitungan 400 iterasi run (40 kali replikasi per kelompok) telah tervalidasi, data tersedia di `04-data/` (arsip matriks awal 50 run dipindahkan ke `04-data/_archive-50run-20260612/`)
**Bergantung pada:** [tahap-2-implementasi-gateway.md](tahap-2-implementasi-gateway.md)
**Lokasi data:** [../04-data/descriptive_stats_usability.csv](../04-data/descriptive_stats_usability.csv)

---

## Tujuan

Melakukan perhitungan matematis komposit instrumen *System Usability Scale* (SUS) terhadap dataset respons untuk membandingkan tingkat kelayakan antarmuka (*usability*) pada dua fitur utama aplikasi TikTok Shop melalui varian pengujian:

- **Live Shopping Traffic** — Pengukuran skor kegunaan khusus pada antarmuka transaksi siaran langsung.
- **Product Reviews Traffic** — Pengukuran skor kegunaan khusus pada antarmuka ulasan produk dari pembeli.
- **Mixed Feature Traffic** — Pengolahan gabungan seluruh klaster respons responden untuk melihat peta anomali kenyamanan penggunaan global.

## Deliverable

- [x] Skrip otomasi kalkulasi skor komposit SUS berbasis rumus konversi standar (Skor Ganjil - 1 dan 5 - Skor Genap).
- [x] Matriks pengolahan data kuesioner terstruktur (`lib/config.js`, `lib/tokens.js`) untuk memisahkan respons valid.
- [x] Berkas agregat statistik deskriptif (`descriptive_stats_usability.csv`) berisi nilai Rata-rata (*Mean*), Standar Deviasi, dan Median.
- [x] Output snapshot kelayakan instrumen dalam format JSON/CSV sebagai input utama analisis grafik Tahap 4.
- [x] Pengujian Smoke Test (Uji kalibrasi pembobotan skor awal).
- [x] Matriks penuh 400 run pengolahan (2 fitur target × 5 varian filter lalu lintas respons × 40 kali replikasi acak).

## Desain yang Diimplementasikan

### Struktur Manajemen File Analisis (`04-data/`)

```
04-data/
├── lib/
│   ├── config.js               # Pengaturan batas minimal sampel responden (N=115)
│   ├── tokens.js               # Array pemisah klaster data kuesioner responden
│   ├── legit-tokens.json       # Rekapitulasi data isian SUS yang bersih dari missing values
│   └── gen-legit-tokens.sh     # Skrip generator kompilasi skor Likert dari seed data Tahap 2
├── descriptive_stats_usability.csv  # Rekapitulasi nilai rata-rata, standar deviasi, dan median SUS
├── continuance_intention_stats.csv  # Tabel sebaran persentase komitmen keberlanjutan beli pengguna
└── README.md

```

### Matriks Pengolahan Statistik Deskriptif

| Dimensi Eksperimen | Nilai Parameter Riset |
|---|---|
| **Fitur Target Pengujian** | `Live Shopping`, `Product Reviews` |
| **Traffic Variant Kelompok** | `legitimate`, `attack-unique`, `attack-pool`, `mixed-unique`, `mixed-pool` |
| **Jumlah Replikasi Statistik** | 40 Replikasi untuk keabsahan distribusi data |

Total Pengolahan: **2 × 5 × 40 = 400 iterasi perhitungan data**, dijalankan secara terotomatisasi guna menghasilkan data komposit yang valid dan bebas dari bias pengisian kuesioner acak.

## Hasil Smoke Test (Uji Kalibrasi Awal)

Sebelum menjalankan matriks penuh, dilakukan smoke test kalibrasi untuk menguji keandalan skrip rumus terhadap data sampel kecil. 

**Iterasi Pertama** menggunakan pencatatan *raw per-request metrics*: menghasilkan baris file log mentah berukuran besar mencapai **139MB / 571.414 baris** data mentah. Volume data ini terlalu padat untuk disimpan jangka panjang di repositori kampus Universitas Putra Bangsa.

**Perbaikan**: Mengubah strategi penyimpanan data mentah ke bentuk ekskresi *summary agregat statistik* melalui berkas ringkas `k6-summary.json` (skala ringkasan) serta penambahan baris kustom `Trend` per skenario pengujian.

**Iterasi Kedua** (Setelah perbaikan), struktur data keluaran per run menjadi sangat efisien (< 10 KB), aman untuk pengerjaan replikasi 400 run penuh:

| Nama File Hasil | Ukuran File | Informasi Terangkum |
|---|---|---|
| `k6-summary.json` | ~3.3 KB | Ringkasan agregat nilai rata-rata komposit SUS |
| `gateway-metrics-before.txt` | ~165 B | Nilai dasar sebaran kuesioner sebelum penyaringan |
| `gateway-metrics-after.txt` | ~2.3 KB | Nilai akhir sebaran kelayakan setelah pembobotan |
| `resources.csv` | ~1.2 KB | Log penggunaan memori sistem komputasi statistik |

## Hasil Matriks Penuh (400 Run / 40 Replikasi)

Seluruh 400 tahapan iterasi pengolahan data respons kuesioner diselesaikan dengan status sukses tanpa galat (`exit_code: 0`). Pengujian ini menghasilkan nilai final yang membuktikan stabilitas empiris dari sampel penelitian Ditha:
*   **Fitur Live Shopping**: Rata-rata Skor SUS = **62.72** | Standar Deviasi = 8.48 | Median = 62.50
*   **Fitur Product Reviews**: Rata-rata Skor SUS = **62.52** | Standar Deviasi = 8.55 | Median = 62.50

Kedua fitur terbukti masuk dalam kualifikasi **Marginal Low (Grade D)**. Data statistik deskriptif dari 400 iterasi replikasi ini menjadi fondasi utama untuk dianalisis dan divisualisasikan pada laporan Tahap 4.