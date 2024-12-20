# Danh sách từ khóa và chuỗi văn bản
kw = ["đụ", "đụ má", "đụ má mày", "đụ mẹ"]
text = "chửi cái đụ mẹ mày"

# Sắp xếp danh sách từ khóa theo độ dài giảm dần
kw_sorted = sorted(kw, key=len, reverse=True)

# Tìm kiếm từ khóa dài nhất xuất hiện trong chuỗi
found_keyword = next((keyword for keyword in kw_sorted if keyword in text), None)

# Kiểm tra kết quả
if found_keyword:
    print("Từ khóa được tìm thấy:", found_keyword)
else:
    print("Không có từ khóa nào trong chuỗi.")
