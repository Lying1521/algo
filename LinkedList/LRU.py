# 请你设计并实现一个满足  LRU (最近最少使用) 缓存 约束的数据结构。
# 实现 LRUCache 类：
# LRUCache(int capacity) 以 正整数 作为容量 capacity 初始化 LRU 缓存
# int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
# void put(int key, int value) 如果关键字 key 已经存在，则变更其数据值 value ；
# 如果不存在，则向缓存中插入该组 key-value 。如果插入操作导致关键字数量超过 capacity ，则应该 逐出 最久未使用的关键字。
# 函数 get 和 put 必须以 O(1) 的平均时间复杂度运行。

# 思路： O(1)的访问考虑使用哈希表，O(1)的插入使用双向链表,使用哈希表存储链表节点
#       自定义双向链表节点，包含key,value

class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node(0, 0)
        self.foot = Node(-1, -1)
        self.head.next = self.foot
        self.foot.prev = self.head
        self.values = {}
        self.capacity = capacity
        self.count = 0

    def insert_to_head(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

        self.head.next.prev = node
        node.prev = self.head
        node.next = self.head.next
        self.head.next = node

    def get(self, key: int) -> int:
        if key in self.values:
            node = self.values[key]
            self.insert_to_head(node)

            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.values:
            node = self.values[key]
            self.insert_to_head(node)
            node.val = value
        else:
            node = Node(key, value)
            self.head.next.prev = node
            node.next = self.head.next
            node.prev = self.head
            self.head.next = node
            self.values[key] = node
            if self.count >= self.capacity:
                temp = self.foot.prev
                temp.prev.next = self.foot
                self.foot.prev = temp.prev
                temp.prev = None
                temp.next = None
                self.values.pop(temp.key)
            else:
                self.count += 1


class Node:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None