# WS-06: System-Experiment Mapping

> **Bab 6 — System Design sebagai Experimental Artifact**

---

## Ringkasan Materi

### Sistem = Instrumen Pengujian, Bukan Produk

Seorang engineer bertanya "apakah sistem bekerja?" — seorang peneliti bertanya "apa yang bisa dibuktikan sistem ini?" Sistem dalam riset adalah **artifact** — objek yang sengaja dibuat untuk menguji klaim spesifik.

### System as Experiment Model

```
RQ → Variable → System Component → Experimental Setup → Output
```

Setiap komponen sistem harus bisa ditelusuri ke variabel riset (top-down), dan setiap pengukuran harus menjawab RQ (bottom-up).

### Mapping Variabel ke Komponen

| Tipe Variabel | Peran di Sistem | Contoh |
|---------------|----------------|--------|
| **IV** (Independent) | Modul yang bisa di-toggle/swap | Algoritma A vs B |
| **DV** (Dependent) | Modul pengukuran | Logger, metrics collector |
| **CV** (Control) | Config yang dikunci | Dataset, parameter tetap |

Jika variabel tidak bisa di-map ke komponen apapun → arsitektur perlu didesain ulang.

### 4 Prinsip Desain Eksperimental

| Prinsip | Pertanyaan Kunci |
|---------|-----------------|
| **Traceability** | Komponen ini melayani variabel yang mana? |
| **Modularity** | Bisakah IV diubah tanpa memengaruhi yang lain? |
| **Controllability** | Apakah CV dieksternalisasi ke config file? |
| **Measurability** | Apakah sistem otomatis menghasilkan data yang dibutuhkan? |

### Variable Isolation melalui Arsitektur

- **Modular architecture** — Pisahkan berdasarkan variabel
- **Configuration-driven** — Ubah config (YAML/JSON), bukan code
- **Feature toggles** — On/off flag untuk ablation study

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan sistem | Memenuhi kebutuhan user | Menguji hipotesis, menghasilkan bukti |
| Arsitektur | Optimasi performa & skalabilitas | Optimasi isolasi variabel & reprodusibilitas |
| Konfigurasi | Sering hardcoded | Dieksternalisasi ke config file |
| Fitur tambahan | Menambah nilai user | Menambah noise jika tidak terkait RQ |

### Istilah Penting

- **Artifact** — Objek yang sengaja dibuat untuk memecahkan masalah atau menguji proposisi
- **Traceability** — Kemampuan menelusuri hubungan RQ → variabel → komponen → output
- **Variable Isolation** — Mengubah hanya satu variabel sambil menahan yang lain konstan
- **Ablation Study** — Menguji kontribusi tiap komponen dengan melepasnya satu per satu
- **Configuration-driven Execution** — Semua parameter di config file, bukan hardcoded

---

## Template A.6 — Mapping RQ ke Arsitektur Sistem

