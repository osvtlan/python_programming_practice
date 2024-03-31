import unittest
from custom_meta import CustomClass, CustomMeta


class TestCustomClass(unittest.TestCase):
    def test_set_custom_attrs(self):
        inst = CustomClass()
        self.assertEqual(inst.custom_x, 50)
        self.assertEqual(inst.custom_val, 99)
        self.assertEqual(inst.custom_line(), 100)
        self.assertEqual(str(inst), "Custom_by_metaclass")

    def test_custom_dynamic(self):
        inst = CustomClass()
        inst.dynamic = "added later"
        self.assertEqual(inst.custom_dynamic, "added later")

    def test_inst_hasattr(self):
        inst = CustomClass()
        self.assertTrue(hasattr(inst, "custom_val"))
        self.assertTrue(hasattr(inst, "custom_line"))
        inst.dynamic = "added later"
        self.assertTrue(hasattr(inst, "custom_dynamic"))

    def test_check_old_attrs(self):
        inst = CustomClass()
        self.assertFalse(hasattr(inst, "x"))
        self.assertFalse(hasattr(inst, "val"))
        self.assertFalse(hasattr(inst, "line"))

        self.assertTrue(hasattr(inst, "custom_x"))
        self.assertTrue(hasattr(inst, "custom_val"))
        self.assertTrue(hasattr(inst, "custom_line"))

        self.assertTrue(hasattr(inst, "__str__"))
        self.assertTrue(hasattr(inst, "__setattr__"))

        self.assertEqual(str(inst), "Custom_by_metaclass")
        setattr(inst, "dynamic", "added later")
        self.assertEqual(inst.custom_dynamic, "added later")

    def test_private_attr(self):
        inst = CustomClass()
        setattr(inst, "__private", 42)
        self.assertEqual(getattr(inst, "custom___private"), 42)

    def test_protected_attr(self):
        inst = CustomClass()
        self.assertFalse(hasattr(inst, "_protected"))

        inst._protected = 73
        self.assertEqual(inst.custom__protected, 73)

    def test_check_attrs_via_class(self):
        with self.assertRaises(AttributeError):
            return CustomClass.x

        with self.assertRaises(AttributeError):
            return CustomClass.val

        with self.assertRaises(AttributeError):
            return CustomClass.line()

        with self.assertRaises(AttributeError):
            return CustomClass.dynamic

    def test_check_custom_attrs_via_class(self):
        self.assertTrue(hasattr(CustomClass, "custom_x"))
        self.assertEqual(CustomClass.custom_x, 50)

        with self.assertRaises(AttributeError):
            return CustomClass.custom_val

        self.assertTrue(hasattr(CustomClass, "custom_line"))
        self.assertEqual(CustomClass.custom_line(CustomClass), 100)

        with self.assertRaises(AttributeError):
            return CustomClass.custom_dynamic

    def test_custom_meta_setattr(self):
        inst = CustomClass()
        inst.dynamic = "added later"
        self.assertTrue(hasattr(inst, CustomMeta.prefix + "dynamic"))
        self.assertFalse(hasattr(inst, "dynamic"))
        self.assertTrue(hasattr(inst, CustomMeta.prefix + "val"))
        self.assertFalse(hasattr(inst, "val"))
        self.assertTrue(hasattr(inst, CustomMeta.prefix + "line"))
        self.assertFalse(hasattr(inst, "line"))


if __name__ == "__main__":
    unittest.main()
