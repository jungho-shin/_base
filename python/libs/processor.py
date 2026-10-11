from .events import Event


class FileProcessor:
    def __init__(self):
        self._parsers = {}
        self.on_parsed = Event()
        self.on_error = Event()

    def register(self, ext, parser):
        self._parsers[ext] = parser

    def process(self, path):
        parser = self._parsers.get(path.suffix)

        if parser is None:
            self.on_error(path, f"지원하지 않는 형식: {path.suffix}")
            return None

        try:
            text = path.read_text(encoding="utf-8")
            data = parser.run(text)
        except FileNotFoundError:
            self.on_error(path, "파일이 없습니다")
            return None
        except Exception as e:
            self.on_error(path, f"파싱 실패: {e}")
            return None

        self.on_parsed(path, data)
        return data
