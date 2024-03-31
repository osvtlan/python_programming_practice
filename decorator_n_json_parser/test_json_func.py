import unittest
from unittest.mock import Mock
from json_func import parse_json


class TestParseJson(unittest.TestCase):
    def setUp(self):
        self.json_data = '{"key1": "Word1 word2", "key2": "word2 word3"}'
        self.required_fields = ["key1", "key2"]
        self.keywords = ["word1", "word3", "word2"]

    def test_correct_calls(self):
        mock_callback = Mock()
        parse_json(self.json_data, self.required_fields, self.keywords, mock_callback)
        mock_callback.assert_any_call("word2", "key2")
        mock_callback.assert_any_call("word1", "key1")
        mock_callback.assert_any_call("word3", "key2")
        mock_callback.assert_any_call("word2", "key1")
        self.assertEqual(mock_callback.call_count, 4)

    def test_missing_required_fields(self):
        json_data = '{"key1": "Word1 word2"}'
        mock_callback = Mock()
        parse_json(json_data, self.required_fields, self.keywords, mock_callback)
        mock_callback.assert_any_call("word1", "key1")
        mock_callback.assert_any_call("word2", "key1")
        self.assertEqual(mock_callback.call_count, 2)

    def test_json_empty_required_fields(self):
        json_data = '{"key1": "Word1 word2", "key2": "word2 word3"}'
        mock_callback = Mock()
        parse_json(json_data, ["", "key2"], self.keywords, mock_callback)
        mock_callback.assert_any_call("word2", "key2")
        mock_callback.assert_any_call("word3", "key2")
        self.assertEqual(mock_callback.call_count, 2)

    def test_json_empty_values(self):
        json_data = '{"key1": "", "key2": ""}'
        mock_callback = Mock()
        parse_json(json_data, self.required_fields, self.keywords, mock_callback)
        mock_callback.assert_not_called()

    def test_invalid_json(self):
        json_data = '{key1: "Word1 word2", "key2": "word2 word3"}'
        with self.assertRaises(ValueError):
            mock_callback = Mock()
            parse_json(json_data, self.required_fields, self.keywords, mock_callback)

    def test_field_register(self):
        json_data = '{"Key1": "Word1 word2", "Key2": "word2 word3"}'
        mock_callback = Mock()
        parse_json(json_data, self.required_fields, self.keywords, mock_callback)
        mock_callback.assert_not_called()

    def test_keyword_register(self):
        json_data = '{"key1": "Word1 word2", "key2": "word2 word3"}'
        mock_callback = Mock()
        parse_json(
            json_data, self.required_fields, ["WORD1", "word3", "WORD2"], mock_callback
        )
        mock_callback.assert_any_call("WORD1", "key1")
        mock_callback.assert_any_call("WORD2", "key1")
        mock_callback.assert_any_call("word3", "key2")
        mock_callback.assert_any_call("WORD2", "key2")
        self.assertEqual(mock_callback.call_count, 4)

    def test_parse_empty(self):
        json_data = "{}"
        mock_callback = Mock()
        parse_json(json_data, self.required_fields, self.keywords, mock_callback)
        mock_callback.assert_not_called()

    def test_no_required_fields(self):
        mock_callback = Mock()
        parse_json(self.json_data, [], self.keywords, mock_callback)
        mock_callback.assert_not_called()

    def test_no_keywords(self):
        mock_callback = Mock()
        parse_json(self.json_data, self.required_fields, [], mock_callback)
        mock_callback.assert_not_called()

    def test_none_required_fields(self):
        mock_callback = Mock()
        parse_json(self.json_data, None, self.keywords, mock_callback)
        mock_callback.assert_not_called()

    def test_none_keywords(self):
        mock_callback = Mock()
        parse_json(self.json_data, None, self.keywords, mock_callback)
        mock_callback.assert_not_called()

    def test_none_keyword_callback(self):
        mock_callback = Mock()
        parse_json(self.json_data, self.required_fields, self.keywords, None)
        mock_callback.assert_not_called()


if __name__ == "__main__":
    unittest.main()
