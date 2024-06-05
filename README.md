Soal: Analisis Penjualan Toko Buku
Anda memiliki dataset yang berisi informasi penjualan sebuah toko buku. Dataset tersebut terdiri dari empat kolom:
1.	Tanggal (format: YYYY-MM-DD): Tanggal penjualan buku.
2.	Nama_Buku: Nama buku yang terjual.
3.	Jumlah: Jumlah buku yang terjual.
4.	Pendapatan: Pendapatan dari penjualan buku tersebut.

**Langkah-langkah:**
1.	Persiapan Lingkungan Kerja:
o	Pastikan Python dan library yang dibutuhkan sudah terpasang (pandas, matplotlib, seaborn).
o	Import library yang diperlukan.

python
Copy code
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
2.	Membaca Dataset:
o	Baca dataset dari file CSV.
python
Copy code
data = pd.read_csv('nama_file.csv')
3.	Menampilkan Informasi Dataset:
o	Cek informasi dasar mengenai dataset.
python
Copy code
print(data.info())
print(data.head())
print(data.describe())
4.	Analisis Data:
o	Analisis statistik deskriptif.
o	Melihat distribusi jumlah buku yang terjual dan pendapatannya.
python
Copy code
# Statistik deskriptif
print(data.describe())

# Distribusi jumlah buku yang terjual
plt.figure(figsize=(10, 6))
sns.histplot(data['Jumlah'], bins=20, kde=True)
plt.title('Distribusi Jumlah Buku yang Terjual')
plt.xlabel('Jumlah Buku')
plt.ylabel('Frekuensi')
plt.show()

# Distribusi pendapatan
plt.figure(figsize=(10, 6))
sns.histplot(data['Pendapatan'], bins=20, kde=True)
plt.title('Distribusi Pendapatan')
plt.xlabel('Pendapatan')
plt.ylabel('Frekuensi')
plt.show()
5.	Analisis Trend Penjualan:
o	Melihat trend penjualan dari waktu ke waktu.
python
Copy code
# Mengubah tipe data Tanggal menjadi datetime
data['Tanggal'] = pd.to_datetime(data['Tanggal'])

# Mengurutkan data berdasarkan Tanggal
data = data.sort_values('Tanggal')

# Plot trend penjualan
plt.figure(figsize=(12, 6))
plt.plot(data['Tanggal'], data['Jumlah'], marker='o', linestyle='-')
plt.title('Trend Penjualan Buku')
plt.xlabel('Tanggal')
plt.ylabel('Jumlah Buku Terjual')
plt.grid(True)
plt.show()
6.	Analisis Kategori Buku Terlaris:
o	Mengetahui buku apa yang paling laris terjual.
python
Copy code
# Menghitung total penjualan per buku
penjualan_per_buku = data.groupby('Nama_Buku')['Jumlah'].sum().reset_index()

# Sorting berdasarkan jumlah penjualan
penjualan_per_buku = penjualan_per_buku.sort_values('Jumlah', ascending=False)

# Plot 10 buku terlaris
plt.figure(figsize=(10, 6))
sns.barplot(x='Jumlah', y='Nama_Buku', data=penjualan_per_buku.head(10))
plt.title('Top 10 Buku Terlaris')
plt.xlabel('Jumlah Terjual')
plt.ylabel('Nama Buku')
plt.show()

