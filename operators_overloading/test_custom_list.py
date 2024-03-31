import unittest
from custom_list import CustomList


class TestCustomList(unittest.TestCase):
    def test_add(self):
        list1 = CustomList([1, 2, 3])
        list2 = CustomList([4, 5, 6])

        original_list1 = list1.copy()
        original_list2 = list2.copy()

        instance_result = list1 + list2
        expected_res = CustomList([5, 7, 9])
        self.assertEqual(len(instance_result), len(expected_res))
        for i in range(len(expected_res)):
            self.assertTrue(instance_result[i] == expected_res[i])

        list_result = list1 + [4, 5, 6]
        expected_list = CustomList([5, 7, 9])
        self.assertEqual(len(list_result), len(expected_list))
        for i in range(len(expected_list)):
            self.assertTrue(list_result[i] == expected_list[i])

        self.assertEqual(len(list1), len(original_list1))
        for i in range(len(original_list1)):
            self.assertTrue(list1[i] == original_list1[i])

        self.assertEqual(len(list2), len(original_list2))
        for i in range(len(original_list2)):
            self.assertTrue(list2[i] == original_list2[i])

    def test_add_different_len_custom(self):
        list1 = CustomList([1, 2, 3, 4])
        list2 = CustomList([5, 6])
        expected_sum = CustomList([6, 8, 3, 4])

        original_list1 = list1.copy()
        original_list2 = list2.copy()

        res_sum1 = list1 + list2
        self.assertEqual(len(res_sum1), len(expected_sum))
        for i in range(len(expected_sum)):
            self.assertTrue(res_sum1[i] == expected_sum[i])

        res_sum2 = list2 + list1
        self.assertEqual(len(res_sum2), len(expected_sum))
        for i in range(len(expected_sum)):
            self.assertTrue(res_sum2[i] == expected_sum[i])

        self.assertEqual(len(list1), len(original_list1))
        for i in range(len(original_list1)):
            self.assertTrue(list1[i] == original_list1[i])

        self.assertEqual(len(list2), len(original_list2))
        for i in range(len(original_list2)):
            self.assertTrue(list2[i] == original_list2[i])

    def test_add_different_len_list(self):
        list1 = CustomList([1, 2])
        list2 = [3, 4, 5, 6]
        expected_sum = CustomList([4, 6, 5, 6])

        original_list1 = list1.copy()
        original_list2 = list2.copy()

        res_sum1 = list1 + list2
        self.assertEqual(len(res_sum1), len(expected_sum))
        for i in range(len(expected_sum)):
            self.assertTrue(res_sum1[i] == expected_sum[i])

        res_sum2 = list2 + list1
        self.assertEqual(len(res_sum2), len(expected_sum))
        for i in range(len(expected_sum)):
            self.assertTrue(res_sum2[i] == expected_sum[i])

        self.assertEqual(len(list1), len(original_list1))
        for i in range(len(original_list1)):
            self.assertTrue(list1[i] == original_list1[i])

        self.assertEqual(len(list2), len(original_list2))
        for i in range(len(original_list2)):
            self.assertTrue(list2[i] == original_list2[i])

    def test_sub(self):
        list1 = CustomList([5, 7, 9])
        list2 = CustomList([1, 2, 3])

        original_list1 = list1.copy()
        original_list2 = list2.copy()

        instance_result = list1 - list2
        expected_res = CustomList([4, 5, 6])
        self.assertEqual(len(instance_result), len(expected_res))
        for i in range(len(expected_res)):
            self.assertTrue(instance_result[i] == expected_res[i])

        list_result = list1 - [2, 3]
        expected_list = CustomList([3, 4, 9])
        self.assertEqual(len(list_result), len(expected_list))
        for i in range(len(expected_list)):
            self.assertTrue(list_result[i] == expected_list[i])

        self.assertEqual(len(list1), len(original_list1))
        for i in range(len(original_list1)):
            self.assertTrue(list1[i] == original_list1[i])

        self.assertEqual(len(list2), len(original_list2))
        for i in range(len(original_list2)):
            self.assertTrue(list2[i] == original_list2[i])

    def test_sub_different_len_custom(self):
        list1 = CustomList([1, 2, 3, 4])
        list2 = CustomList([5, 6])

        original_list1 = list1.copy()
        original_list2 = list2.copy()

        res1 = list1 - list2
        expected1 = CustomList([-4, -4, 3, 4])
        self.assertEqual(len(res1), len(expected1))
        for i in range(len(expected1)):
            self.assertTrue(res1[i] == expected1[i])

        res2 = list2 - list1
        expected2 = CustomList([4, 4, -3, -4])
        self.assertEqual(len(res2), len(expected2))
        for i in range(len(expected2)):
            self.assertTrue(res2[i] == expected2[i])

        self.assertEqual(len(list1), len(original_list1))
        for i in range(len(original_list1)):
            self.assertTrue(list1[i] == original_list1[i])

        self.assertEqual(len(list2), len(original_list2))
        for i in range(len(original_list2)):
            self.assertTrue(list2[i] == original_list2[i])

    def test_sub_different_len_list1(self):
        list1 = CustomList([1, 2])
        list2 = [3, 4, 5, 6]

        original_list1 = list1.copy()
        original_list2 = list2.copy()

        res1 = list1 - list2
        expected1 = CustomList([-2, -2, -5, -6])
        self.assertEqual(len(res1), len(expected1))
        for i in range(len(expected1)):
            self.assertTrue(res1[i] == expected1[i])

        res2 = list2 - list1
        expected2 = CustomList([2, 2, 5, 6])
        self.assertEqual(len(res2), len(expected2))
        for i in range(len(expected2)):
            self.assertTrue(res2[i] == expected2[i])

        self.assertEqual(len(list1), len(original_list1))
        for i in range(len(original_list1)):
            self.assertTrue(list1[i] == original_list1[i])

        self.assertEqual(len(list2), len(original_list2))
        for i in range(len(original_list2)):
            self.assertTrue(list2[i] == original_list2[i])

    def test_sub_different_len_list2(self):
        list1 = [1, 2]
        list2 = CustomList([3, 4, 5, 6])

        original_list1 = list1.copy()
        original_list2 = list2.copy()

        res1 = list1 - list2
        expected1 = CustomList([-2, -2, -5, -6])
        self.assertEqual(len(res1), len(expected1))
        for i in range(len(expected1)):
            self.assertTrue(res1[i] == expected1[i])

        res2 = list2 - list1
        expected2 = CustomList([2, 2, 5, 6])
        self.assertEqual(len(res2), len(expected2))
        for i in range(len(expected2)):
            self.assertTrue(res2[i] == expected2[i])

        self.assertEqual(len(list1), len(original_list1))
        for i in range(len(original_list1)):
            self.assertTrue(list1[i] == original_list1[i])

        self.assertEqual(len(list2), len(original_list2))
        for i in range(len(original_list2)):
            self.assertTrue(list2[i] == original_list2[i])

    def test_cmp(self):
        list1 = CustomList([3, 4, 6])
        list2 = CustomList([1, 2, 5])
        self.assertFalse(list1 == list2)
        self.assertTrue(list1 != list2)
        self.assertTrue(list1 > list2)
        self.assertTrue(list1 >= list2)
        self.assertFalse(list1 < list2)
        self.assertFalse(list1 <= list2)

    def test_sum_equal(self):
        list1 = CustomList([1, 2, 3])
        list2 = CustomList([4, 5, -3])
        self.assertEqual(list1, list2)

        list3 = CustomList([1, 2, 3])
        list4 = CustomList([4, 5, 6])
        self.assertNotEqual(list3, list4)

    def test_str(self):
        list1 = CustomList([1, 2, 3])
        self.assertEqual(str(list1), "CustomList([1, 2, 3], Sum: 6)")
        self.assertEqual(list1, CustomList([1, 2, 3]))

    def test_empty_custom(self):
        list1 = CustomList([])
        result = list1 + CustomList([1, 2, 3])
        expected = CustomList([1, 2, 3])
        self.assertEqual(len(result), len(expected))
        for i in range(len(expected)):
            self.assertTrue(result[i] == expected[i])

        result1 = list1 - CustomList([1, 2, 3])
        expected1 = CustomList([-1, -2, -3])
        self.assertEqual(len(result1), len(expected1))
        for i in range(len(expected1)):
            self.assertTrue(result1[i] == expected1[i])


if __name__ == "__main__":
    unittest.main()
