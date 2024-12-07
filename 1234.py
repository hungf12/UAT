import pandas as pd
import numpy as np

# Tạo DataFrame từ bảng
data = {
    "EngineSize": [2.0, 2.4, 1.5, 3.5, 3.5, 3.5, 3.5, 3.7, 3.7, 2.4],
    "Cylinders": [4, 4, 4, 6, 6, 6, 6, 6, 6, 4],
    "FuelConsumption_COMB": [8.5, 9.6, 5.9, 11.1, 10.6, 10.0, 10.1, 11.1, 11.6, 9.2],
    "CO2Emissions": [196, 221, 136, 256, 244, 230, 232, 255, 267, None]  # Chưa biết giá trị cuối cùng
}

df = pd.DataFrame(data)

# Tính trung bình của các biến
means = df.mean(numeric_only=True)

print(means)

X = df[["EngineSize", "Cylinders", "FuelConsumption_COMB"]].values
y = df["CO2Emissions"].dropna().values.reshape(-1, 1)
# Thêm cột hệ số chặn (1) vào X
X_with_intercept = np.hstack((np.ones((len(y), 1)), X[:len(y)]))  # Chỉ lấy hàng có y hợp lệ

# Tính các hệ số hồi quy
beta = np.linalg.inv(X_with_intercept.T @ X_with_intercept) @ (X_with_intercept.T @ y)

# Tách hệ số chặn (b_0) và các hệ số hồi quy
b_0 = beta[0, 0]  # Hệ số chặn
coefficients = beta[1:].flatten()  # Hệ số của các biến độc lập

print(f"hệ số chặn: {b_0}")
print(f"hệ số các biến độc lập {coefficients}")

