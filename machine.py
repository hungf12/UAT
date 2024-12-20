import json

# Dữ liệu đầu vào
data = [
    "ăn cơm hay ăn",
    "con kia",
    "âm mưu lừa đảo",
    "âm mưu trốn nợ",
    "ăn của người ta",
    "ăn dốc nói láo",
    "ăn gì tôi cúng",
    "ăn gì tui cúng",
    "ăn giựt tiền",
    "ăn quỵt tiền"
]

# Các bucket
buckets = ["Predue", "B0 Promo", "B1NEW"]

# Tạo JSON array hai chiều
result = []

for bucket in buckets:
    bucket_data = {
        "bucket": bucket,
        "items": data
    }
    result.append(bucket_data)

# Chuyển đổi thành JSON
json_result = json.dumps(result, ensure_ascii=False, indent=2)

# In kết quả
print(json_result)
