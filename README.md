
# 🎯 Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech (HR Analytics)

## 🧠 Business Understanding

Perusahaan Edutech mengalami tantangan dalam mengelola tenaga kerjanya, khususnya terkait tingkat *attrition* (keluar/mundurnya karyawan). Tingginya angka keluar masuk karyawan menyebabkan instabilitas, naiknya biaya rekrutmen, dan menurunnya produktivitas. Oleh karena itu, diperlukan analisis data SDM untuk:

- Memahami pola attrition berdasarkan usia, departemen, gender, dan job satisfaction.
- Mengidentifikasi area yang memerlukan intervensi dari manajemen.
- Menyusun strategi retensi karyawan berbasis data.

---

## ❗ Permasalahan Bisnis

- Tingkat attrition karyawan sebesar **12.18%** tergolong tinggi.
- Departemen **Sales** menjadi kontributor terbesar attrition (**59.78%**).
- Attrition tertinggi terjadi pada kelompok usia **25–34 tahun**, yang merupakan usia produktif.
- Banyak karyawan dengan tingkat **kepuasan kerja rendah** (Level 1 dan 2).
- Bidang pendidikan tertentu seperti **Life Sciences** paling banyak ditinggalkan.

---

## 📦 Cakupan Proyek

- Melakukan eksplorasi dan analisis data HR.
- Membuat dashboard visual interaktif menggunakan **Tableau**.
- Mengidentifikasi faktor penyebab attrition.
- Menyusun rekomendasi berbasis data.
- Membangun **model prediksi** dengan `predict.py`.
- Menyusun laporan dalam format **notebook (.ipynb)** dan presentasi video.

---

## 📂 Persiapan

**Sumber Data**: Dataset HR Analytics sebanyak 1.470 data karyawan.
**File data**: https://drive.google.com/file/d/1F2zUvz-kJdLG5Vd1dUWafSJaXATlCYTC/view?usp=sharing

- File Tableau: `HR ANALYTIC DASHBOARD.twbx`
- Notebook Analisis: `notebook (5).ipynb`
- Script Prediksi: `predict.py`

**Format**: CSV, Tableau Workbook (.twbx), Notebook (.ipynb)


---

## ✅ Setup Environment

- Python 3.10+
- Library Python:
  - `pandas`
  - `numpy`
  - `matplotlib`
  - `seaborn`
  - `scikit-learn`
- Tableau Public (untuk dashboard)

**Membuat dan Mengaktifkan Virtual Environment (venv)**
bash 
python -m venv venv

bash 
source venv/bin/activate

**install dependency**
pip install -r requirements.txt 

pip > freeze requirements.txt 

**cara menjalankan prediction.py**

!python prediction.py

---

## 📊 Business Dashboard

**Fitur Dashboard:**

- Total karyawan, jumlah attrition, active employee, dan rata-rata umur.
- Attrition berdasarkan gender, departemen, usia, dan bidang pendidikan.
- Peringkat job satisfaction per role.
- Distribusi umur dan attrition berdasarkan kelompok usia.

> Link Dashboard (jika tersedia online): *[https://public.tableau.com/app/profile/hadi.baskoro/viz/HRANALYTICDASHBOARD_17493579788710/HRANALYTICSDASHBOARD]*

---

## ✅ Conclusion

- Tingkat attrition terbesar berasal dari karyawan usia **25–34 tahun**, kelompok usia produktif.
- **Sales** menjadi divisi dengan attrition tertinggi (~60%) → perlu evaluasi leadership, beban kerja, atau kompensasi.
- **Life Sciences** dan **Medical** adalah bidang pendidikan dengan angka attrition tinggi → perlu evaluasi proses rekrutmen atau jalur karier.
- Job satisfaction rendah pada beberapa peran seperti **Manager** dan **Sales Representative** → perlu strategi engagement baru.

---

## 🔁 Rekomendasi Action Items

### 1. Retain Young Talents (25–34 Tahun)
Buat program pengembangan karier dan mentorship untuk menurunkan attrition di kelompok usia ini.

### 2. Evaluasi dan Revitalisasi Divisi Sales
Tinjau ulang sistem insentif dan lingkungan kerja divisi Sales. Lakukan survei karyawan untuk memahami penyebab attrition.

### 3. Perkuat Engagement & Job Satisfaction
Tingkatkan komunikasi dan feedback antar tim. Evaluasi manajemen dan budaya kerja.

### 4. Optimasi Rekrutmen Berdasarkan Data
Hindari rekrutmen besar-besaran dari bidang pendidikan dengan attrition tinggi tanpa mengevaluasi kecocokan kerja.

---

© 2025 | HR Analytics Final Project | Edutech Case Study
