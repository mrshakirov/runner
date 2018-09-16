import collections
import datetime as dt
import io
import os
import zipfile

import matplotlib.pyplot as plt

import conf


class Report:
    __words = dict()
    __exclude = ',.:;!?()'

    @classmethod
    def words(cls) -> dict:
        return cls.__words.copy()

    @classmethod
    def clear(cls):
        cls.__words.clear()

    @classmethod
    def add(cls, words: dict):
        words = {cls.pre_process(k): v for k, v in words.items()}
        cls.__words = collections.Counter(cls.__words) + collections.Counter(words)

    @classmethod
    def pre_process(cls, word: str) -> str:
        result = ''.join(i for i in word if i not in cls.__exclude)
        return result.lower()

    @classmethod
    def draw(cls):
        file = '%s/%s.png' % (conf.OUT_PATH, str(dt.datetime.now()))
        fig, ax = plt.subplots(figsize=(conf.OUT_WIDTH, conf.OUT_HEIGHT))
        ax.bar(cls.__words.keys(), cls.__words.values())
        plt.xticks(rotation=90)
        plt.savefig(file)


class TXTReader:
    @staticmethod
    def read(file: str):
        with open(file, 'r') as f:
            content = f.read()
            Report.add(collections.Counter(content.split()))


class ZIPReader:
    @classmethod
    def read(cls, file: str = None, stream: bytes = None):
        with zipfile.ZipFile(file or io.BytesIO(stream)) as z:
            for zfile in z.namelist():
                path, extension = os.path.splitext(zfile)
                if path.startswith('__MACOSX'):
                    continue
                if extension == '.txt':
                    content = z.read(zfile).decode()
                    Report.add(collections.Counter(content.split()))
                elif extension == '.zip':
                    cls.read(stream=z.read(zfile))


class Runner:
    @classmethod
    def start(cls, path: str):
        for root, _, files in os.walk(path):
            for file in files:
                file = os.path.join(root, file)
                _, extension = os.path.splitext(file)
                if extension == '.txt':
                    TXTReader.read(file)
                elif extension == '.zip':
                    ZIPReader.read(file)
