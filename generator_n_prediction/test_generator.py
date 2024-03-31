import unittest
from unittest.mock import mock_open, patch
from io import StringIO
from generator import matches


class TestMatches(unittest.TestCase):
    @patch("builtins.open", new_callable=mock_open, read_data="one\ntwo\nThree\nА роза упала на лапу Азора\nфрукты на столе\n")
    def test_file_match(self, mock_file):
        expected_matches = ["two\n", "Three\n", "А роза упала на лапу Азора\n"]
        result = list(matches("./temp.txt", ["two", "Three", "Роза", "фрукт"]))
        self.assertEqual(result, expected_matches)

    def test_textio_match(self):
        input_data = "Белая береза\nПод моим окном\nПринакрылась снегом\nТочно серебром\nsnow White\n"
        text_io = StringIO(input_data)
        expected_matches = ["Под моим окном\n", "snow White\n"]
        result = list(matches(text_io, ["white", "принакрыл", "берёза", "Моим"]))
        self.assertEqual(result, expected_matches)

    def test_none(self):
        input_data = "Белая береза\nПод моим окном\nПринакрылась снегом\nТочно серебром\nsnow White\n"
        text_io = StringIO(input_data)
        expected_matches = []
        result = list(matches(text_io, ["one", "two", "Three"]))
        self.assertEqual(result, expected_matches)

    def test_register(self):
        input_data = "This is a first Test\nThis is a second test\n"
        text_io = StringIO(input_data)
        expected_matches = ["This is a first Test\n", "This is a second test\n"]
        result = list(matches(text_io, ["thIS", "SECOND"]))
        self.assertEqual(result, expected_matches)

    def test_same_matches(self):
        input_data = "apple\napple\napple\n"
        text_io = StringIO(input_data)
        expected_matches = ["apple\n", "apple\n", "apple\n"]
        result = list(matches(text_io, ["apple"]))
        self.assertEqual(result, expected_matches)

    def test_several_filters(self):
        input_data = "apple grape orange juice\ngrape orange juice\norange juice\njuice\napple\n"
        text_io = StringIO(input_data)
        expected_matches = ["apple grape orange juice\n", "grape orange juice\n", "orange juice\n", "juice\n", "apple\n"]
        result = list(matches(text_io, ["grape", "orange", "juice", "apple"]))
        self.assertEqual(result, expected_matches)

    def test_same_search_words(self):
        input_data = "red green blue\ngreen blue\nblue\nred\n"
        text_io = StringIO(input_data)
        expected_matches = ["red green blue\n", "green blue\n", "blue\n", "red\n"]
        result = list(matches(text_io, ["blue", "green", "red", "green", "blue"]))
        self.assertEqual(result, expected_matches)

    def test_filter_matches_string(self):
        input_data = "This is a first string\nThis is a second string\n"
        text_io = StringIO(input_data)
        expected_matches = []
        result = list(matches(text_io, ["This is a first string"]))
        self.assertEqual(result, expected_matches)


if __name__ == '__main__':
    unittest.main()
