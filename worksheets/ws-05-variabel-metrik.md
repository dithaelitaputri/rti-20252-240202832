# WS-05: Variabel & Metrik

> **Bab 5 — Metric, Measurement & Data**

---

## Ringkasan Materi

### Measurement Alignment Model

Setiap pengukuran yang valid harus bisa ditelusuri melalui rantai ini tanpa lompatan logis:

```
Problem → Concept → Variable → Metric → Data → Result
```

### Operationalization = Keputusan Desain

Menerjemahkan konsep abstrak menjadi variabel terukur bukan proses mekanis. "Code quality" yang diukur via SonarQube code smells membawa asumsi implisit. Setiap operasionalisasi harus didokumentasikan dan dijustifikasi.

### Empat Tipe Data (NOIR)

| Tipe | Ciri | Contoh | Operasi Valid |
|------|------|--------|---------------|
| **Nominal** | Kategori, tanpa urutan | Jenis algoritma (RF, SVM, CNN) | Modus, chi-square |
| **Ordinal** | Urutan, interval tidak sama | Skala Likert (1-5) | Median, Spearman |
| **Interval** | Jarak bermakna, tanpa nol absolut | Suhu Celsius | Mean, Pearson, t-test |
| **Ratio** | Jarak bermakna + nol absolut | Waktu eksekusi (ms) | Semua operasi |

Tipe data menentukan uji statistik yang valid. Kebanyakan metrik performa TI = ratio; persepsi pengguna = ordinal.

### Kriteria Pemilihan Metrik

- **Representative** — Mewakili konsep yang diteliti
- **Sensitive** — Cukup peka menangkap perbedaan bermakna (hindari ceiling effect)
- **Feasible** — Bisa dikumpulkan dalam batasan waktu dan biaya

### Pre-registration

Metrik harus ditentukan **sebelum** eksperimen. Memilih metrik setelah melihat data = **p-hacking**. Metrik tambahan yang ditemukan kemudian dilaporkan sebagai *exploratory*, bukan *confirmatory*.

### Primary vs Secondary Metric

- **Primary Metric** — Langsung terikat ke hipotesis, menentukan kesimpulan
- **Secondary Metric** — Pendukung, dilaporkan di samping primary; statusnya suplementer

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Pemilihan metrik | Berdasarkan kebiasaan/tool yang ada | Berdasarkan construct validity |
| Anomali | Dihapus untuk laporan bersih | Diinvestigasi — bisa jadi temuan |
| Kapan dipilih | Setelah sistem jadi (monitoring) | Sebelum eksperimen (by design) |

### Istilah Penting

- **Operationalization** — Transformasi konsep abstrak menjadi variabel terukur
- **Construct Validity** — Sejauh mana pengukuran benar-benar mengukur konsep yang dimaksud
- **Measurement Scale** — Klasifikasi data (NOIR) yang menentukan analisis valid
- **Multi-metric Evaluation** — Menggunakan beberapa metrik untuk menangkap konsep kompleks

---

## Template A.5 — Definisi Variabel, Metrik & Justifikasi

```
VARIABLE & METRIC DEFINITION

Research Question: Bagaimana pengaruh usability level fitur (live shopping dan product reviews) terhadap retensi pengguna TikTok Shop pada Generasi Z, dan bagaimana pola prediksinya menggunakan Naïve Bayes?

| Variabel | Tipe | Konsep | Metrik | Skala | Satuan | Cara Mengukur | Justifikasi |
| Usability Fitur | IV | Kualitas pengalaman pengguna pada fitur spesifik. | Skor SUS per fitur. | Ordinal | Skor (0-100). | Kuesioner SUS (10 pertanyaan) | Standar industri untuk mengukur efektivitas dan kepuasan pengguna. |
| Retensi Pengguna | DV | Keputusan untuk menggunakan kembali platform | Status Retensi (Kategorik). | Nominal | - | Pertanyaan biner (Ya/Tidak). | Menentukan perilaku keberlanjutan pengguna secara konkret. | 
| Kondisi Pengambilan Data | CV | Keseragaman konteks penelitian | Jumlah responden tetap (115), instrumen SUS baku, platform tunggal (TikTok Shop) | Nominal | - | Purposive sampling dengan kriteria ketat | Memastikan hasil tidak dipengaruhi perbedaan konteks pengukuran |


Alignment Check:
  RQ → Concept → Variable → Metric → Data → Result
  [x] Setiap langkah terdokumentasi
  [x] Tidak ada "lompatan logis"
  [x] Metrik mengukur apa yang dimaksud (construct validity)
```

