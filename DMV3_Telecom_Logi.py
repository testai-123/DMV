# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

df = pd.read_csv("DMV3.csv")

print("Dataset Structure:")
print(df.info())
print("\nDataset Preview:")
print(df.head())

df.fillna(0, inplace=True)  # Fill missing values with the column mean (for numerical columns)

df.drop_duplicates(inplace=True)

df['Dependents'] = df['Dependents'].str.lower()

df['PhoneService'] = df['PhoneService'].apply(lambda x: True if x == 'Yes' else False)

from scipy import stats
z_scores = stats.zscore(df['MonthlyCharges'])
outliers_mask = (z_scores > 3) | (z_scores < -3)
df = df[~outliers_mask]  # Remove rows with outliers

df['TotalChargesPerMonth'] = df['TotalCharges'] / df['MonthlyCharges']

scaler = StandardScaler()
df[['MonthlyCharges', 'TotalCharges']] = scaler.fit_transform(df[['MonthlyCharges', 'TotalCharges']])

X = df.drop('Churn', axis=1)  # Features (excluding target column 'Churn')
y = df['Churn']  # Target variable

X = pd.get_dummies(X,drop_first=True)  # One-hot encode categorical columns

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

df.to_csv('Cleaned_Telecom_Customer_Churn.csv', index=False)

model = LogisticRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)

# Print results
print(f'Accuracy: {accuracy * 100:.2f}%')
print('Confusion Matrix:')
print(conf_matrix)
