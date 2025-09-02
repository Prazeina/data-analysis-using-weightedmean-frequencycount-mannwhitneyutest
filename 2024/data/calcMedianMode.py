import pandas as pd

# Load the dataset
df = pd.read_csv("/Users/prazeina/Documents/repos/RS/2024/data/testData/2024 - Rank-Gender.csv")

# Separate the dataset by gender
df_female = df[df["Gender"] == "F"]
df_male = df[df["Gender"] == "M"]

# Function to compute median and mode for each skill column
def compute_stats(group_df):
    median_vals = group_df.median(numeric_only=True)
    mode_vals = group_df.mode(numeric_only=True).iloc[0]  # Take the first mode in case of multiple
    return pd.DataFrame({"Median": median_vals, "Mode": mode_vals})

# Compute for females and males
female_stats = compute_stats(df_female)
male_stats = compute_stats(df_male)

# Combine into a single DataFrame for output
combined_stats = pd.concat([female_stats, male_stats], axis=1)
combined_stats.columns = ['Female_Median', 'Female_Mode', 'Male_Median', 'Male_Mode']

# Save to CSV
combined_stats.to_csv("/Users/prazeina/Documents/repos/RS/2024/data/result/GenderMMRank.csv")

# ------------------------------------------------------------------------------------------------------------------------------------------------

# Load the dataset
df = pd.read_csv("/Users/prazeina/Documents/repos/RS/2024/data/testData/2024 - Confidence-Gender.csv")

# Define a mapping for qualitative to numeric
rating_map = {
    "Poor": 5,
    "Fair": 4,
    "Good": 3,
    "Very Good": 2,
    "Excellent": 1
}

# Replace text with numeric values
df_numeric = df.replace(rating_map)

# Separate by gender
df_female = df_numeric[df_numeric["Gender"] == "F"]
df_male = df_numeric[df_numeric["Gender"] == "M"]

# Function to compute median and mode for each column
def compute_stats(group_df):
    median_vals = group_df.median(numeric_only=True)
    mode_vals = group_df.mode(numeric_only=True).iloc[0]
    return pd.DataFrame({"Median": median_vals, "Mode": mode_vals})

# Compute stats
female_stats = compute_stats(df_female)
male_stats = compute_stats(df_male)

# Combine results
combined_stats = pd.concat([female_stats, male_stats], axis=1)
combined_stats.columns = ['Female_Median', 'Female_Mode', 'Male_Median', 'Male_Mode']

# Save to CSV
combined_stats.to_csv("confidence_stats_by_gender.csv")


# Save to CSV
combined_stats.to_csv("/Users/prazeina/Documents/repos/RS/2024/data/result/GenderMMConfidence.csv")

# ---------------------------------------------------------------------------------------------------------------------------


# LEVEL

# Load the dataset
df = pd.read_csv("/Users/prazeina/Documents/repos/RS/2024/data/testData/2024 - Rank-Level.csv")

# Separate the dataset by gender
df_female = df[df["Level"] == "G"]
df_male = df[df["Level"] == "U"]

# Function to compute median and mode for each skill column
def compute_stats(group_df):
    median_vals = group_df.median(numeric_only=True)
    mode_vals = group_df.mode(numeric_only=True).iloc[0]  # Take the first mode in case of multiple
    return pd.DataFrame({"Median": median_vals, "Mode": mode_vals})

# Compute for females and males
female_stats = compute_stats(df_female)
male_stats = compute_stats(df_male)

# Combine into a single DataFrame for output
combined_stats = pd.concat([female_stats, male_stats], axis=1)
combined_stats.columns = ['Graduate_Median', 'Graduate_Mode', 'Undergraduate_Median', 'Undergraduate_Mode']

# Save to CSV
combined_stats.to_csv("/Users/prazeina/Documents/repos/RS/2024/data/result/LevelMMRank.csv")

# ------------------------------------------------------------------------------------------------------------------------------------------------

# Load the dataset
df = pd.read_csv("/Users/prazeina/Documents/repos/RS/2024/data/testData/2024 - Confidence-Level.csv")

# Define a mapping for qualitative to numeric
rating_map = {
    "Poor": 5,
    "Fair": 4,
    "Good": 3,
    "Very Good": 2,
    "Excellent": 1
}

# Replace text with numeric values
df_numeric = df.replace(rating_map)

# Separate by gender
df_female = df_numeric[df_numeric["Level"] == "G"]
df_male = df_numeric[df_numeric["Level"] == "U"]

# Function to compute median and mode for each column
def compute_stats(group_df):
    median_vals = group_df.median(numeric_only=True)
    mode_vals = group_df.mode(numeric_only=True).iloc[0]
    return pd.DataFrame({"Median": median_vals, "Mode": mode_vals})

# Compute stats
female_stats = compute_stats(df_female)
male_stats = compute_stats(df_male)

# Combine results
combined_stats = pd.concat([female_stats, male_stats], axis=1)
combined_stats.columns = ['Graduate_Median', 'Graduate_Mode', 'Undergraduate_Median', 'Undergraduate_Mode']

# Save to CSV
combined_stats.to_csv("confidence_stats_by_gender.csv")


# Save to CSV
combined_stats.to_csv("/Users/prazeina/Documents/repos/RS/2024/data/result/LevelMMConfidence.csv")
