import pandas as pd

# Load the gender-based ranking data
df = pd.read_csv('/Users/prazeina/Documents/repos/RS/2024/data/testData/2024 - Rank-Gender.csv')

# Get list of skill columns (all except the last column 'Gender')
skill_columns = df.columns[:-1]

# Calculate frequency counts for each ranking (1-5) per skill, separated by Gender
gender_rank_freq = {}

for gender in ['F', 'M']:
    gender_df = df[df['Gender'] == gender]
    freq_table = {}

    for skill in skill_columns:
        # Get the frequency count for each ranking (1-5) in this skill
        freq = gender_df[skill].value_counts().sort_index()
        # Get the frequency count for each ranking (1-5) in this skill
        freq.index = freq.index.astype(int)  
        freq_table[skill] = freq

    gender_rank_freq[gender] = pd.DataFrame(freq_table).fillna(0).astype(int)

# Save the results in separate CSV files for Female and Male
gender_rank_freq['F'].to_csv('/Users/prazeina/Documents/repos/RS/2024/data/result/female_ranking_frequency.csv', index=True)
gender_rank_freq['M'].to_csv('/Users/prazeina/Documents/repos/RS/2024/data/result/male_ranking_frequency.csv', index=True)

# ------------------------------------------------------------------------------------------------------------------------------------------

# Load the gender-based ranking data
df_confidence = pd.read_csv('/Users/prazeina/Documents/repos/RS/2024/data/testData/2024 - Confidence-Gender.csv')

# Define the custom order of rankings
rank_order = ['Excellent', 'Very Good', 'Good', 'Fair', 'Poor']

# Get list of skill columns for confidence data (all except the last column 'Gender')
skill_columns_confidence = df_confidence.columns[:-1]

# Calculate frequency counts for each ranking (1-5) per skill, separated by Gender for confidence data
gender_confidence_rank_freq = {}

for gender in ['F', 'M']:
    gender_df_confidence = df_confidence[df_confidence['Gender'] == gender]
    freq_table_confidence = {}

    for skill in skill_columns_confidence:
        # Get the frequency count for each ranking in this skill
        freq = gender_df_confidence[skill].value_counts()

        # Manually create a Series to ensure all rankings (1-5) appear, even if they're missing
        freq_with_all_ranks = pd.Series(0, index=rank_order)

        # Fill the existing ranks in the frequency table
        freq_with_all_ranks.update(freq)

        # Store frequency counts in the correct order
        freq_table_confidence[skill] = freq_with_all_ranks

    # Store the result for each gender in a separate DataFrame
    gender_confidence_rank_freq[gender] = pd.DataFrame(freq_table_confidence)

# Save the results in separate CSV files for Female and Male for confidence data
gender_confidence_rank_freq['F'].to_csv('/Users/prazeina/Documents/repos/RS/2024/data/result/female_confidence_frequency.csv', index=True)
gender_confidence_rank_freq['M'].to_csv('/Users/prazeina/Documents/repos/RS/2024/data/result/male_confidence_frequency.csv', index=True)

