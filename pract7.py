# Pract 7 : Classification using Logistic Regression and K-Nearest Neighbours

"""
Steps:
1)Import libraries
2)Load dataset
3)Display basic info
4)Split data into training and testing
5)Scale the measurement features b4 training
6)Train the models
7)Predictions for the test data
8)Results : Calculate and Compare Scores
9)Display Confusion matrix for both models

"""

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, ConfusionMatrixDisplay, classification_report


#Load dataset
dataset = load_breast_cancer(as_frame=True)
X = dataset.data
y = dataset.target

#Display basics
print("First five records : ")
print(X.head())

print("\nDataset Shape : ", X.shape)

print("\nClass Labels : ", dict(enumerate(dataset.target_names)))

print("\nMissing values : ", int(X.isnull().sum().sum()))

print("\nClass Distribution : ", y.value_counts().rename(index={0 : "malignant", 1: "benign"}))

#Split the data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42, stratify=y
)

#Scale measurements b4 training
logistic_model = make_pipeline(
    StandardScaler(),
    LogisticRegression(max_iter=5000, random_state=42)
)

knn_model = make_pipeline(
    StandardScaler(),
    KNeighborsClassifier(n_neighbors=5)
)

#Train both models
logistic_model.fit(X_train, y_train)
knn_model.fit(X_train, y_train)

#Predictions
y_pred_logistic = logistic_model.predict(X_test)
y_pred_knn = knn_model.predict(X_test)

models = {
    "Logistic Regression" : y_pred_logistic,
    "KNN (k=5) " : y_pred_knn
}

#Calculate and compare scores
results = []

for model_name, y_pred in models.items():
    results.append({
        "Model": model_name,
        "Accuracy Score " : accuracy_score(y_test, y_pred),
        "Precision Score " : precision_score(y_test, y_pred, zero_division = 0),
        "Recall Score " : recall_score(y_test, y_pred, zero_division = 0),
        "F1 Score " : f1_score(y_test, y_pred, zero_division = 0)
    })

results_df = pd.DataFrame(results)
print("\nPerformance Comparison : ")
print(results_df.round(4).to_string(index=False))

#Show confusion matrix
for model_name, y_pred in models.items():
    cm = confusion_matrix(y_test, y_pred, labels=[0,1])

    print(f"\nConfusion Matrix - {model_name}")
    print("\nClass order : malignant, benign")
    print(cm)

    display = ConfusionMatrixDisplay(
        confusion_matrix=cm,
        display_labels=dataset.target_names
    )

    display.plot(cmap="Greens", values_format="d")
    plt.title(f"Confusion Matrix - {model_name}")
    plt.tight_layout()
    plt.show()

#Claasification report
for model_name, y_pred in models.items():
    print(f"\nClassification Report - {model_name}")
    print(classification_report(y_test, y_pred, target_names=dataset.target_names, zero_division=0))

#Identify best model with high f1 score
best_idx = results_df["F1-Score"].idxmax()
print("\nModel with teh highest F1-score : " , results_df.loc[best_idx, "Model"])