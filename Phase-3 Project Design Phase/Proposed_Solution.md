# Project Initialization and Planning Phase

## Project Proposal (Proposed Solution) Report

OptiCrop transforms crop selection using machine learning, boosting agricultural efficiency and
productivity. It tackles poor crop selection, inefficient resource use, and low yield caused by
environmental uncertainty, promising better farming decisions and improved profitability. Key
features include a multi-algorithm crop recommendation model and a simple, real-time web
interface for farmers.

### Project Overview
| Field | Details |
|---|---|
| Objective | To help farmers, researchers, and agribusinesses identify the most suitable crop for given soil and climate conditions using machine learning. |
| Scope | The project covers data collection, preprocessing, model training/evaluation (KNN, Logistic Regression, K-Means), and deployment of a web application that delivers real-time crop recommendations. |

### Problem Statement
| Field | Details |
|---|---|
| Description | Farmers struggle to determine the most suitable crop based on soil nutrients (N, P, K) and climate conditions (temperature, humidity, rainfall, pH), leading to financial losses and reduced yield. |
| Impact | Solving this improves agricultural productivity, reduces resource wastage, supports sustainable farming, and increases farmer profitability. |

### Proposed Solution
| Field | Details |
|---|---|
| Approach | Train and evaluate multiple ML algorithms on a labeled crop dataset (soil + climate → crop), select the best-performing model, and serve it through a Flask web application. |
| Key Features | - Multi-algorithm crop classification (KNN, Logistic Regression) <br> - K-Means clustering for exploratory soil/climate grouping <br> - Real-time prediction via a responsive web interface <br> - Model evaluation and persistence of the best model |

### Resource Requirements
| Resource Type | Description | Specification / Allocation |
|---|---|---|
| Computing Resources | CPU specification | Standard laptop CPU (no GPU required for classical ML models) |
| Memory | RAM specification | 8 GB |
| Storage | Disk space for data, models, logs | ~1 GB |
| Frameworks | Python frameworks | Flask |
| Libraries | Additional libraries | scikit-learn, pandas, numpy, matplotlib, seaborn |
| Development Environment | IDE | Jupyter Notebook, VS Code |
| Data | Source, size, format | Crop recommendation dataset (Kaggle), CSV, ~2200 rows × 8 columns (N, P, K, temperature, humidity, pH, rainfall, label) |

