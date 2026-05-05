# WS-03: Literature Mapping & Gap

> **Bab 3 — Literature Review, Research Gap & Baseline**

---

## Ringkasan Materi

### Literature Review = Positioning, Bukan Ringkasan

Literature review bukan merangkum paper satu per satu. Pendekatan yang benar adalah **concept-centric** — organisasi berdasarkan tema, metode, atau variabel. Tujuan: menemukan **pola, kontradiksi, dan gap**.

### Empat Jenis Research Gap

| Jenis Gap | Deskripsi | Contoh |
|-----------|----------|--------|
| **Performance Gap** | Performa belum memadai | Akurasi deteksi hanya 78% pada kasus tertentu |
| **Method Gap** | Pendekatan belum diterapkan | Belum ada yang pakai transformer untuk task ini |
| **Data Gap** | Dataset terbatas/tidak representatif | Semua studi pakai dataset sintetis |
| **Context Gap** | Belum diuji pada konteks berbeda | Belum ada evaluasi di negara berkembang |

Gap terkuat = kombinasi 2+ jenis.

### Systematic Search Strategy

1. **Database**: IEEE Xplore, ACM DL, Scopus, Google Scholar
2. **Boolean query** yang terdokumentasi eksplisit
3. **Snowballing**: backward (telusuri referensi) + forward (cari yang mengutip)
4. Klaim "belum ada penelitian" harus didukung **bukti pencarian**

### Baseline Selection — 3 Kriteria

| Kriteria | Pertanyaan |
|----------|-----------|
| **Relevan** | Apakah menyelesaikan masalah yang sama? |
| **Representatif** | Apakah mewakili common practice? |
| **State-of-the-Art** | Apakah terbaru/terbaik? |

Membandingkan deep learning 2024 dengan decision tree sederhana tanpa justifikasi = **straw man comparison** (perbandingan tidak jujur).

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan baca literatur | Mencari solusi yang sudah ada | Memahami apa yang belum terjawab |
| Cara membaca paper | Tutorial, how-to | Metode, limitasi, gap |
| Baseline | Framework terpopuler | State-of-the-art yang rigorous |
| Dokumentasi pencarian | Tidak diperlukan | Wajib (reproducible) |

### Istilah Penting

- **Concept-centric** — Organisasi literatur berdasarkan konsep/metode, bukan per penulis
- **Snowballing** — Backward (telusuri referensi) + Forward (cari yang mengutip paper kunci)
- **Research Position** — Pernyataan eksplisit posisi riset terhadap studi sebelumnya
- **Straw man comparison** — Memilih baseline lemah agar metode sendiri terlihat lebih baik

---

## Template A.3 — Literature Mapping & Gap Identification

