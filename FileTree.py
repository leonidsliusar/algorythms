from abc import ABC, abstractmethod


class Folder:
    __slots__ = ('name', '__children')
    def __init__(self, name):
        self.name = name
        self.__children = []

    def __repr__(self):
        return f'{self.name}: {self.size}'
    @property
    def children(self):
        return self.__children

    def add_child(self, value):
        self.__children.append(value)
    @property
    def size(self):
        size = 0
        if self.__children:
            for child in self.__children:
                size += child.size
        return size

class File:
    __slots__ = ('name', 'size')
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def __repr__(self):
        return f'{self.name}: {self.size}'

class BaseManager(ABC):
    @abstractmethod
    def touch(self):
        pass

    @abstractmethod
    def add(self):
        pass

    @abstractmethod
    def remove(self):
        pass

    @abstractmethod
    def show(self):
        pass


class FileManager(BaseManager):

    @staticmethod
    def mkdir(name):
        return Folder(name)

    @staticmethod
    def touch(name, size):
        return File(name, size)

    @staticmethod
    def add(folder, obj):
        folder.add_child(obj)

    @staticmethod
    def remove(folder, file):
        folder.children.remove(file)

    @staticmethod
    def show(folder):
        return folder.children


manager = FileManager()

file1 = manager.touch('file1', 1)
file2 = manager.touch('file2', 1)
file3 = manager.touch('file3', 1)

root = manager.mkdir('root')
folder1 = manager.mkdir('folder1')
folder2 = manager.mkdir('folder2')
folder3 = manager.mkdir('folder3')

manager.add(root, folder1)
manager.add(root, folder2)
manager.add(root, folder3)

manager.add(folder1, file1)
manager.add(folder1, file2)
manager.add(folder1, file3)

print(manager.show(root))
print(manager.show(folder1))
