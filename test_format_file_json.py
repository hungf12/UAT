import json
import os
import pandas as pd
from pathlib import Path

# Base folder containing subfolders with JSON files
#base_folder = 'C:/Users/Admin/Downloads/1726815685803-json'
base_folder = input("folder path: ")

# Initialize an empty list to hold the merged data
merged_data = []

# Walk through all folders and subfolders
for root, dirs, files in os.walk(base_folder):
    for file in files:
        if file.endswith('.json'):
            file_path = os.path.join(root, file)
            # Open and read each JSON file
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                # If the data is a list, extend the merged list, otherwise append
                if isinstance(data, list):
                    merged_data.extend(data)
                else:
                    merged_data.append(data)

def clean_content(content):
    if len(content) == 0:
        return None
    content_df = pd.DataFrame(content)[["channel", "text"]]
    return content_df.to_dict("records")

def clean_meta(metadata):
    metadata = eval(
        metadata.replace("true", "True")
        .replace("false", "False")
        .replace("null", "None")
    )["public"]
    return metadata

# Write the merged data to a new JSON file
path = Path(base_folder)
file_name = path.name
output_file = f'C:/Users/Admin/Downloads/test/{file_name}.json'
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(merged_data, f, indent=4, ensure_ascii=False)
#print(f"Data from JSON files in multiple folders has been merged into {output_file}")

if __name__ == "__main__":
    file_name = output_file
    data_call = pd.read_json(file_name)[["name", "agentChannel", "content", "metadata"]]

    data_call["content"] = data_call["content"].apply(clean_content)
    data_call["metadata"] = data_call["metadata"].apply(clean_meta)
    data_call.to_json(
        file_name.split(".")[0] + "_clean.json",
        orient="records",
        force_ascii=False,
        indent=2,
    )
