import json
import re

# Load JSON data from files
with open('fec_clx_500_clean.json', 'r', encoding='utf-8') as file:
    data_file = json.load(file)

with open('keywords_sentiment 3.json', 'r', encoding='utf-8') as file:
    keyword_file = json.load(file)

# Initialize an empty list to store the results
results = []

# Function to check for keywords and extract surrounding text
def check_keywords(data_file, keyword_file):
    for call in data_file:
        content = call["content"]
        for i, entry in enumerate(content):
            text = entry["text"]
            # Check if any keyword is present in the text
            for keyword in keyword_file:
                if re.search(r'\b' + re.escape(keyword) + r'\b', text):
                    # Extract surrounding context: two lines before and two lines after
                    start = max(0, i - 2)
                    end = min(len(content), i + 3)
                    surrounding_text = " ".join([content[j]['text'] for j in range(start, end)])
                    results.append({
                        "file": call["name"],
                        "keyword": keyword,
                        "content_text": surrounding_text
                    })
    return results

# Check for keywords in the data file
result = check_keywords(data_file, keyword_file)

# Print results
for r in result:
    print(f"File: {r['file']}")
    print(f"Keyword: {r['keyword']}")
    print(f"Content:  {r['content_text']}")
    print("-" * 40)

# Optionally, write the results to a JSON file
with open('results.json', 'w', encoding='utf-8') as file:
    json.dump(result, file, ensure_ascii=False, indent=4)
