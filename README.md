# OptiCrop: Smart Agricultural Production Optimization Engine

OptiCrop is an advanced Machine Learning-powered smart agricultural recommendation system
designed to support modern, data-driven farming practices by providing accurate and intelligent
crop prediction solutions. The system analyzes critical environmental and soil-related parameters
— Nitrogen (N), Phosphorous (P), Potassium (K), temperature, humidity, soil pH, and rainfall — to
determine the most suitable crop for cultivation under specific conditions.

This repository combines the full project documentation (problem definition through demo
planning) with the actual working codebase.

## Team
| Team ID | Project Name | Members |
|---|---|---|
| OC-2026-01 | OptiCrop: Smart Agricultural Production Optimization Engine | Jagadeeswari P., Manjusha Elubandi, *[add remaining team members]* |

## Repository Structure

| Folder | Phase | Notes |
|---|---|---|
| `1. Brainstorming & Ideation` | Problem framing & ideation | Docs only |
| `2. Requirement Analysis` | Requirements & tech stack | Docs only |
| `3. Project Design Phase` | Architecture & design | Docs + `ER_Diagram.png`, `Use_Case_Diagram.png` |
| `4. Project Planning Phase` | Sprint planning | Docs only |
| `5. Project Development Phase` | **Implementation** | **Actual working Flask app + ML pipeline** |
| `6. Project Testing` | Testing & evaluation | Docs only |
| `7. Project Documentation` | Documentation | Docs only |
| `8. Project Demonstration` | Demo & presentation | Docs only |

## What's Actually Running (Phase 5)
- **`train_model.py`** — loads `crop_recommendation.csv`, cleans data, removes outliers (IQR),
  runs EDA (boxplot, correlation heatmap, pairplot), does seasonal crop grouping, runs K-Means
  clustering + Elbow Method, trains and compares **Logistic Regression** vs. **Random Forest**,
  and saves the best model to `model.pkl`.
- **`app.py`** — Flask app with three pages: **Home**, **About**, and **Find Your Crop**
  (the prediction form), plus a `/predict` endpoint.
- **`templates/`**, **`static/`** — the HTML/CSS/JS frontend.

## Tech Stack
- **Language:** Python 3.10+
- **ML Libraries:** scikit-learn (Logistic Regression, Random Forest, K-Means), pandas, numpy, matplotlib, seaborn
- **Backend:** Flask
- **Frontend:** HTML, CSS, JavaScript
- **Deployment:** Gunicorn (`Procfile` included)
- **Version Control:** Git & GitHub

## How to Run
```bash
git clone https://github.com/<your-username>/OptiCrop-Smart-Agricultural-Production-Optimization.git
cd OptiCrop-Smart-Agricultural-Production-Optimization/5.\ Project\ Development\ Phase
pip install -r requirements.txt
python train_model.py   # optional: regenerates model.pkl and EDA plots
python app.py
```
Then open `http://127.0.0.1:5000` in your browser.

## Replace placeholder content
Each `.md` file inside the numbered phase folders (1–4, 6–8) follows the official evaluation
template format (Date / Team ID / Project Name / Maximum Marks) — replace bracketed
placeholders `[...]` with your team's actual details before submission.

