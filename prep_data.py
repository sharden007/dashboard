import pandas as pd

# Read the CSV file
df = pd.read_csv('dataset.csv')

# Convert to JSON and save as a valid JSON array
with open('dataset.json', 'w') as json_file:
    # Convert DataFrame to JSON string with records orientation
    json_data = df.to_json(orient='records', lines=False)
    
    # Ensure proper formatting by wrapping in square brackets
    json_file.write(f"[{json_data[1:-1]}]")  # Remove outer braces and wrap in brackets
