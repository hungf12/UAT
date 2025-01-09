import math

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
# a = input()
# b = list(map(float, a.split()))
#
# s1 = 1
# for i in b:
#     s1 *= i
# s = s1/2
# round_s = round(s, 3)
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

#tìm số chia hết cho 3
# a = int(input())
# dem = 0
# for i in range(1, a+1):
#     if i % 3 == 0:
#         dem += 1
# print(dem)

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

#tính tổng các số từ m đén n
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
# import math
#
# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(math.sqrt(num)) + 1):
#         if num % i == 0:
#             return False
#     return True
#
# k = int(input())
# count = 0
# n = 2
# prime_numbers = []
# while count < k:
#     if is_prime(n):
#         prime_numbers.append(n)
#         count += 1
#     n += 1
#
# print(f"{' '.join(map(str, prime_numbers))}")
# kiểm tra số chính phương
# n = int(input())
# if n < 0:
#     result = 0
# else:
#     b = int(math.sqrt(n))
#     if b * b == n:
#         print("Yes")
#     else:
#         print("No")

# def ktra_chinh_phuong(n):
#     cp = int(math.sqrt(n))
#     return cp * cp == n
# n = int(input())
# c = ktra_chinh_phuong(n)
# print(c)
#in ra k số chính phương đầu tiên
# kiểm tra số chính phương
# def ktra_chinh_phuong(n):
#     cp = int(math.sqrt(n))
#     return cp * cp == n
#
# def in_so_cp(k):
#     sum_result = []
#     a = 0
#     while len(sum_result) < k:
#         if ktra_chinh_phuong(a):
#             sum_result.append(a)
#         a += 1
#     return sum_result
#
#
# k = int(input())
# print(in_so_cp(k))

#tạo mảng n phần tử tính tổng các phần tử trong mảng
# a = int(input())
# n = []
# for i in range(a):
#     arr = int(input(i+1))
#     n.append(arr)
# tong = sum(n)
# print(tong)

# đếm số dương trong mảng
# a = int(input())
# n = []
# for i in range(a):
#     arr = int(input(i+1))
#     n.append(arr)
# dem = 0
# for j in n:
#     if j > 0:
#         dem += 1
#
# print(dem)

# đếm số chẵn trong mảng
# a = int(input())
# n = []
#
# for i in range(a):
#     arr = int(input(i+1))
#     n.append(arr)
#
# dem = 0
# for j in n:
#     if j % 2 == 0:
#         dem += 1
# print(dem)

# tổng các phần tử ở vị trí chẵn
# a = int(input())
# n = []
#
# for i in range(a):
#     arr = int(input(i))
#     n.append(arr)
#
# dem = 0
# m = []
# for j in range(a):
#     if j % 2 == 0:
#         m.append(n[j])
# tong_chan = sum(m)
# print(m)
# print(tong_chan)

#tổng các phần tử chẵn trong mảng
# a = int(input())
# n = []
#
# for i in range(a):
#     arr = int(input(i))
#     n.append(arr)
#
# dem = 0
# tong = 0
# m = []
# for j in n:
#     if j % 2 == 0:
#         m.append(j)
#         tong += j
#
# # tong = sum(m)
# print(m)
# print(tong)

# tìm số X trong mảng
# a = int(input())
# n = []
#
# for i in range(a):
#     arr = int(input(i))
#     n.append(arr)
#
# print(n)
# x = int(input())
# m = []
# c = ""
# for j in range(len(n)):
#     if n[j] == x:
#         m.append(j)
#         c = f"Yes {m}"
#         break
# print(f"{c}")


#in số âm và số dương trong mảng
# a = int(input())
# n = []
# for i in range(a):
#     arr = int(input(i+1))
#     n.append(arr)
# dem_so_duong = 0
# dem_so_am = 0
# mang_am = []
# mang_duong = []
# for j in n:
#     if j > 0:
#         dem_so_duong += 1
#         mang_duong.append(j)
#     else:
#         dem_so_am += 1
#         mang_am.append(j)
# print(f"{dem_so_duong} {mang_duong}")
# print(f"{dem_so_am} {mang_am}")

#in ra các số chia hết cho 5 và tổng rong mảng
# a = int(input())
#
# n = []
#
# for i in range(a):
#     arr = int(input(i))
#     n.append(arr)
# m = []
# tong_5 = 0
# for j in n:
#     if j % 5 == 0:
#         m.append(j)
#         tong_5 += j
# print(m)
# print(tong_5)

