# WS-11: Data Validation & Integrity

> **Bab 11 — Validasi Data & Integritas**

---

## Ringkasan Materi

### Data Trust Model

```
Raw Data → Data Cleaning → Consistency Check → Validation Process → Trusted Data
```

Data mentah belum bisa dipercaya. Harus melewati pipeline validasi sebelum siap untuk analisis statistik.

### Empat Pilar Data Quality

| Pilar | Deskripsi | Contoh Pelanggaran |
|-------|----------|-------------------|
| **Accuracy** | Nilai dalam range masuk akal | Akurasi = 1.5 (di luar [0,1]) |
| **Consistency** | Format seragam di semua run | Run 1: CSV, Run 2: JSON |
| **Completeness** | Tidak ada data hilang dari plan | 97 dari 100 run tercatat |
| **Validity** | Data sesuai desain eksperimen | Parameter baseline tercampur treatment |

### Proses Validasi Progresif

1. **Format validation** — Tipe file, header, kolom
2. **Range validation** — Nilai dalam batas logis
3. **Consistency validation** — Format seragam antar-run
4. **Logic validation** — Data cocok dengan desain eksperimen

Jika gagal di langkah awal → tidak perlu lanjut.

### Anomaly Detection — 3 Jenis

| Jenis | Deskripsi | Deteksi |
|-------|----------|---------|
| **Statistical outlier** | Nilai di luar distribusi normal | IQR: < Q1-1.5×IQR atau > Q3+1.5×IQR |
| **Contextual anomaly** | Normal absolut, abnormal dalam konteks | Run 1-10: ~91%, Run 11-20: ~88% |
| **Pattern anomaly** | Pola sistematis (bukan random) | Performa menurun berurutan |

**Prinsip:** Detect → Investigate → Document → Decide — **JANGAN langsung hapus.**

### Engineering vs Research Validation

| Aspek | Engineering | Research |
|-------|-----------|---------|
| Tujuan | Data sesuai spesifikasi bisnis | Data layak untuk analisis statistik |
| Missing data | Impute / set default | Investigasi penyebab → dokumentasi |
| Outlier | Bug → fix | Mungkin temuan → investigasi |
| Dokumentasi | Minimal (log error) | Komprehensif (anomali + keputusan) |

### Jebakan Kognitif

1. "Logging otomatis ≠ data benar" → bisa ada bug di logger
2. "Outlier = hapus" → bisa jadi temuan penting
3. "Dataset kecil tidak perlu validasi" → justru lebih rentan
4. "Mean normal = data benar" → [94, 95, 93, **44**, 94] → mean 84% terlihat wajar

---

## Template A.11 — Data Validation Checklist

```
DATA VALIDATION CHECKLIST

Completeness:
  [x] Semua skenario tercakup
  [x] Jumlah run sesuai rencana
  [x] Tidak ada file output hilang
  Missing: 0 dari 5 data points

Format Consistency:
  [x] Semua file format sama (Dataset utama dalam format .csv/.xlsx, output model berupa metrik log standar)
  [x] Header konsisten
  [x] Tipe data konsisten (Skor kuesioner berupa integer skala 1-5, variabel target berupa kategorikal biner)

Range & Logic:
  [x] Nilai dalam range masuk akal
  [x] Tidak ada waktu negatif
  [x] Metrik 0–100%, tidak di luar range
  Anomali ditemukan: Terdeteksi 15 data tidak lolos screening (tidak berbelanja dalam 3 bulan terakhir) dan langsung disisihkan sebelum kalkulasi fitur.

Cross-Validation:
  [x] Run identik → hasil mendekati
  [x] Trend konsisten dengan ekspektasi teori

Keputusan:
  [x] Data siap analisis
  [ ] Perlu cleaning
  [ ] Perlu re-run (skenario: ____)
```

---

## Latihan 1 — Completeness Check

Verifikasi apakah semua data yang direncanakan sudah terkumpul.

| Skenario | Run Direncanakan | Run Tercatat | Missing | Alasan |
|----------|-----------------|-------------|---------|--------|
| *Kausalitas Eksplanatori (Python)* | *1* | *1* | *0* | *—* |
| *Klasifikasi Naïve Bayes (Seed 42)* | *1* | *1* | *0* | *-* |
| *Klasifikasi Naïve Bayes (Seed 123)* | *1* | *1* | *0* | *-* |
| *Klasifikasi Naïve Bayes (Seed 999)* | *1* | *1* | *0* | *-* |
| *Klasifikasi Naïve Bayes ((Seed 2026))* | *1* | *1* | *0* | *-* |


