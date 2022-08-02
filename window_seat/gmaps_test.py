from google_map_address import get_address


def test_get_address():
    assert get_address(6.171849, -75.424919) == "https://www.google.com/maps/@6.171849,-75.424919,15z"
