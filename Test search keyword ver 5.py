import json
import re
# Define the data file and keyword file as provided
'''
data_file = [
    {
        "name": "R7QO3PU3BH4C15LAKVHOR5I70O0MKN4D.mp3",
        "agentChannel": 1,
        "content": [
            {"channel": 1, "text": "dạ alo"},
            {"channel": 2, "text": "alo"},
            {"channel": 1, "text": "alo dạ alo anh thịnh nghe máy đúng không ạ"},
            {"channel": 2, "text": "à rồi anh nghe đây"},
            {"channel": 1, "text": "chào anh em gọi từ bên fe á anh thịnh"},
            {"channel": 2, "text": "đúng rồi em"},
            {"channel": 1, "text": "cái khoản vay tiền mặt của anh bên fe 3004000 đó anh"},
            {"channel": 2, "text": "ừ"},
            {"channel": 1, "text": "dạ không biết là hôm trước ngân hàng có gọi thông báo nè anh đóng chưa anh thịnh"},
            {"channel": 2, "text": "chưa chắc sáng mai anh ra anh đóng đó em"},
            {"channel": 1, "text": "hôm nay là mình có lương có tiền đóng chưa ạ"},
            {"channel": 2, "text": "chưa em sáng mai bắt đầu anh mới có lương thì sáng mai ra anh đóng luôn"},
            {"channel": 1, "text": "dạ anh ơi có gì anh tranh thủ sắp xếp hôm nay mình ghé mình đóng luôn đi anh mượn đỡ người thân thanh toán nợ trước đi anh thịnh tại vì ngân hàng cũng dựa trên lịch sử thanh toán của anh đánh giá hồ sơ này mới gọi thông báo cho anh tranh thủ đóng á"},
            {"channel": 2, "text": "ừ"},
            {"channel": 1, "text": "đánh giá hồ sơ tốt nó cũng là quyền lợi sau này của anh mà sau này anh vay mượn cũng dễ lãi suất cũng đỡ hơn cho mình nữa"},
            {"channel": 2, "text": "ok ok anh biết rồi"},
            {"channel": 2, "text": "rồi"},
            {"channel": 1, "text": "dạ vậy có gì anh tranh thủ hôm nay sắp xếp mình ghé mình đóng luôn anh nha dạ thì chiều nếu mà chiều chiều thì anh cố gắng tra thử trước 3 giờ cũng được đó anh thịnh"},
            {"channel": 2, "text": "ờ"},
            {"channel": 1, "text": "tại vì ngân hàng cũng dựa trên lịch sử thanh toán của anh đánh giá hồ sơ thôi cho mình tranh thủ đóng đi anh đánh giá hồ sơ tốt nó cũng là quyền lợi sau này của mình đó anh"},
            {"channel": 2, "text": "rồi anh biết rồi"},
            {"channel": 1, "text": "dạ rồi vậy em ghi nhận anh nha cố gắng tranh thủ là hôm nay dạ vậy sau 3 giờ ngày gọi xác nhận nha chào anh ạ"}
        ],
        "metadata": {
            "duration": "63260",
            "accessgroups": "[\"/COLL/EC/SUP_PD/TEAM_PD_10\"]",
            "BUCKET_OR_REGION": "PREDUE",
            "agentId": "26096",
            "GSW_CAMPAIGN_NAME": "COL_PREDUE_PEGA_CAMPAIGN",
            "USER_GENESYS": "nguyenthithuthao36",
            "startTime": "2024-05-13T01:46:40.000+0000",
            "LINE_MANAGER_1_TEAMLEADER": "Tạ Thị Mỹ Nhiên",
            "id": "R7QO3PU3BH4C15LAKVHOR5I70O0MKN4D",
            "username": "nguyenthithuthao36"
        }
    },
    {
        "name": "R7QO3PU3BH4C15LAKVHOR5I70O0MKLMG.mp3",
        "agentChannel": 1,
        "content": [
            {"channel": 2, "text": "alo"},
            {"channel": 1, "text": "rồi chị tú anh đúng không"},
            {"channel": 2, "text": "ừ"},
            {"channel": 1, "text": "chào chị em gọi từ fe nè thằng điên hợp đồng tiền mặt kỳ tháng 5 của chị 2774000 đến hạn rồi 10 giờ sáng nay gấp rút ra thanh toán liền nha chị anh bữa giờ sao không thấy đóng tiền chị để cải thiện hồ sơ tháng trước cũng đóng trễ rồi"},
            {"channel": 2, "text": "à ráng giùm chị ngày mai được không em"},
            {"channel": 1, "text": "dạ không được đâu chị ngân hàng hỗ trợ tháng vừa rồi rồi bây giờ tháng này đang trùng với đợt đánh giá lịch sử tín dụng của toàn bộ khách hàng á chị muốn vay lại được hay không thì chị gấp rút xoay tiền ra đóng liền trước 11 giờ trưa nay mới kịp nha để mất uy tín sau này chị khó vay lãi cho công ty tài chính bất kỳ á chị là người chịu thiệt đúng không không có tiền vô ít nhất cũng 2 ngày mới xử lý tiền thành công rồi bên em mới nhận được tiền của chị đó sau 48 giờ chị có thể tham gia chương trình vòng may mắn được rỡ hóa đơn 500000 chỉ có 1 lượt quay miễn phí đảm bảo 11 giờ em gọi lại có biên lai đóng tiền nha cuộc gọi được ghi âm xin phép gác máy"}
        ],
        "metadata": {
            "duration": "55703",
            "accessgroups": "[\"/COLL/EC/SUP_PD/TEAM_PD_01\"]",
            "BUCKET_OR_REGION": "PREDUE",
            "agentId": "26077",
            "GSW_CAMPAIGN_NAME": "COL_PREDUE_PEGA_CAMPAIGN",
            "USER_GENESYS": "lethithuytrang26",
            "startTime": "2024-05-13T01:46:07.000+0000",
            "LINE_MANAGER_1_TEAMLEADER": "Trương Thị Kim Hương",
            "id": "R7QO3PU3BH4C15LAKVHOR5I70O0MKLMG",
            "username": "lethithuytrang26"
        }
    }
]

# Define keyword file
keyword_file = [
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
    "khùng hả",
    "cho bà con chòm xóm",
    "láu cá"
]
'''
# Load JSON data from files
with open('fec_clx_500_clean.json', 'r', encoding='utf-8') as file:
    data_file = json.load(file)

