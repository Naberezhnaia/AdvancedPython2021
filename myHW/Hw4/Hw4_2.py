def author(_author):
    def inner(function):
        function.author = _author
        return function
    return inner

@author("Mrs Christian Johann Henrich Heine")
def add2(num: int) -> int:
    return num + 2

print(add2.author)
