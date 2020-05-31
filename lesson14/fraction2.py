import math

class Fraction:
    def __init__(self, numer=0, denom=1):
        if isinstance(numer, str):
            # đối số là chuỗi tử/mẫu hoặc chỉ có tử
            nums = numer.split("/")
            numer = int(nums[0])
            denom = 1 if len(nums) == 1 else int(nums[1])
        
        gcd = math.gcd(numer, denom)
        if denom < 0:
            gcd = -gcd
        self._numer = numer // gcd # tử số
        self._denom = denom // gcd # mẫu số
                    
    def __repr__(self):
        if self._denom == 1:
            return str(self._numer)
        else:
            return "%d/%d" % (self._numer, self._denom)

    def __float__(self):
        return self._numer / self._denom

    def __lt__(self, other):
        return float(self) < float(other)

    def __add__(self, other):
        r_numer = self._numer*other._denom + self._denom*other._numer
        r_denom = self._denom*other._denom
        return Fraction(r_numer, r_denom)
