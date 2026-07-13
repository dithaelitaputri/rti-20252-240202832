# Metadata Eksekusi Pengujian (Raw Test Logs)

Dokumen ini mencatat log mentah, konfigurasi lingkungan, dan timestamp eksekusi pengujian sistem mitigasi JWKS Flooding.

---

## 1. Lingkungan Pengujian (Test Environment)
- **Alat Uji (Load Testing Tool)**: k6 v0.45.0
- **Database Storage**: PostgreSQL v15 (Alokasi Maks: 2 VCPU, 2GB RAM)
- **Caching Layer**: Redis v7.0 Cluster (Alokasi Maks: 1 VCPU, 1GB RAM)
- **Durasi per Run**: 300 Detik (5 Menit)

---

## 2. Matriks Log Eksekusi Kontainer

| Run ID | Timestamp (WIB) | Konfigurasi (`CACHE_MODE`) | Jenis Traffic | Rata-rata CPU Gateway | Rata-rata CPU Redis | Status Utama |
|---|---|---|---|---|---|---|
| RUN-001 | 2026-07-13 09:00 | `none` (Tanpa Cache) | Legitimate (Normal) | 12.5% | 0.2% | Sukses |
| RUN-002 | 2026-07-13 09:15 | `none` (Tanpa Cache) | Attack (Flooding) | 88.2% | 0.1% | **Kelaparan Sumber Daya / DB Down** |
| RUN-003 | 2026-07-13 09:30 | `hybrid` (Pos & Neg) | Attack (Flooding) | 14.1% | 8.5% | Sukses Terfilter |
| RUN-004 | 2026-07-13 09:45 | `hybrid` (Pos & Neg) | Mixed (Campuran) | 18.2% | 6.2% | Sukses Terfilter |

---

## 3. Lokasi Penyimpanan Berkas Mentah (Raw Output Path)

Seluruh output mentah hasil *export* otomatis dari k6 disimpan pada sub-direktori internal:
- JSON Data Mentah: `04-data/raw/k6-metrics-{RUN_ID}.json`
- Resource Monitor Log: `04-data/raw/docker-stats-{RUN_ID}.csv`