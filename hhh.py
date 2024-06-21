import json

# Path to the JSON Transcript file
file_path = 'C:/Users/Admin/Downloads/FEC_CLX/transcript/fec_clx_500_clean.json'

# Read the JSON Transcript file
with open(file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

# Path to the JSON Data KeyWord Motivation file
file_path_motivation = 'C:/Users/Admin/Downloads/FEC_CLX/transcript/data_kw_motivation.json'
# Read the JSON Data KeyWord Motivation file
with open(file_path_motivation, 'r', encoding='utf-8') as file:
    json_data = json.load(file)

# Print the contents of the JSON file
#print(data)


def check_audio_file_content(audio_id):
    for audio in data:
        if audio['name'] == audio_id:
            return audio['content']
    return None

# Check content for the specified audio file
#audio_id = "R7QO3PU3BH4C15LAKVHOR5I70O0RG3GL.mp3"
audio_id = input("Audio input: ")
content = check_audio_file_content(audio_id)
# check file audio có tồn tại không
#print(content)

'''
keyword = "thanh toán"
def find_keyword_sentences(content, keyword):
    sentences_with_keyword = [entry['text'] for entry in content if keyword in entry['text']]
    return sentences_with_keyword
sentences = find_keyword_sentences(content, keyword)
'''
'''
json_data = [
    {"Bucket": "motivation_b1bom", "key": "thanh toán"},
    {"Bucket": "motivation_b1bom", "key": "đi vay khó"},
    {"Bucket": "motivation_b1bom", "key": "khó đi vay đi mượn mua đồ trả góp"}
]
'''

def check_text_for_keywords(text, keywords):
    #a= "khôn tìm thấy"
    for keyword_obj in keywords:
        keyword = keyword_obj['key']
        bucket = keyword_obj['Bucket']
        if keyword in text:
            return f"Text: {text}  \nBucket: {bucket}  \nKeyword: {keyword}"
    return None


# Function to iterate through JSON data and check content against keywords (lặp để tìm câu chứa từ khóa tìm được)
def process_json_data(json_data, content):
    results = []
    for item in content:
        text = item['text']
        result = check_text_for_keywords(text, json_data)
        if result:
            results.append(result)
    return results
#

if content == None:
    status = "Không tìm thấy file Audio"
    results = ""
else:
    status = "Thành công"
    results = process_json_data(json_data, content)


for point in results:
    print(f"Trạng thái: {status}  \nKết quả: {point}")
