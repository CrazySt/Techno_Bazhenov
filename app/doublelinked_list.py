"""DoubleLInked list with Items. what can i add?"""


class Item:
    """Item class for list"""
    def __init__(self, elem):
        """this is constructor"""
        self.elem = elem
        self.next_item = None
        self.prev_item = None

    def next(self):
        """return link to the next Item"""
        return self.next_item

    def prev(self):
        """returns link to the previous Item"""
        return self.prev_item


class EmptyListException(Exception):
    """custom exception for empty list"""
    def __init__(self):
        """initialazing of custom exception for empty list"""
        Exception.__init__(self, "This double_linked_list is empty!")


class DoubleLinkedList:
    """class of list"""
    def __init__(self, *args):
        """constructor"""
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
            self.last_item = item1
        else:
            self.first_item = None
            self.last_item = None

    def last(self):
        """returns last element in list"""
        if self.last_item:
            return self.last_item.elem
        else:
            raise EmptyListException()

    def first(self):
        """returns first element in list"""
        if self.first_item:
            return self.first_item.elem
        else:
            raise EmptyListException()

    def push(self, something):
        """adds something in the end of list"""
        new_elem = Item(something)
        if self.last_item:
            self.last_item.next_item = new_elem
            new_elem.prev_item = self.last_item
            self.last_item = new_elem
        else:
            self.last_item = new_elem
            self.first_item = new_elem
        return True

    def length(self):
        """returns amount of Items in the list"""
        j = 0
        if self.first_item:
            i = self.first_item
            while i:
                _ = i.next_item
                i = _
                j += 1
        return j

    def contains(self, query):
        """checks if list contains some element"""
        if self.first_item:
            i = self.first_item
            while i:
                if i.elem == query:
                    return True
                _ = i.next_item
                i = _
        return False

    def pop(self):
        """deletes and returns last element of the list"""
        if self.last_item:
            last = self.last_item
            if last is self.first_item:
                self.first_item = None
                self.last_item = None
            else:
                pre = last.prev_item
                pre.next_item = None
                self.last_item = pre
            return last.elem
        else:
            raise EmptyListException()

    def delete(self, query):
        """deletes and returns query element of the list if it is"""
        i = self.first_item
        if i:
            while i:
                if i.elem == query:
                    prev = i.prev_item
                    next = i.next_item
                    if prev:
                        prev.next_item = next
                    else:
                        self.first_item = next
                    if next:
                        next.prev_item = prev
                    else:
                        self.last_item = prev
                    return True
                i = i.next_item
            return False
        raise EmptyListException()

    def unshift(self, new_elem):
        """inserts new Item with new_elem in the beginnng of the list"""
        if self.first_item:
            i = Item(new_elem)
            i.next_item = self.first_item
            self.first_item = i
        else:
            self.first_item = Item(new_elem)
        return True

    def shift(self):
        """deletes and returns first element of the list"""
        if self.first_item:
            i = self.first_item
            self.first_item = i.next_item
            if self.first_item:
                self.first_item.prev_item = None
            else:
                self.last_item = None
            return i.elem
        else:
            raise EmptyListException()
