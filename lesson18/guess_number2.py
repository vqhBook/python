import random

def binary_guess():
    if left <= right:
        return (left + right) // 2
    else:
        return None

def hint(n, msg):
    global left, right

    if msg == "less":
        left = n + 1
    else:
        right = n - 1

max = 1000
print("Trò chơi đoán số!")
print(f"Bạn đoán một con số nguyên trong phạm vi 1-{max}.")

left, right = 1, max
secret = random.randint(1, max)
count = 0
while True:
    count += 1
    input("Press Enter to guess.")
    n = binary_guess()
    print(f"Đoán lần {count} số {n}")
    
    if n < secret:
        print("Số bạn đoán nhỏ quá!")
        hint(n, "less")
    elif n > secret:
        print("Số bạn đoán lớn quá!")
        hint(n, "greater")
    else:
        print(f"Bạn đoán đúng số {secret} sau {count} lần.")
        break
