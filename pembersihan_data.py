import pandas as pd

# Membaca dataset
data = pd.read_csv('data_penjualan.csv')

# 1. Memeriksa nilai yang hilang (missing values)
print("Jumlah nilai yang hilang sebelum pembersihan:")
print(data.isnull().sum())

# 2. Memeriksa nilai yang duplikat
print("\nJumlah data duplikat sebelum pembersihan:", data.duplicated().sum())

# 3. Pembersihan nilai yang hilang (jika ada)
# Misalnya, kita akan menghapus baris yang memiliki nilai yang hilang
data.dropna(inplace=True)

# 4. Pembersihan data duplikat
data.drop_duplicates(inplace=True)

# 5. Memastikan perubahan telah dilakukan
print("\nJumlah nilai yang hilang setelah pembersihan:")
print(data.isnull().sum())

print("\nJumlah data duplikat setelah pembersihan:", data.duplicated().sum())

# 6. Menyimpan dataset yang sudah dibersihkan
data.to_csv('data_penjualan_bersih.csv', index=False)
