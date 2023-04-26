import sys


class Node:
    def __init__(self, data=None, next=None, previous=None):
        self.data = data
        self.next = next
        self.prev = previous

    def set_next(self, val):
        self.next = val

    def set_prev(self, val):
        self.prev = val

    def __del__(self):
        print(f'Элемент с данными {self.data} удален. На объект было {sys.getrefcount(self)} ссылки')

class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None

    # stop_index - необязательный аргумент.Останавливает индексирование на указанном элементе списка.
    # return_object - необязательный аргумент.Возвращает словарь с ссылками на элементы списка.
    def set_index(self, stop_index=None, return_object=False):
        cur_node = self.__head
        index = 0
        if return_object == False:
            dict = {index: cur_node.data}
            while cur_node.next != None:
                cur_node = cur_node.next
                index += 1
                dict[index] = cur_node.data
                if index == stop_index:
                    break
            return dict
        else:
            dict = {index: cur_node}
            while cur_node.next != None:
                cur_node = cur_node.next
                index += 1
                dict[index] = cur_node
                if index == stop_index:
                    break
            return dict

    def push_front(self, data):
        new_node = Node(data)
        cur_node = new_node
        if self.__head is None:
            self.__head = new_node
        if self.__tail is None:
            self.__tail = new_node
            return
        else:
            self.__head.prev = cur_node
            cur_node.next = self.__head
            self.__head = cur_node
            return

    def push_back(self, data):
        new_node = Node(data)
        cur_node = new_node
        if self.__head is None:
            self.__head = new_node
        if self.__tail is None:
            self.__tail = new_node
            return
        else:
            self.__tail.next = cur_node
            cur_node.prev = self.__tail
            self.__tail = cur_node
            return

    @property
    def get_front(self):
        return self.__head.data

    @property
    def get_back(self):
        return self.__tail.data

    def insert(self, data, index): #index-индекс элемента перед которым нужно сделать вставку
        dict = self.set_index(index, return_object=True)
        new_node = Node(data)
        cur_node = new_node
        cur_node.next = dict[index]
        cur_node.prev = dict[index-1]
        dict[index].prev = cur_node
        dict[index-1].next = cur_node
        return


    def get(self, index):
        dict = self.set_index(index)
        return dict[index]

    @property
    def show(self):
        cur_node = self.__head
        out = ''
        while cur_node != None:
            out += str(cur_node.data) + " \u21C4 "
            cur_node = cur_node.next
        print('None' + ' \u21C4 ' + out + 'None')

    @property
    def len(self):
        cur_node = self.__head
        length = 0
        while cur_node != None:
            cur_node = cur_node.next
            length += 1
        return length

    @property
    def pop_front(self):
        if self.__head.next:
            cur_node = self.__head.next
            cur_node.set_prev(None)
            self.__head = cur_node
            return
        else:
            self.__head.set_next(None)
            self.__head.set_prev(None)
            self.__tail.set_next(None)
            self.__tail.set_prev(None)
            self.__head = self.__tail = None
            return
    @property
    def pop_back(self):
        if self.__tail.prev:
            cur_node = self.__tail.prev
            cur_node.set_next(None)
            self.__tail = cur_node
            return
        else:
            self.__head.set_next(None)
            self.__head.set_prev(None)
            self.__tail.set_next(None)
            self.__tail.set_prev(None)
            self.__head = self.__tail = None
            return
    #Последний элемент удалять pop_back/pop_front
    def erase(self, index):
        dict = self.set_index(index+1, return_object=True)
        cur_node = dict[index]
        cur_node.prev.set_next(dict[index+1])
        cur_node.next.set_prev(dict[index-1])
        return

"""
Example:
ll = LinkedList()
ll.push_front(0)
ll.push_back(2)
ll.show
ll.insert(1, 1)
ll.show
print(ll.len)
print(ll.get_front)
print(ll.get_back)
print(ll.get(1))
ll.erase(1)
ll.show
print(ll.get(1))
ll.pop_back
ll.show
print(ll.get_back, ll.get_front)
ll.pop_back
ll.show
"""