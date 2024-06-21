# chỗ này là chạy tools như qq

import json

# Path to the JSON Transcript file
file_path = 'C:/Users/Admin/Downloads/FEC_CLX/transcript/fec_clx_887_clean.json'

# Read the JSON Transcript file
with open(file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

# Path to the JSON Data KeyWord Motivation file
file_path_motivation = 'C:/Users/Admin/Downloads/FEC_CLX/transcript/keywords_sentiment 3.json'
# Read the JSON Data KeyWord Motivation file
with open(file_path_motivation, 'r', encoding='utf-8') as file:
    json_data = json.load(file)



''''
# Define the content list and keywords list
content = [
    {"channel": 2, "text": "alo"},
    {"channel": 1, "text": "ngu học"},
    {"channel": 2, "text": "dạ ừ"},
    {"channel": 1, "text": "dạ em chào chị em gọi đến cho mình từ công ty tài chính fe có khoản vay của mình á chị 2151000 á có gì chiều mình ghé thế giới di động điện máy xanh bách hóa xanh mình năm mười phút là thanh toán giúp em nha để bên em ghi nhận lịch sử thanh toán tốt á sau này vay vốn trả góp cho nó cũng được ưu tiên và lãi suất cũng như có chương trình"}
]

keywords = [
    "cái lồn mẹ mày",
    "sao không chửi nữa",
    "xàm",
    "ngu học",
    "câm cái mõm lại",
    "có đầu óc suy nghĩ không"
]
'''

def check_audio_file_content(audio_id):
    for audio in data:
        if audio['name'] == audio_id:
            return audio['content']
    return None

# Check content for the specified audio file
#audio_id = "R7QO3PU3BH4C15LAKVHOR5I70O0RG3GL.mp3"
audio_id = input("Audio input: ")
content = check_audio_file_content(audio_id)

if content == None:
    status = False
else:
    status = True

if status == True:
    # Extract texts where "channel" is 1
    channel_1_texts = [entry['text'] for entry in content if entry['channel'] == 1]

    # Check if any keyword is in the extracted texts
    matches = {text: [keyword for keyword in json_data if keyword in text] for text in channel_1_texts}

    # Output the results
    for text, matched_keywords in matches.items():
        print(f"Samples: '{text}'")
        if matched_keywords:
            print(f"Violate keywords: {matched_keywords}")
        else:
            print("Contains no keywords")
        print()
else:
    print("Audio file does not exist")