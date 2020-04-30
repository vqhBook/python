a, b = 10, 100
for i in range(a, b + 1):
    if i % 2 == 0:
        continue

    if int(i**0.5)**2 == i: # i là số chính phương
        print(i)
        break

else:
    print("Không tìm thấy số nào!")

print("Done!")
