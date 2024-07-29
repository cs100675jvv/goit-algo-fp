class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.value, end=" -> ")
            current_node = current_node.next
        print("None")

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def merge_sort(self):
        if self.head is None or self.head.next is None:
            return self.head

        middle = self.get_middle(self.head)
        next_to_middle = middle.next

        middle.next = None

        left = LinkedList()
        right = LinkedList()

        left.head = self.head
        right.head = next_to_middle

        left.merge_sort()
        right.merge_sort()

        self.head = self.sorted_merge(left.head, right.head)

    def get_middle(self, head):
        if head is None:
            return head

        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def sorted_merge(self, a, b):
        result = None

        if a is None:
            return b
        if b is None:
            return a

        if a.value <= b.value:
            result = a
            result.next = self.sorted_merge(a.next, b)
        else:
            result = b
            result.next = self.sorted_merge(a, b.next)

        return result

def merge_two_sorted_lists(l1, l2):
    dummy = Node(0)
    tail = dummy

    while l1 and l2:
        if l1.value < l2.value:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    if l1:
        tail.next = l1
    if l2:
        tail.next = l2

    return dummy.next

# Приклад використання
if __name__ == "__main__":
    ll = LinkedList()
    ll.append(3)
    ll.append(1)
    ll.append(4)
    ll.append(2)
    ll.append(5)

    print("Первинний список:")
    ll.print_list()

    print("Реверсований список:")
    ll.reverse()
    ll.print_list()

    ll.reverse()  # Повернути до початкового стану

    print("Відсортований список:")
    ll.merge_sort()
    ll.print_list()

    # Об'єднання двох відсортованих списків
    l1 = LinkedList()
    l1.append(1)
    l1.append(3)
    l1.append(5)

    l2 = LinkedList()
    l2.append(2)
    l2.append(4)
    l2.append(6)

    print("Перший відсортований список:")
    l1.print_list()

    print("Другий відсортований список:")
    l2.print_list()

    merged_head = merge_two_sorted_lists(l1.head, l2.head)

    print("Об'єднаний відсортований список:")
    merged_list = LinkedList()
    merged_list.head = merged_head
    merged_list.print_list()
