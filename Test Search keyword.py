import json
# Define the JSON structure and keywords to check

data = {
    "name": "R7QO3PU3BH4C15LAKVHOR5I70O0QS9LL.mp3",
    "agentChannel": 1,
    "content": [
        {"channel": 2, "text": "alo"},
        {"channel": 1, "text": "alo dạ em chào anh ạ anh dư nghe máy đúng không anh"},
        {"channel": 2, "text": "đụ má"},
        {"channel": 2, "text": "dạ"},
        {"channel": 1, "text": "anh như ơi"},
        {"channel": 1, "text": "nghe máy trả lời giúp em nha"},
        {"channel": 2, "text": "ừ nghe"},
        {"channel": 1, "text": "sao mà nghe máy không trả lời vậy anh"},
        {"channel": 2, "text": "số điện thoại"},
        {"channel": 1, "text": "alo"},
        {"channel": 2, "text": "vâng biết rồi"},
        {"channel": 1, "text": "anh dư ơi mình có quen biết hay liên hệ được qua cho anh sang không anh báo anh sang ra thanh toán tiền góp giùm em nha"},
        {"channel": 2, "text": "ừ"},
        {"channel": 1, "text": "alo"},
        {"channel": 2, "text": "để"},
        {"channel": 2, "text": "alo"},
        {"channel": 2, "text": "ừ"},
        {"channel": 2, "text": "ấy"},
        {"channel": 2, "text": "hả"},
        {"channel": 1, "text": "nghe máy trả lời giùm em đi anh ơi"},
        {"channel": 2, "text": "nữa"},
        {"channel": 1, "text": "alo"},
        {"channel": 2, "text": "trả"}
    ],
}

'''
with open('keywords_sentiment 4.json', 'r', encoding='utf-8') as file:
    keywords = json.load(file)

data = []
with open('fec_clx_887_clean.json', 'w', encoding='utf-8') as f:
    json.dump(data, f)

'''
keywords = ["đụ má", "ngu"]

# Initialize an empty list to store results
results = []

# Loop through the content to find keywords and add surrounding context
for item in data:
    for i, entry in enumerate(data["content"]):
        if any(kw in entry["text"] for kw in keywords):
            # Collect two previous, current, and two next entries if available
            start = max(0, i - 2)
            end = min(len(data["content"]), i + 3)
            surrounding_text = [data["content"][j]["text"] for j in range(start, end)]
            results.append(surrounding_text)


print(results)
'''
out_put = " ".join(results[0])
print(out_put)
'''


