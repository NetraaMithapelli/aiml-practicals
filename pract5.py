# Practical 5 : Data Preprocessing and Exploratory Data Analysis

"""
Steps : 
1)Import libraries : pandas, matplotlib, model_selection, preprocessing, pipeline, compose, impute
2)Load dataset : remove duplicates, unused columns , missing target rows, separate target
3)Display dataset details , missing values info , Statistical Summary
4)Plot histograms and boxplots for numerical features
5)Split data into training and testing sets
6)Prepare numerical and categorical columns using imputation , scaling and encoding
7)Learn preparation data from training data and apply to both sides
8)Convert encoded output to regular arrays if needed
9)Show processed output, split sizes and remaining values

"""
# Import the required libraries.
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import make_pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder

# Download Titanic data, remove duplicates and unused columns, and separate target.
df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv")
df = df.drop_duplicates().drop(columns=["who", "adult_male", "alive"], errors="ignore")
df = df.dropna(subset=["survived"])
X, y = df.drop(columns="survived"), df["survived"]

# Show dataset details, missing values, and statistics.
print("Dataset shape:", df.shape)
print("\nData types:\n", df.dtypes)
print("\nMissing values before imputation:\n", X.isnull().sum())
print("\nStatistical summary:\n", df.describe(include="all").T)

# Plot histograms and boxplots for numerical features.
nums = X.select_dtypes(include="number").columns
X[nums].hist(figsize=(10, 7), bins=20, edgecolor="black")
plt.suptitle("Histograms of Numerical Features")
plt.tight_layout()
plt.show()

for col in nums:
    X.boxplot(column=col, vert=False)
    plt.title(f"Boxplot of {col}")
    plt.show()

# Split data into training and testing sets.
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Prepare numerical and categorical columns with imputation, scaling, and encoding.
num_cols = X_train.select_dtypes(include="number").columns
cat_cols = X_train.select_dtypes(exclude="number").columns

prep = ColumnTransformer([
    ("num", make_pipeline(SimpleImputer(strategy="median"), StandardScaler()), num_cols),
    ("cat", make_pipeline(SimpleImputer(strategy="most_frequent"),
                          OneHotEncoder(handle_unknown="ignore")), cat_cols)
])

# Learn preparation from training data and apply it to both sets.
X_train_processed = prep.fit_transform(X_train)
X_test_processed = prep.transform(X_test)

# Convert encoded output to regular arrays if needed.
if hasattr(X_train_processed, "toarray"):
    X_train_processed = X_train_processed.toarray()
if hasattr(X_test_processed, "toarray"):
    X_test_processed = X_test_processed.toarray()

# Show processed rows, split sizes, and remaining missing values.
print("\nFirst five processed training rows:")
display(pd.DataFrame(X_train_processed).head())
print("Training feature shape:", X_train_processed.shape)
print("Testing feature shape:", X_test_processed.shape)
print("Training target shape:", y_train.shape)
print("Testing target shape:", y_test.shape)
print("\nMissing values after preprocessing:")
print("Training:", pd.isna(X_train_processed).sum())
print("Testing:", pd.isna(X_test_processed).sum())