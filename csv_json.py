import pandas as pd

# Read the CSV file
df = pd.read_csv('dataset.csv')

# Convert to JSON and save as a valid JSON array
with open('dataset.json', 'w') as json_file:
    json_file.write('[')  # Start the JSON array
    df.to_json(json_file, orient='records', lines=True)
    json_file.seek(json_file.tell() - 1, 0)  # Move back to overwrite the last newline
    json_file.write(']')  # Close the JSON array
