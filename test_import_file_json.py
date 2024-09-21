import json
import os

# List of JSON files to read
#json_folder = 'C:/Users/Admin/Downloads/1726815685803-json/1726815685803-json'  # Folder containing JSON files
json_folder = input("file_path: ")
json_files = [f for f in os.listdir(json_folder) if f.endswith('.json')]

# Initialize an empty list to hold the merged data
merged_data = []

# Loop through each file and load its content
for json_file in json_files:
    file_path = os.path.join(json_folder, json_file)

    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        # If each JSON file contains a list of objects, extend the main list
        if isinstance(data, list):
            merged_data.extend(data)
        else:
            merged_data.append(data)

# Write the merged data to a new JSON file
output_file = 'C:/Users/Admin/Downloads/test/merged_file.json'
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(merged_data, f, indent=4, ensure_ascii=False)

print(f"Data from {len(json_files)} files has been merged into {output_file}")
