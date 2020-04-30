print("Hoan nghênh đo chiều cao, cân nặng, đo huyết áp, thử sức kéo!")

cân_nặng = float(input("Nhập cân nặng của bạn (kg): "))
chiều_cao = float(input("Nhập chiều cao của bạn (m): "))

BMI = cân_nặng / chiều_cao**2
print(f"Chỉ số BMI của bạn là: {BMI:.1f}")

if BMI < 18.5:
    print("Thân hình hơi gầy một tí!")
    print("Đề nghị ăn uống bồi dưỡng thêm.")
elif BMI < 25:
    print("Thân hình hoàn toàn bình thường!")
elif BMI < 30:
    print("Thân hình hơi béo một tí!")
else: # BMI >= 30
    print("Thân hình không được bình thường!")
    print("Đề nghị tập thể dục thường xuyên.")
