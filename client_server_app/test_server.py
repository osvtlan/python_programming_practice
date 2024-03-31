import unittest
from unittest.mock import patch, Mock
from server import WorkerThread


class TestServer(unittest.TestCase):
    @patch("server.requests.get")
    def test_worker_thread_successful_request(self, mock_requests_get):
        mock_connection = Mock()
        mock_address = ("localhost", 8080)
        mock_requests_get.return_value.status_code = 200
        mock_requests_get.return_value.text = "<html><body>Hello, World!</body></html>"

        worker = WorkerThread(mock_connection, mock_address, top_k=5)
        worker.run()

        mock_connection.sendall.assert_called_once_with(b'{"hello": 1, "world": 1}')
        mock_connection.close.assert_called_once()

    @patch("server.requests.get")
    def test_worker_thread_failed_request(self, mock_requests_get):
        mock_connection = Mock()
        mock_address = ("localhost", 8080)
        mock_requests_get.return_value.status_code = 404

        worker = WorkerThread(mock_connection, mock_address, top_k=5)
        worker.run()

        mock_connection.sendall.assert_called_once_with(
            b'{"error": "Failed to fetch URL: 404"}'
        )

    @patch("server.requests.get", side_effect=Exception("Test Exception"))
    def test_worker_thread_exception(self, mock_requests_get):
        mock_connection = Mock()
        mock_address = ("localhost", 8080)

        worker = WorkerThread(mock_connection, mock_address, top_k=5)
        worker.run()

        mock_connection.sendall.assert_called_once_with(
            b'{"error": "Error: Test Exception"}'
        )


if __name__ == "__main__":
    unittest.main()
