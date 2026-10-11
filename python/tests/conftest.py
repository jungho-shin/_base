import pytest

from libs.file_types import E_FileType
from libs.parsers import JsonParser
from libs.processor import FileProcessor


class EventRecorder:
    def __init__(self, processor):
        self.parsed = []
        self.errors = []
        processor.on_parsed += self._on_parsed
        processor.on_error += self._on_error

    def _on_parsed(self, path, data):
        self.parsed.append((path, data))

    def _on_error(self, path, msg):
        self.errors.append((path, msg))

    def assert_single_error(self, path, expected_text):
        assert self.parsed == []
        assert len(self.errors) == 1

        p, msg = self.errors[0]
        assert p == path
        assert expected_text in msg

@pytest.fixture
def processor():
    processor = FileProcessor()
    processor.register(E_FileType.JSON, JsonParser())
    return processor

@pytest.fixture
def recorder(processor):
    return EventRecorder(processor)