---

## Latihan 1 — Operationalization Chain

Gunakan RQ dari WS-04. Definisikan variabel dan metriknya.

**RQ:** Bagaimana pengaruh usability fitur terhadap retensi pengguna TikTok Shop?

| Variabel | Tipe | Konsep Abstrak | Metrik Konkret | Skala (NOIR) | Satuan |
|Usability|IV|Kemudahan penggunaan fitur.|System Usability Scale (SUS).|Ordinal|Skor.|
| Retensi | DV | Loyalitas/Penggunaan ulang. | Label Klasifikasi (Ya/Tidak). | Nominal | - |
| Prediksi | - | Akurasi model. | F1-Score & Accuracy. | Ratio | Persen (%) |

**Apakah ada lompatan logis dalam rantai?** [ ] Ya / [x] Tidak
> Jika ya, di mana?
---

## Latihan 2 — Evaluasi Metrik

Evaluasi metrik DV yang dipilih di Latihan 1 menggunakan 3 kriteria.

| Kriteria | Skor (1-5) | Justifikasi |
|----------|-----------|-------------|
| Representative | 5 | SUS sudah divalidasi secara global untuk mengukur usability perangkat lunak. |
| Sensitive | 4 | Skala 1-5 pada SUS cukup peka untuk menangkap variasi persepsi pengguna. |
| Feasible | 5 | dikumpulkan melalui kuesioner online (Google Forms) |

**Apakah perlu secondary metric?** [x] Ya / [ ] Tidak
> Jika ya, apa dan mengapa? Perlu metrik performa model (Akurasi/F1-Score) karena selain melihat pengaruh (regresi), penelitian ini juga membangun model prediksi (Naïve Bayes).

**Contoh kasus ceiling effect untuk metrik ini:**
> Ceiling effect terjadi jika skor SUS fitur live shopping hampir semuanya menyentuh angka 90-100 (sangat tinggi). Hal ini membuat metrik menjadi tidak sensitif karena kita tidak bisa membedakan mana pengguna yang benar-benar puas dan mana yang sangat puas, sehingga sulit melihat pengaruhnya terhadap retensi karena datanya terlalu homogen di batas atas

---

## Latihan 3 — Data Quality Check

Bayangkan data yang akan dikumpulkan dari eksperimen. Evaluasi 4 dimensi kualitas data.

| Dimensi | Pertanyaan | Jawaban | Strategi Mitigasi |
|---------|-----------|---------|------------------|
| Completeness | *Apakah semua data point terkumpul?* | Ya, 115 responden. | Melakukan cleaning pada data kuesioner yang tidak lengkap. |
| Consistency | *Apakah ada kontradiksi internal?* | Ada kemungkinan responden mengisi asal. | Menggunakan logic check (misal: skor SUS yang semuanya 5 atau semuanya 1 dihapus). |
| Validity | *Apakah benar-benar mengukur yang dimaksud?* | Ya, menggunakan instrumen baku. | Uji validitas dan reliabilitas pada kuesioner sebelum disebar luas. |
| Representativeness | *Apakah sampel mewakili populasi target?* | Ya, khusus Gen Z. | Filter ketat pada awal kuesioner mengenai usia dan pengalaman belanja. |

---

## Refleksi

> Mengapa memilih metrik setelah melihat data dianggap p-hacking? Apa bedanya dengan eksplorasi data yang sah?

**Jawaban:**
> Memilih metrik setelah melihat data dianggap curang karena peneliti cenderung hanya akan memilih metrik yang "terlihat bagus" atau mendukung hipotesis mereka secara signifikan. Ini merusak objektivitas sains. Bedanya dengan eksplorasi data yang sah adalah eksplorasi bertujuan untuk mencari insight baru (temuan awal) yang harus diuji lagi, sedangkan confirmatory research (seperti skripsi/jurnal ini) harus menetapkan metrik di awal untuk membuktikan hipotesis secara adil.