import os
import joblib
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import LocalOutlierFactor


# Load Dataset

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
dataset_path = os.path.join(
    BASE_DIR,
    "data",    
    "retail_sales_dataset.xlsx"
)

df = pd.read_excel(dataset_path)

print("Dataset Loaded Successfully")
print(df.head())

# Feature Selection

X =df[[

        "Quantity",        
        "UnitPrice",
        "TotalAmount",
        "DayOfWeek"
    ]]

encoder = LabelEncoder()

for col in X.select_dtypes(include="object").columns:
    X[col] = encoder.fit_transform(X[col])


# Data Scaling

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
print("Data Preprocessing Completed")


# Train Isolation Fores

model = IsolationForest(
    contamination=0.05,
    random_state=42
)
model.fit(X_scaled)
print("Model Training Completed")


# Save Model

models_folder = os.path.join(BASE_DIR, "models")
os.makedirs(models_folder, exist_ok=True)
joblib.dump(
    model,
    os.path.join(
    models_folder,
       "isolation_forest.pkl"
    )
)

joblib.dump(
    scaler,
    os.path.join(    models_folder,
       "scaler.pkl"
    )
)

print("Model Saved Successfully")

# -----------------------------
# Train Local Outlier Factor
# -----------------------------

lof_model = LocalOutlierFactor(

    n_neighbors=20,

    contamination=0.05,

    novelty=True

)

lof_model.fit(X_scaled)

print("LOF Model Training Completed")

joblib.dump(

    lof_model,

    os.path.join(
        models_folder,
        "lof.pkl"
    )

)

print("LOF Model Saved Successfully")