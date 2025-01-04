import  math

# a = input()
# b = list(map(int, a.split()))
#
# avg = sum(b)/len(b)
#
# round_avg = round(avg, 1)
# print(round_avg)

#tính chu vi & diện tích tam giác
# a = input()
# b= list(map(float, a.split()))
# cv = sum(b)
# p= cv/2
# c = [p - i for i in b]
#
# tich = 1
# for j in c:
#     tich *= j
#
# s= math.sqrt(p * tich)
# round_s = round(s, 3)
# print(f"{cv} {round_s}")


#tính diện tích tam giác
# a= input()
# b= list(map(float, a.split()))
#
# s1 = 1
# for i in b:
#     s1 *= i
# s = s1/2
# round_s = round(s,3)
#
# print(round_s)

#tính bán kinh R đường tròn ngoại tiếp
# a = int(input())
# b = int(input())
# c = int(input())
#
# #tính nửa chu vi tam giác và diện tích
# p = (a + b+ c) / 2
# s_abc = math.sqrt(p*(p-a)*(p-b)*(p-c))
# print(f"{p} {c}")
# #tính bán kinh
#
# r = (a * b * c) / (4 * s_abc)
#
# round_r =  round(r, 3)
#
# print(round_r)

# tính điểm trung bình
# a = float(input())
# b = float(input())
# c = float(input())
#
# diem_toan = a * 2
# diem_van = b * 2
#
# avg_point = (diem_toan + diem_van + c) / 5
#
# round_avg = round(avg_point,1)
#
# print(round_avg)

# chia táo
# a = int(input())
# b = int(input())
#
# c1, c2 = divmod(a,b)
#
# print(f"{c1} {c2}")

#tính giờ phút giây
# a= int(input())
#
# hour = a // 3600
#
# minute = (a % 3600) // 60
#
# s = (a % 3600) % 60
#
# print(f"{hour}:{minute}:{s}")

# nhập số có 3 chữ số in ra hai chữ số đầu và 2 chữ số cuối
# a = int(input())
# if 100 <= abs(a) <= 999:
#     b1 = f"{a:03}"
#     a1 = b1[:2]
#     a2 = b1[1:]
#     # a1 = a // 10
#     # a2 = a % 100
# else:
#     a1 = a2 = None
#
# print(f"{a1} {a2}")


#tìm số lớn nhất trong 3 số
# a = input()
# b = list(map(int, a.split()))
#
# print(max(b))

#tính tuổi
# a = int(input())
# if 0 < a <= 150:
#     if 0 < a <= 11:
#         print("thiếu nhi")
#     elif 11 < a <= 25:
#         print("thiếu niên")
#     elif 25 < a <= 50:
#         print("trung niên")
#     else:
#         print("người già")
# else:
#     print("tuổi không nằm trong khoảng từ 0 đến 150")


#kiểm tra a,b,c có là cạnh của tam giác
# a = int(input())
# b = int(input())
# c = int(input())
#
# a1 = a + b
# a2 = a + c
# a3 = b + c
#
# if a3 > a and a2 > b and a1 > c:
#     p = (a + b + c)
#     s_abc = math.sqrt(p*(p-a)*(p-b)*(p-c))
#     print(f"{p} {s_abc}")
# else:
#     print("không phải 3 cạnh tam giác")

#tính điểm trung bình cả năm

# a = float(input())
# b = float(input())
#
# avg = (a + (b * 2)) /3
# round_avg = round(avg, 2)
#
# if round_avg >= 8:
#     print("giỏi")
# elif 6.5 <= round_avg < 8:
#     print("khá")
# elif 5.0 <= round_avg < 6.5:
#     print("trung bình")
# elif 3.5 <= round_avg < 5:
#     print("Yếu")
# else:
#     print("kém")

#tính mà trong năm

# a= int(input())
# if 1 <= a <= 12:
#     if a in [1, 2, 3]:
#         print("Mùa xuân")
#     elif a in [4, 5, 6]:
#         print("Mùa hạ")
#     elif a in [7, 8, 9]:
#         print("mùa thu")
#     else:
#         print("mùa đông")
# else:
#     print("tháng không hợp lệ")

# thang = int(input())
# nam = int(input())
#
# #check năm nhuận
# # if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
# #     if thang in [4, 6, 9, 11]:
# #         print("tháng có 30 ngày")
# #     elif thang in [1, 3, 5, 7, 8, 10, 12]:
# #         print("tháng có 31 ngày")
# #     elif thang in [2]:
# #         print("tháng có 29 ngày")
# # else:
# #     if thang in [4, 6, 9, 11]:
# #         print("tháng có 30 ngày")
# #     elif thang in [1, 3, 5, 7, 8, 10, 12]:
# #         print("tháng có 31 ngày")
# #     elif thang in [2]:
# #         print("tháng có 28 ngày")


# Dãy số
# number = int(input())
# mod = 10
# tong_day_so = sum(int(digit) for digit in str(number))
# nut = tong_day_so % mod
#
# if nut == 9:
#     print("số may mắn")
# else:
#     print("số không may mắn")

