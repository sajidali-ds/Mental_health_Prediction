# Mental Health Prediction

> 🚧 **Work in progress:** this project is actively being improved. The current release focuses on classical NLP baselines, while transformer-based experiments are in progress.

## Overview

A machine learning project that classifies text statements into **7 mental health categories** using Natural Language Processing and supervised learning.

**Classes**

- Anxiety
- Bipolar
- Depression
- Normal
- Personality Disorder
- Stress
- Suicidal

---

## Dataset

- **~53,000** text statements
- **7 target classes**
- Class imbalance handled with class-weighted models where appropriate

---

## Workflow

```text
Raw Text
   ↓
Cleaning & Preprocessing
   ↓
TF-IDF / Word2Vec
   ↓
ML Classifiers
   ↓
Evaluation
   ↓
Streamlit App
```

---

## Preprocessing

- Lowercase conversion
- Special character removal
- Whitespace normalization
- Porter stemming

---

## Models Compared

| Features | Model | Accuracy | Macro F1 |
|---|---|---:|---:|
| **TF-IDF** | **LinearSVC** | **0.77** | **0.73** |
| TF-IDF | Logistic Regression | 0.77 | 0.72 |
| TF-IDF | Random Forest | 0.74 | 0.68 |
| TF-IDF | Naive Bayes | 0.47 | 0.21 |
| Word2Vec | Random Forest | 0.73 | 0.67 |
| Word2Vec | LinearSVC | 0.65 | 0.58 |
| Word2Vec | Logistic Regression | 0.64 | 0.57 |

## Best Model

**TF-IDF + LinearSVC**

- **Accuracy:** 77%
- **Macro F1:** 0.73
- **Weighted F1:** 0.77

---

## Streamlit Demo

Example:

```text
Input:
I am feeling nervous and restless.

Prediction:
Anxiety
```

Run locally:

```bash
streamlit run app.py
```

---

## Project Structure

```text
Mental_health_Prediction/
│
├── Data/
├── Notebooks/
├── models/
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Roadmap

- [x] TF-IDF baseline
- [x] Word2Vec baseline
- [x] Streamlit interface
- [ ] Hyperparameter tuning
- [ ] DistilBERT fine-tuning
- [ ] MentalBERT comparison
- [ ] Better handling of minority classes
- [ ] Cloud deployment

---

## Disclaimer

This project is for **educational and research purposes only**. It is **not** a medical diagnosis tool and should not replace professional mental health support.
