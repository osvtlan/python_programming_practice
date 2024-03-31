import socket
import json
import threading
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
import requests
from bs4 import BeautifulSoup
import re
import queue


class WorkerThread(threading.Thread):
    def __init__(self, connection, address, top_k):
        super().__init__()
        self.connection = connection
        self.address = address
        self.top_k = top_k

    @staticmethod
    def extract_text_from_html(html_content):
        soup = BeautifulSoup(html_content, "html.parser")
        words = re.findall(r"\b\w+\b", soup.get_text().lower())
        return words

    def run(self):
        data = self.connection.recv(1024).decode()
        url = data.strip()

        try:
            response = requests.get(url)
            if response.status_code == 200:
                html_content = response.text
                words = self.extract_text_from_html(html_content)
                word_counts = Counter(words)
                top_words = dict(word_counts.most_common(self.top_k))
            else:
                top_words = {"error": f"Failed to fetch URL: {response.status_code}"}
        except Exception as e:
            top_words = {"error": f"Error: {str(e)}"}

        response_data = json.dumps(top_words, ensure_ascii=False).encode("utf-8")
        self.connection.sendall(response_data)
        self.connection.close()


class MasterServer:
    def __init__(self, host, port, num_workers, top_k):
        self.running = True
        self.host = host
        self.port = port
        self.num_workers = num_workers
        self.top_k = top_k
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((host, port))
        self.executor = ThreadPoolExecutor(max_workers=num_workers)
        self.url_queue = queue.Queue()

    def start(self):
        print(
            f"Server listening on {self.host}:{self.port} with {self.num_workers} workers..."
        )
        self.server_socket.listen()

        with self.executor as executor:
            while self.running:
                client_socket, address = self.server_socket.accept()
                executor.submit(self._worker_thread, client_socket, address)

    def stop(self):
        self.running = False
        self.server_socket.close()

    def _worker_thread(self, client_socket, address):
        worker = WorkerThread(client_socket, address, self.top_k)
        worker.start()
        worker.join()


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-w", "--num_workers", type=int, required=True, help="Number of worker threads"
    )
    parser.add_argument(
        "-k", "--top_k", type=int, required=True, help="Top K frequent words"
    )
    args = parser.parse_args()
    server = MasterServer("localhost", 12345, args.num_workers, args.top_k)
    server.start()
