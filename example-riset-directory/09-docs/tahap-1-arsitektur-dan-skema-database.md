# Tahap 1 — Perancangan Arsitektur & Skema Database

**Status:** Selesai

---

## 1. Komponen Sistem

1. **Populasi dan Sampel Target** — Pengguna aktif aplikasi TikTok Shop di kalangan mahasiswa/masyarakat umum yang pernah melakukan transaksi belanja minimal satu kali.
2. **Kuesioner Variabel Usability (System Usability Scale - SUS)**
   - Terdiri dari 10 item instrumen pertanyaan standar global (pertanyaan positif ber-id ganjil, pertanyaan negatif ber-id genap).
   - Skala pengukuran: Skala Likert 5 poin (1 = Sangat Tidak Setuju, 5 = Sangat Setuju).
   - Target pengukuran: Fitur **Live Shopping** dan Fitur **Product Reviews**.
3. **Kuesioner Variabel Continuance Intention (Niat Keberlanjutan)**
   - Menggunakan model pilihan biner eksplisit guna memetakan komitmen responden untuk tetap memilih bertransaksi di TikTok Shop di masa mendatang.

## 2. Alur Resolusi Kunci (Mitigasi)

```
Penyebaran Google Form → Pengumpulan Respons Responden → Filter Validasi Sampel (N=115)
  │
  ├─ Pemisahan Lembar Kerja per Fitur Aplikasi
  │     ├─ Dataset 1: Fitur Live Shopping 
  │     └─ Dataset 2: Fitur Product Reviews
  │
  ├─ Proses Kalkulasi Aturan Skor SUS (Konversi Likert ke Nilai Komposit)
  │     ├─Item Ganjil (Positif) : (Skor Respons - 1)
  │     └─ Item Genap (Negatif)  : (5 - Skor Respons)
  │
  ├─ Agregasi & Total Nilai per Responden
  │     ├─ Rumus: Jumlah Poin Hasil Konversi × 2.5 (Menghasilkan Skala 0–100)
  │     
  │
  └─ Pemetaan Statistik Deskriptif & Distribusi Kualitatif
        ├─ Skor Rata-rata < 68  → Kategori Marginal Low (Grade D / Kelayakan Rendah)
        └─ Persentase Pilihan   → Mengukur Rasio Komitmen Continuance Intention
```

Catatan: Proses evaluasi performa kenyamanan aplikasi ini dirancang secara terpisah per kelompok fitur agar perbandingan nilai kelemahan antarmuka (*usability interface gap*) dapat dipetakan secara berimbang (*apple-to-apple*) demi menjamin keabsahan analisis pada Tahap 3 dan Tahap 4.


## 3. Skema Penyusunan Struktur Data (Variabel Kuesioner)

### Struktur Kolom Responden & Evaluasi SUS (Skala Likert)

```sql
CREATE TABLE responden_sus_evaluations (
    responden_id    SERIAL PRIMARY KEY,
    timestamp       TIMESTAMP NOT NULL,
    fitur_target    VARCHAR(50) NOT NULL, -- 'Live Shopping' atau 'Product Reviews'
    q1_sering_pakai INTEGER CHECK (q1_sering_pakai BETWEEN 1 AND 5),
    q2_rumit        INTEGER CHECK (q2_rumit BETWEEN 1 AND 5),
    q3_mudah_pakai  INTEGER CHECK (q3_mudah_pakai BETWEEN 1 AND 5),
    q4_butuh_teknisi INTEGER CHECK (q4_butuh_teknisi BETWEEN 1 AND 5),
    q5_fungsi_terintegrasi INTEGER CHECK (q5_fungsi_terintegrasi BETWEEN 1 AND 5),
    q6_tidak_konsisten INTEGER CHECK (q6_tidak_konsisten BETWEEN 1 AND 5),
    q7_cepat_paham   INTEGER CHECK (q7_cepat_paham BETWEEN 1 AND 5),
    q8_membingungkan INTEGER CHECK (q8_membingungkan BETWEEN 1 AND 5),
    q9_percaya_diri  INTEGER CHECK (q9_percaya_diri BETWEEN 1 AND 5),
    q10_butuh_belajar INTEGER CHECK (q10_butuh_belajar BETWEEN 1 AND 5)
);
```

-- Representasi logis pemetaan niat keberlanjutan beli konsumen

```sql
CREATE TABLE continuance_intention_records (
    responden_id         INTEGER PRIMARY KEY,
    tetap_menggunakan    VARCHAR(5) NOT NULL, -- 'Ya' atau 'Tidak'
    alasan_utama_bertahan TEXT                 -- Kualitatif pendukung (Diskon/Gratis Ongkir)
);
```


## 4. Matriks Indikator Penilaian Penentuan Klasifikasi SUS

|Komponen Fitur | Batas Jumlah Sampel | Target Pengukuran | Tujuan Utama | 
| Live Shopping | 115 Data Responden |Skala Komposit (0–100) | Mengukur tingkat kenyamanan interaksi transaksi langsung | 
Product Reviews | 115 Data Responden | Skala Komposit (0–100) | Mengukur kejelasan navigasi fitur ulasan produk |

## 5. Keputusan Teknis (Final)

1. Ukuran Sampel Final: Ditentukan sebanyak 115 responden aktif pengguna platform TikTok Shop guna memenuhi keabsahan kaidah pengujian kuantitatif deskriptif.

2. Kakas Pengolah: Menggunakan Spreadsheet (.CSV) dikombinasikan dengan pustaka analisis data untuk menghitung kalkulasi matematis komposit secara otomatis.

3. Metode Validasi: Pengujian reliabilitas instrumen mengacu pada standardisasi rumus komposit System Usability Scale (SUS) yang diakui secara global di bidang ilmu komputer dan interaksi manusia-komputer.

4. Variabel Dependen Utama: Mengisolasi nilai akhir Continuance Intention ke dalam persentase rasio biner guna melihat seberapa kuat dorongan nilai eksternal (ekonomi/diskon) mempengaruhi retensi loyalitas transaksi pengguna.