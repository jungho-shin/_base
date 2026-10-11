# import sys

from libs.parsers import JsonParser, TextParser

# for p in sys.path:
#     print(p)


from pathlib import Path

from libs.processor import FileProcessor


class Stats:
    def __init__(self):
        self.success = 0
        self.error = 0

    def count_success(self, path, data):
        self.success += 1

    def count_error(self, path, msg):
        self.error += 1

    def report(self):
        print(f"결과: 성공 {self.success}, 실패 {self.error}")

def main():
    processor = FileProcessor()
    processor.register(".json", JsonParser())
    processor.register(".txt", TextParser())

    processor.on_parsed += lambda path, data: print(f"[성공] {path.name} -> {data}")
    processor.on_error += lambda path, msg: print(f"[실패] {path.name} -> {msg}")

    stats = Stats()
    processor.on_parsed += stats.count_success
    processor.on_error += stats.count_error

    BASE_DIR = Path(__file__).parent
    SAMPLE_DIR = BASE_DIR / "sample"

    paths = [
        SAMPLE_DIR / "empty.txt",
        SAMPLE_DIR / "empty.json",
    ]

    for path in paths:
        processor.process(path)

    stats.report()

if __name__ == '__main__':
    main()
