import os
import tkinter as tk
from tkinter import ttk

def list_files_in_directory(directory):
    """Liệt kê các tệp trong thư mục."""
    try:
        return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    except FileNotFoundError:
        return []

def on_select(event):
    """Hàm xử lý khi chọn một tệp từ dropdown."""
    selected_file = dropdown_var.get()
    label_result.config(text=f"Bạn đã chọn: {selected_file}")

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Danh sách tệp")

# Thư mục cần đọc
directory = "C:/Users/Admin/Downloads/FEC_CLX/Units test"  # Thư mục hiện tại
files = list_files_in_directory(directory)

# Tạo biến cho dropdown
dropdown_var = tk.StringVar()
dropdown_var.set("Chọn một tệp")  # Giá trị mặc định

# Tạo dropdown
dropdown = ttk.OptionMenu(root, dropdown_var, *files, command=on_select)
dropdown.pack(pady=10)

# Hiển thị kết quả lựa chọn
label_result = tk.Label(root, text="")
label_result.pack(pady=10)

# Chạy giao diện
root.mainloop()
