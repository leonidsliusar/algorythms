# You shall not do this although you can
class MyKey:
    def __init__(self, value):
        self.__value = value

    def __hash__(self):  #Implementation of __hash__ dunder method makes you're custom data type hashable
        return super().__hash__()


    def __eq__(self, other):  #Implementation of __eq__ dunder method makes objects of you're custom data type possible to '=='
        return isinstance(other, MyKey) and self.__value == other.__value


    def __repr__(self):
        return str(self.__value)


key1 = MyKey(1)
print(hash(key1))


key2 = MyKey(2)
some_list = [key1, key2]
print(key1 == key2)
print(key1 is key2)

new_dict = {key1: 'first', key2: 'second'}
print(new_dict)
print(hash(key1))
key1._MyKey__value = 10
print(hash(key1))
print(new_dict)