```
SYSTEM-EXPERIMENT MAPPING

Research Question: Bagaimana pengaruh usability fitur live shopping dan 
product reviews terhadap retensi pengguna TikTok Shop 
pada Generasi Z, dan bagaimana pola prediksinya 
menggunakan Naïve Bayes?

Variable → Component Mapping:
| Variabel | Tipe | Komponen Sistem | Cara Manipulasi/Pengukuran |
| Usability fitur | IV | Kuesioner SUS 10 item | Skor SUS (0–100) per fitur |                          |
| Retensi Pengguna | DV |  Modul Prediksi Naïve Bayes | Label biner (Ya/Tidak) |
| Sampel Responden | CV | Filter Data Input | 115 responden Gen Z |

4 Prinsip Desain:
  [x] Traceability — Setiap komponen bisa ditelusuri ke variabel
  [x] Variable Isolation — IV bisa diubah tanpa mengubah CV
  [x] Measurement Integration — Pengukuran DV built-in
  [x] Reproducibility — Setup bisa direkonstruksi

Experimental Setup:
  Input data     : File dataset hasil kuesioner (skor SUS dan label retensi) dari 115 responden Gen Z.
  Parameter      : Pengujian validitas instrumen, Regresi Logistik Biner (uji signifikansi), dan Naïve Bayes dengan skema evaluasi 10-Fold Cross-Validation.
  Output format  : Nilai p-value (uji pengaruh), tabel Confusion Matrix, tingkat Accuracy, Precision, Recall, dan F1-Score (performa prediksi).

---

## Latihan 1 — Variable-to-Component Mapping

Gunakan RQ dan variabel dari WS-05. Petakan ke komponen sistem.

**RQ:** Bagaimana pengaruh usability fitur live shopping dan product reviews terhadap retensi pengguna TikTok Shop pada Generasi Z, dan bagaimana pola prediksinya menggunakan Naïve Bayes?

| Variabel | Tipe | Komponen Sistem | Cara Manipulasi / Pengukuran |
|Usability fitur live shopping| IV | Kuesioner SUS Bagian A (10 item) | Skor 0–100 dihitung dari jawaban Likert 1–5 |
| *Usability fitur product reviews* | *IV* | *Kuesioner SUS Bagian B (10 item)* | *Skor 0–100 dihitung dari jawaban Likert 1–5* |
| Retensi pengguna | DV | Modul label klasifikasi | Output Ya/Tidak berdasarkan 3 indikator perilaku |
| Kondisi sampling | CV | Filter kriteria responden | 115 responden, usia 13–28 tahun, aktif pakai TikTok Shop |

**Apakah semua variabel bisa di-map?** [x] Ya / [ ] Tidak
> Jika tidak, komponen apa yang perlu ditambahkan? _________

---

## Latihan 2 — 4 Prinsip Desain

Evaluasi desain sistem terhadap 4 prinsip.

| Prinsip | Status | Bukti / Penjelasan |
|---------|--------|-------------------|
| Traceability | * ✅ * | Kuesioner SUS Bagian A → langsung menghasilkan skor IV live shopping. Kuesioner SUS Bagian B → langsung menghasilkan skor IV product reviews. Label retensi → langsung jadi DV. Setiap komponen jelas melayani variabel mana. |
| Modularity | ✅ | Skor live shopping dan product reviews diukur di bagian kuesioner yang terpisah, jadi kalau mau ganti salah satu fitur tidak mengganggu yang lain. |
| Controllability | ✅ | Kriteria responden dikunci sejak awal: 115 orang, usia 13–28 tahun, aktif pakai TikTok Shop, pernah pakai kedua fitur. Instrumen SUS yang dipakai juga baku dan tidak berubah. |
| Measurability | ✅ | Kuesioner otomatis menghasilkan skor numerik (0–100) yang langsung bisa dimasukkan ke SPSS untuk regresi logistik dan RapidMiner untuk Naïve Bayes. |

**Prinsip mana yang paling sulit dipenuhi? ** Controllability

**Strategi untuk mengatasinya:**
> Karena data dikumpulkan lewat kuesioner online, peneliti tidak bisa 100% memastikan semua responden benar-benar aktif menggunakan kedua fitur. Mitigasinya adalah dengan menambahkan pertanyaan filter di awal kuesioner — jika responden belum pernah pakai live shopping atau product reviews, otomatis tidak bisa lanjut mengisi

---

## Latihan 3 — Ablation Study Planning

Jika sistem memiliki 3 komponen utama, rencanakan ablation study.

| Kondisi | Komponen A | Komponen B | Komponen C | Hasil yang Diharapkan |
|---------|A (SUS Live Shopping)|B (SUS Product Reviews)|(Naïve Bayes)|----------------------|
| Full | *✅* | *✅* | *✅* | *Performa model paling lengkap — kedua skor SUS masuk sebagai input, Naïve Bayes memprediksi retensi secara optimal* |
| – A | ❌(hanya pakai skor product reviews) | ✅ | ✅ | Akurasi dan F1-score diprediksi turun jika live shopping berkontribusi pada pola retensi |
| – B | ✅ | ❌ ❌ (hanya pakai skor live shopping) | ✅ | Akurasi dan F1-score diprediksi turun jika product reviews berkontribusi pada pola retensi |
| – C | ✅ | ✅ | ❌ (hanya regresi logistik, tanpa Naïve Bayes) | Kehilangan kemampuan prediktif — penelitian hanya bisa menjelaskan hubungan, tidak bisa mengklasifikasikan pola retensi |

**Komponen mana yang diprediksi paling berkontribusi?**  Komponen C (Naïve Bayes)
**Mengapa?**
> Karena tanpa Naïve Bayes, penelitian ini kehilangan seluruh pendekatan prediktifnya dan menjadi penelitian regresi biasa saja. Naïve Bayes adalah yang membedakan penelitian ini dari studi-studi sebelumnya yang hanya pakai regresi. Ini juga yang mengisi gap metodologis yang ditemukan di WS-03.

---

## Refleksi

> Apa risiko jika sistem dibangun seperti produk (monolitik, fitur lengkap) lalu baru dilakukan eksperimen? Mengapa arsitektur modular penting untuk riset?

**Jawaban:**
> Jika sistem dibangun monolitik — misalnya skor live shopping dan product reviews digabung jadi satu nilai rata-rata tanpa dipisah — peneliti tidak bisa tahu fitur mana yang lebih memengaruhi retensi. Semua hasil menjadi blur dan tidak bisa diinterpretasikan per fitur. Arsitektur modular penting karena memungkinkan peneliti membuktikan kontribusi tiap komponen secara terpisah, sehingga klaim dalam penelitian bisa dipertanggungjawabkan secara ilmiah.