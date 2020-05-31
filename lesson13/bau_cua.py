import random

def chung_tiền(ds_cược, mặt_ra):
    cược = sum(ds_cược.values())
    for lv in set(LINH_VẬT) - set(mặt_ra):
        cược -= ds_cược.get(lv, 0)
    for lv in mặt_ra:
        cược += ds_cược.get(lv, 0)
    return cược

def bầu_cua():
    mặt_ra = random.choices(LINH_VẬT, k=3)
    t1 = chung_tiền({"TÔM": 3}, mặt_ra)
    t2 = chung_tiền({"TÔM": 2, "CUA": 1}, mặt_ra)
    t3 = chung_tiền({"TÔM": 1, "CUA": 1, "BẦU": 1}, mặt_ra)
    return t1, t2, t3

def trung_bình(N):
    k_quả = [bầu_cua() for _ in range(N)]
    return [sum([k[c] for k in k_quả])/N for c in [0, 1, 2]]
    
LINH_VẬT = ["TÔM", "CUA", "BẦU", "CÁ", "GÀ", "NAI"]
