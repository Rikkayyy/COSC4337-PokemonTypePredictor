import pandas as pd

# Load the data
df = pd.read_csv('pokedex.csv')

# Clean up the 'type' column (remove curly braces and split by comma)
df['type_clean'] = df['type'].str.strip('{}')

# Create a new column to determine Mono or Dual based on the number of types
df['type_count'] = df['type_clean'].apply(lambda x: 'Dual' if ',' in x else 'Mono')

# Save the updated DataFrame
df.to_csv('pokedex_with_type_count.csv', index=False)

