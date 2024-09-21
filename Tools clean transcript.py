import json
import os
import pandas as pd
from pathlib import Path
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import re

def submit_info():
    base_folder = entry_base_folder.get()
    regex = r'^[a-zA-Z]:[\\\/]([^\\\/:*?"<>|]+[\\\/])*[^\\\/:*?"<>|]*$'
    if re.match(base_folder, regex):
        merged_data = []

        # Walk through all folders and subfolders
        for root, dirs, files in os.walk(base_folder):
            for file in files:
                if file.endswith('.json'):
                    file_path = os.path.join(root, file)
                    # Open and read each JSON file
                    with open(file_path, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                        # If the data is a list, extend the merged list, otherwise append
                        if isinstance(data, list):
                            merged_data.extend(data)
                        else:
                            merged_data.append(data)

        def clean_content(content):
            if len(content) == 0:
                return None
            content_df = pd.DataFrame(content)[["channel", "text"]]
            return content_df.to_dict("records")

        def clean_meta(metadata):
            metadata = eval(
                metadata.replace("true", "True")
                .replace("false", "False")
                .replace("null", "None")
            )["public"]
            return metadata

        # Write the merged data to a new JSON file
        path = Path(base_folder)
        file_name = path.name
        output_file = f'C:/Users/Admin/Downloads/test/{file_name}.json'
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(merged_data, f, indent=4, ensure_ascii=False)
        # print(f"Data from JSON files in multiple folders has been merged into {output_file}")

        if __name__ == "__main__":
            file_name = output_file
            data_call = pd.read_json(file_name)[["name", "agentChannel", "content", "metadata"]]

            data_call["content"] = data_call["content"].apply(clean_content)
            data_call["metadata"] = data_call["metadata"].apply(clean_meta)
            data_call.to_json(
                file_name.split(".")[0] + "_clean.json",
                orient="records",
                force_ascii=False,
                indent=2,
            )
        messagebox.showinfo("Successfully", f"Name Transcript: {file_name}")
        folder_path = 'C:/Users/Admin/Downloads/test'
        os.startfile(folder_path)
    else:
        messagebox.showerror("Error", "Invalid file path")

def exit_app():
    # Kiểm tra nếu tất cả các trường đều trống
    root.destroy()
    # if not entry_base_folder.get():
    #     root.destroy()  # Thoát chương trình
    # else:
    #     messagebox.showwarning("Warning", "Vui lòng hoàn tất thông tin hoặc xóa hết để thoát.")
def clear_text():
    if not entry_base_folder.get():
        messagebox.showwarning("Warning","File path is required")
    else:
        entry_base_folder.delete(0, tk.END)

# Tạo cửa sổ chính
root = tk.Tk()
root.geometry("400x300")
root.title("Format Clean Transcript")

# Tạo icon cho From nhập
icon_image = Image.open('logo-fpt-inkythuatso-1-01-01-14-33-35.jpg')
icon_photo = ImageTk.PhotoImage(icon_image)
root.iconphoto(False, icon_photo)


#Tạo background hình ảnh
background_image = Image.open('tri-tue-nhan-tao-ai-la-gi-cac-ung-dung-va-tiem-nan-11-800x450.jpg')
background_photo = ImageTk.PhotoImage(background_image)
background_label = tk.Label(root, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Tạo text bõ nhập file path
label_name = tk.Label(root, text="File path:")
label_name.grid(row=0, column=0, padx=10, pady=10)

entry_base_folder = tk.Entry(root)
entry_base_folder.grid(row=0, column=1, padx=10, pady=5)

# Tạo nút submit
btn_submit = tk.Button(root, text="Submit", command=submit_info)
btn_submit.grid(row=3, column=0, pady=5)

# Tạo nút thoát
btn_exit = tk.Button(root, text="Exit", command=exit_app)
btn_exit.grid(row=3, column=3, pady=5)

# Tạo nút thoát
btn_exit = tk.Button(root, text="Delete", command=clear_text)
btn_exit.grid(row=3, column=1, pady=5)

# Chạy ứng dụng
root.mainloop()
