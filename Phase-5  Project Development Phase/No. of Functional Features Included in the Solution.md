# No. of Functional Features Included in the Solution

## Functional Features Overview

| S.No | Feature Name | Feature Description | Module/Component | Status | Marks Contribution |
|---|---|---|---|---|---|
| 1 | Dataset Loader & Cleaning | Loads `crop_recommendation.csv`, removes duplicates and missing values | `train_model.py` | Done | — |
| 2 | Outlier Removal (IQR) | Detects and removes outliers per feature using the Interquartile Range method | `train_model.py` | Done | — |
| 3 | Exploratory Data Analysis | Boxplots (univariate), correlation heatmap (bivariate), pairplot (multivariate) | `train_model.py` → `static/images/` | Done | — |
| 4 | Seasonal Crop Grouping | Rule-based grouping of crops into summer/winter/rainy categories for insight | `train_model.py` | Done | — |
| 5 | K-Means Clustering + Elbow Method | Unsupervised clustering of soil/climate profiles with optimal-k visualization | `train_model.py` → `static/images/elbow.png` | Done | — |
| 6 | Model Comparison (Logistic Regression vs. Random Forest) | Trains both, compares accuracy/precision/recall/F1, selects the best | `train_model.py` | Done | — |
| 7 | Model Persistence | Saves the best model + feature order to `model.pkl` | `train_model.py` | Done | — |
| 8 | Home Page | Landing page introducing OptiCrop | `templates/home.html` | Done | — |
| 9 | About Page | Objectives, methodology, and input feature explanation | `templates/about.html` | Done | — |
| 10 | Find Your Crop (Prediction) Page | Input form + real-time crop recommendation | `templates/findyourcrop.html`, `app.py` | Done | — |

## Feature Summary

| Metric | Count / Value |
|---|---|
| Total Features Planned | 10 |
| Total Features Implemented | 10 |
| Core / Must-Have Features | 7 (Data loading/cleaning, outlier removal, model comparison, persistence, prediction page) |
| Additional / Nice-to-Have Features | 3 (Seasonal grouping, K-Means + Elbow, About page) |
| Features Tested & Verified | 10 |

## Feature Category Breakdown

| S.No | Category | Features in Category | Example Features |
|---|---|---|---|
| 1 | User Interface (UI) | 3 | Home, About, Find Your Crop pages |
| 2 | Backend / Logic | 2 | Flask routing, input validation in `/predict` |
| 3 | Database / Storage | 2 | CSV dataset, serialized `model.pkl` |
| 4 | ML / Prediction | 5 | IQR outlier removal, EDA, K-Means + Elbow, Logistic Regression, Random Forest |
| 5 | Security / Authentication | 0 | Not applicable — single-session, stateless app |
