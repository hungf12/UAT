import re
import json

with open('keywords_sentiment 4.json', 'r', encoding='utf-8') as file:
    keywords = json.load(file)

with open('fec_clx_887_clean.json','r',encoding='utf-8') as f:
    data = json.load(f)



'''
keywords = [
    "cái lồn mẹ mày",
    "sao không chửi nữa",
    "xàm",
    "ngu học",
    "câm cái mõm lại",
    "có đầu óc suy nghĩ không",
    "thằng điên",
    "óc trâu",
    "chém hộ",
    "phát ngôn ra dơ",
    "hãm lờ",
    "thằng cha mày",
    "chó cái",
    "cút cái đĩ mẹ mày",
    "ngu",
]
'''

sentence = "nguyễn văn a sao ngu"

# Tìm và so sánh các từ khóa
matched_keywords = []
for keyword in keywords:
    if re.search(r'\b' + re.escape(keyword) + r'\b', sentence):
        matched_keywords.append(keyword)

# Kết quả
print("Keywords found:", matched_keywords)
