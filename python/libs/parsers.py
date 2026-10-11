import csv
import json
from abc import ABC, abstractmethod
from typing import final


class abParser(ABC):

    @final
    def run(self, text):
        if text.strip() == "":
            raise ValueError("빈 파일입니다")
        return self.parse(text)

    @abstractmethod
    def parse(self, text):...

class JsonParser(abParser):
    def parse(self, text):
        return json.loads(text)

class TextParser(abParser):
    def parse(self, text):
        return text.splitlines()

class CsvParser(abParser):
    def __init__(self, skip_spaces=False):
        self.skip_spaces = skip_spaces

    def parse(self, text):
        return list(csv.DictReader(text.splitlines(),
                                   skipinitialspace=self.skip_spaces))

class LogParser(abParser):
    def __init__(self, keyword):
        self.keyword = keyword

    def parse(self, text):
        filtered_lines = []
        for line in text.splitlines():
            if self.keyword in line:
                filtered_lines.append(line)

        return filtered_lines
