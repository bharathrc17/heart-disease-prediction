# heart-disease-prediction-using-machine-learning
A machine learning model to predict the presence of heart disease based on clinical features like age, cholesterol, and ECG results.
# Heart Disease Prediction 🫀

A machine learning project that predicts the presence of heart disease using clinical parameters.

## 📊 Dataset Features
- **age**: Age of the person
- **sex**: Gender (1 = male; 0 = female)
- **cp**: Chest pain type (0–3)
- **trestbps**: Resting blood pressure
- **chol**: Serum cholesterol (mg/dl)
- **fbs**: Fasting blood sugar > 120 mg/dl (1 = true; 0 = false)
- **restecg**: Resting electrocardiographic results (0–2)
- **thalach**: Maximum heart rate achieved
- **exang**: Exercise-induced angina (1 = yes; 0 = no)
- **oldpeak**: ST depression induced by exercise
- **slope**: Slope of peak exercise ST segment (0–2)
- **ca**: Number of major vessels colored by fluoroscopy (0–3)
- **thal**: Thalassemia (1 = normal; 2 = fixed defect; 3 = reversible defect)
- **target**: 1 = heart disease, 0 = no heart disease

## 🧠 ML Model
- Tried various models: Logistic Regression, Decision Tree, KNN, Random Forest
- Best-performing model: `Random Forest Classifier`

## 🛠️ Tech Stack
- Python
- pandas, scikit-learn, matplotlib
- Jupyter Notebook / Streamlit (optional UI)

## ⚙️ How to Run
# Install dependencies
pip install -r requirements.txt

# Run model or Streamlit app
python predict.py
# or
streamlit run app.py 
