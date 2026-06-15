# =========================
# main.py
# =========================

from src.preprocess import load_and_preprocess
from src.model_1 import train_model_lr
from src.model_2 import train_model_rf

from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

import matplotlib.pyplot as plt
import seaborn as sns

# =========================
# LOAD DATA
# =========================

X_train, X_test, y_train, y_test = load_and_preprocess()

# =====================================================
# LOGISTIC REGRESSION
# =====================================================

print("\n" + "="*50)
print("LOGISTIC REGRESSION")
print("="*50)

lr_model = train_model_lr(
    X_train,
    y_train
)

lr_pred = lr_model.predict(
    X_test
)

lr_acc = accuracy_score(
    y_test,
    lr_pred
)

print(f"\nAccuracy: {lr_acc:.4f}")

print("\nClassification Report:")

print(
    classification_report(
        y_test,
        lr_pred
    )
)

# =====================================================
# RANDOM FOREST
# =====================================================

print("\n" + "="*50)
print("RANDOM FOREST")
print("="*50)

rf_model = train_model_rf(
    X_train,
    y_train
)

rf_pred = rf_model.predict(
    X_test
)

rf_acc = accuracy_score(
    y_test,
    rf_pred
)

print(f"\nAccuracy: {rf_acc:.4f}")

print("\nClassification Report:")

print(
    classification_report(
        y_test,
        rf_pred
    )
)

# =====================================================
# FINAL COMPARISON
# =====================================================

print("\n" + "="*50)
print("MODEL COMPARISON")
print("="*50)

print(f"Logistic Regression Accuracy : {lr_acc:.4f}")
print(f"Random Forest Accuracy       : {rf_acc:.4f}")

if rf_acc > lr_acc:
    print("\n✅ Random Forest performed better.")
elif lr_acc > rf_acc:
    print("\n✅ Logistic Regression performed better.")
else:
    print("\n✅ Both models achieved the same accuracy.")

# =====================================================
# CONFUSION MATRIX - LR
# =====================================================

cm_lr = confusion_matrix(
    y_test,
    lr_pred
)

plt.figure(figsize=(6,5))

sns.heatmap(
    cm_lr,
    annot=True,
    fmt='d',
    cmap='Blues'
)

plt.title("Logistic Regression")
plt.xlabel("Predicted")
plt.ylabel("Actual")

plt.show()

# =====================================================
# CONFUSION MATRIX - RF
# =====================================================

cm_rf = confusion_matrix(
    y_test,
    rf_pred
)

plt.figure(figsize=(6,5))

sns.heatmap(
    cm_rf,
    annot=True,
    fmt='d',
    cmap='Greens'
)

plt.title("Random Forest")
plt.xlabel("Predicted")
plt.ylabel("Actual")

plt.show()

# =====================================================
# PROFESSIONAL ACCURACY COMPARISON
# =====================================================

models = [
    "Logistic Regression",
    "Random Forest"
]

accuracies = [
    lr_acc * 100,
    rf_acc * 100
]

plt.figure(figsize=(8, 5))

bars = plt.bar(
    models,
    accuracies,
    color=['orange', 'green']
)

plt.title(
    "Accuracy Comparison of Detection Models"
)

plt.ylabel(
    "Accuracy (%)"
)

plt.ylim(80, 101)

for bar in bars:

    yval = bar.get_height()

    plt.text(
        bar.get_x() + bar.get_width()/2,
        yval + 0.1,
        f"{yval:.2f}%",
        ha='center'
    )

plt.grid(
    axis='y',
    linestyle='--',
    alpha=0.7
)

plt.show()