with open('keywords_sentiment 3.json', 'r', encoding='utf-8') as file:
    keyword_file = json.load(file)

# Function to check data file with keywords and create full sentences around the keyword if found
def check_data_file(data, keywords):
    results = []
    for entry in data:
        agent_channel = entry["agentChannel"]
        content = entry["content"]
        for i, line in enumerate(content):
            if line["channel"] == agent_channel:
                text = line["text"]
                for keyword in keywords:
                    if re.search(r'\b' + re.escape(keyword) + r'\b', text):
                        # Extract surrounding sentences for context
                        start = max(i - 2, 0)
                        end = min(i + 3, len(content))
                        surrounding_text = " ".join([content[j]["text"] for j in range(start, end)])
                        results.append({"file": entry["name"], "keyword": keyword, "context": surrounding_text})
    return results

# Call the function with the data file and keyword file
keyword_occurrences = check_data_file(data_file, keyword_file)
print(f"log{keyword_occurrences}")

for r in keyword_occurrences:
    print(f"File: {r['file']}")
    print(f"Keyword: {r['keyword']}")
    print(f"Content:  {r['context']}")
    print("-" * 40)


# Optionally, write the results to a JSON file
with open('Result keyword.json', 'w', encoding='utf-8') as file:
    json.dump(keyword_occurrences, file, ensure_ascii=False, indent=4)