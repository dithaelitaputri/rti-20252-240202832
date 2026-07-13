import os
import matplotlib.pyplot as plt

# Data hasil tabulasi silang kuesioner
labels = ['Ya', 'Tidak']
sizes = [87.7, 12.3]  # Persentase dari data bersih responden
colors = ['#4CAF50', '#F44336']  # Warna hijau dan merah kemerahan

# Mengatur ukuran kanvas grafik
plt.figure(figsize=(6, 4))

# Membuat pie chart
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors, 
        wedgeprops={'edgecolor': 'white', 'linewidth': 1})

# Menambahkan judul sesuai format manuskrip
plt.title("Niat Melanjutkan Penggunaan (Continuance Intention)\nTikTok Shop di Masa Depan", fontsize=11)

plt.tight_layout()

# --- PERBAIKAN DI SINI ---
# Mendapatkan direktori folder tempat file skrip ini disimpan
folder_skrip = os.path.dirname(os.path.abspath(__file__))

# Menggabungkan jalur folder skrip dengan nama file gambar tujuan
jalur_simpan = os.path.join(folder_skrip, 'fig_continuance_intention.png')

# Menyimpan grafik langsung ke folder target tanpa error path
plt.savefig(jalur_simpan, dpi=300)
# -------------------------

plt.show()