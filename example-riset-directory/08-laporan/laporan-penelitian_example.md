# Laporan Akhir Hasil Penelitian Mandiri (08-laporan / laporan-penelitian.md)

**Judul Penelitian:** Analisis Usability dan Continuance Intention Fitur Live Shopping dan Product Reviews pada Platform TikTok Shop
**Peneliti Utama:** Ditha Elita Putri (NIM: 240202832)
**Program Studi:** Informatika / Sistem Informasi
**Institusi:** Universitas Putra Bangsa (UPB)
**Status Capaian:** Selesai (Tahap 1 s.d. Tahap 4 Selesai, Tahap 5 Pengolahan Manuskrip)

---

## 1. Ringkasan Eksekutif (Executive Summary)

Penelitian mandiri ini dilakukan untuk mengevaluasi kualitas antarmuka (*usability*) serta tingkat loyalitas konsumen (*continuance intention*) pengguna platform *social commerce* TikTok Shop, dengan fokus khusus pada fitur *Live Shopping* dan *Product Reviews*. Evaluasi empiris ini didasarkan pada data kuesioner yang dikumpulkan dari **115 responden aktif**. Pengolahan data statistik deskriptif dan pengujian performa sistem dihitung menggunakan kerangka kerja *System Usability Scale* (SUS) standar global untuk menentukan tingkat penerimaan sistem oleh pengguna.

**Temuan Utama:**
*   **Kualitas Antarmuka di Bawah Standar (Marginal Low)**: Hasil perhitungan skor SUS menunjukkan bahwa fitur *Live Shopping* memperoleh nilai rata-rata sebesar **62.72** dan fitur *Product Reviews* sebesar **62.52**. Berdasarkan standar penilaian global SUS, kedua skor ini berada di bawah ambang batas ideal (skor 68) dan masuk ke dalam kategori **Grade D (Marginal Low)**.
*   **Retensi Loyalitas Pengguna Sangat Tinggi**: Meskipun aspek antarmuka dinilai cukup rumit atau membingungkan oleh responden, analisis niat keberlanjutan (*Continuance Intention*) menunjukkan anomali positif yang masif, di mana **86.96%** (100 dari 115 responden) berkomitmen untuk tetap menggunakan platform ini di masa mendatang.
*   **Anomali Perilaku Konsumen**: Terjadi korelasi paradoks di mana rendahnya nilai *usability* tidak serta-merta menurunkan minat transaksi. Hal ini dipicu oleh dorongan nilai eksternal ekosistem belanja TikTok Shop yang kuat, seperti potongan harga (diskon), promo gratis ongkir, serta daya tarik interaksi langsung bersama *live host*.

---

## 2. Latar Belakang dan Rumusan Masalah

### 2.1 Latar Belakang Masalah
Pesatnya pertumbuhan *social commerce* menuntut platform seperti TikTok Shop untuk menyajikan fitur belanja yang intuitif. Dua fitur utama yang paling sering berinteraksi langsung dengan keputusan pembelian konsumen adalah *Live Shopping* (interaksi belanja waktu nyata) dan *Product Reviews* (ulasan produk sebagai referensi validitas). Namun, keluhan pengguna terkait kepadatan informasi antarmuka dan penataan menu berpotensi menurunkan kenyamanan belanja. Oleh karena itu, penelitian ini dilakukan untuk mengukur secara objektif apakah kendala visual tersebut berdampak langsung terhadap niat pengguna untuk meninggalkan atau tetap bertahan menggunakan platform ini.

### 2.2 Rumusan Masalah Penelitian
1. Bagaimana tingkat kualitas antarmuka (*usability*) fitur *Live Shopping* dan *Product Reviews* pada TikTok Shop berdasarkan persepsi pengguna menggunakan metode *System Usability Scale* (SUS)?
2. Seberapa besar persentase niat keberlanjutan (*continuance intention*) pengguna dalam memanfaatkan platform TikTok Shop untuk bertransaksi ke depan?
3. Apakah terdapat kesenjangan (*anomali*) antara nilai kepuasan desain antarmuka (*usability*) dengan loyalitas nyata pengguna untuk terus menggunakan platform tersebut?

