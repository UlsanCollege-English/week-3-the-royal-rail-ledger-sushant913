"""Week 3 homework: The Royal Rail Ledger."""

from __future__ import annotations


class SLLNode:
    def __init__(self, value: int, next: "SLLNode | None" = None) -> None:
        self.value = value
        self.next = next


class SinglyLinkedList:
    def __init__(self) -> None:
        self.head: SLLNode | None = None


class DLLNode:
    def __init__(
        self,
        value: int,
        prev: "DLLNode | None" = None,
        next: "DLLNode | None" = None,
    ) -> None:
        self.value = value
        self.prev = prev
        self.next = next


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head: DLLNode | None = None
        self.tail: DLLNode | None = None


def build_sll_from_list(values: list[int]) -> SinglyLinkedList:
    sll = SinglyLinkedList()

    current = None
    for val in values:
        node = SLLNode(val)
        if sll.head is None:
            sll.head = node
            current = node
        else:
            current.next = node
            current = node

    return sll


def sll_to_list(sll: SinglyLinkedList) -> list[int]:
    result = []
    current = sll.head

    while current:
        result.append(current.value)
        current = current.next

    return result


def find_first_repeat_sll(sll: SinglyLinkedList) -> int | None:
    seen = set()
    current = sll.head

    while current:
        if current.value in seen:
            return current.value
        seen.add(current.value)
        current = current.next

    return None


def remove_all_from_dll(dll: DoublyLinkedList, target: int) -> None:
    current = dll.head

    while current:
        next_node = current.next

        if current.value == target:
            # Fix previous pointer
            if current.prev:
                current.prev.next = current.next
            else:
                dll.head = current.next

            # Fix next pointer
            if current.next:
                current.next.prev = current.prev
            else:
                dll.tail = current.prev

        current = next_node


def is_train_palindrome(dll: DoublyLinkedList) -> bool:
    left = dll.head
    right = dll.tail

    while left and right:
        if left.value != right.value:
            return False

        # Stop when pointers meet or cross
        if left == right or left.next == right:
            break

        left = left.next
        right = right.prev

    return True