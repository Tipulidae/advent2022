from src.calories import calories_per_elf


def test_calories_per_elf():
    inp = [[1, 2, 3], [30, 10], [125]]
    expected = [6, 40, 125]
    assert calories_per_elf(inp) == expected
