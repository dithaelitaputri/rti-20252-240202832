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
Nama Peneliti    : Ditha Elita Putri
Tanggal          : 13 April 2026

1. Ketika membaca klaim "metode X 95% akurat":
   - Pertanyaan pertama saya: Dari mana sumber datanya dan apakah jawabannya benar-benar bisa dipercaya atau cuma karangan AI saja?
   - Data yang dibutuhkan untuk verifikasi: Daftar referensi atau rujukan asli yang digunakan, supaya kita tahu informasinya bukan hasil asal ambil (misalnya melalui tinjauan pustaka atau eksperimen)

2. Posisi paradigma:
   - Pendekatan: [ ] Positivis  [ ] Interpretivis  [] Design Science  [ ] Mixed
   - Alasan: Topik mengenai ChatGPT dalam riset TI pada jurnal ini lebih banyak mengeksplorasi makna, persepsi, serta tantangan etika melalui tinjauan literatur (kualitatif) daripada melakukan uji eksperimen numerik terkontrol (positivis).

3. Identifikasi distorsi:
   - Asumsi tersembunyi:Anggapan kalau ChatGPT itu asisten yang selalu benar, padahal dia cuma merangkum data tanpa tahu itu fakta atau hoax.
   - Sumber bias potensial: Misinformation atau informasi yang berasal dari portal propaganda yang dirangkum oleh AI tanpa rujukan sumber yang jelas.
   - Langkah mitigasi: Harus rajin cek ulang (cross-check) kebenaran informasi dan pakai aplikasi pendeteksi AI seperti ZeroGPT
4. Komitmen etika:
   - Data yang tidak akan dimanipulasi: Sumber rujukan asli dari para ahli dan temuan asli mengenai dampak negatif penggunaan AI (seperti menurunnya kemampuan berpikir algoritmik).
   - Batasan yang diakui sejak awal: Keterbatasan ChatGPT dalam menyediakan rujukan yang kredibel secara langsung dan adanya potensi tindakan plagiarisme jika alat bantu ini tidak digunakan secara bijak
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
| Analysis → Inference | *Menyimpulkan peluang dan tantangan ChatGPT di bidang TI.* | *Inference bias: Menggeneralisasi dampak ChatGPT tanpa melihat variasi sub-bidang TI.* |
| Inference → Knowledge | *Menghasilkan panduan etika penggunaan AI bagi akademisi.* | *Construct Validity: Metrik "kualitas akademis" mungkin sulit diukur secara objektif.* |

**Distorsi paling besar di tahap:** Reality → Data (Karena kualitas tinjauan sangat bergantung pada variasi sumber data awal)

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

**Topik riset:** Peluang dan Tantangan Penggunaan ChatGPT dalam Riset TI


| Kriteria | Positivis | Interpretivis | Design Science |
|----------|-----------|---------------|----------------|
| Kesesuaian dengan topik (1–5) | *2* | *5* | *3* |
| Jenis data yang dikumpulkan | *Statistik jumlah pengguna ChatGPT.* | *Hasil wawancara, pandangan subjektif.* | *Performa sistem, Pengembangan tool deteksi AI (seperti ZeroGPT).* |
| Limitasi paradigma | *Hanya angka, tidak menjelaskan "mengapa" mahasiswa malas.* | *Hasil bisa sangat subjektif tergantung partisipan.* | *Fokus pada alat, bukan pada dampak perilaku manusianya.* |

**Paradigma yang dipilih:** Interpretivis

**Alasan:** 
Karena fokus utama adalah membangun dan mengevaluasi penggunaan ChatGPT sebagai instrumen/artefak praktis untuk membantu tugas-tugas teknis seperti pemrograman dan perencanaan studi.
---

## Refleksi

> Sebelum membaca materi ini, apakah pernah mempertanyakan klaim "95% akurat"? Setelah memahami rantai distorsi, pertanyaan apa yang sekarang akan diajukan saat membaca paper?

**Jawaban:**
> Dulu saya mengira riset hanya soal mencari jawaban yang benar. Sekarang saya paham bahwa proses transformasi data sangat rawan distorsi. Saat membaca paper, saya akan bertanya: "Bagaimana peneliti menjaga etika saat memakai AI?" dan "Apakah sumber referensi yang diberikan AI itu nyata atau hasil halusinasi sistem?"