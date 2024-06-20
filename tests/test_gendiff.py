from gendiff.modules.generate_diff import generate_diff


def test():
    expected_result = (
        "{\n"
        "  - follow: false\n"
        "    host: hexlet.io\n"
        "  - proxy: 123.234.53.22\n"
        "  - timeout: 50\n"
        "  + timeout: 20\n"
        "  + verbose: true\n"
        "}"
    )
    assert generate_diff('tests/fixtures/file1.json',
                         'tests/fixtures/file2.json') == expected_result
    assert generate_diff('tests/fixtures/file1.yaml',
                         'tests/fixtures/file2.yaml') == expected_result
    