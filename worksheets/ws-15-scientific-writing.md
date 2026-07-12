# WS-15: Scientific Writing

> **Bab 15 — Penulisan Ilmiah**

---

## Ringkasan Materi

### Scientific Argument Flow

```
Problem → Gap → RQ → Method → Result → Analysis → Conclusion → Contribution
```

Paper ilmiah adalah **satu argumen utuh** dari masalah ke kontribusi. Setiap node harus terhubung logis ke node sebelum dan sesudahnya.

### Struktur IMRAD

| Section | Peran | Pertanyaan Kunci |
|---------|-------|-----------------|
| **Introduction** | Motivasi + frame | Why is this needed? |
| **Method** | Deskripsi (reproducible) | How was it done? |
| **Results** | Laporan objektif | What was found? |
| **Discussion** | Interpretasi + refleksi | What does it mean? |
| **Conclusion** | Ringkasan + kontribusi | So what? |

### Logical Flow — "Red Thread"

Setiap paragraf menjawab satu pertanyaan dan memicu pertanyaan berikutnya. Alur logis ini harus terasa di tiga level:
1. **Antar-kalimat** dalam paragraf
2. **Antar-paragraf** dalam section
3. **Antar-section** dalam paper

### Internal Consistency

Setiap elemen yang dijanjikan di Introduction harus hadir di Discussion/Conclusion.

**Consistency Matrix:**
```
           Intro  Method  Result  Discuss  Conclude
RQ1          ✓      ✓       ✓       ✓        ✓
RQ2          ✓      ✓       ✓       ✗ ←      ✓
Metrik-X     ✗      ✗       ✓ ←     ✗        ✗
```
**Masalah:** RQ2 dibahas di semua bagian kecuali Discussion. Metrik-X muncul di Result tapi tidak diperkenalkan di Method.

### Writing Quality Triad

| Kualitas | Deskripsi | Contoh Buruk → Baik |
|----------|----------|---------------------|
| **Clarity** | Dipahami sekali baca | "Performa meningkat" → "Accuracy meningkat dari 85.3% ke 89.7%" |
| **Precision** | Istilah eksak, tanpa ambiguitas | "signifikan" → "signifikan secara statistik (p=0.003, d=1.2)" |
| **Conciseness** | Setiap kata menambah informasi | Hapus kalimat redundan, filler words |

### Urutan Penulisan yang Disarankan

1. **Method & Results** — paling stabil, tulis pertama
2. **Discussion** — interpretasi berdasarkan hasil
3. **Introduction** — frame sesuai temuan aktual
4. **Abstract & Conclusion** — terakhir

### Target Jumlah Kata

| Section | Target |
|---------|--------|
| Introduction | 500–700 |
| Related Work | 700–1000 |
| Method | 800–1200 |
| Results | 500–800 |
| Discussion | 600–900 |
| Conclusion | 200–400 |

### Jebakan Kognitif

1. "Lebih panjang = lebih lengkap" → conciseness lebih berharga
2. "Introduction harus ditulis pertama" → justru ditulis terakhir
3. "Jargon teknis = lebih ilmiah" → clarity lebih penting
4. "Discussion = ringkasan Results" → Discussion = interpretasi + konteks

---

## Template A.15 — Paper Structure Checklist

```
PAPER STRUCTURE CHECKLIST

Title   : Analisis Eksplanatori Usability Fitur Live Shopping dan Product Reviews Terhadap Retensi Pengguna Gen Z Menggunakan Metode Naïve Bayes
Target  : [x] Jurnal  [ ] Konferensi  [ ] Laporan

Section Check:
  [x] Abstract — masalah, metode, hasil utama, kontribusi (max 250 kata)
  [x] Introduction — konteks → gap → RQ → kontribusi → struktur paper
  [x] Related Work — concept-centric, gap positioning
  [x] Method — reproducible: desain, variabel, metrik, setup, prosedur
  [x] Results — tabel + grafik + observasi (tanpa interpretasi)
  [x] Discussion — interpretasi, perbandingan, implikasi, limitation
  [x] Conclusion — jawaban RQ, kontribusi, future work

Consistency Matrix:
  [x] RQ di Introduction = RQ di Method = RQ di Conclusion
  [x] Variabel di Method = variabel di Results
  [x] Klaim di Discussion didukung data di Results
  [x] Limitasi di Discussion di-address di Conclusion/Future Work

Writing Quality:
  [x] Clarity — mudah dipahami tanpa re-read
  [x] Precision — tidak ada istilah ambigu
  [x] Conciseness — tidak ada kalimat redundan
```

