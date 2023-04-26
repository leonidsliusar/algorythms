from typing import List
class Iterator_Upper:
    def __init__(self, some_string: str):
        self.obj = some_string
        self.position = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.position < len(self.obj):
            res = self.obj[self.position]
            self.position += 1
            return res.upper()
        raise StopIteration

i = Iterator_Upper('hello')


def generator_upper(n: str):
    for i in n:
        yield i.upper()

j = generator_upper('Hello')
print(next(j))
print(j.__next__())
