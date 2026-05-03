# WS-02: Problem Statement

> **Bab 2 — Problem Formulation & System Context**

---

## Ringkasan Materi

### Problem Formation Model

Masalah riset melewati 5 tahap transformasi. Melompat langsung dari Reality ke Variable adalah kesalahan paling umum.

```
Reality → Observed Issue (Symptom) → Diagnosed Problem (Root Cause)
→ Researchable Problem (Scoped) → Measurable Variable (Operationalized)
```

### Topic ≠ Problem ≠ Research Problem

| Level | Contoh | Status |
|-------|--------|--------|
| **Topik** | Keamanan IoT | Terlalu luas, tidak bisa diuji |
| **Problem** | MQTT tidak terenkripsi | Spesifik tapi belum riset |
| **Research Problem** | Belum ada studi membandingkan overhead TLS 1.3 vs DTLS pada MQTT di IoT RAM < 64KB | Bisa dirancang eksperimennya |

### Symptom vs Root Cause

Apa yang diamati (gejala) ≠ mengapa terjadi (akar masalah). Gunakan **5 Whys** atau **Fishbone Diagram** untuk menggali.

Contoh: "User meninggalkan checkout" (symptom) → "Waktu loading > 8 detik karena API call sequential" (root cause).

### System Thinking

Setiap masalah riset TI harus terikat pada komponen sistem: **Input → Process → Output → Outcome → Constraints → Stakeholders**.

### Problem Quality Check

Masalah riset yang layak harus memenuhi 5 kriteria:
- **Clarity** — Satu orang membaca akan paham
- **Measurability** — Ada metrik kuantitatif
- **Relevance** — Penting untuk domain
- **Testability** — Bisa gagal (falsifiable)
- **Impact** — Ada kontribusi jika terjawab

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan | Menyelesaikan masalah (*solve*) | Memahami dan membuktikan (*understand & prove*) |
| Masalah | Bug, error, fitur belum ada | Gap dalam pengetahuan |
| Scope | Selesaikan semua yang perlu | Batasi agar bisa dibuktikan |
| Output | Working system | Evidence, paper, replicable findings |

### Istilah Penting

- **Problem Statement** — Formulasi tertulis: konteks sistem + gap + dampak + justifikasi
- **System Context** — Deskripsi lengkap: input, proses, output, outcome, constraints, stakeholders
- **Problem Drift** — Masalah "bermutasi" dari pendahuluan ke metodologi karena statement awal tidak presisi
- **Solution-First Thinking** — Memulai dari solusi tanpa masalah yang jelas — berbahaya dalam riset
- **Operational Definition** — Definisi variabel yang cukup jelas agar peneliti lain bisa mengukur hal yang sama

---

## Template A.2 — Problem Statement Builder

```
PROBLEM STATEMENT BUILDER

Domain & Konteks
  Domain   : Kecerdasan Buatan (AI) & Pendidikan Teknologi Informasi.
  Konteks  : Penggunaan ChatGPT untuk membantu mahasiswa atau peneliti dalam mengerjakan tugas dan riset.

System Context
  Input       : Pertanyaan atau instruksi (prompt) dari pengguna.
  Process     : ChatGPT mengolah data teks dalam skala besar untuk menjawab pertanyaan.
  Output      : Jawaban atau penjelasan teks yang dihasilkan AI.
  Outcome     : Pengguna mendapatkan informasi atau bantuan koding secara instan.
  Constraints : AI sering tidak memberikan referensi asli dan bisa memberikan informasi salah (halusinasi).
  Stakeholders: Mahasiswa, Dosen, Peneliti, dan Institusi Pendidikan.

Fenomena → Problem
  Fenomena yang diamati             : Banyak mahasiswa menggunakan ChatGPT untuk mengerjakan tugas kuliah.
  Gejala (symptom) yang terukur     : Meningkatnya tugas yang isinya serupa namun tidak punya rujukan rujukan ilmiah.
  Masalah yang didiagnosis          : Kurangnya pemahaman mahasiswa tentang etika akademis dan verifikasi data saat memakai AI.
  Masalah riset (researchable)      : Sejauh mana efektivitas penggunaan alat deteksi AI dan aturan etika dalam menurunkan tingkat plagiarisme tidak sengaja akibat ChatGPT.
  Variabel yang terukur             : Skor plagiarisme (persentase) dan tingkat akurasi rujukan yang digunakan mahasiswa.

Problem Quality Check
  [ ] Clarity — Apakah satu orang membaca akan paham?
  [ ] Measurability — Apakah ada metrik kuantitatif?
  [ ] Relevance — Apakah penting untuk domain?
  [ ] Testability — Apakah bisa gagal?
  [ ] Impact — Apakah ada kontribusi jika terjawab?

Problem Statement (1 paragraf):
Meskipun ChatGPT menawarkan peluang besar dalam meningkatkan efisiensi riset dan pembelajaran koding bagi mahasiswa Teknologi Informasi, penggunaannya tanpa pengawasan etika memicu kekhawatiran serius terhadap integritas akademis. Mahasiswa cenderung menjadi kurang kreatif dan memiliki kemampuan berpikir algoritmik yang rendah jika terlalu bergantung pada jawaban otomatis tanpa verifikasi sumber. Oleh karena itu, diperlukan sebuah kerangka kerja atau pedoman etika yang mampu menyeimbangkan pemanfaatan AI sebagai alat bantu tanpa mengorbankan kualitas intelektual dan kejujuran akademis peneliti muda.
```

