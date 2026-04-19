# WS-01: Distorsi & Paradigma

> **Bab 1 — Research Mindset in IT**

---

## Ringkasan Materi

### Research Trust Model

Pengetahuan ilmiah tidak muncul langsung dari kenyataan. Ia melewati **6 tahap transformasi** yang masing-masing rawan distorsi:

```
Reality → Data → Processing → Analysis → Inference → Knowledge
```

Etika mencegah distorsi yang disengaja (fabrikasi, cherry-picking). Validitas mendeteksi distorsi yang tidak disengaja (confounding variable, sampling bias).

### Tiga Jenis Validitas

| Jenis | Pertanyaan | Contoh Ancaman |
|-------|-----------|----------------|
| **Internal Validity** | Apakah hubungan kausal benar ada? | Confounding variable |
| **External Validity** | Apakah bisa digeneralisasi? | Dataset terlalu homogen |
| **Construct Validity** | Apakah mengukur hal yang benar? | Metrik tidak sesuai klaim |

### Paradigma Riset

Mata kuliah ini menggunakan pendekatan **Positivist** (fenomena TI bisa diukur objektif melalui eksperimen terkontrol) diperkuat **Design Science Research** (artefak dibuat sebagai instrumen pengujian hipotesis, bukan tujuan akhir).

### Mode Berpikir Peneliti

**Curious** (mempertanyakan fenomena) → **Critical** (mengevaluasi klaim berdasarkan bukti) → **Systematic** (merancang investigasi terstruktur dan reproducible).

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan | Membuat sistem yang bekerja | Menghasilkan pengetahuan yang valid |
| Pertanyaan khas | "Bagaimana membuatnya jalan?" | "Apakah klaim ini benar?" |
| Ukuran sukses | Sistem berfungsi, client puas | Hipotesis terjawab, temuan tervalidasi |
| Kegagalan | Harus dihindari | Harus dilaporkan (negative result = kontribusi) |

### Istilah Penting

- **Research Mindset** — Pola pikir yang menuntut bukti dan mempertanyakan asumsi
- **Research Ethics** — Prinsip perilaku: kejujuran, objektivitas, keterbukaan, akuntabilitas
- **HARKing** — Hypothesizing After Results are Known — merumuskan hipotesis setelah melihat data
- **Falsifiability** — Hipotesis harus bisa dibuktikan salah

---

## Template A.1 — Research Mindset Self-Assessment

```
Nama Peneliti    : ____________________
Tanggal          : ____________________

1. Ketika membaca klaim "metode X 95% akurat":
   - Pertanyaan pertama saya: ____________________
   - Data yang dibutuhkan untuk verifikasi: ____________________

2. Posisi paradigma:
   - Pendekatan: [ ] Positivis  [ ] Interpretivis  [ ] Design Science  [ ] Mixed
   - Alasan: ____________________

3. Identifikasi distorsi:
   - Asumsi tersembunyi: ____________________
   - Sumber bias potensial: ____________________
   - Langkah mitigasi: ____________________

4. Komitmen etika:
   - Data yang tidak akan dimanipulasi: ____________________
   - Batasan yang diakui sejak awal: ____________________
```

---

## Latihan 1 — Identifikasi Distorsi

Pilih satu paper riset di bidang TI yang mengklaim "metode X meningkatkan performa." Telusuri setiap tahap Research Trust Model.

**Paper yang dipilih:**
> Judul: Peluang dan Tantangan Penggunaan ChatGPT dalam Lingkungan Riset Teknologi Informasi: Sebuah Tinjauan
> Penulis (Tahun): Stanislaus Jiwandana Pinasthika & Yuniar Indrihapsari (2023)

> Link jurnal: https://www.researchgate.net/profile/Stanislaus-Pinasthika/publication/375422847_Peluang_dan_Tantangan_Penggunaan_ChatGPT_dalam_Lingkungan_Riset_Teknologi_Informasi_Sebuah_Tinjauan/links/6549f489ce88b87031d13823/Peluang-dan-Tantangan-Penggunaan-ChatGPT-dalam-Lingkungan-Riset-Teknologi-Informasi-Sebuah-Tinjauan.pdf