#tìm phần tử lơn nhất trong mảng
# a = int(input())
# n = []
#
# for i in range(a):
#     arr = int(input(i))
#     n.append(arr)
#
# print(n)
# max_val = n[0]
# for j in n:
#     if j > max_val:
#         max_val = j
# print(max_val)

#sắp xếp mảng tăng dần
# a = int(input())
# n = []
#
# for i in range(a):
#     arr = int(input(i))
#     n.append(arr)
#
# lengh = len(n)
#
# for i in range(0, lengh - 1):
#     for j in range(i+1, lengh):
#         if n[i] > n[j]:
#             tempt = n[i]
#             n[i] = n[j]
#             n[j] = tempt
# print(n)

# sắp xếp giảm dần
# a = int(input())
# n = []
#
# for i in range(a):
#     arr = int(input(i))
#     n.append(arr)
#
# lengh = len(n)
#
# for i in range(0, lengh - 1):
#     for j in range(i+1, lengh):
#         if n[i] < n[j]:
#             tempt = n[j]
#             n[j] = n[i]
#             n[i] = tempt
# print(n)

# in và tính tổng số nguyên tố trong mảng
# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(math.sqrt(num)) + 1):
#         if num % i == 0:
#             return False
#     return True
#
# a = int(input())
# n= []
# for i in range(a):
#     arr = int(input(i))
#     n.append(arr)
#
# m = []
# tong_nguyen_to = 0
# for j in n:
#     if is_prime(j):
#         m.append(j)
#         tong_nguyen_to += j
# print(m)
# print(tong_nguyen_to)

# tính chung bình các số nguyên tố trong mảng
# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(math.sqrt(num)) + 1):
#         if num % i == 0:
#             return False
#     return True
#
# a = int(input())
# n= []
# for i in range(a):
#     arr = int(input(i))
#     n.append(arr)
#
# m = []
# tong_nguyen_to = 0
# dem = 0
# for j in n:
#     if is_prime(j):
#         m.append(j)
#         dem += 1
#         tong_nguyen_to += j
# avg_nguyen_to = tong_nguyen_to / dem
# round_avg_nguyen_to = round(avg_nguyen_to, 2)
# print(m)
# print(tong_nguyen_to)
# print(round_avg_nguyen_to)

#tìm số nguyên tố lớn nhất trong mảng
# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(math.sqrt(num)) + 1):
#         if num % i == 0:
#             return False
#     return True
#
# a = int(input())
# n= []
# for i in range(a):
#     arr = int(input(i))
#     n.append(arr)
#
# m = []
# for j in n:
#     if is_prime(j):
#         m.append(j)
#
# print(m)
#
# max_nguyen_to = m[0]
# for items in m:
#     if items > max_nguyen_to:
#         max_nguyen_to = items
# print(max_nguyen_to)

#tìm số âm lớn nhất
# a = int(input())
# n= []
# for i in range(a):
#     arr = int(input(i))
#     n.append(arr)
#
# max_am = 0
# result = 0
# for j in n:
#     if j < 0:
#        if max_am == 0 or j > max_am:
#            max_am = j
#
# if max_am == 0:
#     result = 0
# else:
#     result = max_am
#
# print(result)

#tìm phần tử lơn thứ nhì trong mảng
# a = int(input())
# n = []
# for i in range(a):
#     arr = int(input(i))
#     n.append(arr)
#
# print(n)
# max_val_1 = max_val_2 = float('-inf')
# for j in n:
#     if j > max_val_1:
#         max_val_2 = max_val_1
#         max_val_1 = j
#     elif j > max_val_2 and j != max_val_1:
#         max_val_2 = j
# print(max_val_2)

#tìm phần tử lơn thứ 3 trong mảng
# a = int(input())
# n = []
# for i in range(a):
#     arr = int(input(i))
#     n.append(arr)
#
# print(n)
# # max_val_1 = max_val_2 = max_val_3 = float('-inf') #lưu giá trị lớn thứ 1,2,3
# max_val_1 = max_val_2 = max_val_3 = float('inf') #lưu giá trị nhỏ thứ 1,2,3
# for j in n:
#     if j < max_val_1:
#         max_val_2 = max_val_1
#         max_val_1 = j
#     elif j < max_val_2:
#         max_val_3 = max_val_2
#         max_val_2 = j
#     elif j < max_val_3 and j != max_val_1 and j != max_val_2:
#         max_val_3 = j
# print(max_val_3)

