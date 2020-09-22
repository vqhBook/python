import random

max = 1000
print("Trò chơi đoán số!")
print(f"Bạn đoán một con số nguyên trong phạm vi 1-{max}.")

secret = random.randint(1, max)
count = 0
while True:
    count += 1
    n = int(input(f"Mời bạn đoán lần {count}: "))
    
    if n < secret:
        print("Số bạn đoán nhỏ quá!")
    elif n > secret:
        print("Số bạn đoán lớn quá!")
    else:
        print(f"Bạn đoán đúng số {secret} sau {count} lần.")
        break
