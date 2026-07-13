# Proposal Penelitian

---

## Judul Penelitian

Analisis Eksplanatori Usability Fitur Live Shopping dan Product Reviews Terhadap Retensi Pengguna Gen Z Menggunakan Metode Naïve Bayes.

## 1. Latar Belakang

Lanskap belanja digital di Indonesia mengalami pergeseran masif seiring popularitas *social commerce* yang mendominasi aktivitas harian Generasi Z (Gen Z). Platform interaktif seperti TikTok Shop berhasil mengaburkan batas antara hiburan dan transaksi lewat dua fitur krusialnya, yakni *Live Shopping* dan *Product Reviews*. Di lingkungan akademis Universitas Putra Bangsa, kenyamanan operasional atau aspek *usability* dari kedua fitur tersebut diproyeksikan menjadi indikator kuat yang memengaruhi loyalitas digital mahasiswa. Walaupun angka penetrasi pasar platform ini sangat tinggi, hal tersebut tidak secara otomatis menjamin kualitas antarmuka teknisnya bebas dari keluhan. Oleh karena itu, investigasi empiris mengenai performa kegunaan fitur-fitur ini mendesak untuk dilakukan.

Sejauh ini, pemetaan literatur menunjukkan adanya pemisahan (*gap*) yang kentara antara evaluasi kegunaan sistem berbasis *System Usability Scale* (SUS) dengan pemodelan prediktif perilaku konsumen. Mayoritas riset terdahulu cenderung membedah variabel luar seperti perang harga, promo, atau tingkat kepercayaan makro. Penelitian ini dirancang untuk menjembatani celah tersebut dengan menempatkan kenyamanan teknis antarmuka fitur spesifik sebagai basis data prediktor utama loyalitas konsumen melalui implementasi teknik data mining.


## 2. Rumusan Masalah dan Pertanyaan Penelitian

Berdasarkan latar belakang di atas, pertanyaan penelitian utama (Research Question/RQ) yang ingin dijawab adalah:

> **RQ1: ** Bagaimana tingkat *usability* fitur *Live Shopping* dan *Product Reviews* pada platform TikTok Shop berdasarkan sudut pandang Gen Z jika diukur memakai metrik *System Usability Scale* (SUS)? **

**RQ2:** Seberapa tinggi tingkat akurasi algoritma *Naïve Bayes* dalam memprediksi probabilitas Retensi Pengguna Gen Z dengan memanfaatkan nilai *usability* tersebut?

Untuk menjawab pertanyaan tersebut secara kuantitatif, penelitian ini akan menguji hipotesis berikut terkait performa klasifikasi algoritma:

> **H1: Algoritma Naïve Bayes memiliki tingkat akurasi yang tinggi dan stabil (di atas 80%) dalam mengklasifikasikan keputusan retensi konsumen digital.**

## 3. Tujuan dan Kontribusi Penelitian

### Tujuan

1. Mengukur nilai evaluasi *usability* fitur *Live Shopping* dan *Product Reviews* secara objektif menggunakan konversi skor baku SUS.
2. Membangun model klasifikasi data mining berbasis *Naïve Bayes* untuk memprediksi kecenderungan loyalitas konsumen berdasarkan interaksi antarmuka.
3. Melakukan *failure analysis* terhadap performa prediksi model guna mengidentifikasi batas toleransi kesalahan antarmuka (*usability tolerance*) pada target pengguna.


### Kontribusi

Penelitian ini diharapkan dapat memberikan kontribusi berikut:
1. **Kontribusi Praktis:** Memberikan rekomendasi taktis bagi pengembang *social commerce* mengenai prioritas perbaikan komponen antarmuka fitur belanja interaktif.
2. **Kontribusi Akademis:** Memberikan validasi empiris mengenai integrasi metrik evaluasi deskriptif SUS ke dalam algoritma klasifikasi probabilistik untuk memetakan perilaku konsumen digital.

