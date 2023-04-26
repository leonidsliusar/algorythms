#CUSTOM ITERATOR
class Tumbochka_Iterator:
    def __init__(self, obj):
        self.obj = obj
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.current < len(self.obj.d[1] + self.obj.d[2]):
            result = (self.obj.d[1] + self.obj.d[2])[self.current]
            self.current += 1
            return result
        raise StopIteration


class Tumbochka:
    def __init__(self, *val):
        self.d = {
            1: [],
            2: [],
        }
        detupling = 0
        while detupling < len(val):
            elem = val[detupling]
            if type(elem) is int or type(elem) is float:
                self.d[1].append(elem)
                detupling += 1
            elif type(elem) is str or type(elem) is bool:
                self.d[2].append(elem)
                detupling += 1

    def __iter__(self):
        return Tumbochka_Iterator(self)

    def __str__(self):
        return f'Числа {self.d[1]}, все остальное {self.d[2]}'

tumb = Tumbochka(1, 5, True, 10)
for e in tumb:
    print(e)