---

## Latihan 1 — Paper Outline

Buat outline paper untuk riset Anda menggunakan struktur IMRAD.

| Section | Konten Utama (2-3 kalimat) | Target Kata |
|---------|---------------------------|------------|
| Abstract | *Retensi pengguna social commerce Gen Z krusial namun pemetaan fiturnya masih parsial. Studi ini mengevaluasi usability fitur Live Shopping dan Product Reviews (N=100) menggunakan standar SUS dan memprediksi dampaknya dengan Naïve Bayes. Ditemukan skor SUS berada pada kategori Marginal OK (~62-63) dan performa akurasi Naïve Bayes mencapai konsistensi mutlak 88.00% akibat class imbalance alami.* | 200-250 |
| Introduction | *Konteks: Fenomena adopsi belanja digital TikTok Shop di kalangan mahasiswa Universitas Putra Bangsa. Gap: Jarang ada penelitian yang menguji pengaruh empiris kegunaan teknis fitur interaktif spesifik langsung terhadap keputusan retensi beli ulang. RQ: Bagaimana pengaruh parsial kegunaan fitur serta bagaimana akurasi Naïve Bayes memprediksi loyalitas konsumen berdasarkan metrik SUS?* | 500-700 |
| Related Work | Sintesis literatur mengenai evolusi social commerce, metodologi System Usability Scale (SUS) menurut Brooke (1996), serta aplikasi pemodelan probabilitas berbasis Teorema Bayes dalam klasifikasi perilaku konsumen. | 700-1000 |
| Method | Desain penelitian survei kuantitatif non-eksperimental. Pengumpulan data menggunakan kuesioner terstruktur wajib isi (100 data tersaring bersih), dilanjutkan kalkulasi konversi skor baku SUS, dan pemodelan klasifikasi lewat RapidMiner dengan validasi 10-Fold Cross-Validation. | 800-1200 |
| Results | Penyajian Tabel Statistik Deskriptif (Skor SUS X1 = 62.48 -+ 8.46$, X2 = 63.18 -+ 8.05). Penyajian matriks performa klasifikasi model Naïve Bayes yang menghasilkan nilai rata-rata akurasi stabil sebesar 88.00% dan Macro F1-Score 0.47 lintas variasi benih acak (seed). | 500-800 |
| Discussion | Interpretasi ketidaksignifikanan regresi logistik (p > 0.05) dan bias performa Naïve Bayes. Pembahasan batasan toleransi antarmuka (usability tolerance) Gen Z di mana faktor kegunaan sistem tergeser oleh kepuasan nilai ekonomi (promo/harga). | 600-900 |
| Conclusion | Menyimpulkan jawaban kedua RQ bahwa kegunaan fitur bukan penentu tunggal retensi beli ulang mahasiswa UPB. Merekomendasikan penyeimbangan dataset (oversampling) dan penambahan variabel kepuasan ekonomi untuk riset lanjutan. | 200-400 |

---

## Latihan 2 — Consistency Matrix

Buat consistency matrix untuk memverifikasi internal consistency paper Anda.

|  | Intro | Method | Result | Discussion | Conclusion |
|--|-------|--------|--------|-----------|-----------|
| *Contoh: RQ1* | *✓* | *✓* | *✓* | *✓* | *✓* |
| *Contoh: Metrik-X* | *✗ ←* | *✗ ←* | *✓* | *✗ ←* | *✗ ←* |
| RQ1 |✓ | ✓|✓ |✓ |✓ |
| RQ2 | ✓|✓ |✓ |✓ |✓ |
| Metrik utama | ✓|✓ |✓ |✓ |✓ |
| Variabel IV |✓ | ✓|✓ | ✓|✓ |
| Variabel DV | ✓|✓ | ✓|✓ | ✓|
| Klaim/kontribusi |✓ |✓ | ✓|✓ |✓ |

**Isi setiap sel:** ✓ (ada & konsisten), ✗ (missing), ~ (ada tapi inkonsisten)