```
LITERATURE MAPPING

Topik      : Peluang dan Tantangan ChatGPT dalam Riset TI
Database   : Google Scholar, IEEE Xplore, Emerald, Elsevier
Query      : "ChatGPT" AND "academic research" AND "ethics"
Tahun      : 2022 – 2023
Hasil awal : 15 paper → Screening → 5 paper final

Literature Matrix (concept-centric):

| Study | Tahun | Method | Data | Result | Limitation |
| Pinasthika & Indrihapsari | 2023 | Literature Review |Artikel jurnal (IEEE, Elsevier, dll) | Identifikasi peluang (asisten riset) & tantangan (plagiarisme) | Tidak melakukan eksperimen langsung ke mahasiswa | Yilmaz et al. | 2023 | Survey/Interview | Mahasiswa IT di Turki | ChatGPT bantu belajar koding tapi bikin malas berpikir | Subjektivitas tinggi karena berbasis persepsi | Lund & Wang | 2023 | Discussion Paper | Dampak pada perpustakaan & akademisi | AI mengubah cara mencari literatur secara radikal | Belum ada panduan etika yang konkret | Saquib Sohail et al. | 2023 | Taxonomy/Review | Tantangan riset AI | Klasifikasi masalah: halusinasi data & etika | Fokus pada teknis NLP, bukan perilaku pengguna | Mohammadzadeh et al. | 2023 | Policy Analysis |Plagiarisme teknologi tinggi | Pengusulan penggunaan NFT untuk proteksi karya | Implementasi NFT dalam akademik masih sulit | 
 

Pola yang ditemukan:
  Metode dominan     : Kualitatif dan Literature Review.Usability Scale (SUS) untuk evaluasi teknis.
  Dataset umum       : Artikel ilmiah dan hasil wawancara persepsi.
  Limitasi berulang  : ChatGPT sering memberikan informasi tanpa rujukan asli

GAP IDENTIFICATION

Gap 1: [Jenis: context Gap]
  Deskripsi    : Sebagian besar studi dilakukan di tingkat global/luar negeri (seperti Turki atau AS).
  Bukti        : Jurnal utama menyebutkan pedoman etika di Indonesia masih dalam tahap penyusunan oleh Kominfo.
  Signifikansi : Perlu uji coba pada konteks mahasiswa di Indonesia untuk melihat kesiapan budaya akademis lokal.

Gap 2: [Jenis: Method Gap]
  Deskripsi    : Belum banyak riset yang menguji efektivitas tool deteksi AI (seperti ZeroGPT) secara eksperimental dalam menurunkan angka plagiarisme.
  Bukti        : Jurnal utama baru sebatas menyarankan penggunaan tool tersebut sebagai solusi praktis.
  Signifikansi : Validasi alat deteksi sangat penting agar dosen tidak salah tuduh (false positive).

Baseline Selection:
| Larangan total penggunaan AI | Salah satu solusi praktis yang banyak diambil instansi | Mewakili pendekatan konservatif | Mohammadzadeh et al. | 
|Penggunaan detektor AI (ZeroGPT)	| Solusi teknis untuk memitigasi plagiarisme | Umum disarankan dalam literatur terbaru | Pinasthika & Indrihapsari |

```

---

## Latihan 1 — Concept-Centric Literature Table

Gunakan topik riset dari WS-02. Cari minimal 5 paper relevan menggunakan Google Scholar atau database lain.

**Topik riset:** Peluang dan Tantangan Penggunaan ChatGPT dalam Riset TI
**Query pencarian:** "ChatGPT" AND "academic quality" AND "research"
**Database:** Emerald, IEEE Xplore, Frontiers, ACS Publications, dan Elsevier

| # | Study | Tahun | Method | Dataset | Result | Limitasi |
|---|-------|-------|--------|---------|--------|----------|
| 1 | *Pinasthika & Indrihapsari* | *2023* | *Literature Review* | *Artikel jurnal internasional* | *Identifikasi peluang asisten riset & risiko plagiarisme* | *Belum ada uji eksperimen langsung* |
| 2 | Yilmaz et al. | 2023 | Survey | Mahasiswa Departemen Teknologi Komputer | ChatGPT bantu koding, tapi mahasiswa jadi malas & kurang kreatif | Berfokus pada persepsi subjektif mahasiswa |
| 3 | Lund & Wang | 2023 | Discussion | Dampak AI pada perpustakaan | AI secara radikal mengubah cara mencari literatur ilmiah | Belum menyentuh kebijakan etika yang spesifik |
| 4 | Saquib Sohail et al. | 2023 | Taxonomy | Klasifikasi riset AI | Pemetaan tantangan teknis seperti halusinasi data AI | Lebih fokus ke sisi teknis daripada etika pengguna |
| 5 | Zhu et al. | 2023 | Review | Riset Lingkungan & TI | AI membantu menyusun redaksi karya ilmiah dengan cepat | AI sering tidak memberikan rujukan yang jelas/kredibel |

