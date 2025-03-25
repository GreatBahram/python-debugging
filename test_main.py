from main import area_of_rectangle


def test_area_of_rectangle():
    area = area_of_rectangle(height="3", width="6")
    assert area == 18