| Tahap | Apa yang Dilakukan | Potensi Distorsi |
|-------|-------------------|-----------------|
| Reality → Data | *Mengumpulkan artikel dari Emerald, IEEE Xplore, Frontiers, dll.* | *Sampling Bias: Hanya mengambil artikel dari penerbit tertentu.* |
| Data → Processing | *Melakukan tinjauan pustaka terhadap artikel terkait ChatGPT di dunia akademis.*|*Cherry-picking: Memilih hanya artikel yang mendukung argumen tertentu.* |
| Processing → Analysis | *Menganalisis dampak positif dan negatif penggunaan ChatGPT.*| *Confounding Variable: Faktor luar seperti kebijakan institusi yang berbeda-beda.*|
| Analysis → Inference | *Menyimpulkan peluang dan tantangan ChatGPT di bidang TI.* | * Inference bias: Menggeneralisasi dampak ChatGPT tanpa melihat variasi sub-bidang TI. * |
| Inference → Knowledge | *Menghasilkan panduan etika penggunaan AI bagi akademisi.* | *Construct Validity: Metrik "kualitas akademis" mungkin sulit diukur secara objektif.* |

**Distorsi paling besar di tahap:** ________________________

**Dua distorsi spesifik yang teridentifikasi:**
1. ChatGPT menyajikan informasi tanpa rujukan jelas, sehingga asal-usul data menjadi kabur (distorsi validitas).
2. Ketidakseimbangan data pada bidang tertentu yang membuat AI memberikan jawaban yang kurang akurat

---

## Latihan 2 — Analisis Kasus Etika

Skenario: Seorang peneliti menemukan bahwa jika 3 data point outlier dihapus, hasil eksperimennya menjadi signifikan. Dengan outlier, hasilnya tidak signifikan.

| Perspektif | Analisis |
|------------|---------|
| Kejujuran ilmiah | *Peneliti wajib melaporkan semua data, termasuk outlier, karena penghapusan tanpa dasar ilmiah yang kuat termasuk manipulasi data* |
| Transparansi | *Harus mencantumkan rujukan dan metode yang digunakan secara jelas agar dapat divalidasi oleh peneliti lain* |
| Peer review | *Penilai (reviewer) berhak mengetahui adanya data yang tidak konsisten untuk menilai validitas temuan tersebut.* |

**Keputusan akhir dan justifikasi:**
> Melaporkan kedua versi hasil (dengan dan tanpa outlier). Dalam riset, kegagalan atau ketidakkonsistenan data (negative results) adalah sebuah kontribusi pengetahuan yang valid dan harus dilaporkan demi integritas akademik.

---

## Latihan 3 — Posisi Paradigma

**Topik riset:** ________________________________________

| Kriteria | Positivis | Interpretivis | Design Science |
|----------|-----------|---------------|----------------|
| Kesesuaian dengan topik (1–5) | * 3. Digunakan untuk menguji akurasi jawaban AI.* | *4.Pahami persepsi mahasiswa/dosen terhadap AI. * | *5. ChatGPT digunakan sebagai artefak untuk memecahkan masalah koding. * |
| Jenis data yang dikumpulkan | * Metrik akurasi, nilai ujian* | * Hasil wawancara, pandangan subjektif.* | *Performa sistem, efisiensi debugging. * |
| Limitasi paradigma | | | |

**Paradigma yang dipilih:** _____________________________
**Alasan:** 
Karena fokus utama adalah membangun dan mengevaluasi penggunaan ChatGPT sebagai instrumen/artefak praktis untuk membantu tugas-tugas teknis seperti pemrograman dan perencanaan studi.
---

## Refleksi

> Sebelum membaca materi ini, apakah pernah mempertanyakan klaim "95% akurat"? Setelah memahami rantai distorsi, pertanyaan apa yang sekarang akan diajukan saat membaca paper?

**Jawaban:**
> ___________________________________________________
> ___________________________________________________
