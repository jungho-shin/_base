import pytest

from libs.parsers import JsonParser, TextParser, CsvParser, LogParser


def test_json_parser():
    parser = JsonParser()
    result = parser.run('{"name": "철수", "age": 25}')
    assert result == {"name": "철수", "age": 25}

def test_text_parser():
    parser = TextParser()
    result = parser.run("첫 줄\n둘째 줄")
    assert result == ["첫 줄", "둘째 줄"]

def test_csv_parser_skip_spaces_true():
    parser = CsvParser(skip_spaces=True)
    result = parser.run("name, score\n철수, 85\n영희, 92")
    assert result == [{"name": "철수", "score": "85"}, {"name": "영희", "score": "92"}]

def test_csv_parser_with_skip_spaces_false():
    parser = CsvParser(skip_spaces=False)
    result = parser.run("name, score\n철수, 85\n영희, 92")
    assert result == [{"name": "철수", " score": " 85"}, {"name": "영희", " score": " 92"}]

def test_log_parser():
    parser = LogParser("INFO")
    result = parser.run("INFO 서버 시작\nERROR DB 연결 실패\nINFO 사용자 로그인\nERROR 파일 없음")
    assert result == ["INFO 서버 시작", "INFO 사용자 로그인"]

def test_empty_text_raises():
    parser = TextParser()
    with pytest.raises(ValueError, match="빈 파일"):
        parser.run("")

@pytest.mark.parametrize("parser", [
    JsonParser(),
    TextParser(),
    CsvParser(),
    LogParser("ERROR"),
], ids=["json", "text", "csv", "log"])
def test_empty_input_raises(parser):
    with pytest.raises(ValueError, match="빈 파일"):
        parser.run("   ")