def divide_and_format(numerator, denominator):
    try:
        result = numerator / denominator
        formatted_result = "{:.2f}".format(result)
        return formatted_result
    except ZeroDivisionError:
        return "Độ chính xác trên case No: 100%"

# Ví dụ
numerator = 1
denominator = 0
print(divide_and_format(numerator, denominator))  # Kết quả: Error: Division by zero

numerator = 5
denominator = 2
print(divide_and_format(numerator, denominator))  # Kết quả: 2.50
