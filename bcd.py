#code này dùng để định dạng lại json để train bot
import json
# Đọc tệp JSON
with open('greetByeThankHCPA_09_08_output.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Đưa dữ liệu về dạng chuẩn (Pretty-printed JSON)
with open('formatted_file.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, indent=4, ensure_ascii=False)

print("formater successfully")
