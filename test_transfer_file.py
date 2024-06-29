import pandas as pd

# Đọc file Excel
excel_file = 'C:/Users/Admin/Downloads/data_test.xlsx'
df = pd.read_excel(excel_file)

# Chuyển đổi DataFrame sang định dạng JSON
json_data = df.to_json(orient='records')

# Lưu dữ liệu JSON vào file
with open('output_file.json', 'w') as json_file:
    data = json_file.write(json_data)
print(data)