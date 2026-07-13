import pandas as pd

def hitung_skor_sus(file_path):
    # 1. Membaca data mentah kuesioner
    df = pd.read_csv(file_path)
    cols = df.columns.tolist()

    # Memisahkan kolom pertanyaan (10 pertanyaan Live Shopping, 10 Product Reviews)
    live_shopping_cols = cols[4:14]
    product_review_cols = cols[14:24]

    def kalkulasi(data, kolom_fitur):
        total_skor = 0
        # SUS: Pertanyaan ganjil (indeks 0,2,4,6,8) dikurang 1
        # SUS: 5 dikurang pertanyaan genap (indeks 1,3,5,7,9)
        for i, col in enumerate(kolom_fitur):
            nilai = pd.to_numeric(data[col], errors='coerce').fillna(3)
            if i % 2 == 0:
                total_skor += (nilai - 1)
            else:
                total_skor += (5 - nilai)
        # Skor total dikali 2.5 untuk skala 0-100
        return (total_skor * 2.5).mean()

    # 2. Hitung rata-rata skor akhir
    skor_live = kalkulasi(df, live_shopping_cols)
    skor_review = kalkulasi(df, product_review_cols)

    # 3. Hitung persentase Continuance Intention
    niat_lanjut = df[cols[24]].value_counts(normalize=True) * 100

    print(f"--- HASIL OLAH DATA KUESIONER ---")
    print(f"Rata-rata Skor SUS Live Shopping: {skor_live:.2f}")
    print(f"Rata-rata Skor SUS Product Reviews: {skor_review:.2f}")
    print(f"Continuance Intention (Ya): {niat_lanjut.get('Ya', 0):.1f}%")

if __name__ == "__main__":
    # Menjalankan fungsi dengan file csv responden
    hitung_skor_sus("data_115_responden_v2.csv")