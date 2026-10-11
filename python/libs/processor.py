from .events import Event
from .file_types import E_FileType


class FileProcessor:
    def __init__(self):
        self._parsers = {}
        self.on_parsed = Event()
        self.on_error = Event()

    def register(self, file_type, parser):
        if not isinstance(file_type, E_FileType):
            raise TypeError(f"file_type은 E_FileType이어야 합니다: {file_type!r}")
        self._parsers[file_type] = parser

    def process(self, path):
        try:
            file_type = E_FileType(path.suffix.lower())
        except ValueError:
            file_type = None

        parser = self._parsers.get(file_type)

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
