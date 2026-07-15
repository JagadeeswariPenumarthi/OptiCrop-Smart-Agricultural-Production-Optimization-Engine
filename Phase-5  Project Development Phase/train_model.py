"""
train_model.py
----------------
OptiCrop: Smart Agricultural Production Optimization Engine

This script performs the full machine learning pipeline for the crop
recommendation system:

    1. Load and inspect the dataset
    2. Clean the data (missing values, duplicates)
    3. Detect and remove outliers using the IQR method
    4. Explore the data (univariate, bivariate, multivariate analysis, seasonal groupings)
    5. Split into train / test sets
    6. Train and compare Logistic Regression and Random Forest
    7. Run K-Means clustering + Elbow Method as a complementary analysis
    8. Evaluate both models (accuracy, precision, recall, F1, report) and pick the best
    9. Persist the best model to model.pkl

Run with:
    python train_model.py
"""

import pickle

import matplotlib
matplotlib.use("Agg")  # allows saving plots without a display
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    f1_score,
    precision_score,
    recall_score,
)
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

DATA_PATH = "crop_recommendation.csv"
MODEL_PATH = "model.pkl"
PLOTS_DIR = "static/images"


def load_data(path: str = DATA_PATH) -> pd.DataFrame:
    """Load the crop recommendation dataset and print a quick summary."""
    df = pd.read_csv(path)
    print("Dataset shape:", df.shape)
    print("\nColumn dtypes:\n", df.dtypes)
    print("\nFirst 5 rows:\n", df.head())
    return df


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Report and remove missing values / duplicate rows."""
    print("\nMissing values per column:\n", df.isnull().sum())

    n_duplicates = df.duplicated().sum()
    print(f"\nDuplicate rows found: {n_duplicates}")
    df = df.drop_duplicates().reset_index(drop=True)
    return df


def remove_outliers_iqr(df: pd.DataFrame, columns) -> pd.DataFrame:
    """Remove outliers from the given numeric columns using the IQR rule."""
    cleaned = df.copy()
    for col in columns:
        q1 = cleaned[col].quantile(0.25)
        q3 = cleaned[col].quantile(0.75)
        iqr = q3 - q1
        lower = q1 - 1.5 * iqr
        upper = q3 + 1.5 * iqr
        before = len(cleaned)
        cleaned = cleaned[(cleaned[col] >= lower) & (cleaned[col] <= upper)]
        removed = before - len(cleaned)
        print(f"  {col}: removed {removed} outlier rows")
    return cleaned.reset_index(drop=True)


def plot_boxplots(df: pd.DataFrame, columns, out_path: str):
    plt.figure(figsize=(12, 6))
    sns.boxplot(data=df[columns])
    plt.title("Feature Distributions (Boxplot)")
    plt.tight_layout()
    plt.savefig(out_path)
    plt.close()
    print(f"Saved boxplot to {out_path}")


def plot_correlation_heatmap(df: pd.DataFrame, columns, out_path: str):
    """Bivariate analysis: correlation between numeric features."""
    plt.figure(figsize=(9, 7))
    corr = df[columns].corr()
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="YlGnBu", square=True)
    plt.title("Correlation Heatmap (Bivariate Analysis)")
    plt.tight_layout()
    plt.savefig(out_path)
    plt.close()
    print(f"Saved correlation heatmap to {out_path}")


def plot_pairplot(df: pd.DataFrame, columns, out_path: str, sample_crops=None):
    """Multivariate analysis: pairwise relationships between features, colored by crop."""
    subset = df
    if sample_crops:
        subset = df[df["label"].isin(sample_crops)]
    plot_cols = columns + ["label"]
    grid = sns.pairplot(subset[plot_cols], hue="label", diag_kind="hist", height=1.8)
    grid.savefig(out_path)
    plt.close("all")
    print(f"Saved pairplot to {out_path}")


def seasonal_crop_analysis(df: pd.DataFrame):
    """Simple rule-based grouping used for exploratory insight only."""
    summer = df[(df.temperature > 30) & (df.humidity > 50)]["label"].unique()
    winter = df[(df.temperature < 20) & (df.humidity > 30)]["label"].unique()
    rainy = df[(df.rainfall > 200) & (df.humidity > 50)]["label"].unique()

    print("\nSummer crops:", list(summer))
    print("Winter crops:", list(winter))
    print("Rainy season crops:", list(rainy))


def elbow_method(X_scaled, out_path: str, k_range=range(1, 11)):
    """Fit K-Means for a range of k and plot inertia (elbow curve)."""
    inertias = []
    for k in k_range:
        km = KMeans(n_clusters=k, n_init=10, random_state=42)
        km.fit(X_scaled)
        inertias.append(km.inertia_)

    plt.figure(figsize=(8, 5))
    plt.plot(list(k_range), inertias, marker="o")
    plt.xlabel("Number of clusters (k)")
    plt.ylabel("Inertia")
    plt.title("Elbow Method for Optimal k")
    plt.tight_layout()
    plt.savefig(out_path)
    plt.close()
    print(f"Saved elbow plot to {out_path}")
    return inertias


def evaluate_model(name, model, X_train, X_test, y_train, y_test):
    """Fit a model and return its evaluation metrics."""
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    metrics = {
        "name": name,
        "model": model,
        "accuracy": accuracy_score(y_test, y_pred),
        "precision": precision_score(y_test, y_pred, average="weighted", zero_division=0),
        "recall": recall_score(y_test, y_pred, average="weighted", zero_division=0),
        "f1": f1_score(y_test, y_pred, average="weighted", zero_division=0),
        "report": classification_report(y_test, y_pred),
    }
    return metrics


def train_and_evaluate(X_train, X_test, y_train, y_test):
    """Train and compare multiple algorithms, then return the best-performing model."""
    candidates = {
        "Logistic Regression": Pipeline([
            ("scaler", StandardScaler()),
            ("clf", LogisticRegression(max_iter=1000)),
        ]),
        "Random Forest": Pipeline([
            ("scaler", StandardScaler()),
            ("clf", RandomForestClassifier(n_estimators=200, random_state=42)),
        ]),
    }

    results = []
    for name, model in candidates.items():
        results.append(evaluate_model(name, model, X_train, X_test, y_train, y_test))

    print("\n=== Model Comparison ===")
    print(f"{'Model':<22}{'Accuracy':<12}{'Precision':<12}{'Recall':<12}{'F1-score':<12}")
    for r in results:
        print(f"{r['name']:<22}{r['accuracy']:<12.4f}{r['precision']:<12.4f}{r['recall']:<12.4f}{r['f1']:<12.4f}")

    best = max(results, key=lambda r: r["accuracy"])
    print(f"\nBest model: {best['name']} (accuracy = {best['accuracy']:.4f})")
    print(f"\nClassification Report for {best['name']}:\n", best["report"])

    return best["model"]


def main():
    feature_cols = ["N", "P", "K", "temperature", "humidity", "ph", "rainfall"]

    df = load_data()
    df = clean_data(df)
    df = remove_outliers_iqr(df, feature_cols)

    import os
    os.makedirs(PLOTS_DIR, exist_ok=True)
    plot_boxplots(df, feature_cols, f"{PLOTS_DIR}/boxplot.png")
    plot_correlation_heatmap(df, feature_cols, f"{PLOTS_DIR}/correlation_heatmap.png")
    sample_crops = ["rice", "maize", "cotton", "coffee", "watermelon"]
    plot_pairplot(df, feature_cols, f"{PLOTS_DIR}/pairplot.png", sample_crops=sample_crops)
    seasonal_crop_analysis(df)

    X = df[feature_cols]
    y = df["label"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=42, stratify=y
    )

    # K-Means / Elbow method as an unsupervised complement to the classifier
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    elbow_method(X_scaled, f"{PLOTS_DIR}/elbow.png")

    model = train_and_evaluate(X_train, X_test, y_train, y_test)

    with open(MODEL_PATH, "wb") as f:
        pickle.dump({"model": model, "features": feature_cols}, f)
    print(f"\nModel saved to {MODEL_PATH}")


if __name__ == "__main__":
    main()
