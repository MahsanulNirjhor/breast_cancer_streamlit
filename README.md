# 🧠 Breast Cancer Predictor ML App

A beginner-friendly machine learning web app that predicts whether a tumor is **benign** or **malignant** using logistic regression.  
Built with **Streamlit**, powered by **scikit-learn**, and deployed with a full **CI/CD DevOps pipeline** using **GitHub Actions** and **Streamlit Cloud**.

> 🎓 Developed as part of a mentorship project to help students learn real-world machine learning, test-driven development, and DevOps best practices.

---

## 🔍 Project Highlights

- ✅ Built using **Logistic Regression** with the Wisconsin Breast Cancer Dataset
- 🎨 Interactive UI using **Streamlit** (no frontend code needed)
- 🧪 **Test-Driven Development** using `pytest`
- ☁️ Fully automated **CI/CD pipeline** (GitHub Actions + auto-merge)
- 📁 Supports both **manual input** (via sliders) and **CSV batch prediction**
- 🧠 Includes auto-reset, result download, and prediction visualization (optional)

---

## 🧠 Problem Statement

Early detection of breast cancer can save lives. This app demonstrates how machine learning can assist in predicting tumor diagnosis based on real medical features.

---

## 📊 Technologies Used

| Tool/Tech        | Purpose                         |
|------------------|----------------------------------|
| `Python`         | Core programming language        |
| `scikit-learn`   | Logistic regression model        |
| `pandas`         | Data manipulation                |
| `Streamlit`      | Frontend and web interface       |
| `pytest`         | Automated testing (TDD)          |
| `GitHub Actions` | CI/CD and automation             |
| `Docker`         | (Optional) containerization      |
| `Streamlit Cloud`| App deployment                   |

---

## 🚀 Live Demo

🔗 [Click here to try the live app](https://breastcancerapp-j35rgsxozekug8vwbys8pn.streamlit.app/)

---

## ⚙️ How It Works

1. User inputs feature values manually **or uploads a CSV file**
2. The logistic regression model predicts whether the tumor is **benign** or **malignant**
3. The app displays the result, and allows users to download batch predictions as CSV

---

## 🧪 Test-Driven Development

We follow TDD principles:
- All ML logic is **unit tested** using `pytest`
- CI pipeline automatically runs tests on every push
- The app only deploys if **all tests pass successfully**

✅ Tests give users and developers confidence in model performance and app stability.

---

## 🔁 CI/CD DevOps Pipeline

This app features a **full CI/CD workflow** using GitHub Actions:

| Stage       | Description |
|-------------|-------------|
| **CI (Tests)** | On every push to `dev`, unit tests run via GitHub Actions |
| **CD (Deploy)** | Streamlit Cloud deploys the latest version from `main` |

🔐 Includes optional branch protection rules and secrets for secure auto-merge.

---

## 🧑‍💻 How to Run Locally

```bash
git clone https://github.com/your-username/breast-cancer-predictor.git
cd breast-cancer-predictor
pip install -r requirements.txt
streamlit run streamlit_app.py
