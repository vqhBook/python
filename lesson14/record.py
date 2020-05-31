def Record(typename, field_names, pri_key=None):
    class _Record:
        nonlocal pri_key
        
        __slots__ = field_names
        if pri_key and not pri_key in __slots__:
            pri_key = None
            
        def __init__(self, **kwargs):
            for name in self.__slots__:
                setattr(self, name, kwargs.get(name, None))

        def __repr__(self):
            atts = [f"{name}={getattr(self, name)}"
                    for name in self.__slots__]
            return "%s(%s)" % (typename, ", ".join(atts))

        def __eq__(self, other):
            if pri_key:
                return (getattr(self, pri_key)
                        == getattr(other, pri_key))
            else:
                atts = [getattr(self, name) == getattr(other, name)
                        for name in self.__slots__]
                return all(atts)
            
        def __delattr__(self, name):
            if name in self.__slots__:
                setattr(self, name, None)

    _Record.__name__ = typename
    return _Record
