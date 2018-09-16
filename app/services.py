import collections
import datetime as dt
import io
import os
import zipfile

import matplotlib as m
m.use('agg')
import matplotlib.pyplot as mp

import conf


class Report:
    __words = dict()

    @classmethod
    def add(cls, words: dict):
        words = {k.lower(): v for k, v in words.items()}
        cls.__words = collections.Counter(cls.__words) + collections.Counter(words)

    @classmethod
    def draw(cls):
        file = '%s/%s.png' % (conf.OUT, str(dt.datetime.now()))
        money = [i[1] for i in cls.__words]
        fig, ax = mp.subplots()
        mp.bar(money, money)
        mp.xticks(money, [i[0] for i in cls.__words])
        mp.savefig(file)


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
