import tkinter as tk
from tkinter import ttk

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Dropdown Menu")

# Tạo biến để lưu giá trị lựa chọn
selected_option = tk.StringVar()

# Tạo danh sách các lựa chọn cho dropdown
options = ["Lựa chọn 1", "Lựa chọn 2", "Lựa chọn 3", "Lựa chọn 4"]

# Tạo widget dropdown (Combobox)
dropdown = ttk.Combobox(root, textvariable=selected_option, values=options)

# Đặt giá trị mặc định
dropdown.current(0)

# Đặt vị trí dropdown trên cửa sổ
dropdown.pack(pady=10)

# Hàm để hiển thị lựa chọn khi người dùng chọn giá trị từ dropdown
def show_selection():
    print("Bạn đã chọn:", selected_option.get())

# Tạo nút để in lựa chọn
button = ttk.Button(root, text="Xác nhận", command=show_selection)
button.pack(pady=10)

# Chạy chương trình
root.mainloop()
