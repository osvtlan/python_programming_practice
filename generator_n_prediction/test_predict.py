import unittest
from unittest.mock import patch, call
from predict import SomeModel, predict_message_mood


class TestPredictMessageMood(unittest.TestCase):
    def test_predict_message_mood_bad(self):
        with patch.object(SomeModel, 'predict', return_value=0.2) as mock_predict:
            result = predict_message_mood("Чапаев и пустота", SomeModel())
            mock_predict.assert_called_with("Чапаев и пустота")
            self.assertEqual(result, "неуд")

    def test_predict_message_mood_good(self):
        with patch.object(SomeModel, 'predict', return_value=0.9) as mock_predict:
            result = predict_message_mood("Чапаев и пустота", SomeModel())
            mock_predict.assert_called_with("Чапаев и пустота")
            self.assertEqual(result, "отл")

    def test_predict_message_mood_normal(self):
        with patch.object(SomeModel, 'predict', return_value=0.5) as mock_predict:
            result = predict_message_mood("Чапаев и пустота", SomeModel())
            mock_predict.assert_called_with("Чапаев и пустота")
            self.assertEqual(result, "норм")

    def test_predict_message_mood_thresholds(self):
        with patch.object(SomeModel, 'predict', return_value=0.3) as mock_predict:
            result = predict_message_mood("Чапаев и пустота", SomeModel(), bad_thresholds=0.3, good_thresholds=0.8)
            mock_predict.assert_called_with("Чапаев и пустота")
            self.assertEqual(result, "норм")

    def test_equal_bad(self):
        with patch.object(SomeModel, 'predict', return_value=0.3) as mock_predict:
            result = predict_message_mood("Чапаев и пустота", SomeModel(), bad_thresholds=0.3, good_thresholds=0.8)
            mock_predict.assert_called_with("Чапаев и пустота")
            self.assertEqual(result, "норм")

    def test_equal_good(self):
        with patch.object(SomeModel, 'predict', return_value=0.8) as mock_predict:
            result = predict_message_mood("Чапаев и пустота", SomeModel(), bad_thresholds=0.3, good_thresholds=0.8)
            mock_predict.assert_called_with("Чапаев и пустота")
            self.assertEqual(result, "норм")

    def test_below_bad(self):
        with patch.object(SomeModel, 'predict', return_value=0.299) as mock_predict:
            result = predict_message_mood("Чапаев и пустота", SomeModel(), bad_thresholds=0.3, good_thresholds=0.8)
            mock_predict.assert_called_with("Чапаев и пустота")
            self.assertEqual(result, "неуд")

    def test_higher_good(self):
        with patch.object(SomeModel, 'predict', return_value=0.801) as mock_predict:
            result = predict_message_mood("Чапаев и пустота", SomeModel(), bad_thresholds=0.3, good_thresholds=0.8)
            mock_predict.assert_called_with("Чапаев и пустота")
            self.assertEqual(result, "отл")

    def test_change_thresholds(self):
        with patch.object(SomeModel, 'predict', return_value=0.4) as mock_predict:
            result = predict_message_mood("Чапаев и пустота", SomeModel(), bad_thresholds=0.2, good_thresholds=0.5)
            mock_predict.assert_called_with("Чапаев и пустота")
            self.assertEqual(result, "норм")

    def test_model_args(self):
        with patch.object(SomeModel, 'predict', return_value=0.3) as mock_predict:
            result = predict_message_mood("Чапаев и пустота", SomeModel(), bad_thresholds=0.3, good_thresholds=0.8)
            expected_call = call("Чапаев и пустота")
            mock_predict.assert_called_once_with(*expected_call.args, **expected_call.kwargs)
            self.assertEqual(result, "норм")


if __name__ == '__main__':
    unittest.main()
