# Data Mentah Hasil Pengujian Sistem (Tahap 4)

Dokumen ini berisi catatan mentah hasil simulasi performa sistem Gateway saat menghadapi traffic normal dan serangan flooding.

## 1. Matriks Kombinasi Uji Coba

Berikut adalah hasil rekaman data performa sistem setelah dijalankan menggunakan tools pengujian (k6):

| Run ID | Mode Sistem (`CACHE_MODE`) | Jenis Traffic | Status Database PostgreSQL | Keterangan Hasil |
|---|---|---|---|---|
| **RUN-001** | `none` (Tanpa Cache) | Legitimate (Normal) | Aman (CPU < 15%) | Sistem berjalan lancar karena request normal. |
| **RUN-002** | `none` (Tanpa Cache) | Attack (Flooding) | **Down / Crash (CPU 100%)** | Database jebol karena overload menerima ribuan request palsu. |
| **RUN-003** | `none` (Tanpa Cache) | Mixed (Campuran) | Melambat (CPU > 80%) | Pengguna asli ikut terkena dampak lemot karena sistem sibuk. |
| **RUN-004** | `hybrid` (Dengan Cache) | Legitimate (Normal) | Sangat Aman (CPU < 5%) | Request langsung ditangani Redis, database tidak terbebani. |
| **RUN-005** | `hybrid` (Dengan Cache) | Attack (Flooding) | **Aman (CPU < 10%)** | Serangan berhasil diblokir oleh *Negative Cache* di layer Redis. |
| **RUN-006** | `hybrid` (Dengan Cache) | Mixed (Campuran) | Aman (CPU < 10%) | Pengguna asli tetap lancar, sedangkan penyerang otomatis diblokir. |

## 2. Parameter Beban Pengujian
- **Jumlah Virtual Users (VUs)**: Maksimal 1.000 pengguna virtual serentak.
- **Durasi Tembakan**: 5 menit per skenario pengujian.
- **Tools Monitor**: Docker Stats (untuk mencatat konsumsi CPU dan RAM kontainer).