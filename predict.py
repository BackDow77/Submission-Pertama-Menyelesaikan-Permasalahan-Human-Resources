
# --- KONFIGURASI ---
MODEL_TYPE = 'classification'
MODEL_PATH = 'random_forest_classifier_model.joblib'  # ganti sesuai nama model

import joblib
import pandas as pd

def predict(data_input):
    """
    Prediksi menggunakan model Random Forest (classification).
    """
    try:
        # 1. Load model
        model = joblib.load(MODEL_PATH)
        print("✅ Model berhasil dimuat.")

        # 2. Convert input dict ke DataFrame
        input_df = pd.DataFrame([data_input])
        print("📄 Data yang diprediksi:\n", input_df)

        # 3. Prediksi
        prediction = model.predict(input_df)[0]

        # 4. Interpretasi hasil
        if MODEL_TYPE == 'classification':
            if prediction == 1:
                return "🔴 Prediksi: Karyawan kemungkinan AKAN KELUAR (Attrition = 1)."
            else:
                return "🟢 Prediksi: Karyawan kemungkinan TETAP BEKERJA (Attrition = 0)."
        else:
            return f"Hasil prediksi: {prediction:.2f}"

    except FileNotFoundError:
        return f"❌ Error: Model tidak ditemukan di path '{MODEL_PATH}'"
    except Exception as e:
        return f"❌ Terjadi error saat prediksi: {e}"

# --- CONTOH PENGGUNAAN ---
if __name__ == "__main__":
    # Data input harus cocok dengan fitur asli sebelum preprocessing
    # Pastikan urutan kolom dan tipe data sesuai dengan data training
    data_baru = {
        'Age': 30,
        'BusinessTravel': 'Travel_Rarely',
        'DailyRate': 800,
        'Department': 'Sales',
        'DistanceFromHome': 3,
        'Education': 2,
        'EducationField': 'Marketing',
        'EnvironmentSatisfaction': 4,
        'Gender': 'Female',
        'HourlyRate': 65,
        'JobInvolvement': 3,
        'JobLevel': 2,
        'JobRole': 'Sales Executive',
        'JobSatisfaction': 2,
        'MaritalStatus': 'Single',
        'MonthlyIncome': 5500,
        'MonthlyRate': 20000,
        'NumCompaniesWorked': 1,
        'OverTime': 'Yes',
        'PercentSalaryHike': 12,
        'PerformanceRating': 3,
        'RelationshipSatisfaction': 3,
        'StockOptionLevel': 0,
        'TotalWorkingYears': 7,
        'TrainingTimesLastYear': 2,
        'WorkLifeBalance': 2,
        'YearsAtCompany': 5,
        'YearsInCurrentRole': 2,
        'YearsSinceLastPromotion': 1,
        'YearsWithCurrManager': 3
    }

    hasil = predict(data_baru)
    print("-" * 40)
    print(hasil)
    print("-" * 40)