Hasil dan Interpretasi Gambar
Gambar 1
![Figure_1](https://github.com/YennyClaraManihuruk/Pythonn/assets/166583340/ff36d216-f0ed-4610-845a-1f46be9e2371)
Interpretasi Grafik: Distribusi Jumlah Buku yang Terjual
Grafik yang ditampilkan adalah histogram dengan kurva KDE untuk kolom 'Jumlah Buku yang Terjual'. Berikut adalah interpretasi dari grafik tersebut: 
• Sumbu X (Horizontal): Menunjukkan rentang jumlah buku yang terjual. 
• Sumbu Y (Vertikal): Menunjukkan frekuensi atau jumlah kejadian untuk setiap rentang jumlah buku yang terjual. 
• Histogram (Bar): Menunjukkan berapa banyak data (frekuensi) yang berada dalam rentang jumlah buku tertentu. 
• Kurva KDE (Garis Melengkung): Memberikan gambaran halus dari distribusi jumlah buku yang terjual. Ini membantu kita melihat pola distribusi data tanpa terganggu oleh variasi bar yang mungkin terjadi karena ukuran bin yang dipilih.
Pengamatan dari Grafik:
1.	Rentang jumlah buku yang paling sering terjual adalah sekitar 40 buku dengan frekuensi tertinggi (4).
2.	Terdapat beberapa rentang jumlah buku dengan frekuensi yang lebih rendah, terutama di sekitar 35 dan 45 buku.
3.	Kurva KDE menunjukkan puncak distribusi sekitar 40 buku dan menurun setelah itu, menunjukkan bahwa sebagian besar data jumlah buku yang terjual terkonsentrasi di sekitar 40 buku dan berkurang seiring bertambahnya atau berkurangnya jumlah buku yang terjual.
Ini memberikan gambaran bahwa distribusi jumlah buku yang terjual dalam dataset memiliki puncak di sekitar 40 buku dan cenderung menurun di jumlah yang lebih sedikit atau lebih banyak dari itu.

Gambar 2 
![Figure_2](https://github.com/YennyClaraManihuruk/Pythonn/assets/166583340/6f4bc375-2daf-46f3-80fd-a9d75412cf66)
Interpretasi Grafik: Jumlah Buku Terjual vs Pendapatan
Grafik yang ditampilkan adalah scatter plot yang menunjukkan hubungan antara jumlah buku terjual dan pendapatan. Berikut adalah interpretasi dari grafik tersebut:
•	Sumbu X (Horizontal): Menunjukkan jumlah buku yang terjual.
•	Sumbu Y (Vertikal): Menunjukkan pendapatan yang diperoleh dari penjualan buku.
Pengamatan dari Grafik:
•	Hubungan Linear Positif: Grafik menunjukkan bahwa terdapat hubungan linear positif antara jumlah buku yang terjual dan pendapatan. Semakin banyak buku yang terjual, semakin tinggi pendapatan yang diperoleh.
•	Distribusi Titik Data: Titik-titik data tersebar dengan pola yang hampir membentuk garis lurus, yang mengindikasikan bahwa hubungan antara jumlah buku terjual dan pendapatan adalah konsisten dan proporsional.
Rentang Data:
•	Jumlah Buku Terjual: Rentang jumlah buku yang terjual adalah antara sekitar 25 hingga 60.
•	Pendapatan: Rentang pendapatan berkisar dari sekitar 250,000 hingga 600,000.
Grafik ini memberikan gambaran yang jelas bahwa pendapatan meningkat secara proporsional dengan peningkatan jumlah buku yang terjual. Hubungan yang terlihat linier menunjukkan bahwa setiap tambahan buku yang terjual memberikan kontribusi yang relatif konstan terhadap peningkatan pendapatan.

Gambar 3
![Figure_3](https://github.com/YennyClaraManihuruk/Pythonn/assets/166583340/00e37e4e-d5f3-4052-9168-6528d858e7a1)
Grafik: Total Penjualan per Buku
Grafik yang ditampilkan adalah diagram batang yang menunjukkan total penjualan untuk masing-masing buku. Berikut adalah interpretasi dari grafik tersebut:
• Sumbu X (Horizontal): Menunjukkan nama buku (Buku A, Buku B, Buku C, Buku D).
• Sumbu Y (Vertikal): Menunjukkan total penjualan untuk setiap buku.
• Bar (Batang): Menunjukkan jumlah total penjualan untuk masing-masing buku.
Pengamatan dari Grafik:
•	Buku A memiliki total penjualan tertinggi dengan lebih dari 250 penjualan.
•	Buku B memiliki total penjualan terendah, sekitar 150 penjualan.
•	Buku C memiliki total penjualan sekitar 200.
•	Buku D juga memiliki total penjualan sekitar 200, sedikit lebih tinggi daripada Buku C.
Grafik ini menunjukkan bahwa Buku A adalah yang paling populer di antara keempat buku yang ditampilkan, sementara Buku B memiliki penjualan terendah. Buku C dan Buku D memiliki penjualan yang cukup seimbang.

Gambar 4
![Figure_4](https://github.com/YennyClaraManihuruk/Pythonn/assets/166583340/913594d2-cde9-4778-a9c9-0dd70d3df3b9)
Interpretasi Grafik: Trend Penjualan Buku
Grafik yang ditampilkan adalah plot garis untuk kolom 'Jumlah Buku Terjual' terhadap 'Tanggal'. Berikut adalah interpretasi dari grafik tersebut:
•	Sumbu X (Horizontal): Menunjukkan rentang waktu atau tanggal penjualan buku dari 2024-01-01 hingga 2024-01-19.
•	Sumbu Y (Vertikal): Menunjukkan jumlah buku yang terjual pada setiap tanggal yang ditunjukkan di sumbu X.
•	Plot Garis (Garis Berkelok): Menunjukkan perubahan jumlah buku yang terjual dari hari ke hari dalam rentang waktu yang ditentukan.
•	Titik Data (Marker): Menunjukkan nilai sebenarnya dari jumlah buku yang terjual pada setiap tanggal.
Pengamatan dari Grafik:
•	Fluktuasi Penjualan: Jumlah buku yang terjual mengalami fluktuasi yang signifikan setiap harinya.
•	Penjualan Tertinggi: Penjualan tertinggi terjadi pada tanggal 2024-01-05, 2024-01-09, dan 2024-01-15, dengan jumlah buku yang terjual mencapai sekitar 55-60 buku.
•	Penjualan Terendah: Penjualan terendah terjadi pada tanggal 2024-01-07 dan 2024-01-17, dengan jumlah buku yang terjual sekitar 25 buku.
•	Tren Penjualan: Meskipun terdapat fluktuasi yang tajam, secara umum terlihat adanya beberapa pola kenaikan dan penurunan yang konsisten selama periode waktu tersebut.
Ini memberikan gambaran bahwa penjualan buku selama periode tersebut sangat berfluktuasi dengan beberapa puncak penjualan yang signifikan diikuti oleh penurunan drastis. Analisis lebih lanjut mungkin diperlukan untuk memahami faktor-faktor yang mempengaruhi fluktuasi ini, seperti promosi, musim, atau kejadian khusus.




