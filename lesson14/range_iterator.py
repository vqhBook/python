class range:
    def __init__(self, start=0, stop=None, step=1):
        self._start = start
        self._stop = stop
        self._step = step
        self._cur = self._start

    def __iter__(self):
        # self._cur = self._start
        return self
    
    def __next__(self):
        if (self._stop != None and
            (self._step > 0 and self._cur >= self._stop
             or self._step < 0 and self._cur <= self._stop)):
            raise StopIteration
        self._cur = (prev := self._cur) + self._step
        return prev
