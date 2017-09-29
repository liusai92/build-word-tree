#!usr/bin/python
# _*_ coding:utf-8 _*_

class Node(object):

    def __init__(self, value):
        self._children = []
        self._value = value
        self._is_root = True

    def __str__(self):
        return "Node<{}>".format(self._value)

    def __eq__(self, that):
        if not isinstance(that, Node):
            return False
        return self._value == that.value

    def __lt__(self, that):
        if not isinstance(that, Node):
            return False
        if len(self._value) >= len(that.value):
            return False
        return (self._value in that.value)

    @property
    def value(self):
        return self._value

    @property
    def children(self):
        return self._children

    def add_children(self, chn):
        if not isinstance(chn, Node):
            raise ValueError('added item must be node object')
        self._children.append(chn)

    @property
    def is_root(self):
        return self._is_root

    @is_root.setter
    def is_root(self, bl):
        if not isinstance(bl, bool):
            raise ValueError('argument must be boolean')
        self._is_root = bl

if __name__=="__main__":
    node = Node('t')