# đếm số lượng các phần tử khác nhau trong mảng
# a = int(input())
# n = []
#
# for i in range(a):
#     arr = int(input(i))
#     n.append(arr)
#
# so_nguyen_khac_nhau = []
#
# for j in n:
#     if j not in so_nguyen_khac_nhau:
#         so_nguyen_khac_nhau.append(j)
# count = len(so_nguyen_khac_nhau)
# print(so_nguyen_khac_nhau)
# print(count)

# số lần xuất hện
# a = int(input())
# n = []
#
# for i in range(a):
#     arr = int(input(i))
#     n.append(arr)
#
# so_nguyen_khac_nhau = {}
#
# for j in n:
#     if j in so_nguyen_khac_nhau:
#         so_nguyen_khac_nhau[j] += 1
#     else:
#         so_nguyen_khac_nhau[j] = 1
#
#
# count_max =0
# tan_xuat = []
# for num, count in so_nguyen_khac_nhau.items():
#     if count > count_max:
#         count_max = count
#         tan_xuat = [num]
#     elif count == count_max:
#         tan_xuat.append(num)
# print(f"{tan_xuat}  {count_max}")

#tính trung bình cộng số chính phương trong mảng
# def so_nguyen_to(a):
#     if a < 0:
#         return 0
#     else:
#         b = int(math.sqrt(a))
#         if b * b == a:
#             result = "yes"
#         else:
#             result = "no"
#     return result
#
# a = int(input())
# n = []
#
# for i in range(a):
#     arr = int(input(i))
#     n.append(arr)
# k = []
# tong = 0
# dem = 0
# for j in n:
#     if so_nguyen_to(j) == "yes":
#         tong += j
#         dem += 1
#         k.append(j)
# avg_chinh_phuong = tong / dem
# round_avg_cp = round(avg_chinh_phuong, 2)
# print(k)
# print(round_avg_cp)

#in ra câu chào họ tên
# a = input()
#
# if a != "":
#     print(f"Chao {a}")
# else:
#     print("fail")

# đảo ngược chuỗi
# a = input()
# b = ""
# for i in a:
#     b = i + a
# print(f"{b}")
#in in chuỗi với mỗi ký tự hiển thị trên 1 dòng
# a = input()
# for i in a:
#     print(i)

# xóa khoảng trắng trong chuỗi
# a = input()
# b = ""
# for i in a:
#     if i != " ":
#         b += i
# print(b)

# xâu đối xứng
# def xau_dx(a):
#     n = len(a)
#     for i in range(n // 2):
#         if a[i] != a[n - i - 1]:
#             return 0
#     return 1
#
# a = input()
#
# if xau_dx(a):
#     print(a)
# else:
#     print("")

#xóa khoảng trắng ở đầu chuỗi
# a = input()
# i = 0
# while i < len(a) and a[i] == " ": # duyệt tìm vị trí đầu tiền của chuỗi không chứa khoảng trắng nếu có khoảng trắng tăng i + 1 lên để tìm dừng khi tìm thấy kí tự đầu tiên không chứa khoảng trằng
#     i += 1
# c = ""
# for j in range(i, len(a)): # lặp trong chuỗi chạy từ i đến a
#     c += a[j]
# print(c)

# xóa khoảng trắng ở cuối chuỗi
# a = input()
# i = len(a) - 1
# while i >= 0 and a[i] == " ": # duyệt tìm các phần tử không chứa khoảng trắng ghép thành 1 chuỗi mới dừng khi tìm thấy khoảng trắng sau khi đã duyệt hết các phần tử
#     i -= 1
# c = ""
# for j in range(0, i + 1): # lặp trong chuỗi chạy từ 0 đến i+1
#     c += a[j]
# print(c)

#xóa khoảng trắng ở giữa
# a = input()
# c = ""
# b = False
#
# for i in a:
#     if i != " ":
#         c += i
#         b = True
#     elif b:
#         c += " "
#         b = False
# print(c)

# đếm số từ trong chuỗi
# a = input()
# c = 0
# b = False
#
# for i in a:
#     if i != " " and not b:
#         c += 1
#         b = True
#     elif i == " ":
#         b = False
# print(c)

# đổi ký tự đầu thành chứ in hoa
# a = input()
# c = a[0].upper() + a[1:]
# print(c)

# tìm và thay thế thế chuỗi
# s = input()
# x = input()
# y = input()
# z = ""
# for i in s:
#     if i == x:
#         z += y
#     else:
#         z += i
# print(z)

