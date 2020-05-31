import pprint
from record import Record

SV = Record("SinhViên", ["mã_số", "tên", "điểm"],
            pri_key="mã_số")

sv = [SV(mã_số=19001, tên="SV A", điểm=6.0),
      SV(mã_số=19005, tên="SV", điểm=7.5),
      SV(mã_số=19004, tên="SV C", điểm=50.0),
      SV(mã_số=19010, tên="SV D", điểm=0.5),
      SV(mã_số=19009, tên="SV E", điểm=10.0)]
sv[1].tên = "SV B"
sv[sv.index(SV(mã_số=19004))].điểm = 5.0

sv.sort(key=lambda sinh_vien: sinh_vien.mã_số)
pprint.pprint(sv)
print(max(sv, key=lambda sinh_vien: sinh_vien.điểm))
