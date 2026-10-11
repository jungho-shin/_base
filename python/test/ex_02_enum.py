from libs.file_types import E_FileType


def main():
    # 1. 멤버, 이름, 값
    print(E_FileType.JSON)
    print(E_FileType.JSON.name)
    print(E_FileType.JSON.value)

    # 2. 값으로 멤버 찾기, 이름으로 멤버 찾기
    print(E_FileType(".json"))
    print(E_FileType["JSON"])

    # 3. 전체 멤버 둘러보기
    for file_type in E_FileType:
        print(file_type, file_type.value)

    # 4. 멤버와 문자열 비교
    print(E_FileType.JSON == ".json")
    print(E_FileType.JSON.value == ".json")
    print(E_FileType(".json") is E_FileType.JSON)

    E_FileType.JSON = ".xml"

if __name__ == '__main__':
    main()