# đổi tất cả các kí tự từ in thường sang in hoa
# a = input()
# print(a.upper())
# đổi tất cả các kí tự từ in hoa sang in thường
# a = input()
# print(a.lower())

#dảo ngược từ trong chuỗi
# a = input()
# b = a.split()
# print(b)
# c = []
# for i in range(len(b)-1, -1, -1):
#     c.append(b[i])
# print(c)
# d = ""
# for j in range(len(c)):
#     if j == len(c)-1:
#         d += c[j]
#     else:
#         d += c[j] + " "
# print(d)

# đảo ngược chuỗi
# a = input()
# b = a.split()
# print(b)
# c = []
# for i in b:
#     f = ""
#     for k in i:
#         f = k+f
#     c.append(f)
# print(c)
# d = ""
# for j in range(len(c)):
#     if j == len(c)-1:
#         d += c[j]
#     else:
#         d += c[j] + " "
# print(d)

# đếm số lần xuất hiện ký tự trong chuỗi
# s = input()
# x = input()
# z = 0
# for i in s:
#     if i == x:
#         z += 1
#     else:
#         z = 0
# print(z)

# đếm các kí tự khác nhau trong chuỗi
# a = input()
# c = []
# for i in a:
#     if i not in c:
#         c.append(i)
# d = len(c)
# print(d)

# đếm số lần xuất hiện của từng kí tự
# a = input().lower()
#
# n = {}
#
# for i in a:
#     if i in n:
#         n[i] += 1
#     else:
#         n[i] = 1
#
# count_m = 0
# c = ""
# for char, count in n.items():
#     c += f"{char}:{count} "
# print(c)

# in ra kí tự có số lần xuất hiện nhiều nhất trong chuỗi
# a = input().lower()
# a = a.replace(" ","")
#
# n = {}
#
# for i in a:
#     if i in n:
#         n[i] += 1
#     else:
#         n[i] = 1
#
# count_max = 0
# tan_xuat = ""
# for char, count in n.items():
#     if count > count_max:
#         count_max = count
#         tan_xuat = char
#     elif count == count_max:
#         tan_xuat += char
# print(f"{tan_xuat}:{count_max}")

#tìm phần tử x ở vị trí đầu tiên xuất hiện
# s = input()
# x = input()
# y = ""
# for i in range(len(s)):
#     if s[i] == x:
#         y = f"{i}"
#         break
#     else:
#         y = -1
# print(y)
#tìm phần tử x ở vị trí cuối x xuất hiện
# s = input()
# x = input()
# y = ""
# for i in range(len(s) - 1, -1, -1):
#     if s[i] == x:
#         y = f"{i}"
#         break
#     else:
#         y = -1
# print(y)

# đếm kí tự in hoa
# s = input()
# dem = 0
# for i in s:
#     if i.isupper():
#         dem += 1
# print(dem)

# đếm kí tự thường
# s = input()
# dem = 0
# for i in s:
#     if i.islower():
#         dem += 1
# print(dem)

# lấy tên từ chuỗi họ tên
# a = input()
# b = a.split()
# if b:
#     c = b[-1]
# print(c)

# in ra họ tên
# a = input()
# b = a.split()
# c = ""
# #c1
# # for i in range(len(b)-1):
# #     if len(b) > 1:
# #         c += b[i] + " "
# #     else:
# #         c = ""
# # print(c)
# #c2
# if len(b) > 1:
#     for i in range(len(b)-1):
#         c += b[i] + " "
# else:
#     c = ""
# print(c)

#viết hàm tính chu vi tam giác
#
# def cv_triagle(a, b, c):
#     p = a + b + c
#     round_p = round(p,3)
#     return round_p
#
# def dt_triagle(a, b, c):
#     p = (a + b + c) / 2
#     dt = math.sqrt(p*(p-a)*(p-b)*(p-c))
#     round_dt = round(dt,3)
#     return round_dt
#
# a,b,c = map(int, input("").split())
# d_cv = cv_triagle(a, b, c)
# d_dt = dt_triagle(a, b, c)
#
# print(f"{d_cv} {d_dt}")

#hàm chia check n chia hết cho 5

