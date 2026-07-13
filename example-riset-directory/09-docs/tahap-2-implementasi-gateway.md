# Tahap 2 — Implementasi API Gateway (Go)

**Status:** Selesai
**Acuan arsitektur:** [tahap-1-arsitektur-dan-skema-database.md](tahap-1-arsitektur-dan-skema-database.md)
**Lokasi kode:** [../04-data/](../04-data/)

---

## Tujuan
Melakukan kompilasi, pembersihan, dan standarisasi data mentah kuesioner dari instrumen Google Form (115 responden) ke dalam bentuk penyimpanan data lokal terstruktur (.CSV) agar siap dianalisis dan direplikasi oleh pustaka pengolah statistik.

## Deliverable
- [x] Ekstraksi dataset mentah dari instrumen Google Form ke dalam format baris dan kolom yang bersih.
- [x] Pembersihan data (*data cleaning*) untuk memastikan tidak ada pengisian kuesioner yang menggantung atau terlewat (*missing values*).
- [x] `descriptive_stats_usability.csv` — Berkas tabel data kompilasi jawaban nilai Likert 1–5 untuk 10 pertanyaan standar SUS dari ke-115 responden (terbagi untuk Fitur *Live Shopping* dan *Product Reviews*).
- [x] `continuance_intention_stats.csv` — Berkas tabel data rekapitulasi pilihan biner pilihan loyalitas responden ('Ya' atau 'Tidak') beserta ringkasan alasan kualitatifnya.
- [x] Dokumentasi kamus variabel kuesioner di dalam berkas `README.md` pada folder kode/data untuk acuan replikasi riset lanjutan di Universitas Putra Bangsa.

## Hasil Verifikasi Kesiapan Data

## Hasil Verifikasi End-to-End

Diverifikasi secara mandiri melalui pemeriksaan struktur file menggunakan kakas editor spreadsheet:

- **Validitas Baris Data**: Memastikan total baris data kuesioner yang siap diolah berjumlah tepat **115 responden**.
- **Integritas Isian SUS**: Menguji bahwa seluruh jawaban pertanyaan ganjil (1, 3, 5, 7, 9) dan pertanyaan genap (2, 4, 6, 8, 10) terisi penuh dengan rentang angka 1 sampai 5 (tanpa ada karakter teks ilegal).
- **Rasio Kontingensi Loyalitas**: Memastikan sebaran data *Continuance Intention* terpetakan dengan komposisi **100 data menyatakan 'Ya'**, **14 data menyatakan 'Tidak'**, dan **1 data kosong/missing**.

## Catatan Lingkungan

- Berkas data CSV disimpan dan dienkode menggunakan format **UTF-8** untuk mencegah terjadinya kerusakan karakter (*corrupted characters*) saat file dibaca oleh berbagai platform perangkat lunak analisis data.
- Folder penyimpanan data lokal dikondisikan agar mudah diakses langsung oleh *pipeline execution script* Python atau SPSS tanpa perlu melakukan konfigurasi ulang jalur *path directory* absolut komputer.
