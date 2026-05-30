#  Insurance Expense Prediction App

A machine learning web application built with **Streamlit** that predicts medical insurance expenses based on personal health and demographic information.

---

##  Project Structure

```
Insurance_Prediction/
│
├── app.py                       # Streamlit web application
├── Insurance_Prediction.ipynb   # Jupyter notebook (EDA + Model training)
├── pipe.pkl                     # Trained ML pipeline (saved model)
├── insurance.csv                # Dataset
├── requirements.txt             # Python dependencies
└── README.md                    # Project documentation
```

---

##  Dataset

- **Source:** `insurance.csv`
- **Records:** 1338 rows, 7 columns
- **Target column:** `expenses` (medical insurance cost in USD)

| Column | Type | Description |
|---|---|---|
| `age` | Numeric | Age of the person (18–64) |
| `sex` | Categorical | `male` / `female` |
| `bmi` | Numeric | Body Mass Index (16.0–53.1) |
| `children` | Numeric | Number of children (0–5) |
| `smoker` | Categorical | `yes` / `no` |
| `region` | Categorical | `northwest`, `northeast`, `southwest`, `southeast` |
| `expenses` | Numeric | Medical insurance expenses (target) |

---


##  Model

| Detail | Value |
|---|---|
| Algorithm | `SGDRegressor` |
| Encoding | `OneHotEncoder` (for categorical columns) |
| Scaling | `StandardScaler` (for `age` and `bmi`) |
| Pipeline | `sklearn.pipeline.Pipeline` |

### Pipeline Steps

```
Input DataFrame
      ↓
ColumnTransformer
  ├── OneHotEncoder  →  sex, smoker, region, children_expense
  └── StandardScaler →  age, bmi
      ↓
SGDRegressor
      ↓
Predicted Expense ($)
```

---

##  How to Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the app

```bash
streamlit run app.py
```

### 3. Open in browser

```
http://localhost:8501
```

---

##  Requirements

```
streamlit
pandas
scikit-learn
```

---

##  App Usage

1. Enter your **Age**
2. Select your **Sex**
3. Enter your **BMI**
4. Select **Children Expense** level:
   - `lower expenses` → 0–1 children
   - `high expenses` → 2–3 children
   - `medium expenses` → 4–5 children
5. Select **Smoker** status
6. Select your **Region**
7. Click **"Predict Expense"** to get the predicted insurance cost

---

##  Important Notes

- The column names in the input DataFrame **must exactly match** the training column names.
- The `children_expense` category values must be exactly: `'lower expenses'`, `'high expenses'`, `'medium expenses'` (with spaces, not underscores).
- The model was trained with **scikit-learn 1.7.1** — using a different version may show warnings.

---


