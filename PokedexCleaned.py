import pandas as pd

# Load the dataset
df = pd.read_csv('pokedex_with_type_count.csv')

# --- 1. Split `type_clean` into `type1` and `type2` ---
df[['type1', 'type2']] = df['type_clean'].str.split(',', n=1, expand=True)

# Replace NaN in type2 (Mono types) with None
df['type2'] = df['type2'].where(df['type2'].notnull(), None)

# --- 2. Convert `type_count` to category ---
df['type_count'] = df['type_count'].astype('category')

# --- 3. Create binary classification column ---
df['is_dual_type'] = df['type_count'].apply(lambda x: 1 if x == 'Dual' else 0)

# --- 4. Save cleaned DataFrame to a new CSV ---
output_path = 'pokedex_cleaned.csv'
df.to_csv(output_path, index=False)

print(f"✅ Cleaned dataset saved to '{output_path}'")
