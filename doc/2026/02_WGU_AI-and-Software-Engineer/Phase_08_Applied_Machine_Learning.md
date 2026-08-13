# Phase 8: Applied Machine Learning
**Duration:** Weeks 18–20 (3 Weeks)  
**Target WGU Course:** Applied Machine Learning for Business Solutions (3 CUs)

---

## 1. Official WGU Competencies Covered
- [ ] Analyze industry opportunities and challenges for machine learning adoption.
- [ ] Apply appropriate machine learning models to solve specific business requirements.
- [ ] Communicate machine learning strategies and technical metrics to non-technical stakeholders.
- [ ] Select, train, and evaluate machine learning algorithms based on strategic objectives.

---

## 2. Comprehensive Study Topics

### 8.1 Machine Learning Taxonomy & Business Context
- **Spectrum:** AI $\supset$ Machine Learning $\supset$ Deep Learning $\supset$ Generative AI.
- **Learning Paradigms:**
  - *Supervised Learning:* Labeled data $ightarrow$ Predict target (Regression, Classification).
  - *Unsupervised Learning:* Unlabeled data $ightarrow$ Discover patterns (Clustering, Dimensionality Reduction).
  - *Reinforcement Learning:* Agent $ightarrow$ Environment interaction $ightarrow$ Reward optimization.

### 8.2 End-to-End Machine Learning Pipeline
1. **Problem Formulation:** Defining target variable and business KPI (e.g., predict customer churn).
2. **Data Acquisition & Preprocessing:** Handling missing values, outlier detection, scaling/normalization (`StandardScaler`, `MinMaxScaler`).
3. **Feature Engineering:** One-Hot Encoding, Categorical Embeddings, Feature Selection.
4. **Model Training & Hyperparameter Tuning:** Train/Validation/Test splits, Cross-Validation, Grid Search / Random Search.
5. **Evaluation & Deployment:** Validation against business metrics, inference pipeline construction.

### 8.3 Algorithms & Performance Metrics
- **Regression Algorithms:** Linear Regression, Ridge/Lasso, Decision Tree Regressor.
  - *Metrics:* Mean Absolute Error (MAE), Mean Squared Error (MSE), Root Mean Squared Error (RMSE), $R^2$ Score.
- **Classification Algorithms:** Logistic Regression, Decision Trees, Random Forest, XGBoost, Support Vector Machines (SVM), k-Nearest Neighbors (k-NN).
  - *Metrics:* Confusion Matrix, Accuracy, Precision, Recall, $F_1$-Score, ROC-AUC Curve.
- **Unsupervised Algorithms:** K-Means Clustering, Hierarchical Clustering, PCA.

### 8.4 Model Diagnostics & Overfitting Control
- **Bias-Variance Trade-off:** High Bias (Underfitting) vs. High Variance (Overfitting).
- **Mitigation Techniques:** Regularization ($L_1/L_2$), Cross-Validation, Ensemble methods (Bagging, Boosting), Feature reduction.
- **Data Leakage:** Preventing future/target info from leaking into feature training sets.

---

## 3. Algorithm Selection Guide

| Business Problem Type | Target Variable | Recommended Algorithm | Key Evaluation Metric |
| :--- | :--- | :--- | :--- |
| **Predict House Prices** | Continuous numerical | Random Forest / XGBoost Regressor | RMSE / $R^2$ Score |
| **Customer Churn Prediction** | Binary (1/0) | Logistic Regression / XGBoost Classifier | Precision / Recall / $F_1$-Score |
| **Customer Segmentation** | Unlabeled groups | K-Means Clustering | Silhouette Score |
| **Fraud Detection** | Highly imbalanced binary | Random Forest / Isolation Forest | ROC-AUC / Recall |

---

## 4. Phase Deliverable
**Project:** End-to-End ML Business Solution Notebook & Executive Pitch  
**Requirement:** Build a complete Python Machine Learning solution (`Jupyter Notebook` / `.py`):
1. Import dataset, perform Exploratory Data Analysis (EDA), missing value handling, and feature encoding.
2. Train and tune at least 2 distinct models (e.g., Logistic Regression vs. Random Forest).
3. Evaluate models using Confusion Matrix, Precision, Recall, $F_1$-Score, and ROC-AUC.
4. Author an **Executive Business Recommendation Brief**: Explain model results, business impact, and strategic deployment advice in non-technical stakeholder language.

---

## 5. Weekly Schedule & Action Plan

```
Week 18: ML Foundations, Workflow, & Data Preprocessing
├── Mon-Tue: AI/ML definitions, Supervised vs Unsupervised vs Reinforcement learning.
├── Wed-Thu: Data preprocessing: handling nulls, scaling, One-Hot Encoding (`scikit-learn`).
└── Fri-Sun: Train/Validation/Test splits, preventing data leakage, exploratory data analysis.

Week 19: Supervised Learning, Algorithms, & Metrics
├── Mon-Tue: Regression algorithms (Linear, Ridge) and metrics (MAE, RMSE, R²).
├── Wed-Thu: Classification algorithms (Logistic Regression, Decision Trees, Random Forest).
└── Fri-Sun: Classification metrics: Confusion Matrix, Precision, Recall, F1-Score, ROC-AUC.

Week 20: Model Optimization, Unsupervised Learning, & Deliverable
├── Mon-Tue: Bias-Variance trade-off, Hyperparameter tuning (GridSearchCV), K-Means clustering.
├── Wed-Thu: Translating technical metrics into business ROI for executives.
└── Fri-Sun: Complete Phase Deliverable (Python ML Project + Executive Brief).
```

---

## 6. WGU Competency Verification Checklist
- [ ] Can perform complete data preprocessing and feature engineering using `scikit-learn`.
- [ ] Can choose between Precision and Recall optimization based on business failure costs.
- [ ] Can explain over-fitting diagnostics using learning curves.
- [ ] Can present ML model predictions as business value to non-technical leaders.
