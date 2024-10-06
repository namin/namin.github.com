```python
import pandas as pd
from sklearn.model_selection import KFold
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import numpy as np

# Load the data
train_df = pd.read_csv('./input/train.csv')
test_df = pd.read_csv('./input/test.csv')

# Feature engineering: Convert MSSubClass to categorical
train_df['MSSubClass'] = train_df['MSSubClass'].astype(str)
test_df['MSSubClass'] = test_df['MSSubClass'].astype(str)

# Drop the Id column from both datasets
train_df.drop(columns=['Id'], inplace=True)
test_df.drop(columns=['Id'], inplace=True)

# Split into features and target variable
X = train_df.drop(columns=['SalePrice'])
y = np.log1p(train_df['SalePrice'])

# KFold cross-validation
kf = KFold(n_splits=5, shuffle=True, random_state=42)
oof_predictions = np.zeros(len(X))
test_predictions = np.zeros((len(test_df), 5))

for fold_idx, (train_idx, valid_idx) in enumerate(kf.split(X)):
    X_train, y_train = X.iloc[train_idx], y.iloc[train_idx]
    X_valid, y_valid = X.iloc[valid_idx], y.iloc[valid_idx]
    
    # Model training
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Validation and test predictions
    oof_predictions[valid_idx] = model.predict(X_valid)
    test_predictions[:, fold_idx] = model.predict(test_df)

# Compute the final OOF score
oof_score = np.sqrt(mean_squared_error(y, oof_predictions))
print(f'OOF Score: {oof_score:.4f}')

# Save test predictions to submission.csv
test_df['SalePrice'] = np.expm1(np.mean(test_predictions, axis=1))
submission_df = pd.DataFrame({'Id': test_df.Id, 'SalePrice': test_df.SalePrice})
submission_df.to_csv('./working/submission.csv', index=False)
```