# Mảng data
import json

data = [{
    "fileName": "B5D5P6L9J574P8VDBK9LQG9Q9C2G903B.mp3",
    "agentChannel": 1,
    "time_load_info": 0.004342079162597656,
    "criterias_order": [],
    "context_analysis": {
        "searchInvalidKeyword": [
            {
                "raw_text": "mình đi vay tiền mà sao không có khả năng đóng là sao anh bảo hiểm nào chị vậy",
                "keywords": [],
                "index": 10,
                "channel": 1,
                "text": "ủa cái khoản vay của anh ở bên fe sao chưa ra thanh toán vậy lý do vì sao vậy anh mình đi vay tiền mà sao không có khả năng đóng là sao anh bảo hiểm nào chị vậy hả nãy giờ anh mới là người nói chuyện mất dạy á chứ không phải em đâu",
                "intent": "impolite",
                "intents": [
                    "impolite"
                ]
            }
        ]
    },
    "searchInvalidKeyword": {
        "evaluate": "yes",
        "evaluate_channel": {
            "1": "yes",
            "2": "no"
        },
        "decision_position": [
            {
                "raw_text": "mình đi vay tiền mà sao không có khả năng đóng là sao anh bảo hiểm nào chị vậy",
                "keywords": [],
                "index": 10,
                "channel": 1,
                "text": "ủa cái khoản vay của anh ở bên fe sao chưa ra thanh toán vậy lý do vì sao vậy anh mình đi vay tiền mà sao không có khả năng đóng là sao anh bảo hiểm nào chị vậy hả nãy giờ anh mới là người nói chuyện mất dạy á chứ không phải em đâu",
                "intent": "impolite",
                "intents": [
                    "impolite"
                ]
            }
        ],
        "decision": "yes",
        "confidence": 1.0,
        "confidence_channel": {
            "1": 1.0,
            "2": 0.0
        }
    }
}]

# Mảng transcript
transcript = [{
    "name": "B5D5P6L9J574P8VDBK9LQG9Q9C2G903B.mp3",
    "agentChannel": 1,
    "content": [
        {
            "channel": 2,
            "text": "alo"
        },
        {
            "channel": 1,
            "text": "ờ alo cho hỏi phải số của mai thanh không anh"
        }
    ],
    "metadata": {
        "duration": "130532",
        "accessgroups": "[\"/COLL/FIELD/LATE-CALL-SUP/TEAM_LOAN_B2_LATE CALL\"]",
        "BUCKET_OR_REGION": "B4B6",
        "GSW_CAMPAIGN_NAME": "COL_EC1_AG04_PEGA_CAMPAIGN",
        "USER_GENESYS": "voyvi",
        "startTime": "2024-11-28T09:10:58.000+0000",
        "LINE_MANAGER_1_TEAMLEADER": "Bùi Quốc Thành",
        "id": "B5D5P6L9J574P8VDBK9LQG9Q9C2G903B",
        "username": "voyvi"
    }
}]
# Kiểm tra và gán BUCKET_OR_REGION từ transcript vào data nếu trùng fileName và name
for item_data in data:
    for item_transcript in transcript:
        if item_data["fileName"] == item_transcript["name"]:
            item_data["BUCKET_OR_REGION"] = item_transcript["metadata"]["BUCKET_OR_REGION"]

# In kết quả
data = json.dumps(item_data, ensure_ascii=False, indent=2)
print(data)
