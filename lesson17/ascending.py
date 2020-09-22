nums = []
while True:
    try:
        nums.append(int(input()))
    except:
        break
		
for num in sorted(nums):
    print(num)