**Pola yang terlihat — Metode dominan:** Tinjauan pustaka (Literature Review) dan survei persepsi pengguna.
**Limitasi yang berulang:** ChatGPT sering menyajikan informasi tanpa rujukan yang jelas dan berisiko menimbulkan halusinasi data

---

## Latihan 2 — Gap Identification

Berdasarkan tabel di Latihan 1, identifikasi gap.

| Jenis Gap | Ditemukan? | Gap Statement |
|-----------|-----------|---------------|
| Performance Gap | [x] Ya / [ ] Tidak | *Akurasi deteksi AI (tool seperti ZeroGPT) masih bervariasi dan belum teruji secara masif untuk mendeteksi berbagai jenis modifikasi teks oleh ChatGPT.* |
| Method Gap | [x] Ya / [ ] Tidak | Belum banyak riset yang menguji efektivitas edukasi etika akademis secara praktis dalam menurunkan angka plagiarisme akibat AI. |
| Data Gap | [ ] Ya / [ ] Tidak | - |
| Context Gap | [x] Ya / [ ] Tidak | Belum banyak studi yang mengeksplorasi tantangan etika ChatGPT secara spesifik pada mahasiswa di lingkungan institusi pendidikan di Indonesia. |

**Gap utama yang dipilih:** Method Gap & Context Gap (Kombinasi antara perlunya edukasi etika dan penerapannya di lingkungan kampus lokal).
**Mengapa gap ini penting (bukan sekadar "belum ada yang meneliti")?**
> Karena pelarangan total terhadap AI dianggap tidak praktis dan menghalangi mahasiswa memperoleh pengetahuan mandiri. Oleh karena itu, membuktikan bahwa "edukasi etika" adalah metode yang lebih efektif daripada "pelarangan" atau sekadar "deteksi" sangat krusial bagi keberlangsungan integritas akademik di masa depan.

---

## Latihan 3 — Baseline Selection

Pilih 2 baseline dari literatur yang sudah dibaca.

| # | Baseline | Mengapa Relevan | Mengapa Representatif | Apakah SOTA? | Sumber |
|---|----------|----------------|----------------------|-------------|--------|
| 1 | *Pelarangan total AI* | *Ini adalah solusi praktis paling awal yang diambil banyak sekolah untuk mencegah plagiarisme.* | *Merupakan kebijakan umum (common practice) bagi instansi yang belum siap beradaptasi.* | *Tidak* | *Mohammadzadeh et al. (2023)* |
| 2 | Deteksi AI (ZeroGPT) | Penggunaan tool teknis untuk memvalidasi apakah sebuah karya adalah buatan manusia atau mesin. | Menjadi standar deteksi teknis saat ini di dunia akademik. | Ya (untuk kategori detection tool) | Pinasthika & Indrihapsari (2023) |

**Apakah pemilihan baseline ini bisa dianggap straw man?** [ ] Ya / [x] Tidak
> Justifikasi: Tidak, karena kedua baseline tersebut benar-benar nyata diterapkan di dunia akademik saat ini dan memiliki kelebihan serta kekurangan masing-masing yang valid untuk dibandingkan.

---

## Refleksi

> Apa perbedaan antara "belum ada yang meneliti ini" (klaim tanpa bukti) dengan research gap yang valid? Bagaimana cara membuktikan bahwa sebuah gap benar-benar ada?

**Jawaban:**
> Perbedaannya terletak pada bukti sistematis. Klaim tanpa bukti hanyalah asumsi, sedangkan research gap yang valid muncul setelah kita melakukan pemetaan literatur (Literature Mapping) dan menemukan titik di mana penelitian sebelumnya berhenti atau memiliki keterbatasan. Cara membuktikannya adalah dengan menunjukkan pola limitasi dari studi-studi terdahulu—misalnya, penelitian A hanya fokus pada teknis, penelitian B hanya di luar negeri—sehingga muncul kebutuhan nyata untuk mengisi celah tersebut (misalnya, penelitian etika di Indonesia).