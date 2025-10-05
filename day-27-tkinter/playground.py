def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

outcome = add(4, 0, 8, 16, 9, 7)
print(outcome)


def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    return n


result = calculate(2, add=3, multiply=5)
print(result)


class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
my_car = Car(make = "Nissan")
print(my_car.model)