**Inkonsistensi yang ditemukan:**
> Evaluasi model klasifikasi menggunakan algoritma Naïve Bayes menunjukkan tingkat stabilitas performa dengan pencapaian akurasi rata-rata sebesar 88.00% dan Macro F1-Score 0.47. Nilai tersebut konsisten secara mutlak di seluruh variasi pengujian seed acak lewat skema 10-Fold Cross-Validation.

**Tindakan perbaikan:**
> Menulis "tentang" riset sekadar melaporkan kronologi aktivitas atau deskripsi data mentah seperti sebuah buku harian harian lab tanpa arah yang jelas. Sebaliknya, menulis sebagai "argumen" riset adalah menyusun sebuah narasi pembuktian logis yang kokoh; sejak awal pembaca dipandu melihat adanya celah (gap), lalu ditunjukkan bagaimana metodologi kita hadir untuk menutup celah tersebut secara valid demi melahirkan sebuah kontribusi baru.

Mengubah urutan penulisan dengan mendahulukan metodologi (Method) dan hasil (Results) memberikan fondasi fakta empiris yang mutlak dan stabil terlebih dahulu. Ketika fakta angka riil sudah terkunci (seperti angka akurasi 88.00% dan kegagalan signifikansi regresi), pembahasan (Discussion) dapat ditulis secara objektif tanpa spekulasi liar. Alhasil, bagian pendahuluan (Introduction) yang ditulis belakangan dapat dirancang secara presisi (memiliki benang merah yang kuat) guna mengarahkan pembaca langsung menuju kebenaran hasil temuan riil tersebut tanpa ada janji-janji analisis yang meleset.
---

## Latihan 3 — Writing Quality Check

Ambil satu paragraf dari tulisan Anda (atau tulis paragraf baru) dan evaluasi kualitasnya.

**Paragraf asli:**
> (tempel paragraf Anda di sini)

| Kriteria | Evaluasi | Perbaikan |
|----------|---------|-----------|
| Clarity | *Penggunaan frasa "model itu bisa menebak" kurang akademis dan kurang jelas dalam konteks data mining.* | *Menggantinya dengan istilah teknis yang tepat seperti "memprediksi probabilitas kelas target".* |
| Precision | kuesioner SUS yang disebar kemarin" tidak spesifik secara waktu, jumlah data, maupun konteks lokasi ilmiah.  | Menambahkan detail institusi "Universitas Putra Bangsa" serta jumlah data mutlak ($N=100$). |
| Conciseness | Kalimat terlalu bertele-tele dengan kata penghubung redundan seperti "dilakukan dengan memakai" dan "yang mana". | Menyederhanakan struktur kalimat agar langsung berfokus pada subjek, metode, dan objek penelitian. |

**Paragraf setelah perbaikan:**
> Klasifikasi retensi pengguna di kalangan mahasiswa Universitas Putra Bangsa dilakukan menggunakan algoritma Naïve Bayes pada tools RapidMiner. Pemodelan ini bertujuan untuk memprediksi probabilitas loyalitas responden berdasarkan metrik System Usability Scale (SUS) dengan memanfaatkan sampel bersih sebanyak $N=100$ data.

---

## Refleksi

> Apa perbedaan antara menulis "tentang" riset dan menulis sebagai "argumen" riset? Bagaimana urutan penulisan (Method → Discussion → Introduction) mengubah kualitas tulisan?

> Menulis "tentang" riset sekadar melaporkan kronologi aktivitas atau deskripsi data mentah seperti sebuah buku harian lab tanpa arah yang jelas. Sebaliknya, menulis sebagai "argumen" riset adalah menyusun sebuah narasi pembuktian logis yang kokoh; sejak awal pembaca dipandu melihat adanya celah (gap), lalu ditunjukkan bagaimana metodologi kita hadir untuk menutup celah tersebut secara valid demi melahirkan sebuah kontribusi baru.
> Mengubah urutan penulisan dengan mendahulukan metodologi (Method) dan hasil (Results) memberikan fondasi fakta empiris yang mutlak dan stabil terlebih dahulu. Ketika fakta angka riil sudah terkunci (seperti angka akurasi 88.00% dan kegagalan signifikansi regresi), pembahasan (Discussion) dapat ditulis secara objektif tanpa spekulasi liar. Alhasil, bagian pendahuluan (Introduction) yang ditulis belakangan dapat dirancang secara presisi (memiliki benang merah yang kuat) guna mengarahkan pembaca langsung menuju kebenaran hasil temuan riil tersebut tanpa ada janji-janji analisis yang meleset.
