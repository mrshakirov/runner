import queue
import os
import threading
import zipfile


TXT_QUEUE = queue.Queue()  # txt files queue
ZIP_QUEUE = queue.Queue()  # zip files queue


class TXTReader(threading.Thread):
    def run(self):
        while True:
            try:
                file = TXT_QUEUE.get(block=False)
            except queue.Empty:
                continue
            with open(file, 'r') as f:
                content = f.read()
            print('file', content)


class ZIPReader(threading.Thread):
    def run(self):
        while True:
            try:
                archive = ZIP_QUEUE.get(block=False)
            except queue.Empty:
                continue
            with zipfile.ZipFile(archive, 'r') as f:
                for file in f.namelist():
                    content = f.read(file)
                    print('zip', content)


class Runner:
    @classmethod
    def start(cls, path: str):
        for root, _, files in os.walk(path):
            for file in files:
                file = os.path.join(root, file)
                cls.dispatch(file)

    @classmethod
    def dispatch(cls, file: str):
        _, extension = os.path.splitext(file)
        if extension == '.txt':
            TXT_QUEUE.put(file)
        elif extension == '.zip':
            ZIP_QUEUE.put(file)


TXTReader().start()
ZIPReader().start()
