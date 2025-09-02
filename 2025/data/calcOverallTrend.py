import pandas as pd

# Load the dataset
df = pd.read_csv("/Users/prazeina/Documents/repos/RS/2025/data/testData/2025 - Rank -Level.csv")

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
frequency_df.to_csv("/Users/prazeina/Documents/repos/RS/2025/data/result/Rank_2025OverallTrend.csv")

# ------------------------------------------------------------------------------------------------------------------------------------------------

# Load the dataset
file_path = "/Users/prazeina/Documents/repos/RS/2025/data/testData/2025 - Confidence Level.csv" 
df = pd.read_csv(file_path)

# Define the categories and the columns that we need to calculate the mean for (based on your original request)
category_ranges = {
    'Career & Self Development': df.columns[1:6],  # Columns B-F
    'Communication': df.columns[6:10],  # Columns G-J
    'Critical Thinking/Problem Solving': df.columns[10:14],  # Columns K-N
    'Promoting a Welcoming Culture': df.columns[14:17],  # Columns O-Q
    'Leadership': df.columns[17:21],  # Columns R-U
    'Professionalism/ Work Ethic': df.columns[21:27],  # Columns V-AA
    'Teamwork': df.columns[27:31],  # Columns AB-AE
    'Technology': df.columns[31:36]  # Columns AF-AJ
}

# Extract the rating rows (Excellent, Very Good, Good, etc.)
ratings = ['Excellent', 'Very Good', 'Good', 'Fair', 'Poor']

# Create an empty DataFrame to store the results
result_df = pd.DataFrame()

# Add the original rating columns to the result_df
result_df['Skill'] = category_ranges.keys()

# Iterate through each category to calculate the mean and frequency counts
for category, columns in category_ranges.items():
    # Select the relevant columns for the current category
    selected_columns = df[columns]
    
    # Count the frequency of each rating (Excellent, Very Good, etc.)
    frequency_counts = selected_columns.apply(pd.Series.value_counts).fillna(0).astype(int)
    
    # Reorder the columns to match the ratings (Excellent, Very Good, Good, Fair, Poor)
    frequency_counts = frequency_counts.T[ratings].sum(axis=1)
    
    # Add the calculated frequency counts and mean to the result DataFrame
    result_df[category] = frequency_counts

# Calculate the mean for each category (Career & Self Development, Communication, etc.)
result_df['Mean'] = result_df.drop(columns=['Skill']).mean(axis=1)

# Save the new data with calculated means to a new CSV file
result_df.to_csv('/Users/prazeina/Documents/repos/RS/2025/data/result/Confidence_2025OverallTrend.csv', index=False)

