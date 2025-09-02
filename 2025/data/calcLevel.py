import pandas as pd

# Load the gender-based ranking data
df = pd.read_csv('/Users/prazeina/Documents/repos/RS/2025/data/testData/2025 - Rank -Level.csv')

# Get list of skill columns (all except the last column 'Gender')
skill_columns = df.columns[:-1]

# Calculate frequency counts for each ranking (1-5) per skill, separated by Gender
gender_rank_freq = {}

for gender in ['G', 'U']:
    gender_df = df[df['Level'] == gender]
    freq_table = {}

    for skill in skill_columns:
        # Get the frequency count for each ranking (1-5) in this skill
        freq = gender_df[skill].value_counts().sort_index()
        # Get the frequency count for each ranking (1-5) in this skill
        freq.index = freq.index.astype(int)  
        freq_table[skill] = freq

    gender_rank_freq[gender] = pd.DataFrame(freq_table).fillna(0).astype(int)

# Save the results in separate CSV files for Female and Male
gender_rank_freq['G'].to_csv('/Users/prazeina/Documents/repos/RS/2025/data/result/graduate_ranking_frequency.csv', index=True)
gender_rank_freq['U'].to_csv('/Users/prazeina/Documents/repos/RS/2025/data/result/undergradaute_ranking_frequency.csv', index=True)

# ------------------------------------------------------------------------------------------------------------------------------------------------

# Load the dataset
file_path = "/Users/prazeina/Documents/repos/RS/2025/data/testData/2025 - Confidence Level.csv"  
df = pd.read_csv(file_path)

# Separate out the 'Level' column
level_col = 'Level'

# Filter rows for Level G and U separately
df_g = df[df[level_col] == 'G']
df_u = df[df[level_col] == 'U']

# Drop the 'Level' column to analyze only the skill ratings
df_g_skills = df_g.drop(columns=[level_col])
df_u_skills = df_u.drop(columns=[level_col])

# Calculate frequency counts for each skill for both levels
g_counts = df_g_skills.apply(lambda col: col.value_counts()).fillna(0).astype(int)
u_counts = df_u_skills.apply(lambda col: col.value_counts()).fillna(0).astype(int)

# Transpose for better readability
g_counts = g_counts
u_counts = u_counts

# Save the frequency counts to CSV
g_counts.to_csv('/Users/prazeina/Documents/repos/RS/2025/data/result/confidence_grad_frequency_counts.csv')
u_counts.to_csv('/Users/prazeina/Documents/repos/RS/2025/data/result/confidence_undergrad_frequency_counts.csv')

# ------------------------------------------------------------------------------------------------------------------------------------------------

# Load the dataset
file_path = "/Users/prazeina/Documents/repos/RS/2025/data/result/confidence_grad_frequency_counts.csv" 
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

# Keep the original ratings columns (Excellent, Very Good, Good, Fair, Poor)
rating_columns = ['Unnamed: 0'] + list(df.columns[1:])  # Including rating columns

# Create an empty DataFrame to store the results
result_df = pd.DataFrame()

# Add the original rating columns to the result_df
result_df['Rating'] = df['Unnamed: 0']  # Rating (Excellent, Very Good, etc.)

# Calculate the mean for each category and store it in the result_df
for category, columns in category_ranges.items():
    # Calculate the mean of the selected columns
    mean_values = df[columns].mean(axis=1)
    
    # Store the result in the new DataFrame with the given category name
    result_df[category] = mean_values

# Save the new data with calculated means to a new CSV file
result_df.to_csv('/Users/prazeina/Documents/repos/RS/2025/data/result/grad_processed_mean_values.csv', index=False)

# ------------------------------------------------------------------------------------------------------------------------------------------------

# Load the dataset
file_path = "/Users/prazeina/Documents/repos/RS/2025/data/result/confidence_undergrad_frequency_counts.csv" 
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

# Keep the original ratings columns (Excellent, Very Good, Good, Fair, Poor)
rating_columns = ['Unnamed: 0'] + list(df.columns[1:])  # Including rating columns

# Create an empty DataFrame to store the results
result_df = pd.DataFrame()

# Add the original rating columns to the result_df
result_df['Rating'] = df['Unnamed: 0']  # Rating (Excellent, Very Good, etc.)

# Calculate the mean for each category and store it in the result_df
for category, columns in category_ranges.items():
    # Calculate the mean of the selected columns
    mean_values = df[columns].mean(axis=1)
    
    # Store the result in the new DataFrame with the given category name
    result_df[category] = mean_values

# Save the new data with calculated means to a new CSV file
result_df.to_csv('/Users/prazeina/Documents/repos/RS/2025/data/result/undergrad_processed_mean_values.csv', index=False)

