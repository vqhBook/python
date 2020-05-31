import pprint
from collections import namedtuple

SV = namedtuple("SinhViên", ["mã_số", "tên", "điểm"])

sv = [SV(mã_số=19001, tên="SV A", điểm=6.0),
      SV(19005, "SV B", 7.5),
      SV(19004, điểm=5.0, tên="SV C"),
      SV(tên="SV D", mã_số=19010, điểm=0.5),
      SV(19009, "SV E", 10.0)]

sv.sort(key=lambda sinh_vien: sinh_vien.mã_số)
pprint.pprint(sv)
print(max(sv, key=lambda sinh_vien: sinh_vien.điểm))