# def check_n(n):
#     result = ""
#     if n > 0:
#         if n % 5 == 0:
#             result = "yes"
#         else:
#             result = "no"
#     else:
#         result = "no"
#     return result
#
# n = int(input())
# a = check_n(n)
# print(a)
#tính tổ hợp
# def to_hop(n, k):
#     if n >= k and k >= 0:
#         return math.factorial(n) // (math.factorial(k) * math.factorial(n - k)) # hàm factorial dùng để tính giai thừa
#     else:
#         return 0
#
# a = int(input())
# c = []
# for _ in range(a):
#     n, k = map(int, input("").split())
#     d = to_hop(n, k)
#     c.append(d)
# tong = 0
# for i in c:
#     tong += i
# print(tong)

#hàm tính trung bình phân tử trong mảng
# def sum_array(n):
#     tong = 0
#     dem = 0
#     round_avg = 0
#     for i in n:
#         tong += i
#         dem += 1
#         round_avg = round(tong/dem, 2)
#     return round_avg
#
# a = int(input())
# n= list(map(int, input().split()))
#
# d = sum_array(n)
# print(d)

#hàm tính trung bình cộng số chẵn
# def agv_chan(n):
#     dem = 0
#     tong = 0
#     round_avg = 0
#     for i in n:
#         if i % 2 == 0:
#             tong += i
#             dem += 1
#             round_avg = round(tong/dem, 2)
#         else:
#             round_avg = 0
#     return round_avg
# a = int(input())
# n = list(map(int, input().split()))
# d = agv_chan(n)
# print(d)
#đếm số nguyên tố trong mảng
# def so_nguyen_to(a):
#     if a < 2:
#         return False
#     for i in range(2, int(math.sqrt(a))+1):
#         if a % i == 0:
#             return False
#     return True
# def count_snt(n):
#     count = 0
#     for i in n:
#         if so_nguyen_to(i):
#             count += 1
#     return count
#
#
# n = list(map(int, input().split()))
# d = count_snt(n)
# print(d)

#trung bình cộng các số nguyên tố
# def so_nguyen_to(a):
#     if a < 2:
#         return False
#     for i in range(2, int(math.sqrt(a))+1):
#         if a % i == 0:
#             return False
#     return True
# def avg_snt(n):
#     count = 0
#     tong = 0
#     round_avg = 0
#     for i in n:
#         if so_nguyen_to(i):
#             count += 1
#             tong += i
#             round_avg = round(tong/count,2)
#     return round_avg
#
#
# n = list(map(int, input().split()))
# d = avg_snt(n)
# print(d)
# trung bình cộng số chính phương dùng function
# def ktra_chinh_phuong(a):
#     if a < 0:
#         return False
#     cp = int(math.sqrt(a))
#     return cp * cp == a
#
# # def check_input(b):
# #     if not isinstance(b, list):
# #         return "invalid"
# #     d = []
# #     for i in b:
# #         if isinstance(i, (int, float)):
# #             d.append(check_scp(i))
# #         else:
# #             d.append("invalid")
# #     return d
# def avg_snt(n):
#     count = 0
#     tong = 0
#     round_avg = 0
#     for i in n:
#         if ktra_chinh_phuong(i):
#             tong += i
#             count += 1
#             round_avg = round(tong/count, 2)
#     return round_avg
#
# n = list(map(int, input().split()))
#
# d = avg_snt(n)
#
# print(d)


#tìm phân tử lơn nhất & nhỏ nhất trong mảng
# def search_max(n):
#     max_val = n[0]
#     index = 0
#     for i in range(1, len(n)):
#         if n[i] > max_val:
#             max_val = n[i]
#             index = i
#     return max_val, index
#
# def search_min(n):
#     min_val = n[0]
#     index = 0
#     for i in range(1, len(n)):
#         if n[i] < min_val:
#             min_val = n[i]
#             index = i
#     return min_val, index
# a = int(input())
# n = list(map(int, input().split()))
# d_1 = search_max(n)
# d_2 = search_min(n)
# print(f"{d_1} {d_2}")

# test

# a = "hello, world"
# for i in a:
#     if i.find("h"):
#         c = 1
#     else:
#         c = 0
# print(c)

# a = [10, 20, 3, 4, 5, 6, 7]
# a = ["x", "b", "c", "d", "e", "f"]
# a.sort(reverse= False)
# print(a)
# for i in range(len(a)):
#     print(a[i])

# newlist = [x for x in a if x != "a"]
# newlist = []
# for i in a:
#     if i != "a":
#         newlist.append(i)
# print(newlist)

# i = 0
# while i < len(a):
#     print(a[i])
#     i += 1

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# # a = thisdict.values()
# # thisdict["color"] = "red"
# # print(a)
#
# for i, j in thisdict.items():
#     print(i,j)