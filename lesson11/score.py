ds_mốc_điểm = [9, 8, 7, 6, 5, 4, 0]
ds_đạt = [True, True, True, True, True, False, False]
ds_học_lực = ["Xuất sắc", "Giỏi", "Khá", "Trung bình khá",
              "Trung bình", "Yếu", "Kém"]

điểm = float(input("Nhập điểm: "))
for i in range(len(ds_mốc_điểm)):
    if điểm >= ds_mốc_điểm[i]:
        print("Bạn " + ("đạt" if ds_đạt[i] else "không đạt"))
        print("Học lực " + ds_học_lực[i])
        break
