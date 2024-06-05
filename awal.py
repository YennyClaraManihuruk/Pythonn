import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Membaca dataset
data = pd.read_csv('data_penjualan.csv')

# Mengubah tipe data Tanggal menjadi datetime
data['Tanggal'] = pd.to_datetime(data['Tanggal'])

# 1. Histogram untuk distribusi jumlah buku yang terjual
plt.figure(figsize=(10, 6))
sns.histplot(data['Jumlah'], bins=10, kde=True)
plt.title('Distribusi Jumlah Buku yang Terjual')
plt.xlabel('Jumlah Buku')
plt.ylabel('Frekuensi')
plt.show()

# 2. Scatter plot untuk hubungan antara jumlah buku yang terjual dan pendapatan
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Jumlah', y='Pendapatan', data=data)
plt.title('Scatter Plot: Jumlah Buku Terjual vs Pendapatan')
plt.xlabel('Jumlah Buku Terjual')
plt.ylabel('Pendapatan')
plt.show()

# 3. Grafik batang untuk menampilkan total penjualan per buku
penjualan_per_buku = data.groupby('Nama_Buku')['Jumlah'].sum().reset_index()
plt.figure(figsize=(10, 6))
sns.barplot(x='Nama_Buku', y='Jumlah', data=penjualan_per_buku)
plt.title('Total Penjualan per Buku')
plt.xlabel('Nama Buku')
plt.ylabel('Total Penjualan')
plt.show()

# 4. Grafik garis untuk menampilkan trend penjualan
trend_penjualan = data.groupby('Tanggal')['Jumlah'].sum().reset_index()
plt.figure(figsize=(12, 6))
plt.plot(trend_penjualan['Tanggal'], trend_penjualan['Jumlah'], marker='o', linestyle='-')
plt.title('Trend Penjualan Buku')
plt.xlabel('Tanggal')
plt.ylabel('Jumlah Buku Terjual')
plt.grid(True)
plt.show()
