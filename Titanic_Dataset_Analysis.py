import pandas as pd

# Step 1: Loading Data
file_path = '/Users/macbook_files/Visual Studio Codes/Practice Environments/Python Active Projects/test.csv.xls'  # Change this to your dataset's path
data = pd.read_csv(file_path)

# Step 2: Data Inspection
print("First 5 rows of the dataset:")
print(data.head())

print("\nDataset Information:")
print(data.info())

print("\nSummary Statistics:")
print(data.describe())

# Step 3: Data Selection
selected_columns = ['Survived', 'Sex', 'Age', 'Fare']
data_selected = data[selected_columns]

print("\nSelected Columns:")
print(data_selected.head())

# Step 4: Filtering [Filter passengers who are female and survived]
female_survivors = data_selected[(data_selected['Sex'] == 'female') & (data_selected['Survived'] == 1)]

print("\nFemale Survivors:")
print(female_survivors.head())

# Step 5: Handling Missing Data [Checking for missing values]
print("\nMissing Data Before Handling:")
print(data_selected.isnull().sum())

# Filling missing 'Age' values with median age
data_selected['Age'].fillna(data_selected['Age'].median(), inplace=True)

# Dropping rows with any remaining missing values
data_cleaned = data_selected.dropna()

print("\nMissing Data After Handling:")
print(data_cleaned.isnull().sum())

# Step 6: Save the cleaned data
data_cleaned.to_csv('cleaned_titanic_data.csv', index=False)
print("\nCleaned data saved successfully as 'cleaned_titanic_data.csv'.")
