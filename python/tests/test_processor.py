import pytest

from libs.parsers import JsonParser


def test_success_fires_on_parsed(tmp_path, processor, recorder):
    # 준비: 테스트용 파일과 처리기
    path = tmp_path / "user.json"
    path.write_text('{"name": "철수"}', encoding="utf-8")

    # 실행
    result = processor.process(path)

    # 검사
    assert result == {"name": "철수"}
    assert recorder.parsed == [(path, {"name": "철수"})]
    assert recorder.errors == []

def test_unsupported_extension_fires_on_error(tmp_path, processor, recorder):
    path = tmp_path / "image.png"

    result = processor.process(path)

    assert result is None
    recorder.assert_single_error(path, "지원하지 않는 형식")

def test_missing_file_fires_on_error(tmp_path, processor, recorder):
    path = tmp_path / "unexisting.json"

    result = processor.process(path)

    assert result is None
    recorder.assert_single_error(path, "파일이 없습니다")

def test_parsing_fails_on_error(tmp_path, processor, recorder):
    path = tmp_path / "broken.json"
    path.write_text('{"name": "철수",', encoding="utf-8")

    result = processor.process(path)

    assert result is None
    recorder.assert_single_error(path, "파싱 실패")

def test_register_with_string_raises(processor):
    with pytest.raises(TypeError, match="E_FileType"):
        processor.register(".json", JsonParser())