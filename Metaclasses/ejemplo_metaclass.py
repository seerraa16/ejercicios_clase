import types
from time import time
class Timer(type):
    def __new__(mcs, name, bases, dct):
        def wrapper(name, method):
            def timeit(self, *args, **kwargs):
                t = time()
                result = method(self, *args, **kwargs)
                print("Llamada de %s:\t%s" % (name, time() - t))
                return result
            timeit.__name__ = method.__name__
            timeit.__doc__ = method.__doc__
            timeit.__dict__ = method.__dict__
            return timeit
        d = {}
        for name, slot in dct.items():
            if type(slot) is types.FunctionType:
                d[name] = wrapper(name, slot)
            else:
                d[name] = slot
        return type.__new__(mcs, name, bases, d)

