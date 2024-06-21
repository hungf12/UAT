# List of content
content = [
    {"channel": 2, "text": "alo"},
    {"channel": 1, "text": "sao mà ngu học"},
    {"channel": 2, "text": "dạ ừ"},
    {"channel": 1, "text": "dạ em chào chị em gọi đến cho mình từ công ty tài chính fe có khoản vay của mình á chị 2151000 á có gì chiều mình ghé thế giới di động điện máy xanh bách hóa xanh mình năm mười phút là thanh toán giúp em nha để bên em ghi nhận lịch sử thanh toán tốt á sau này vay vốn trả góp cho nó cũng được ưu tiên và lãi suất cũng như có chương trình"}
]

# List of keywords
keywords = [
    {"key": "cái lồn mẹ mày"},
    {"key": "sao không chửi nữa"},
    {"key": "xàm"},
    {"key": "ngu học"},
    {"key": "câm cái mõm lại"},
    {"key": "có đầu óc suy nghĩ không"}
]

# Extract keywords
keyword_list = [keyword["key"] for keyword in keywords]

# Check for matches in channel 1
matches = []
for item in content:
    if item["channel"] == 1:
        for keyword in keyword_list:
            if keyword in item["text"]:
                matches.append((item["text"], keyword))

# Print the matches
print("Matches found:", matches)
