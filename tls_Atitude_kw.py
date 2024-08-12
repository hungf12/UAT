# chỗ này là chạy tools như qq

import json
import  re

# Path to the JSON Transcript file
file_path = 'C:/Users/Admin/Downloads/FEC_TLS/Transcript/fec_tls_842_1_clean.json'

# Read the JSON Transcript file
with open(file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

# Path to the JSON Data KeyWord Motivation file
file_path_motivation = 'C:/Users/Admin/Downloads/FEC_TLS/Transcript/Data_Atitude_kw.json'
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
audio_id = int (input("Audio input: "))
content = check_audio_file_content(audio_id)

if content == None:
    status = False
else:
    status = True
#print(status)

if status == True:
    def find_matching_sentences(content, keywords):
        matching_sentences = []
        for entry in content:
            if entry['channel'] == 1:
                text = entry['text']
                for keyword in keywords:
                    if keyword['key'] in text:
                        matching_sentences.append(
                            {'sentence': text, 'bucket': keyword['Bucket'], 'key': keyword['key']})
        return matching_sentences


    matches = find_matching_sentences(content, json_data)
    for item in matches:
        print(f"Samples: {item['sentence']}")
        print(f"Bucket: {item['bucket']}")
        print(f"Keyword: {item['key']}")
        print("----")

else:
    print("Audio file does not exist")
