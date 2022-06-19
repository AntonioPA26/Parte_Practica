import time


def mesureTime(function):
    def wrapper(*args, **kwargs):
        start = time.time()

        result = function(*args, **kwargs)

        total = time.time() - start
        print("La demora de ejecución fue de: {}".format(total))

        return result

    return wrapper

@mesureTime
def Division(a, b):
    s = a/b
    return s


print(Division(5,6))
print(Division(6,7))