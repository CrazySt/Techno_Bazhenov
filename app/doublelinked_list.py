
class Item:
    def __init__(self, elem):
        self.elem = elem
        self.next_item = None
        self.prev_item = None

    def next(self):
        return self.next_item

    def prev(self):
        return self.prev_item


class EmptyListException(Exception):
    def __init__(self):
        Exception.__init__(self, "This double_linked_list is empty!")


class DoubleLinkedList:
    def __init__(self, *args):
        if args:
            j = 0
            for i in args:
                if j == 0:
                    item1 = Item(i)
                    self.first_item = item1
                    j = 1
                else:
                    item2 = Item(i)
                    item1.next_item = item2
                    item2.prev_item = item1
                    item1 = item2
        else:
            self.first_item = None

    def last(self):
        if self.first_item:
            i = self.first_item
            while i.next_item:
                _ = i.next_item
                i = _
        else:
            raise EmptyListException()
        return i.elem

    def first(self):
        if self.first_item:
            return self.first_item.elem
        else:
            raise EmptyListException()

    def push(self, something):
        new_elem = Item(something)
        if self.first_item:
            i = self.first_item
            while i.next_item:
                i = i.next_item
            i.next_item = new_elem
            new_elem.prev_item = i
        else:
            self.first_item = new_elem
        return True

    def length(self):
        j = 0
        if self.first_item:
            i = self.first_item
            while i:
                _ = i.next_item
                i = _
                j += 1
        return j

    def contains(self, query):
        if self.first_item:
            i = self.first_item
            while i:
                if i.elem == query:
                    return True
                _ = i.next_item
                i = _
        return False

    def pop(self):
        if self.first_item:
            last = self.first_item
            while last.next_item:
                last = last.next_item
            if last is self.first_item:
                self.first_item = None
            else:
                pre = last.prev_item
                pre.next_item = None
            return last.elem
        else:
            raise EmptyListException()

    def delete(self, query):
        i = self.first_item
        if i:
            while i:
                if i.elem == query:
                    prev = i.prev_item
                    next_i = i.next_item
                    if prev:
                        prev.next_item = next_i
                    else:
                        self.first_item = next_i
                    if next_i:
                        next_i.prev_item = prev

                    return True
                i = i.next_item
            return False
        return False

    def unshift(self, new_elem):
        if self.first_item:
            i = Item(new_elem)
            i.next_item = self.first_item
            self.first_item = i
        else:
            self.first_item = Item(new_elem)
        return True

    def shift(self):
        if self.first_item:
            i = self.first_item
            self.first_item = i.next_item
            if self.first_item:
                self.first_item.prev_item = None
            return i.elem
        else:
            raise EmptyListException()

    def make_list(self):
        result = list()
        i = self.first_item
        while i:

            result.append(i.elem)
            i = i.next_item
        return result
