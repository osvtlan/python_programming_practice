import socket
import threading
import queue


class Client:

    def __init__(self, host, port, num_threads, urls):
        self.host = host
        self.port = port
        self.num_threads = num_threads
        self.urls = queue.Queue()
        for url in urls:
            self.urls.put(url.strip())

    def send_request(self):
        while not self.urls.empty():
            url = self.urls.get()
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((self.host, self.port))
                s.sendall(url.encode())
                data = s.recv(1024).decode()
                print(f"{url}: {data}")

    def start(self):
        threads = []
        for _ in range(self.num_threads):
            thread = threading.Thread(target=self.send_request)
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("num_threads", type=int, help="Number of threads")
    parser.add_argument("url_file", type=str, help="File containing URLs")
    args = parser.parse_args()

    with open(args.url_file, "r") as file:
        urls = file.readlines()

    client = Client("localhost", 12345, args.num_threads, urls)
    client.start()
