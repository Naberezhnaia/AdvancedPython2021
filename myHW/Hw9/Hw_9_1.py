class Print_Mid(Exception):
    pass

class Print_Dispersion(Exception):
    pass

class Print_Volume(Exception):
    pass

def Coroutine():
    print("Starting coroutine")
    q = 1
    s = 0
    s_sq = 0
    try:
        while True:
            try:
                x = yield
                s += x
                s_sq += x**2
            except Print_Mid:
                yield s/q
            except Print_Dispersion:
                yield (s_sq/q)-(s/q)**2
            except Print_Volume:
                yield q
                q += 1
    finally:
        print("Stop coroutine")

coroutine = Coroutine()
next(coroutine)

while True:
    date = input()
    try:
        date = float(date)
        coroutine.send(date)
        print("Current mid:", coroutine.throw(Print_Mid))
        next(coroutine)
        print("Current dispersion:", coroutine.throw(Print_Dispersion))
        next(coroutine)
        print("Current volume:", coroutine.throw(Print_Volume))
        next(coroutine)
    except:
        break

coroutine.close()
