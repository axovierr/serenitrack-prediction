from flask import Flask, render_template, request
import csv
import os

app = Flask(__name__)

csv_file_path = 'prediction.csv'

def write_csv_header():
    if not os.path.exists(csv_file_path):
        with open(csv_file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            header = ['Gender', 'Age', 'Academic Pressure', 'Study Satisfaction', 'Sleep Duration', 
                      'Dietary Habits', 'Suicidal Thoughts', 'Study Hours', 'Financial Stress', 
                      'Family History', 'Prediction']
            writer.writerow(header)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        form_data = request.form
        
        suicidal = form_data.get('suicidal_thoughts', 'No')
        stress = int(form_data.get('financial_stress', 0))
        pressure = int(form_data.get('academic_pressure', 0))
        
        if suicidal == 'Yes' or (stress > 3 and pressure > 3):
            result = "Depressed"
        else:
            result = "Not Depressed"

        if result == "Depressed":
            message = "Hasil analisis menunjukkan adanya indikasi gejala depresi. Mohon jangan abaikan kondisi kesehatan mental Anda."
            saran = [
                "Kami sangat menyarankan Anda untuk segera berkonsultasi dengan tenaga profesional (psikolog atau psikiater).",
                "Jangan ragu untuk membagikan beban pikiran Anda kepada keluarga atau orang terdekat yang Anda percayai.",
                "Hubungi layanan darurat atau hotline dukungan psikologis jika Anda merasa berada dalam masa krisis."
            ]
        else:
            message = "Hasil analisis menunjukkan kondisi kesehatan mental Anda saat ini relatif stabil."
            saran = [
                "Tetap pertahankan keseimbangan yang sehat antara waktu produktif dan istirahat Anda.",
                "Lakukan aktivitas fisik secara rutin dan kelola asupan nutrisi dengan baik.",
                "Jangan ragu untuk mencari bantuan profesional di kemudian hari jika Anda mulai merasa tertekan."
            ]

        write_csv_header()
        with open(csv_file_path, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([
                form_data.get('gender', ''), 
                form_data.get('age', ''), 
                form_data.get('academic_pressure', ''), 
                form_data.get('study_satisfaction', ''), 
                form_data.get('sleep_duration', ''), 
                form_data.get('dietary_habits', ''), 
                form_data.get('suicidal_thoughts', ''), 
                form_data.get('study_hours', ''), 
                form_data.get('financial_stress', ''), 
                form_data.get('family_history', ''), 
                result
            ])

        return render_template('result.html', result=result, message=message, saran=saran)
    
    except Exception as e:
        return render_template('result.html', result="Error", message=f"Terjadi kesalahan sistem: {e}", saran=[])

if __name__ == '__main__':
    app.run(debug=True)