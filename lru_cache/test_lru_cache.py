import unittest
from lru_cache import LRUCache


class TestLRUCache(unittest.TestCase):

    def test_cache_add_and_retry(self):
        self.cache = LRUCache(2)
        self.cache.set("k1", "val1")
        self.cache.set("k2", "val2")
        self.assertEqual(self.cache.get("k1"), "val1")
        self.assertEqual(self.cache.get("k2"), "val2")

    def test_cache_delete(self):
        self.cache = LRUCache(2)
        self.cache.set("k1", "val1")
        self.cache.set("k2", "val2")
        self.cache.set("k3", "val3")
        self.assertIsNone(self.cache.get("k1"))
        self.assertEqual(self.cache.get("k2"), "val2")
        self.assertEqual(self.cache.get("k3"), "val3")

    def test_cache_limit(self):
        self.cache = LRUCache(2)
        self.cache.set("k1", "val1")
        self.cache.set("k2", "val2")
        self.cache.set("k3", "val3")
        self.assertIsNone(self.cache.get("k1"))
        self.assertEqual(self.cache.get("k2"), "val2")
        self.assertEqual(self.cache.get("k3"), "val3")

    def test_empty_key(self):
        self.cache = LRUCache(2)
        self.cache.set("k1", "val1")
        self.cache.set("k2", "val2")
        self.assertIsNone(self.cache.get("empty"))

    def test_lru(self):
        cache = LRUCache(2)
        cache.set("k1", "val1")
        cache.set("k2", "val2")

        self.assertIsNone(cache.get("k3"))
        self.assertEqual(cache.get("k2"), "val2")
        self.assertEqual(cache.get("k1"), "val1")

        cache.set("k3", "val3")

        self.assertEqual(cache.get("k3"), "val3")
        self.assertIsNone(cache.get("k2"))
        self.assertEqual(cache.get("k1"), "val1")

    def test_existing_key_update(self):
        self.cache = LRUCache(2)
        self.cache.set("k1", "val1")
        self.cache.set("k2", "val2")
        self.cache.set("k1", "new_val1")
        self.assertEqual(self.cache.get("k1"), "new_val1")
        self.assertEqual(self.cache.get("k2"), "val2")

    def test_another_instance(self):
        self.cache = LRUCache(2)
        self.cache.set("k1", "val1")
        self.cache.set("k2", "val2")
        new_cache = LRUCache(2)
        self.assertIsNone(new_cache.get("key1"))
        new_cache.set("key1", "value1")
        self.assertEqual(new_cache.get("key1"), "value1")

    def test_move_to_end_on_get(self):
        self.cache = LRUCache(2)
        self.cache.set("k1", "val1")
        self.cache.set("k2", "val2")
        self.assertEqual(self.cache.get("k1"), "val1")
        end_node_key = self.cache.end.prev.key
        self.assertEqual(end_node_key, "k1")

    def test_move_to_end_on_set(self):
        self.cache = LRUCache(2)
        self.cache.set("k1", "val1")
        self.cache.set("k2", "val2")
        self.cache.set("k1", "new_val1")
        end_node_key = self.cache.end.prev.key
        self.assertEqual(end_node_key, "k1")

    def test_move_to_end_after_several_operations(self):
        self.cache = LRUCache(2)
        self.cache.set("k1", "val1")
        self.cache.set("k2", "val2")
        self.cache.set("k1", "new_val1")
        self.assertEqual(self.cache.get("k2"), "val2")
        self.cache.set("k3", "val3")
        end_node_key = self.cache.end.prev.key
        self.assertEqual(end_node_key, "k3")

    def test_lru_capacity_one(self):
        cache = LRUCache(1)
        cache.set("k1", "val1")
        cache.set("k2", "val2")

        self.assertIsNone(cache.get("k1"))
        self.assertEqual(cache.get("k2"), "val2")

        cache.set("k3", "val3")

        self.assertIsNone(cache.get("k2"))
        self.assertEqual(cache.get("k3"), "val3")

    def test_lru_after_update(self):
        cache = LRUCache(2)
        cache.set("k1", "val1")
        cache.set("k2", "val2")

        cache.set("k1", "updated_val1")
        cache.set("k3", "val3")

        self.assertIsNone(cache.get("k2"))
        self.assertEqual(cache.get("k1"), "updated_val1")
        self.assertEqual(cache.get("k3"), "val3")


if __name__ == "__main__":
    unittest.main()
