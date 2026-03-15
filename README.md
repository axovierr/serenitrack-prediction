# 🧠 SereniTrack - Mental Health Tracker

![SereniTrack UI Preview](static/image2.png)

## 📌 Deskripsi Singkat
**SereniTrack** adalah sebuah platform berbasis web yang digunakan untuk membantu mendeteksi risiko depresi pada mahasiswa berdasarkan pola hidup, tekanan akademis, dan faktor-faktor lainnya. Aplikasi ini berjalan dalam environment Python menggunakan web-framework **Flask** dan memanfaatkan dataset serta model *Machine Learning* (`RandomForestClassifier`) yang sudah dilatih (pretrained).

Website ini dibangun oleh mahasiswa **Teknik Informatika 2023 · Rombel 1 · Kelompok 7**:
1. Josephin Nova Bagaskara (2304130002)
2. Luthfa Qubailatun Najwah (2304130015)
3. Nur Khevin (2304130032)

---

## 🚀 Persiapan dan Instalasi (Local Setup)

Langkah-langkah di bawah ini akan memandu Anda untuk menjalankan website ini di perangkat lokal (localhost) Anda dari awal hingga akhir.

### 1. Prerequisites (Syarat Sistem)
Sebelum memulai, pastikan perangkat Anda sudah terinstal:
- **[Git](https://git-scm.com/downloads)** (Untuk meng-clone repository ini)
- **[Python](https://www.python.org/downloads/)** (Minimal versi 3.9+)

### 2. Clone Repository
Buka terminal/Command Prompt/PowerShell Anda, lalu ketikkan perintah berikut untuk menyalin proyek ini ke perangkat Anda:
```bash
git clone https://github.com/axovierr/serenitrack-prediction.git
cd serenitrack-prediction
```

### 3. Setup Virtual Environment (Opsional namun Sangat Disarankan)
Gunakan virtual environment (.venv) agar dependensi proyek ini tidak bentrok dengan *package* Python lain di komputer Anda.

**Untuk Pengguna Windows:**
```bash
python -m venv .venv
.venv\Scripts\activate
```

**Untuk Pengguna macOS / Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```
*(Ciri-ciri virtual environment sudah aktif adalah munculnya tulisan `(.venv)` di awal baris terminal)*

### 4. Instalasi Dependensi Terkait (Requirements)
Aplikasi ini membutuhkan beberapa library seperti `Flask`, dll. Jalankan sintaks ini (pastikan environment aktif jika Anda menggunakannya):

```bash
pip install Flask
# Jika model machine learning digunakan via pickle, Anda mungkin juga butuh scikit-learn & pandas:
pip install scikit-learn pandas
```

### 5. Menjalankan Aplikasi Web
Setelah instalasi selesai, Anda siap untuk menjalankan aplikasi. Ketik:
```bash
python app.py
```
atau (di beberapa sistem GNU/Linux):
```bash
python3 app.py
```

### 6. Akses di Browser
Aplikasi sekarang telah berjalan secara lokal. Buka browser favorit Anda (Chrome/Firefox/Edge) dan masukkan alamat URL ini:

👉 **http://127.0.0.1:5000** atau **http://localhost:5000**

---

## 🛠 Struktur Proyek

- `app.py`: File utama atau *controller* untuk menjalankan server Flask dan *routing* aplikasi.
- `modeldepression.py`: Script untuk logic pembuatan atau interaksi dataset / AI model.
- `rfc_model.pkl`: *Pre-trained Machine Learning Model* yang sudah dikompilasi ke format pickle.
- `templates/`: Folder berisikan tampilan antarmuka (UI) dalam ekstensi `.html` (`index.html`, `result.html`).
- `static/`: Folder berisikan semua elemen penunjang frontend seperti stylesheet CSS (`style.css`, `result.css`) dan aset gambar/icon pendukung.
- `.venv / myenv`: Direktori *environment* Python untuk isolasi environment (biasanya disembunyikan dalam repositori/ `.gitignore`).

---

## 📄 Catatan Tambahan (Disclaimer)
Prediksi yang dihasilkan oleh aplikasi perantara *Machine learning* ini berbasis dari dataset umum. **Hasil tes tidak dan tidak ditujukan sebagai diagnosis medis resmi**. Selalu konsultasikan kepada psikolog, psikiater, atau profesional medis berlisensi untuk diagnosis mental health yang pasti.

***
Dibuat dengan ❤️ oleh Kelompok 7 ~ TI 2023 Rombel 1 | Mental Health Matters!
