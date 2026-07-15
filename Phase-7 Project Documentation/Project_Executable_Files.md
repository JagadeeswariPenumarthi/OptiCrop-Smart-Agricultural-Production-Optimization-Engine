# Project Executable Files

## Step 1: Submission Checklist

| S.No | Item to Submit | Submitted (Yes/No/NA) |
|---|---|---|
| 1 | Complete source code (all files and folders) | Yes |
| 2 | README / Setup Guide | Yes |
| 3 | requirements.txt | Yes |
| 4 | Database schema / seed files (crop_dataset.csv) | Yes |
| 5 | Environment configuration file | NA — no secrets/API keys used |
| 6 | Deployed application URL (if hosted) | [add if deployed] |
| 7 | APK / Executable binary | NA — web application |
| 8 | Dockerfile / Containerization config | Optional — not included in v1 |
| 9 | Test files and test results | See `6. Project Testing/Performance Testing.md` |
| 10 | Demo video or walkthrough | [add link] |

## Step 2: File / Folder Structure
See the root `README.md` and the repository tree for the complete folder structure
(`1. Brainstorming & Ideation` through `8. Project Demonstration`).

## Step 3: Deployment / Access Details

| Field | Details |
|---|---|
| Hosted / Deployed URL | [add if deployed, e.g., Render/Heroku] |
| Login Credentials (Demo) | NA — no authentication required |
| Platform / Hosting Provider | [e.g., Render, PythonAnywhere] |
| Repository Link | [GitHub repo URL] |
| Demo Video Link | [add link] |

## Step 4: Run Instructions
```bash
cd "5. Project Development Phase"
pip install -r requirements.txt
python train_model.py   # optional — regenerates model.pkl and EDA plots
python app.py
```
Open `http://127.0.0.1:5000` in a browser, navigate to **Find Your Crop**, enter soil
(N, P, K, pH) and climate (temperature, humidity, rainfall) values, and click **Predict Best Crop**.
For a production-style deployment, the included `Procfile` (`web: gunicorn app:app`) is ready to
use on platforms like Heroku.

## Step 5: Known Issues / Limitations

| S.No | Known Issue / Limitation | Workaround / Status |
|---|---|---|
| 1 | Only shows a single top prediction, not top-3 alternatives | Planned for future roadmap |
| 2 | No persistent storage of past predictions | By design — stateless single-session app |
| 3 | Flask dev server not production-hardened | Use Gunicorn/WSGI server for deployment |

