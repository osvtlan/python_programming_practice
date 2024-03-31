import unittest
from unittest.mock import patch
from decorator import mean, foo


class TestMeanDecorator(unittest.TestCase):
    def test_decorator_behavior(self):
        with patch("builtins.print") as mock_print:
            foo("Walter")
            mock_print.assert_called_with(
                "Average execution time of the last 10 function calls - 0.00000"
            )
            self.assertEqual(mock_print.call_count, 1)

    def test_calculate_average(self):
        with patch("builtins.print") as mock_print:
            for _ in range(10):
                foo("Walter")
            mock_print.assert_called_with(
                "Average execution time of the last 10 function calls - 0.00000"
            )

    def test_several_arguments(self):
        calls_to_count = 5

        @mean(calls_to_count)
        def example(arg1, arg2):
            pass

        with patch("builtins.print") as mock_print:
            example("Walter", "Jack")
            mock_print.assert_called_with(
                "Average execution time of the last 1 function calls - 0.00000"
            )
            for _ in range(calls_to_count):
                example("One", "Two")
            mock_print.assert_called_with(
                f"Average execution time of the last {calls_to_count} function calls - 0.00000"
            )


if __name__ == "__main__":
    unittest.main()