# đổi tiền
# a = int(input())
# b = a // 5000
# a %= 5000
# c = a // 2000
# a %= 2000
# d = a // 1000
#
# print(f"{b} {c} {d}")

#tính tiền taxi

# a = int(input())
#
# default_price = 12000
#
# if a == 1:
#     price = default_price
# elif 2 <= a <= 30:
#     price = default_price + (a-1) * 10000
# else:
#     price = default_price + 29 * 10000 + (a - 30) * 9000
#
# print(price)

#tính số điện
# a = int(input())
#
# if 0 < a <= 50:
#     price = a * 600
# elif 50 < a <= 100:
#     price = 50 * 600 + (a - 50) * 800
# elif 100 < a <= 200:
#     price = 50 * 600 + 50 * 800 + (a - 50 - 50) * 1100
# else:
#     price = 50 * 600 + 50 * 800 + 100 * 1100 + (a - 50 - 50 - 100) * 1500
#
# print(price)

# #tìm số chia hết cho 3
# a = int(input())
# for i in range(1, a+1):
#     if i % 3 == 0:
#         count = i // 3
# print(count)

#tính tổng sổ chẵn
# a = int(input())
# b = []
# for i in range(1, a+1):
#     if i % 2 == 0:
#         b.append(i)
# result = sum(b)
# print(result)

# #tính tổng các số chia hết cho 3 và 5 & 3 hoặc 5
# a = int(input())
# b = []
# for i in range(1, a +1):
#     if i % 3 ==0 or i % 5 == 0:
#         b.append(i)
# result = sum(b)
# print(result)

# #đếm n có bao nhiêu ước
# a = int(input())
# dem = 0
# for i in range(1, a+1):
#     if a % i == 0:
#         dem += 1
# print(dem)

#kiểm tra số nguyên tố
# a = int(input())
# dem = 0
# for i in range (1, a+1):
#     if a % i ==0:
#         dem += 1
# if dem == 2:
#     print(f"Yes")
# else:
#     print(f"No")

#tính tổng các số từ a đén b
# a = int(input())
# b = int(input())
# m, n = map(int, input("").split())
# c = []
# if m < n:
#     for i in range(m, n+1):
#         c.append(i)
# result = sum(c)
# print(result)

#đếm số chia hết cho 3 trong khoảng từ m đến n
# m, n = map(int, input("").split())
# dem = 0
# if m < n:
#     for i in range(m, n+1):
#         if i % 3 == 0:
#             dem += 1
# print(dem)

# # đếm số chia hết cho 3 hoặc 5 và tính tổng các số chắn
# m, n = map(int, input("").split())
# dem = 0
# c = []
# if m < n:
#     for i in range(m, n+1):
#         if i % 3 == 0 or i % 5 == 0:
#             dem += 1
#         if i % 2 == 0:
#             c.append(i)
# result = sum(c)
# print(f"{dem} {result}")

#đếm số nguyên tố từ m đến n
# def so_nguyen_to(a):
#     if a < 2:
#         return False
#     for i in range(2, int(math.sqrt(a))+1):
#         if a % i == 0:
#             return False
#     return True
#
#
# m, n = map(int, input("").split())
# dem = 0
# for i in range(m, n+1):
#     if so_nguyen_to(i):
#         dem += 1
# print(dem)

#in các số nguyên tố trong đoạn m đến n
# def so_nguyen_to(a):
#     if a < 2:
#         return False
#     for i in range(2, int(math.sqrt(a))+1):
#         if a % i == 0:
#             return False
#     return True
#
#
# m, n = map(int, input("").split())
# dem = 0
# c = []
# for i in range(m, n+1):
#     if so_nguyen_to(i):
#         c.append(i)
# print(" ".join(map(str, c)))

#tính trung bình cộng các số nguyên tố
# def so_nguyen_to(a):
#     if a < 2:
#         return False
#     for i in range(2, int(math.sqrt(a))+1):
#         if a % i == 0:
#             return False
#     return True
#
#
# m, n = map(int, input("").split())
# dem = 0
# c = []
# for i in range(m, n+1):
#     if so_nguyen_to(i):
#         dem += 1
#         c.append(i)
# result = sum(c)
# avg = result / dem
# round_avg = round(avg, 2)
# print(round_avg)

#tìm UCLN của s số a và b
# a, b = map(int, input("").split())
# while b != 0:
#     a, b = b, a % b
# print(abs(a))

#rút gon phân số
# def rut_gon (a, b):
#     def tim_ucln(x, y):
#         while y:
#             x, y = y, x % y
#         return x
#     ucln = tim_ucln(a, b)
#     a = a // ucln
#     b = b // ucln
#     return a, b
#
# a, b = map(int, input("").split())
# tu, mau = rut_gon(a, b)
# print(f"{tu}/{mau}")

#in ra n số nguyên tố
import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

k = int(input())
count = 0
n = 2      
prime_numbers = []
while count < k:
    if is_prime(n):
        prime_numbers.append(n)
        count += 1
    n += 1

print(f"{' '.join(map(str, prime_numbers))}")