**Total expected:** 5 | **Total actual:** 5 | **Missing:** 0

**Keputusan untuk data missing:**
> Tidak ada data pengujian yang hilang (Zero Missing Data). Semua skrip otomatisasi pengujian model klasifikasi berbasis 10-Fold Cross Validation telah merampungkan komputasinya dan mencatat log metrik secara sempurna.

---

## Latihan 2 — Anomaly Investigation

Periksa data Anda untuk anomali. Gunakan metode IQR atau z-score.

**Dataset akurasi 10-Fold Cross Validation pada model data riil (N=100):**

| Run | Accuracy (%) |
|-----|-------------|
| 1 | *90.00* |
| 2 | *90.00* |
| 3 | *90.00* |
| 4 | *90.00* |
| 5 | *90.00* |
| 6 | *90.00* |
| 7 | *90.00* |
| 8 | *90.00* |
| 9 | *80.00* |
| 10 | *80.00* |

**Deteksi outlier:**
- Q1 = 90.00 | Q3 = 90.00 | 
- IQR = Q3 - Q1 = 90.00 - 90.00 = 0.00
- Batas bawah (Q1 - 1.5×IQR) = 90.00%
- Batas atas (Q3 + 1.5×IQR) =  90.00%
- Outlier terdeteksi: Fold 9 dan Fold 10 (80.00%) karena nilainya berada di bawah ambang batas perhitungan matematika IQR murni.

**Investigasi (untuk setiap outlier):**

| Outlier | Nilai | Kemungkinan Penyebab | Keputusan |
|---------|-------|---------------------|-----------|
| *Fold 9 & 10* | *80.00* | *Penurunan nilai akurasi pada lipatan ke-9 dan ke-10 disebabkan oleh pembagian partisi data kelas minoritas (responden yang memilih 'Tidak' pada Retensi berjumlah 12 data) yang terbagi ke dalam blok fold tersebut, sehingga model mendeteksi adanya variasi karakteristik data asli.* | *Tetap dipertahankan. Penurunan ini bukan disebabkan oleh kesalahan sistem (bug), melainkan dinamika data lapangan yang asli (natural data variance).* |

---

## Latihan 3 — Validation Report

Buat laporan validasi ringkas untuk dataset eksperimen Anda.

**1. Completeness:** 100% data terkumpul
**2. Format:** [x] Konsisten / [ ] Ada inkonsistensi: ____
**3. Range check (anomali):** Terdeteksi penurunan performa lokal pada Fold 9 & 10 (80.00%) akibat sebaran class imbalance alami, namun secara matematis seluruh nilai metrik tetap berada pada rentang batas sah evaluasi (0% - 100%).
**4. Logic check:** [x] Parameter sesuai plan / [ ] Ada ketidaksesuaian: ____

**Kesimpulan:** [x] Data siap analisis / [ ] Perlu tindakan: ____

---

## Refleksi

> Apa perbedaan antara "data yang benar" dan "data yang dipercaya"? Mengapa proses validasi formal diperlukan meskipun data dikumpulkan secara otomatis?

> Data yang benar hanyalah data yang berhasil direkam oleh sistem atau komputer apa adanya (misal, angka sukses keluar di terminal komputer). Sementara data yang dipercaya adalah data yang telah melalui serangkaian pengujian formal untuk membuktikan bahwa struktur internalnya sahih, konsisten, terbebas dari bias tersembunyi, dan logis secara metodologi ilmiah.

> Proses validasi formal tetap mutlak diperlukan sekalipun data dikumpulkan secara otomatis (seperti lewat ekspor otomatis Google Forms). Hal ini karena automasi penulisan log tidak menjamin kebenaran isi; anomali pengisian dari responden yang tidak memenuhi kriteria kelayakan kuesioner tetap berpotensi merusak validitas statistik. Validasi formal memastikan bahwa data tersebut memang layak (trusted) untuk ditarik kesimpulannya dalam sidang skripsi Universitas Putra Bangsa.
