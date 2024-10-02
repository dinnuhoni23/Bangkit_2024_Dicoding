# Bangkit_2024_Dicoding
# Bike Usage Analysis Dashboard
Proyek ini bertujuan untuk menyelesaikan course pada Dicoding yaitu, "Belajar Analisis Data dengan Python". Proyek ini telah dianalisis menggunakan dataset yang telah disediakan oleh pihak Dicoding, kemudian di implementasikan pada Streamlit.
Link: https://penyewaan-sepeda-dashboard-dicoding-2024.streamlit.app/

# 1. Struktur File

```plaintext
.
├── dashboard.py
├── data
|   ├── Readme.txt
│   └── df_day_analisis.csv
├── screenshots
│   ├── Screenshots 1.png
│   ├── Screenshots 2.png
│   ├── Screenshots 3.png
│   ├── Screenshots 4.png
│   ├── Screenshots 5.png
│   ├── Screenshots 6.png
│   ├── Screenshots 7.png
│   ├── Screenshots 8.png
│   ├── Screenshots 9.png
│   ├── Screenshots 10.png
│   └── Screenshots 11.png
├── README.md
└── requirements.txt
```
# 2. Langkah-langkah mengerjakan project

## 1. Data Wrangling:
- **Mengumpulkan Data**: Mengumpulkan data dari sumber yang tersedia, termasuk data penyewaan sepeda harian.
- **Menilai Data**: Menilai kualitas data dengan mengecek tipe data, missing values, dan duplikat.
- **Membersihkan Data**: Menghapus duplikat, menangani missing values, dan menghapus kolom yang tidak relevan.

## 2. Exploratory Data Analysis (EDA):
- **Menentukan Pertanyaan Bisnis**: Menyusun pertanyaan bisnis, seperti tren penggunaan sepeda harian dan pengaruh cuaca.
- **Eksplorasi Data**: Menganalisis data untuk menemukan pola, tren, dan wawasan penting.

## 3. Visualisasi Data:
- **Membuat Visualisasi Data**: Membuat grafik-grafik yang menunjukkan penggunaan sepeda berdasarkan musim, cuaca, dan hari kerja vs akhir pekan.

## 4. Dashboard:
- **Mengatur DataFrame**: Menyiapkan DataFrame hasil analisis untuk digunakan di dashboard.
- **Membuat Komponen Filter**: Menambahkan filter untuk memudahkan pengguna mengeksplorasi data.
- **Melengkapi Dashboard**: Mengintegrasikan berbagai visualisasi ke dalam dashboard menggunakan Streamlit.

# 3. Langkah Menjalankan Project

## Notebook.ipynb
1. **Download File Project**: Unduh file .ipynb.
2. **Buka Google Colab**: Buat notebook baru dan unggah file project.
3. **Hubungkan ke Runtime**: Klik "Connect" dan jalankan cell kode satu per satu.

## Dashboard/dashboard.py atau main.py
1. **Download File Project**: Unduh file dashboard.
2. **Install Streamlit**: Jalankan `pip install streamlit`.
   - Buat file `requirements.txt` dan install dengan `pip install -r requirements.txt`.
3. **Persiapkan Dataset**: Simpan file CSV dalam folder yang sama dengan `dashboard.py` atau `main.py`.
4. **Jalankan Dashboard**:
```
.\venv\Scripts\activate
```
- Jika sudah masuk ke virtual environment, jalankan Streamlit dengan perintah:
```
streamlit run main.py
```
- Jika menggunakan `dashboard.py`, ubah perintahnya menjadi:
```
streamlit run dashboard.py
```

# 4. Screenshots
## a. Judul pada Streamlit
![image](https://github.com/user-attachments/assets/05b7cfb6-e44c-4a85-bd2f-b7fcb34e5f55)

## b. Sidebar
![image](https://github.com/user-attachments/assets/b80b4188-f45c-400f-835b-160f0d1bdc7a)

## c. Total Penggunaan Sepeda per Hari
![image](https://github.com/user-attachments/assets/048386c3-923d-46a2-b10e-0d7d1f9b2ff3)

## d. Penggunaan Sepeda Berdasarkan Kondisi Cuaca
![image](https://github.com/user-attachments/assets/34099dd1-1881-4ef4-a1fa-5d681c34b8e6)

## e. Penggunaan Sepeda Hari Kerja vs Akhir Pekan
![image](https://github.com/user-attachments/assets/da5b2177-b165-4687-9033-40d48dbde1c7)

## f. Penggunaan Sepeda Berdasarkan Musim
![image](https://github.com/user-attachments/assets/fc13ffa6-e068-44ab-82d3-56e8c7d76cd5)

## g. Tren Penggunaan Sepeda Berdasarkan Bulan
![image](https://github.com/user-attachments/assets/8c8367a5-6584-4a65-8d82-ac0208cb00c4)

## h. Statistik Penggunaan Sepeda
![image](https://github.com/user-attachments/assets/7aa5c199-d8dc-47d2-99c0-8d7ca4776c2d)

## i. Proporsi Penggunaan Kasual vs Terdaftar
![image](https://github.com/user-attachments/assets/73d12a8b-4279-4c67-b70a-20425a75b1fc)

## j. Penggunaan Sepeda Berdasarkan Tahun
![image](https://github.com/user-attachments/assets/3f2c418a-cbd8-446d-be9a-4ee145cbebe9)

## k. Kesimpulan
![image](https://github.com/user-attachments/assets/1b55c96a-4aa0-431a-85da-8417a9682a3f)









