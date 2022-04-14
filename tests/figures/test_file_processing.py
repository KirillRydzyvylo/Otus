import json
import pytest


def test_check_json_format():
    with open("../src/files/result.json", "r") as json_file:
        try:
            print(json.load(json_file))
        except json.decoder.JSONDecodeError:
            pytest.fail("Ощибка чтения json", json.decoder.JSONDecodeError)