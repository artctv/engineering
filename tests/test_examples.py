"""
import random
import pytest
from pytest_mock import MockFixture


def mock_save_image(name: str, data: str):
    with open("lol.txt", "w") as f:
        f.write(data)


def check_ext(filename: str) -> bool:
    if not filename.endswith(".jpg"):
        return False
    return True


def is_correct_ext(filename: str):
    if not filename.endswith(".jpg"):
        raise ValueError("not correct ext")


def get_split():
    splits = ["=", "!", "-", " "]
    return splits[random.randint(0, len(splits)-1)]


def parse_string(s: str):
    split = get_split()
    return s.split(split)


def save_image(name: str, data: str):
    with open(name, "w") as f:
        f.write(data)


def some_with_image():
    save_image("kek.txt", "texttext/n")
    x = ""
    with open("kek.txt", "r") as f:
        x = f.read()
    return x



def test_check_ext():
    result = check_ext("kek.jpg")
    assert result
    result = check_ext("kek.png")
    assert not result


def test_correct_ext():
    result = is_correct_ext("kek.jpg")
    assert result is None
    with pytest.raises(ValueError):
        is_correct_ext("kek.png")


def test_parse_string(mocker: MockFixture):
    mock_now = mocker.patch("engineering.utils.get_split")
    mock_now.return_value = "="
    result = parse_string("kek=lol")
    assert result == ["kek", "lol"]


def test_with_image(mocker: MockFixture, r_num):
    mocked_etc_release_data = mocker.mock_open()
    builtin_open = "builtins.open"
    mocker.patch(builtin_open, mocked_etc_release_data)
    assert True


def test_new_simple_test(r_num):
    assert True
"""


# from fastapi.testclient import TestClient
# from .utils import generate_fake_image
#
#
# def test_main(client: TestClient):
#     fake_image = generate_fake_image("jpeg")
#     response = client.post("/predict", files={'file': fake_image})
#     print(response.json())
#     assert response.status_code == 200
#     assert response.json() == {}
