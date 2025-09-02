import pandas as pd

# Load the dataset
df = pd.read_csv("/Users/prazeina/Documents/repos/RS/2024/data/testData/2024 - Rank-Level.csv")

# Exclude the last column (Gender) before counting frequencies
skill_columns = df.drop(columns=["Level"]).columns

# Count frequency of ratings 1 to 5 for each skill, excluding Gender column
frequency_df = pd.DataFrame()
for skill in skill_columns:
    counts = df[skill].value_counts().reindex([1, 2, 3, 4, 5], fill_value=0)
    frequency_df[skill] = counts

# Transpose for better format: skills as rows, ratings as columns
frequency_df = frequency_df.T
frequency_df.columns = ['1', '2', '3', '4', '5']

# Save to CSV
frequency_df.to_csv("/Users/prazeina/Documents/repos/RS/2024/data/result/Rank_2024OverallTrend.csv")

# ------------------------------------------------------------------------------------------------------------------------------------------------

import pandas as pd

# Load the dataset
df = pd.read_csv("/Users/prazeina/Documents/repos/RS/2024/data/testData/2024 - Confidence-Level.csv")

# Define a mapping for qualitative ratings to numeric values
rating_map = {
    "Poor": 5,
    "Fair": 4,
    "Good": 3,
    "Very Good": 2,
    "Excellent": 1
}

# Replace the qualitative ratings with numeric values
df_numeric = df.replace(rating_map)

# Exclude the 'Level' column for frequency count
skill_columns = df_numeric.drop(columns=["Level"]).columns

# Count frequency of ratings 1 to 5 for each skill
frequency_df = pd.DataFrame()
for skill in skill_columns:
    counts = df_numeric[skill].value_counts().reindex([1, 2, 3, 4, 5], fill_value=0)
    frequency_df[skill] = counts

# Transpose for better format: skills as rows, ratings as columns
frequency_df = frequency_df.T
frequency_df.columns = ['Excellent', 'Very Good', 'Good', 'Fair', 'Poor']

# Save to CSV
frequency_df.to_csv("/Users/prazeina/Documents/repos/RS/2024/data/result/Confidence_2024OverallTrend.csv")

