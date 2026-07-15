# Technology Stack


## Technology Stack Details

| S.No | Architecture Component / Layer | Technology Chosen | Justification / Purpose |
|---|---|---|---|
| 1 | Frontend / Client-Side | HTML, CSS, JavaScript | Lightweight, fast to build, no heavy framework overhead needed for a simple input-and-result form |
| 2 | Backend / Server-Side | Python (Flask) | Simple to integrate directly with scikit-learn models; team already has Python/ML proficiency |
| 3 | Machine Learning | scikit-learn (KNN, Logistic Regression, K-Means, Decision Tree, Random Forest) | Well-documented, production-ready implementations of the required classification/clustering algorithms |
| 4 | Data Handling | pandas, numpy | Efficient dataset loading, cleaning, and numerical operations for preprocessing and EDA |
| 5 | Visualization | matplotlib, seaborn | Used during EDA for univariate, bivariate, and multivariate analysis of soil/climate features |
| 6 | Model Persistence | pickle / joblib | Saves the best-performing trained model for fast reuse without retraining on every request |
| 7 | Version Control & CI/CD | Git, GitHub | Enables team collaboration, version history, and structured repository organization |
| 8 | Development Environment | Jupyter Notebook, VS Code / PyCharm | Notebook for EDA/model experimentation; IDE for backend/app development |

