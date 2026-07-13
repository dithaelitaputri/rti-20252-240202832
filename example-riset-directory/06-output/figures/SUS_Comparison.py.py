import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# 1. Mengatur gaya tampilan grafik agar bersih dan profesional
sns.set_theme(style="whitegrid")

# 2. Membuat data tiruan yang sesuai dengan sebaran statistik deskriptif deskripsi riset
# Menyesuaikan dengan Mean ~62.72 & ~62.52 serta rentang nilai boxplot pada gambar
data = {
    'Fitur': ['Live Shopping'] * 115 + ['Product Reviews'] * 115,
    'Skor SUS': (
        [45, 55, 57, 58, 60, 62, 63, 65, 68, 69, 70, 82] * 9 + [62, 63, 65, 68, 60, 55, 58]  # Pas 115 data
    ) + (
        [40, 52, 55, 58, 60, 62, 63, 67, 70, 72, 75, 80] * 9 + [62, 63, 67, 70, 58, 55, 52]  # Pas 115 data
    )
}
df = pd.DataFrame(data)

# 3. Mengatur ukuran kanvas grafik
plt.figure(figsize=(8, 5))

# 4. Membuat Box Plot dengan warna palet yang serupa (Set2 / pastel)
palette_colors = {"Live Shopping": "#66c2a5", "Product Reviews": "#fc8d62"}
ax = sns.boxplot(
    x='Fitur', 
    y='Skor SUS', 
    data=df, 
    palette=palette_colors,
    width=0.7,
    linewidth=1.2
)

# 5. Menambahkan garis horizontal putus-putus merah sebagai indikator standar rata-rata SUS (68)
plt.axhline(y=68, color='red', linestyle='--', linewidth=1.5, label='Rata-rata Standar SUS (68)')

# 6. Menyetel label sumbu koordinat dan judul grafik
plt.title("Perbandingan Skor System Usability Scale (SUS)\nLive Shopping vs Product Reviews", fontsize=12, pad=15)
plt.xlabel("Fitur TikTok Shop", fontsize=10, labelpad=8)
plt.ylabel("Skor SUS (0 - 100)", fontsize=10, labelpad=8)

# 7. Menampilkan legenda untuk garis merah
plt.legend(loc='upper right', frameon=True)

plt.tight_layout()

# --- BAGIAN PENGAMAN PATH AGAR TIDAK ERROR ---
folder_skrip = os.path.dirname(os.path.abspath(__file__))
jalur_simpan = os.path.join(folder_skrip, 'fig_sus_comparison.png')

# Menyimpan grafik langsung menjadi file gambar beresolusi tinggi
plt.savefig(jalur_simpan, dpi=300)
# ---------------------------------------------

plt.show()