## 4. Tinjauan Pustaka

Penelitian ini didasarkan pada tiga pilar literatur utama. Pertama, studi mengenai karakteristik adopsi teknologi belanja digital oleh Gen Z untuk memahami pola retensi konsumen. Kedua, teori evaluasi kegunaan sistem berbasis *System Usability Scale* (SUS) menurut kerangka Brooke (1996) untuk mengukur kenyamanan antarmuka secara terstandardisasi. Ketiga, penerapan algoritma *Naïve Bayes* sebagai salah satu pengklasifikasi probabilistik terbaik dalam domain data mining untuk mengenali pola data survei.

Posisi penelitian ini adalah sebagai studi eksplanatori yang menguji apakah kualitas kegunaan antarmuka fitur spesifik memegang kendali penuh terhadap retensi beli ulang pengguna ataukah terdapat faktor eksternal lain yang menggeser pengaruh tersebut.

## 5. Metodologi Penelitian

### 5.1. Desain Sistem dan Variabel Penelitian

Penelitian ini menggunakan desain survei non-eksperimental dengan pendekatan kuantitatif eksplanatori. Variabel penelitian diidentifikasi sebagai berikut:

| Variabel | Tipe | Deskripsi | Cara Manipulasi/Pengukuran |
|---|---|---|---|
| **Usability Fitur** | Independent (IV) | Skor kenyamanan teknis fitur *Live Shopping* (X_1) dan *Product Reviews* (X_2). | Dihitung melalui konversi 10 instrumen pertanyaan baku skala SUS. |
| **Retensi Pengguna** | Dependent (DV) | Keputusan loyalitas responden untuk melakukan pembelian ulang (Ya/Tidak). | Diukur langsung dari pertanyaan pilihan biner di akhir kuesioner. |
| **Profil Responden** | Control (CV) | Batasan karakteristik sampel penelitian di lapangan. | Dibatasi pada mahasiswa aktif Universitas Putra Bangsa. |

### 5.2. Prosedur Eksperimen

1. **Fase 1 - Penyebaran Kuesioner:** Menyebarkan kuesioner digital terstruktur berisi instrumen SUS dan pertanyaan retensi, mengumpulkan total 115 respons masuk.
2. **Fase 2 - Data Cleaning & Screening:** Mengeliminasi 15 data responden yang tidak memenuhi syarat durasi belanja 3 bulan terakhir, menghasilkan sampel bersih final sebanyak N=100.
3. **Fase 3 - Kalkulasi Skor SUS:** Mengonversi jawaban skala Likert menggunakan rumus baku Brooke untuk mendapatkan skor akhir berskala 0-100.
4. **Fase 4 - Pemodelan Naïve Bayes:** Mengimpor dataset bersih ke dalam perangkat lunak RapidMiner untuk dilakukan proses klasifikasi perilaku retensi.

### 5.3. Instrumen dan Metrik Pengukuran

Instrumen utama menggunakan kuesioner terstruktur dengan 10 butir pertanyaan SUS yang menggunakan skala Likert 1-5. Skor akhir SUS dihitung menggunakan aturan: butir bernomor ganjil dikurangi 1, dan 5 dikurangi butir bernomor genap, kemudian total skor dikalikan 2.5 untuk menghasilkan nilai adopsi sistem persentil.

### 5.4. Rencana Analisis Data

Data skor SUS akan dianalisis secara deskriptif untuk mengetahui nilai rata-rata (*mean*) dan simpangan baku (*standard deviation*). Model klasifikasi *Naïve Bayes* akan dievaluasi kinerjanya menggunakan skema validasi **10-Fold Cross-Validation** lintas variasi benih acak (*seed*). Metrik performa yang dinilai mencakup skor akurasi global dan *Macro F1-Score* untuk mengantisipasi potensi ketimpangan distribusi kelas target (*class imbalance*).