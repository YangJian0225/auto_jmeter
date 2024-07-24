import functools


def outside(fn):
    @functools.wraps(fn)
    def inside(*args, **kwargs):
        print("before")
        res = fn(*args, **kwargs)
        print("after")
        return res

    return inside


@outside
def ri(a):
    val = "111"
    print(val)
    return val


ri(12)
