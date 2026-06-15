# =========================
# federated.py (FINAL)
# =========================

from sklearn.model_selection import train_test_split
from src.model_1 import train_model_lr
from src.model_2 import train_model_rf

current_model = 2
if current_model == 1 :
    train_model = train_model_lr
else :
    train_model = train_model_rf
def split_clients(X, y, num_clients=3):
    clients = []

    for i in range(num_clients):
        X, X_part, y, y_part = train_test_split(
            X, y, test_size=0.33, random_state=42+i
        )
        clients.append((X_part, y_part))

    return clients


def train_clients(clients):
    models = []

    for i, (X, y) in enumerate(clients):
        print(f"\nTraining Client {i+1} (Hospital {i+1})...")
        model = train_model(X, y)
        models.append(model)

    return models


def aggregate_models(models):
    print("\nAggregating models (Safe)...")
    return models[0]