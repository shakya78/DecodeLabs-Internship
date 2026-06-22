
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
    precision_score,
    recall_score,
    f1_score,
    ConfusionMatrixDisplay
)

# ==========================
# STEP 1 : LOAD DATASET
# ==========================

iris = load_iris()

X = iris.data
y = iris.target

print("\n========== DATASET INFORMATION ==========")

print("Total Samples :", len(X))

print("Total Features :", X.shape[1])

print("Flower Classes :", iris.target_names)

# ==========================
# STEP 2 : TRAIN TEST SPLIT
# ==========================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    shuffle=True
)

print("\nDataset Split Completed")

# ==========================
# STEP 3 : FEATURE SCALING
# ==========================

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)

X_test = scaler.transform(X_test)

print("Scaling Completed")

# ==========================
# STEP 4 : KNN MODEL
# ==========================

model = KNeighborsClassifier(
    n_neighbors=5
)

model.fit(
    X_train,
    y_train
)

print("Model Training Completed")

# ==========================
# STEP 5 : PREDICTION
# ==========================

y_pred = model.predict(
    X_test
)

# ==========================
# STEP 6 : METRICS
# ==========================

accuracy = accuracy_score(
    y_test,
    y_pred
)

precision = precision_score(
    y_test,
    y_pred,
    average="weighted"
)

recall = recall_score(
    y_test,
    y_pred,
    average="weighted"
)

f1 = f1_score(
    y_test,
    y_pred,
    average="weighted"
)

print("\n========== RESULTS ==========")

print(f"Accuracy  : {accuracy*100:.2f}%")

print(f"Precision : {precision*100:.2f}%")

print(f"Recall    : {recall*100:.2f}%")

print(f"F1 Score  : {f1*100:.2f}%")

print("\n========== REPORT ==========")

print(
    classification_report(
        y_test,
        y_pred,
        target_names=iris.target_names
    )
)

# ==========================
# GRAPH 1
# METRICS BAR CHART
# ==========================

metrics = [
    "Accuracy",
    "Precision",
    "Recall",
    "F1"
]

scores = [
    accuracy*100,
    precision*100,
    recall*100,
    f1*100
]

plt.figure(figsize=(7,5))

plt.bar(
    metrics,
    scores
)

plt.title(
    "Model Performance"
)

plt.ylabel(
    "Percentage"
)

plt.ylim(
    0,
    100
)

plt.show()

# ==========================
# GRAPH 2
# CONFUSION MATRIX
# ==========================

cm = confusion_matrix(
    y_test,
    y_pred
)

plt.figure(figsize=(6,6))

disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=iris.target_names
)

disp.plot()

plt.title(
    "Confusion Matrix"
)

plt.show()

# ==========================
# GRAPH 3
# IRIS FEATURE SCATTER
# ==========================

plt.figure(figsize=(7,5))

plt.scatter(
    X[:,0],
    X[:,2]
)

plt.xlabel(
    "Sepal Length"
)

plt.ylabel(
    "Petal Length"
)

plt.title(
    "Iris Flower Distribution"
)

plt.show()

# ==========================
# GRAPH 4
# K VALUE VS ACCURACY
# ==========================

k_values = []

accuracies = []

for k in range(1,21):

    temp_model = KNeighborsClassifier(
        n_neighbors=k
    )

    temp_model.fit(
        X_train,
        y_train
    )

    temp_pred = temp_model.predict(
        X_test
    )

    temp_accuracy = accuracy_score(
        y_test,
        temp_pred
    )

    k_values.append(k)

    accuracies.append(
        temp_accuracy*100
    )

plt.figure(figsize=(8,5))

plt.plot(
    k_values,
    accuracies
)

plt.xlabel(
    "K Value"
)

plt.ylabel(
    "Accuracy (%)"
)

plt.title(
    "K Value vs Accuracy"
)

plt.grid()

plt.show()

print("\nProject Completed Successfully ✅")