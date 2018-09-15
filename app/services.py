import io
import os
import zipfile


class Report:
    __files = list()

    @classmethod
    def files(cls) -> list:
        return cls.__files

    @classmethod
    def add(cls, file: str, count: int):
        cls.__files.append((file, count))



class TXTReader:
    @staticmethod
    def read(file: str):
        with open(file, 'r') as f:
            content = f.read()
            Report.add(file, len(content.split()))


class ZIPReader:
    @classmethod
    def read(cls, file: str = None, stream: bytes = None):
        with zipfile.ZipFile(file or io.BytesIO(stream)) as z:
            for zfile in z.namelist():
                path, extension = os.path.splitext(zfile)
                if path.startswith('__MACOSX'):
                    continue
                if extension == '.txt':
                    content = z.read(zfile)
                    Report.add(zfile, len(content.split()))
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