---

## 3. Pelaksanaan Metodologi per Tahap

Penelitian dilaksanakan secara terstruktur melalui 4 tahapan operasional utama:

*   **Tahap 1 — Pengumpulan Data & Penyebaran Kuesioner:** Menyebarkan instrumen penilaian SUS (10 item pertanyaan standar) dan kuesioner kelayakan loyalitas kepada pengguna aktif TikTok Shop hingga berhasil menjaring 115 sampel data bersih.
*   **Tahap 2 — Manajemen & Penyimpanan Data:** Memasukkan dan merangkum hasil kuesioner ke dalam berkas penyimpanan data terstruktur format CSV (`continuance_intention_stats.csv` dan `descriptive_stats_usability.csv`) di dalam direktori penyimpanan data lokal proyek.
*   **Tahap 3 — Analisis Statistik Deskriptif:** Melakukan perhitungan nilai rata-rata (*Mean*), standar deviasi (*Std Dev*), nilai minimum, median, serta nilai maksimum dari sebaran data untuk memetakan performa masing-masing fitur antarmuka.
*   **Tahap 4 — Visualisasi & Penyusunan Laporan:** Memproduksi visualisasi data pendukung (tabel statistik dan diagram sebaran skor) serta menuangkan hasil temuan angka ke dalam dokumen pelaporan resmi institusi ini.

---

## 4. Analisis Data dan Hasil Penelitian

### 4.1 Ringkasan Evaluasi Usability (Skor SUS)
Berdasarkan pengolahan data terhadap 115 responden, diperoleh metrik sebaran skor SUS sebagai berikut:

| Fitur Aplikasi | Rata-rata (*Mean*) | Standar Deviasi | Nilian Median | Kategori Penerimaan |
|---|---|---|---|---|
| **Live Shopping** | 62.72 | 8.48 | 62.50 | Marginal Low (Grade D) |
| **Product Reviews** | 62.52 | 8.55 | 62.50 | Marginal Low (Grade D) |

*Interpretasi:* Kedua fitur belum mencapai batas kelayakan *Acceptable* (skor >68). Pengguna menganggap tata letak menu masih terlalu padat informasi dan terkadang membingungkan saat digunakan secara konkuen.

### 4.2 Persentase Niat Keberlanjutan (Continuance Intention)
Analisis terhadap keinginan responden untuk terus menggunakan TikTok Shop menunjukkan hasil berikut:

*   **Niat Melanjutkan (Ya):** **86.96%** (100 Responden)
*   **Tidak Melanjutkan (Tidak):** **12.17%** (14 Responden)
*   **Data Tidak Mengisi (Missing):** **0.87%** (1 Responden)

Hasil ini mengonfirmasi adanya fenomena paradoks perilaku konsumen: rendahnya nilai estetika/kemudahan antarmuka aplikasi tidak memengaruhi loyalitas selama nilai fungsionalitas ekonomi (promo/diskon) tetap terpenuhi dengan baik.

---

## 5. Kesimpulan dan Rekomendasi

### 5.1 Kesimpulan Penelitian
Metode *System Usability Scale* (SUS) berhasil membuktikan bahwa sistem antarmuka fitur *Live Shopping* dan *Product Reviews* TikTok Shop saat ini masih memerlukan optimalisasi karena berada pada kategori *Marginal Low (Grade D)*. Namun, faktor efisiensi harga, program gratis ongkir, serta interaktivitas belanja berhasil menutupi kekurangan desain tersebut, sehingga tingkat retensi pengguna mandiri tetap bertahan sangat tinggi di angka 86.96%.

### 5.2 Rekomendasi Pengembangan
Direkomendasikan bagi pihak pengembang platform untuk menyederhanakan hirarki visual pada jendela *Live Shopping* agar pop-up keranjang belanja tidak menutupi tayangan video utama, serta mempermudah filter pengelompokan kata kunci pada kolom *Product Reviews* agar ulasan negatif maupun positif dapat disaring dengan lebih cepat.