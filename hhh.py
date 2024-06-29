def extract_surrounding_text(keyword, data, context_size=3):
    result = []

    for record in data:
        content = record['content']
        for i, entry in enumerate(content):
            if keyword in entry['text']:
                start = max(0, i - context_size)
                end = min(len(content), i + context_size + 1)
                surrounding_text = content[start:end]
                result.append({
                    "name": record['name'],
                    "surrounding_text": surrounding_text
                })
                break  # Assuming one match per record for simplicity

    return result

# Example data
data = [
    {
        "name": 1228151252,
        "agentChannel": 1,
        "content": [
            {"channel": 2, "text": "alo"},
            {"channel": 1, "text": "alo à dạ cho em hỏi số này của chị trang đang nghe máy phải lừa đảo"},
            {"channel": 2, "text": "vâng"},
            {"channel": 2, "text": "à ờ có gì không em"},
            {"channel": 1, "text": "à dạ vâng em chờ chị cả em hiểu nhân viên của bên công ty tài chính vpbank smbc anh liên hệ với cái gì kệ nó chị trễ dạ thì em gọi để tránh trường hợp đồng đợt trước á mình có nhân viên bên em mà có hồ sơ trả góp đó là có 1 cái điện thoại samsung đó chị dạ cái này hiện tại thì bên em đang có chương trình tri ân đó"},
            {"channel": 2, "text": "ừ"},
            {"channel": 1, "text": "hỗ trợ chị được tham gia vay vốn tiêu dụng ạ em thấy kỳ này chị được hỗ trợ gói vay lên đến là 62000000 đồng nè thì có gì em tư vấn cho chị trễ mà nghe qua theo gói vay 1 xíu ha"},
            {"channel": 2, "text": "ừ thôi em khi nào chị chị kẹt rồi chị chị"},
            {"channel": 1, "text": "à"},
            {"channel": 2, "text": "chị hỏi chứ giờ chị nói chung là chị cũng không có làm gì hết cho nên cũng không có có hỏi chi nữa đâu em ha"},
            {"channel": 1, "text": "em thấy là hôm rồi mình cũng hay tham gia mua đồ trả góp cũng nhiều nè chừng nào đợt này chị có dự tính là mua đồ trả góp gì thêm nữa không"},
            {"channel": 2, "text": "ừ"},
            {"channel": 2, "text": "ừ à"},
            {"channel": 1, "text": "ti vi hoặc là xe máy tủ lạnh điện thoại gì không"},
            {"channel": 2, "text": "à không em"},
            {"channel": 2, "text": "nói chung là giờ còn xài mấy cái đó nhà chị có rồi khi nào có gì thiếu á chị xuống nha"},
            {"channel": 1, "text": "ừ nói nói chung thì đợt này"}
        ],
        "metadata": {
            "duration": "101344",
            "crmid": "1228151252",
            "uh": "Phạm Thị Mỹ Hằng",
            "code_sales": "TX006769",
            "full_name_tl": "Nguyễn Đăng Khoa",
            "code_tl": "TSA43086",
            "id": "JDOPPEVDTP0D5D1O6LV7E7NI3O1I3EL0",
            "username": "nguyenminhhieu15"
        }
    }
]

# Extracting 3 sentences before and after the keyword "lừa đảo"
keyword = "lừa đảo"
surrounding_text = extract_surrounding_text(keyword, data)

# Display the result
print(surrounding_text)
