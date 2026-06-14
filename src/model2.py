# =========================
# model.py (FINAL HIGH ACCURACY)
# =========================

from xgboost import XGBClassifier
import numpy as np

def train_model(X, y):

    # Fix labels
    unique_classes = np.unique(y)
    class_mapping = {cls: idx for idx, cls in enumerate(unique_classes)}
    y_mapped = np.array([class_mapping[val] for val in y])

    model = XGBClassifier(
        n_estimators=700,
        max_depth=14,
        learning_rate=0.02,
        subsample=0.9,
        colsample_bytree=0.9,
        gamma=0.2,
        reg_lambda=1.5,
        min_child_weight=3,
        eval_metric='mlogloss',
        random_state=42
    )

    model.fit(X, y_mapped)

    model.class_mapping = class_mapping

    return model