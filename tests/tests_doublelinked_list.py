import unittest
from app import doublelinked_list as dll


class DLLMethodsTest(unittest.TestCase):

    def test_init(self):
        i = dll.DoubleLinkedList()
        self.assertEqual(i.first_item, None)
        i = dll.DoubleLinkedList(1)
        self.assertEqual(i.first_item.elem, 1)
        self.assertEqual(i.first_item.next_item, None)
        self.assertEqual(i.first_item.prev_item, None)

    def test_pop(self):
        i = dll.DoubleLinkedList('w', 'q', 'e')
        self.assertEqual(i.pop(), 'e')
        self.assertEqual(i.pop(), 'q')
        self.assertEqual(i.pop(), 'w')
        self.assertEqual(i.pop(), None)

    def test_shift(self):
        i = dll.DoubleLinkedList('w', 'q', 'e')
        self.assertEqual(i.shift(), 'w')
        self.assertEqual(i.shift(), 'q')
        self.assertEqual(i.shift(), 'e')
        self.assertEqual(i.shift(), None)

    def test_delete(self):
        i = dll.DoubleLinkedList('w', 'q', 'e', 'e')
        self.assertEqual(i.delete('e'), True)
        self.assertEqual(i.delete('e'), True)
        self.assertEqual(i.delete('e'), False)

    def test_unshift(self):
        i = dll.DoubleLinkedList(2, 3)
        self.assertEqual(i.unshift(1), True)
        self.assertEqual(i.first_item.elem, 1)

    def test_push(self):
        i = dll.DoubleLinkedList(12)
        self.assertEqual(i.push(14), True)
        self.assertEqual(i.first_item.next_item.elem, 14)

    def test_contains(self):
        i = dll.DoubleLinkedList('w', 'q', 'e')
        self.assertEqual(i.contains('e'), True)
        self.assertEqual(i.contains('r'), False)

    def test_first(self):
        i = dll.DoubleLinkedList('w', 'q', 'e')
        self.assertEqual(i.first(), 'w')
        i = dll.DoubleLinkedList()
        self.assertEqual(i.first(), None)

    def test_last(self):
        i = dll.DoubleLinkedList('w', 'q', 'e')
        self.assertEqual(i.last(), 'e')
        i = dll.DoubleLinkedList()
        self.assertEqual(i.last(), False)

    def test_length(self):
        i = dll.DoubleLinkedList('w', 'q', 'e')
        self.assertEqual(i.length(), 3)
        i = dll.DoubleLinkedList()
        self.assertEqual(i.length(), 0)


if __name__ == '__main__':
    unittest.main()
