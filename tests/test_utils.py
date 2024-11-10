import pytest
from exify.utils import get_file_name_from_path, decimal_to_fraction


@pytest.mark.parametrize(
    "path, expected",
    [
        ("/path/to/file.jpg", "file.jpg"),
        ("path/to/file.jpg", "file.jpg"),
        ("./file.jpg", "file.jpg"),
        ("file.jpg", "file.jpg"),
        ("/", ""),
        ("", ""),
    ],
)
def test_get_file_name_from_path(path, expected):
    result = get_file_name_from_path(path)
    assert result == expected


@pytest.mark.parametrize(
    "decimal, expected",
    [
        (0.25, "1/4"),
        (0.001, "1/1000"),
        (2.0, "2"),
    ],
)
def test_decimal_to_fraction(decimal, expected):
    result = decimal_to_fraction(decimal)
    assert result == expected
