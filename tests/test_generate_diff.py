from gendiff import generate_diff


def test_generate_diff():
    file1 = "fixtures/file1.json"
    file2 = "fixtures/file2.json"

    expected = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""

    result = generate_diff(file1, file2)

    assert result == expected


def test_generate_diff_yaml():
    file1 = "fixtures/file1.yml"
    file2 = "fixtures/file2.yml"

    expected = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""

    result = generate_diff(file1, file2)

    assert result == expected