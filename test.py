import json
def check_input(data, input_name):
    for record in data:
        if record['name'] == input_name:
            return record['content']
    return None
file_path = 'C:/Users/Admin/Downloads/FEC_TLS/Transcript/fec_tls_842_1_clean.json'

# Read the JSON Transcript file
with open(file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)
# Example input
input_name = int(input("Input Name: "))

# Check input and get content
result = check_input(data, input_name)
if result:
    print("Content:", result)
else:
    print("No matching record found.")
