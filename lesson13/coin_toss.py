import random

N = int(input("Bạn muốn tung bao nhiêu lần: "))
coins = [random.randint(0, 1) for i in range(N)]
N_ngua = sum(coins)
N_sap = N - N_ngua
print(f"Số lần ngửa là {N_ngua}/{N} ({N_ngua/N*100:.2f}%)")
print(f"Số lần sấp là {N_sap}/{N} ({N_sap/N*100:.2f}%)")
