# Jadwal & Log Pelaksanaan Penelitian

Catatan kronologis pelaksanaan tiap tahap (sumber: riwayat commit git & dokumen `09-docs/tahap-N-*.md`). Tanggal mengikuti `git log`.

## Log Pelaksanaan

| Tanggal | Tahap | Aktivitas | Referensi |
|---|---|---|---|
| 2026-06-10 s.d. 2026-06-12  | Tahap 1 & 2 | Perancangan instrumen kuesioner System Usability Scale (SUS) untuk fitur Live Shopping (X_1) dan Product Reviews (X_2); penyusunan kuesioner retensi beli ulang via Google Form. | 09-docs/tahap-1-instrumen.md, 01-proposal/proposal.md |

| 2026-06-12 s.d. 2026-06-25 | Tahap 3 | Penyebaran kuesioner secara digital ke mahasiswa Universitas Putra Bangsa; pengumpulan 115 respons masuk. | 04-data/kuesioner-mentah.csv |

| 2026-07-05 | Tahap 4 | Failure Analysis: Menemukan dan mendokumentasikan fenomena class imbalance (88 Ya vs 12 Tidak) yang menyebabkan akurasi Naïve Bayes stabil konstan di angka 88.00%, serta evaluasi ketidaksignifikanan regresi (p > 0.05). | 04-data/dataset-bersih-100.csv | 06-output/failure-analysis.md, 09-docs/tahap-4-analisis.md |

| 2026-07-08 s.d. 2026-07-10 | Tahap 5 | Penyusunan draf laporan riset akhir di folder 08-laporan/ dan pembuatan naskah publikasi di folder 07-manuskrip/; integrasi matriks literatur (metode SUS dan klasifikasi Bayes). | 07-manuskrip/naskah-jurnal.md, 08-laporan/laporan-penelitian.md |

| 2026-07-12 s.d. 2026-07-12 | Tahap 6 | Penyelesaian pembuatan lembar kerja presentasi dan peta pertahanan sidang akhir (WS-16: Presentation & Defense). | worksheets/ws-16-presentation-defense.md |



## Status Ringkas

- **Tahap 1–4**: Selesai (Dataset final terverifikasi: $N=100$ data bersih dari mahasiswa Universitas Putra Bangsa, pengujian Naïve Bayes via RapidMiner tuntas).
- **Tahap 5**: Selesai (Draf naskah jurnal dan strategi Q&A presentasi UAS telah siap 100%).

## Item Tindak Lanjut (Checklist Sebelum Submission)

- [x] Lengkapi matriks literatur terkait teori System Usability Scale (SUS) dan Teorema Bayes.
- [x]  Review akhir seluruh klaim numerik agar konsisten di semua dokumen (Skor SUS X_1 = 62.48, X_2 = 63.18, Akurasi = 88.00%).
- [ ] Pindahkan konten naskah dari 07-manuskrip/naskah-jurnal.md ke dalam format template jurnal target SINTA.
- [ ] Siapkan file salinan cetak grafik adopsi antarmuka (skala adopsi Bangor et al.) sebagai bukti pendukung visual saat Q&A sidang.
- [ ] Lakukan push akhir seluruh file dari WS-10 sampai WS-16 ke GitHub branch main.


## Korespondensi

*(belum ada — tambahkan catatan korespondensi dengan pembimbing/editor jurnal di sini saat tersedia)*