---

## Latihan 1 — Dari Topik ke Masalah Riset

Pilih satu topik di bidang TI yang diminati. Transformasikan melalui 5 tahap Problem Formation Model.

**Topik awal:** Etika Penggunaan ChatGPT dalam Pembelajaran Pemrograman.

| Tahap | Hasil |
|-------|-------|
| Reality | *AI kini bisa membuat kode program secara otomatis berdasarkan logika teks.* |
| Observed Issue (Symptom) | *Mahasiswa sering copy-paste tanpa tahu sumber aslinya.* |
| Diagnosed Problem (Root Cause) | ChatGPT tidak didesain untuk memberikan sumber rujukan yang kredibel secara otomatis |
| Researchable Problem | Apakah pemberian edukasi etika akademis khusus AI dapat meningkatkan kebiasaan verifikasi sumber pada mahasiswa? |
| Measurable Variable | Frekuensi pengecekan rujukan (verifikasi) sebelum dan sesudah edukasi |

**Apakah terjebak solution-first thinking?** [ ] Ya / [x] Tidak
> Jika ya, kembali ke tahap mana? ________________________

---

## Latihan 2 — System Context Decomposition

Gambarkan konteks sistem dari masalah riset di Latihan 1.

| Komponen | Deskripsi |
|----------|----------|
| Input | *Logika program dalam bahasa manusia (prompt) dan source code yang bermasalah.* |
| Process | Analisis sintaks dan logika oleh mesin NLP untuk memberikan saran perbaikan. |
| Output | Teks penjelasan dan blok kode program yang sudah di-debug. |
| Outcome | Siswa memahami langkah perbaikan koding dan waktu pengerjaan tugas menjadi lebih cepat. |
| Constraints | AI sering tidak mencantumkan sumber asli dan berisiko memberikan informasi salah. |
| Stakeholders | Mahasiswa, Pengajar (Guru/Dosen), dan institusi pendidikan. |

**Komponen mana yang paling relevan dengan masalah riset?** _______________

---

## Latihan 3 — Problem Quality Check

Evaluasi problem statement yang sudah dibuat menggunakan 5 kriteria.

| Kriteria | Skor (1-5) | Justifikasi |
|----------|-----------|-------------|
| Clarity | *5* | Masalahnya jelas: penggunaan ChatGPT tanpa etika merusak integritas riset dan kreativitas. |
| Measurability | 4 | Bisa diukur melalui skor plagiarisme, frekuensi penggunaan AI, dan hasil tes koding mandiri. |
| Relevance | 5 | Sangat relevan karena AI sedang menjadi tren besar sekaligus tantangan di dunia akademik saat ini. |
| Testability | 4 | Bisa diuji dengan membandingkan kualitas karya ilmiah antara mahasiswa yang diberi edukasi etika vs yang tidak. |
| Impact | 5 | Memberikan kontribusi berupa saran strategi bagi instansi pendidikan untuk menghadapi perkembangan AI secara bijak. |

**Skor total:** 23 / 25

**Problem statement versi final (1 paragraf):**
> Pemanfaatan ChatGPT dalam riset teknologi informasi memberikan peluang efisiensi yang besar melalui kemampuannya memberikan sudut pandang baru dan bantuan debugging program. Namun, ketergantungan yang tinggi tanpa disertai pemahaman etika akademis menimbulkan risiko plagiarisme dan penurunan kemampuan berpikir algoritmik mahasiswa secara signifikan. Riset ini bertujuan untuk merumuskan pedoman etika penggunaan AI yang adaptif guna memitigasi dampak negatif tersebut, sehingga integritas akademik dan kualitas intelektual mahasiswa tetap terjaga di tengah perkembangan teknologi augmented intelligence.

---

## Refleksi

> Bandingkan "masalah" yang biasa ditemui saat coding (bug, error) dengan masalah riset. Apa perbedaan fundamental dalam cara mendefinisikan dan mendekati keduanya?

**Jawaban:**
> Perbedaan fundamentalnya terletak pada tujuan akhir. Saat koding, masalah dianggap selesai ketika bug hilang dan program berjalan (Engineering Focus). Namun dalam riset, masalah tidak selesai hanya dengan "jawaban" dari AI; kita harus membuktikan kebenaran informasi tersebut, mencantumkan sumber yang kredibel, dan memastikan ada pemahaman intelektual yang bertambah (Research Focus) agar terhindar dari plagiarisme. 
