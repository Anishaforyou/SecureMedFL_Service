# =========================
# main.py (FINAL COMPLETE)
# =========================

from src.preprocess import load_and_preprocess
from src.model_1 import train_model_xg
from src.model_2 import train_model_rf
from src.federated import split_clients, train_clients, aggregate_models
from src.blockchain import create_hash, add_block
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import classification_report

current_model = 2
# =========================
# STEP 1: Load Data
# =========================
X_train, X_test, y_train, y_test = load_and_preprocess()

# =========================
# 🔥 STEP 2: GLOBAL MODEL
# =========================
print("\n🔥 Training Global Model...")
if current_model == 1 :
    train_model = train_model_xg
else :
    train_model = train_model_rf
global_direct_model = train_model(X_train, y_train)

# 🔥 GLOBAL MODEL PREDICTION (ADD HERE)
if current_model == 1 :
    inv_map_global = {v: k for k, v in global_direct_model.class_mapping.items()}

    y_pred_raw_global = global_direct_model.predict(X_test)
    y_pred_global = [inv_map_global[val] for val in y_pred_raw_global]
else :
    y_pred_global = global_direct_model.predict(X_test)

print("🔥 Global Model Accuracy:", accuracy_score(y_test, y_pred_global))

print("\n📊 Classification Report - Global Model")
print(classification_report(y_test, y_pred_global))

# =========================
# CONFUSION MATRIX (GLOBAL)
# =========================

cm = confusion_matrix(y_test, y_pred_global)

plt.figure(figsize=(6,5))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')

plt.title("Confusion Matrix - Global Model")
plt.xlabel("Predicted")
plt.ylabel("Actual")

plt.show()

# =========================
# STEP 3: FEDERATED LEARNING
# =========================
clients = split_clients(X_train, y_train)

models = train_clients(clients)

# =========================
# STEP 4: BLOCKCHAIN
# =========================
print("\n--- Blockchain Logging ---")
for model in models:
    h = create_hash(model)
    add_block(h)

# =========================
# STEP 5: AGGREGATION
# =========================
global_model = aggregate_models(models)

# 🔥 FEDERATED MODEL PREDICTION (ADD HERE)
if current_model == 1 :
    inv_map_fed = {v: k for k, v in global_model.class_mapping.items()}

    y_pred_raw_fed = global_model.predict(X_test)
    y_pred_fed = [inv_map_fed[val] for val in y_pred_raw_fed]
else :
    y_pred_fed = global_model.predict(X_test)

print("\nFederated Model Accuracy:", accuracy_score(y_test, y_pred_fed))

print("\n📊 Classification Report - Federated Model")
print(classification_report(y_test, y_pred_fed))

# =========================
# CONFUSION MATRIX (FEDERATED)
# =========================

cm_fed = confusion_matrix(y_test, y_pred_fed)

plt.figure(figsize=(6,5))
sns.heatmap(cm_fed, annot=True, fmt='d', cmap='Greens')

plt.title("Confusion Matrix - Federated Model")
plt.xlabel("Predicted")
plt.ylabel("Actual")

plt.show()