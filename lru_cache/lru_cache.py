class LRUCache:
    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.prev = None
            self.next = None

    def __init__(self, limit=42):
        self.limit = limit
        self.cache = {}
        self.start = self.Node(None, None)
        self.end = self.Node(None, None)
        self.start.next = self.end
        self.end.prev = self.start

    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def add_to_end(self, node):
        node.prev = self.end.prev
        node.next = self.end
        self.end.prev.next = node
        self.end.prev = node

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self.remove_node(node)
            self.add_to_end(node)
            return node.value
        else:
            return None

    def set(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.remove_node(node)
            self.add_to_end(node)
        else:
            if len(self.cache) >= self.limit:
                oldest_node = self.start.next
                del self.cache[oldest_node.key]
                self.remove_node(oldest_node)
            new_node = self.Node(key, value)
            self.add_to_end(new_node)
            self.cache[key] = new_node


if __name__ == "__main__":
    cache = LRUCache(2)

    cache.set("k1", "val1")
    cache.set("k2", "val2")

    assert cache.get("k3") is None
    assert cache.get("k2") == "val2"
    assert cache.get("k1") == "val1"

    cache.set("k3", "val3")

    assert cache.get("k3") == "val3"
    assert cache.get("k2") is None
    assert cache.get("k1") == "val1"
